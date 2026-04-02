// ============================================================================
// CHECKER 2: Post-Detailing Sheet & Drawing Verification
// Purpose: Run AFTER detailing to verify:
//   - No system marks remain (all members have user piecemarks)
//   - All members are loaded/placed on a detail sheet
//   - BOM quantities are valid
//   - Gather sheet quantities match detail sheet demands
//
// OUTPUT: Excel spreadsheet with Summary, Issues, and System Marks sheets.
//         Issues sheet has a "Resolved" checkbox column with strikethrough.
// ============================================================================
using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Text.RegularExpressions;
using DesignData.SDS2.Database;
using DesignData.SDS2.Model;
using DesignData.SDS2.Detail;
using OfficeOpenXml;
using OfficeOpenXml.Style;

namespace SDS2Workflow
{
    public class PostDetailSheetChecker
    {
        private static readonly Regex SystemMarkPattern = new Regex(
            @"^[A-Z]{1,3}_\d+$", RegexOptions.Compiled);

        private class Issue
        {
            public int MemberNumber { get; set; }
            public string Piecemark { get; set; } = null!;
            public string IssueType { get; set; } = null!;
            public string Sequence { get; set; } = null!;
            public string Details { get; set; } = null!;
        }

        [STAThread]
        public static void Main(string[] args)
        {
            DataDirectory.Open(DataDirectory.Default);

            // --- Step 1: Select Repository ---
            var repositories = Repository.GetAllRepositories();
            Console.WriteLine("==========================================================");
            Console.WriteLine("  Available Repositories:");
            Console.WriteLine("==========================================================");
            for (int i = 0; i < repositories.Count; i++)
                Console.WriteLine($"  [{i + 1}] {repositories[i].Name}");

            Console.Write("\n  Select repository number: ");
            int repoIndex = int.Parse(Console.ReadLine().Trim()) - 1;
            var selectedRepo = repositories[repoIndex];

            // --- Step 2: Select Job ---
            var jobIds = selectedRepo.JobIdentifiers;
            Console.WriteLine($"\n  Jobs in '{selectedRepo.Name}':");
            Console.WriteLine("----------------------------------------------------------");
            for (int i = 0; i < jobIds.Count; i++)
                Console.WriteLine($"  [{i + 1}] {jobIds[i].Name}");

            Console.Write("\n  Select job number: ");
            int jobIndex = int.Parse(Console.ReadLine().Trim()) - 1;
            var selectedJobId = jobIds[jobIndex];

            var job = Job.FindJob(selectedJobId);
            job.Open();
            Console.WriteLine($"\n  Opened: {selectedJobId.Name}");

            // --- Step 3: Discover & Select Sequences ---
            Console.WriteLine("\n  Scanning sequences in model...");
            var allSequences = new Dictionary<string, int>();

            using (var scanTx = new ReadOnlyTransaction(job))
            {
                foreach (var handle in job.Members)
                {
                    var member = MemberBrief.Get(handle);
                    if (member.Sequence == null) continue;
                    string seqName = member.Sequence.Name;
                    if (allSequences.ContainsKey(seqName))
                        allSequences[seqName]++;
                    else
                        allSequences[seqName] = 1;
                }
            }

            Console.WriteLine("\n  Available Sequences:");
            Console.WriteLine("----------------------------------------------------------");
            var seqKeys = new List<string>(allSequences.Keys);
            seqKeys.Sort();
            for (int i = 0; i < seqKeys.Count; i++)
                Console.WriteLine($"  [{i + 1}] {seqKeys[i]}  ({allSequences[seqKeys[i]]} members)");
            Console.WriteLine($"  [A] All sequences");

            Console.Write("\n  Enter sequence numbers (comma-separated) or 'A' for all: ");
            string input = Console.ReadLine().Trim();

            var targetSequences = new List<string>();
            if (input.Equals("A", StringComparison.OrdinalIgnoreCase))
            {
                targetSequences = seqKeys;
            }
            else
            {
                foreach (var part in input.Split(','))
                {
                    int idx = int.Parse(part.Trim()) - 1;
                    if (idx >= 0 && idx < seqKeys.Count)
                        targetSequences.Add(seqKeys[idx]);
                }
            }

            Console.WriteLine($"\n  Checking sequences: {string.Join(", ", targetSequences)}\n");

            RunPostDetailCheck(job, selectedJobId.Name, targetSequences);

            Console.WriteLine("\nPress Enter to exit...");
            Console.ReadLine();
        }

