// ============================================================================
// CHECKER 1: Pre-Detailing Model Verification
// Purpose: Run BEFORE sheets are created to verify the model is complete
//          and ready for detailing. Includes a master report showing all
//          piecemarks categorized as User Marks vs System Marks.
//
// OUTPUT: Excel spreadsheet with Summary, Issues, and Master Report sheets.
//         Issues sheet has a "Resolved" checkbox column with strikethrough.
// ============================================================================
using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Text.RegularExpressions;
using DesignData.SDS2.Database;
using DesignData.SDS2.Model;
using OfficeOpenXml;
using OfficeOpenXml.Style;

namespace SDS2Workflow
{
    public class PreDetailModelChecker
    {
        private static readonly Regex SystemMarkPattern = new Regex(
            @"^[A-Z]{1,3}_\d+$", RegexOptions.Compiled);

        // Issue record for Excel output
        private class Issue
        {
            public int MemberNumber { get; set; }
            public string Piecemark { get; set; }
            public string IssueType { get; set; }
            public string Sequence { get; set; }
            public string Details { get; set; }
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

            RunPreDetailCheck(job, selectedJobId.Name, targetSequences);

            Console.WriteLine("\nPress Enter to exit...");
            Console.ReadLine();
        }

        public static void RunPreDetailCheck(Job job, string jobName, List<string> targetSequences)
        {
            Console.WriteLine("==========================================================");
            Console.WriteLine("  CHECKER 1: Pre-Detailing Model Verification");
            Console.WriteLine("==========================================================\n");

            int totalChecked      = 0;
            int notProcessedCount = 0;
            int notModelComplete  = 0;
            int noShapeAssigned   = 0;

            var userMarks   = new List<string>();
            var systemMarks = new List<string>();
            var issues      = new List<Issue>();

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

                    // Categorize mark
                    if (SystemMarkPattern.IsMatch(pcmk))
                    {
                        if (!systemMarks.Contains(pcmk)) systemMarks.Add(pcmk);
                    }
                    else
                    {
                        if (!userMarks.Contains(pcmk)) userMarks.Add(pcmk);
                    }

                    if (member.IsMarkedForProcess)
                    {
                        notProcessedCount++;
                        issues.Add(new Issue
                        {
                            MemberNumber = member.Number,
                            Piecemark = pcmk,
                            IssueType = "NOT PROCESSED",
                            Sequence = seqName,
                            Details = "Member is still marked for process (stale solids)"
                        });
                    }

                    if (member.ModelCompleteDate == null)
                    {
                        notModelComplete++;
                        issues.Add(new Issue
                        {
                            MemberNumber = member.Number,
                            Piecemark = pcmk,
                            IssueType = "NOT MODEL COMPLETE",
                            Sequence = seqName,
                            Details = "No Model Complete date is set"
                        });
                    }

                    if (member.Shape == null)
                    {
                        noShapeAssigned++;
                        issues.Add(new Issue
                        {
                            MemberNumber = member.Number,
                            Piecemark = pcmk,
                            IssueType = "NO SHAPE",
                            Sequence = seqName,
                            Details = "No shape/section size assigned"
                        });
                    }
                }
            }

            // Console summary
            Console.WriteLine($"  Total members checked:       {totalChecked}");
            Console.WriteLine($"  Need processing:             {notProcessedCount}");
            Console.WriteLine($"  Not marked Model Complete:   {notModelComplete}");
            Console.WriteLine($"  Missing shape assignment:    {noShapeAssigned}");

            // Generate Excel
            userMarks.Sort();
            systemMarks.Sort();

            string timestamp = DateTime.Now.ToString("yyyy-MM-dd_HHmmss");
            string fileName = $"Checker1_{jobName}_{timestamp}.xlsx";
            string outputPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, fileName);

            using (var package = new ExcelPackage())
            {
                // ====== SHEET 1: Summary ======
                var wsSummary = package.Workbook.Worksheets.Add("Summary");
                StyleHeader(wsSummary, "A1:B1", "Pre-Detailing Model Verification");

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
                AddSummaryRow(wsSummary, r++, "Need Processing", notProcessedCount,
                    notProcessedCount == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Not Model Complete", notModelComplete,
                    notModelComplete == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Missing Shape", noShapeAssigned,
                    noShapeAssigned == 0 ? "PASS" : "FAIL");
                AddSummaryRow(wsSummary, r++, "Unique User Marks", userMarks.Count, "");
                AddSummaryRow(wsSummary, r++, "Unique System Marks", systemMarks.Count, "");

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
                    wsIssues.Cells[row, 1].Value = false;  // Resolved checkbox
                    wsIssues.Cells[row, 2].Value = issues[i].MemberNumber;
                    wsIssues.Cells[row, 3].Value = issues[i].Piecemark;
                    wsIssues.Cells[row, 4].Value = issues[i].IssueType;
                    wsIssues.Cells[row, 5].Value = issues[i].Sequence;
                    wsIssues.Cells[row, 6].Value = issues[i].Details;

                    // Data validation for checkbox column (TRUE/FALSE dropdown)
                    var validation = wsIssues.DataValidations.AddListValidation(
                        wsIssues.Cells[row, 1].Address);
                    validation.Formula.Values.Add("TRUE");
                    validation.Formula.Values.Add("FALSE");
                    validation.ShowErrorMessage = true;
                    validation.ErrorTitle = "Invalid";
                    validation.Error = "Select TRUE or FALSE";

                    // Alternate row shading
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
                wsIssues.Column(6).Width = 44;

                // ====== SHEET 3: Master Report ======
                var wsMaster = package.Workbook.Worksheets.Add("Master Report");
                StyleHeader(wsMaster, "A1:D1", "Piecemark Master Report");

                wsMaster.Cells["A3"].Value = "User Marks";
                wsMaster.Cells["C3"].Value = "System Marks";
                StyleTableHeader(wsMaster, "A3:A3");
                StyleTableHeader(wsMaster, "C3:C3");

                for (int i = 0; i < Math.Max(userMarks.Count, systemMarks.Count); i++)
                {
                    int row = i + 4;
                    if (i < userMarks.Count)
                        wsMaster.Cells[row, 1].Value = userMarks[i];
                    if (i < systemMarks.Count)
                        wsMaster.Cells[row, 3].Value = systemMarks[i];
                }

                wsMaster.Cells[3, 2].Value = $"({userMarks.Count})";
                wsMaster.Cells[3, 4].Value = $"({systemMarks.Count})";

                wsMaster.Column(1).Width = 20;
                wsMaster.Column(2).Width = 8;
                wsMaster.Column(3).Width = 20;
                wsMaster.Column(4).Width = 8;

                package.SaveAs(new FileInfo(outputPath));
            }

            Console.WriteLine($"\n  Excel report saved to:\n  {outputPath}");
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
                {
                    ws.Cells[row, 3].Style.Font.Color.SetColor(Color.FromArgb(39, 174, 96));
                }
                else if (status == "FAIL")
                {
                    ws.Cells[row, 3].Style.Font.Color.SetColor(Color.FromArgb(231, 76, 60));
                }
            }
        }
    }
}