        public static void RunPostDetailCheck(Job job, string jobName, List<string> targetSequences)
        {
            Console.WriteLine("==========================================================");
            Console.WriteLine("  CHECKER 2: Post-Detailing Sheet & Drawing Verification");
            Console.WriteLine("==========================================================\n");

            int totalChecked        = 0;
            int systemMarkCount     = 0;
            int missingDrawingCount = 0;
            int missingBOMCount     = 0;
            int bomQuantityIssues   = 0;
            int gatherSheetMissing  = 0;
            int gatherQtyMismatches = 0;

            var systemMarksFound = new List<string>();
            var issues           = new List<Issue>();

            using (var transaction = new ReadOnlyTransaction(job))
            {
                foreach (var handle in job.Members)
                {
                    var member = MemberBrief.Get(handle);

                    if (member.Sequence == null) continue;
                    string seqName = member.Sequence.Name;
                    if (!targetSequences.Contains(seqName)) continue;

                    totalChecked++;
                    string pcmk = member.Piecemark;

                    // CHECK 1: System Marks
                    if (SystemMarkPattern.IsMatch(pcmk))
                    {
                        systemMarkCount++;
                        if (!systemMarksFound.Contains(pcmk))
                            systemMarksFound.Add(pcmk);
                        issues.Add(new Issue
                        {
                            MemberNumber = member.Number,
                            Piecemark = pcmk,
                            IssueType = "SYSTEM MARK",
                            Sequence = seqName,
                            Details = "Member still has a system-generated piecemark"
                        });
                    }

                    // CHECK 2: Loaded On a Sheet
                    var drawings = Drawing.Find(PiecemarkType.Major, pcmk);
                    if (drawings == null || drawings.Count == 0)
                    {
                        missingDrawingCount++;
                        issues.Add(new Issue
                        {
                            MemberNumber = member.Number,
                            Piecemark = pcmk,
                            IssueType = "NO DETAIL SHEET",
                            Sequence = seqName,
                            Details = "Member is not loaded on any detail sheet"
                        });
                        continue;
                    }

                    // CHECK 3: BOM Exists
                    var drawing = drawings[0];
                    var bom = drawing.BillOfMaterial;
                    if (bom == null)
                    {
                        missingBOMCount++;
                        issues.Add(new Issue
                        {
                            MemberNumber = member.Number,
                            Piecemark = pcmk,
                            IssueType = "NO BOM",
                            Sequence = seqName,
                            Details = $"Drawing '{drawing.Name}' has no Bill of Material"
                        });
                        continue;
                    }

                    // CHECK 4: BOM Quantities + Gather Sheets
                    var bomLines = bom.GetLines();
                    foreach (var line in bomLines)
                    {
                        if (line.UnitQuantity < 1 || line.TotalQuantity < 1)
                        {
                            bomQuantityIssues++;
                            issues.Add(new Issue
                            {
                                MemberNumber = member.Number,
                                Piecemark = pcmk,
                                IssueType = "BAD BOM QTY",
                                Sequence = seqName,
                                Details = $"'{line.MinorMark ?? line.Description}': Unit={line.UnitQuantity}, Total={line.TotalQuantity}"
                            });
                        }

                        if (!string.IsNullOrEmpty(line.MinorMark))
                        {
                            var gatherSheets = Drawing.Find(PiecemarkType.Minor, line.MinorMark);
                            if (gatherSheets == null || gatherSheets.Count == 0)
                            {
                                gatherSheetMissing++;
                                issues.Add(new Issue
                                {
                                    MemberNumber = member.Number,
                                    Piecemark = pcmk,
                                    IssueType = "NO GATHER SHEET",
                                    Sequence = seqName,
                                    Details = $"Submaterial '{line.MinorMark}' has no gather sheet"
                                });
                            }
                            else
                            {
                                uint gatherQty = gatherSheets[0].Status.Quantity;
                                if (gatherQty < (uint)Math.Max(0, line.TotalQuantity))
                                {
                                    gatherQtyMismatches++;
                                    issues.Add(new Issue
                                    {
                                        MemberNumber = member.Number,
                                        Piecemark = pcmk,
                                        IssueType = "GATHER QTY MISMATCH",
                                        Sequence = seqName,
                                        Details = $"Gather '{line.MinorMark}' shows {gatherQty}, BOM needs {line.TotalQuantity}"
                                    });
                                }
                            }
                        }
                    }
                }
            }

            // Console summary
            Console.WriteLine($"  Total members checked:           {totalChecked}");
            Console.WriteLine($"  Still have system marks:         {systemMarkCount}");
            Console.WriteLine($"  Members missing detail sheets:   {missingDrawingCount}");
            Console.WriteLine($"  Sheets missing BOM:              {missingBOMCount}");
            Console.WriteLine($"  BOM quantity issues:             {bomQuantityIssues}");
            Console.WriteLine($"  Submaterials missing gathers:    {gatherSheetMissing}");
            Console.WriteLine($"  Gather vs Detail qty mismatches: {gatherQtyMismatches}");

            // Generate Excel
            systemMarksFound.Sort();

            string timestamp = DateTime.Now.ToString("yyyy-MM-dd_HHmmss");
            string fileName = $"Checker2_{jobName}_{timestamp}.xlsx";
            string outputPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, fileName);

            using (var package = new ExcelPackage())
            {
                // ====== SHEET 1: Summary ======
                var wsSummary = package.Workbook.Worksheets.Add("Summary");
                StyleHeader(wsSummary, "A1:B1", "Post-Detailing Sheet & Drawing Verification");

                wsSummary.Cells["A3"].Value = "Job Name";
                wsSummary.Cells["B3"].Value = jobName;
                wsSummary.Cells["A4"].Value = "Run Date";
                wsSummary.Cells["B4"].Value = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
                wsSummary.Cells["A5"].Value = "Sequences Checked";
                wsSummary.Cells["B5"].Value = string.Join(", ", targetSequences);

                wsSummary.Cells["A7"].Value = "Check";
                wsSummary.Cells["B7"].Value = "Count";
                wsSummary.Cells["C7"].Value = "Status";
                StyleTableHeader(wsSummary, "A7:C7");

                int r = 8;
                AddSummaryRow(wsSummary, r++, "Total Members Checked", totalChecked, "");
                AddSummaryRow(wsSummary, r++, "System Marks Remaining", systemMarkCount,
                    systemMarkCount == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Missing Detail Sheets", missingDrawingCount,
                    missingDrawingCount == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Missing BOM", missingBOMCount,
                    missingBOMCount == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "BOM Quantity Issues", bomQuantityIssues,
                    bomQuantityIssues == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Missing Gather Sheets", gatherSheetMissing,
                    gatherSheetMissing == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Gather Qty Mismatches", gatherQtyMismatches,
                    gatherQtyMismatches == 0 ? "PASS" : "FAIL");

                wsSummary.Column(1).Width = 28;
                wsSummary.Column(2).Width = 40;
                wsSummary.Column(3).Width = 12;

                // ====== SHEET 2: Issues ======
                var wsIssues = package.Workbook.Worksheets.Add("Issues");
                StyleHeader(wsIssues, "A1:F1", $"Issues Found: {issues.Count}");

                wsIssues.Cells["A3"].Value = "Resolved";
                wsIssues.Cells["B3"].Value = "Member #";
                wsIssues.Cells["C3"].Value = "Piecemark";
                wsIssues.Cells["D3"].Value = "Issue Type";
                wsIssues.Cells["E3"].Value = "Sequence";
                wsIssues.Cells["F3"].Value = "Details";
                StyleTableHeader(wsIssues, "A3:F3");

                for (int i = 0; i < issues.Count; i++)
                {
                    int row = i + 4;
                    wsIssues.Cells[row, 1].Value = false;
                    wsIssues.Cells[row, 2].Value = issues[i].MemberNumber;
                    wsIssues.Cells[row, 3].Value = issues[i].Piecemark;
                    wsIssues.Cells[row, 4].Value = issues[i].IssueType;
                    wsIssues.Cells[row, 5].Value = issues[i].Sequence;
                    wsIssues.Cells[row, 6].Value = issues[i].Details;

                    var validation = wsIssues.DataValidations.AddListValidation(
                        wsIssues.Cells[row, 1].Address);
                    validation.Formula.Values.Add("TRUE");
                    validation.Formula.Values.Add("FALSE");
                    validation.ShowErrorMessage = true;
                    validation.ErrorTitle = "Invalid";
                    validation.Error = "Select TRUE or FALSE";

                    if (i % 2 == 1)
                    {
                        wsIssues.Cells[row, 1, row, 6].Style.Fill.PatternType = ExcelFillStyle.Solid;
                        wsIssues.Cells[row, 1, row, 6].Style.Fill.BackgroundColor.SetColor(
                            Color.FromArgb(242, 242, 242));
                    }
                }

                // Conditional formatting: strikethrough when Resolved = TRUE
                if (issues.Count > 0)
                {
                    int lastRow = issues.Count + 3;
                    var cfRange = wsIssues.Cells[4, 1, lastRow, 6];
                    var cf = wsIssues.ConditionalFormatting.AddExpression(cfRange);
                    cf.Formula = "$A4=TRUE";
                    cf.Style.Font.Strike = true;
                    cf.Style.Font.Color.Color = Color.Gray;
                }

                wsIssues.Column(1).Width = 12;
                wsIssues.Column(2).Width = 12;
                wsIssues.Column(3).Width = 16;
                wsIssues.Column(4).Width = 24;
                wsIssues.Column(5).Width = 12;
                wsIssues.Column(6).Width = 52;

                // ====== SHEET 3: System Marks ======
                var wsMarks = package.Workbook.Worksheets.Add("System Marks");
                StyleHeader(wsMarks, "A1:B1", $"System Marks Remaining: {systemMarksFound.Count}");

                wsMarks.Cells["A3"].Value = "System Mark";
                wsMarks.Cells["B3"].Value = "Type Prefix";
                StyleTableHeader(wsMarks, "A3:B3");

                for (int i = 0; i < systemMarksFound.Count; i++)
                {
                    int row = i + 4;
                    string mark = systemMarksFound[i];
                    wsMarks.Cells[row, 1].Value = mark;
                    wsMarks.Cells[row, 2].Value = mark.Split('_')[0];

                    if (i % 2 == 1)
                    {
                        wsMarks.Cells[row, 1, row, 2].Style.Fill.PatternType = ExcelFillStyle.Solid;
                        wsMarks.Cells[row, 1, row, 2].Style.Fill.BackgroundColor.SetColor(
                            Color.FromArgb(242, 242, 242));
                    }
                }

                wsMarks.Column(1).Width = 20;
                wsMarks.Column(2).Width = 16;

                package.SaveAs(new FileInfo(outputPath));
            }

            int totalIssues = systemMarkCount + missingDrawingCount + missingBOMCount
                            + bomQuantityIssues + gatherSheetMissing + gatherQtyMismatches;

            Console.WriteLine($"\n  Excel report saved to:\n  {outputPath}");

            if (totalIssues == 0)
                Console.WriteLine("  *** ALL CLEAR — Drawings are complete and verified! ***");
            else
                Console.WriteLine($"  *** {totalIssues} ISSUE(S) FOUND — Review before releasing to shop. ***");

            Console.WriteLine("==========================================================\n");
        }

        // --- Styling Helpers ---
        private static void StyleHeader(ExcelWorksheet ws, string range, string title)
        {
            ws.Cells[range].Merge = true;
            ws.Cells[range].Value = title;
            ws.Cells[range].Style.Font.Size = 16;
            ws.Cells[range].Style.Font.Bold = true;
            ws.Cells[range].Style.Font.Color.SetColor(Color.White);
            ws.Cells[range].Style.Fill.PatternType = ExcelFillStyle.Solid;
            ws.Cells[range].Style.Fill.BackgroundColor.SetColor(Color.FromArgb(44, 62, 80));
            ws.Cells[range].Style.HorizontalAlignment = ExcelHorizontalAlignment.Left;
            ws.Row(1).Height = 36;
            ws.Cells[range].Style.VerticalAlignment = ExcelVerticalAlignment.Center;
        }

        private static void StyleTableHeader(ExcelWorksheet ws, string range)
        {
            ws.Cells[range].Style.Font.Bold = true;
            ws.Cells[range].Style.Font.Color.SetColor(Color.White);
            ws.Cells[range].Style.Fill.PatternType = ExcelFillStyle.Solid;
            ws.Cells[range].Style.Fill.BackgroundColor.SetColor(Color.FromArgb(52, 73, 94));
            ws.Cells[range].Style.Border.Bottom.Style = ExcelBorderStyle.Thin;
        }

        private static void AddSummaryRow(ExcelWorksheet ws, int row, string label, int count, string status)
        {
            ws.Cells[row, 1].Value = label;
            ws.Cells[row, 2].Value = count;

            if (!string.IsNullOrEmpty(status))
            {
                ws.Cells[row, 3].Value = status;
                ws.Cells[row, 3].Style.Font.Bold = true;
                if (status == "PASS")
                    ws.Cells[row, 3].Style.Font.Color.SetColor(Color.FromArgb(39, 174, 96));
                else if (status == "FAIL")
                    ws.Cells[row, 3].Style.Font.Color.SetColor(Color.FromArgb(231, 76, 60));
            }
        }
    }
}
