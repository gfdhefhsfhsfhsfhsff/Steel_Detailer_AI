using System;
using System.Linq;
using DesignData.SDS2.Database;
using DesignData.SDS2.Model;
using DesignData.SDS2.Detail;

namespace SDS2Workflow
{
    public class CheckingScripts
    {
        // =========================================================================
        // MAIN ENTRY POINT
        // =========================================================================
        [STAThread]
        public static void Main(string[] args)
        {
            DataDirectory.Open(DataDirectory.Default);

            var repositories = Repository.GetAllRepositories();
            Console.WriteLine("\n==========================================================");
            Console.WriteLine("  Available Repositories:");
            for (int i = 0; i < repositories.Count; i++)
                Console.WriteLine($"  [{i + 1}] {repositories[i].Name}");

            Console.Write("\n  Select repository number: ");
            if (!int.TryParse((Console.ReadLine() ?? string.Empty).Trim(), out int repoIndex) || repoIndex < 1 || repoIndex > repositories.Count) return;
            var selectedRepo = repositories[repoIndex - 1];

            var jobIds = selectedRepo.JobIdentifiers;
            Console.WriteLine($"\n  Jobs in '{selectedRepo.Name}':");
            for (int i = 0; i < jobIds.Count; i++)
                Console.WriteLine($"  [{i + 1}] {jobIds[i].Name}");

            Console.Write("\n  Select job number: ");
            if (!int.TryParse((Console.ReadLine() ?? string.Empty).Trim(), out int jobIndex) || jobIndex < 1 || jobIndex > jobIds.Count) return;
            var selectedJobId = jobIds[jobIndex - 1];

            Console.Write("\n  Enter Sequence Name to Check (e.g. '1', '2A'): ");
            string targetSequenceName = (Console.ReadLine() ?? string.Empty).Trim();

            VerifyMainMemberDetails(selectedRepo.Name, selectedJobId.Name, targetSequenceName);
            VerifyGatherSheets(selectedRepo.Name, selectedJobId.Name, targetSequenceName);

            Console.WriteLine("\nPress Enter to return...");
            Console.ReadLine();
        }

        // =========================================================================
        // CHECKER 1: Verify Sequence Details & Main BOM
        // Scope: Checks that members in a sequence have detail sheets and valid quantities
        // =========================================================================
        public static void VerifyMainMemberDetails(string repositoryName, string jobName, string targetSequenceName)
        {
            var job = OpenJobAndAuthenticate(repositoryName, jobName);
            if (job == null) return;

            Console.WriteLine($"[CHECKER 1] Starting Detail Sheet & BOM Verification for Sequence: {targetSequenceName}");
            int missingDrawingsCount = 0;
            int bomMismatchesCount = 0;

            using (var transaction = new ReadOnlyTransaction(job))
            {
                foreach (var handle in job.Members)
                {
                    var member = MemberBrief.Get(handle);
                    if (member.Sequence == null || member.Sequence.ToString() != targetSequenceName)
                        continue;

                    var drawings = Drawing.Find(PiecemarkType.Major, member.Piecemark);
                    if (drawings == null || drawings.Count == 0)
                    {
                        Console.WriteLine($"[WARNING] Member {member.Piecemark} is in Sequence {targetSequenceName} but has no drawing/sheet!");
                        missingDrawingsCount++;
                        continue;
                    }

                    var drawing = drawings[0];
                    var bom = drawing.BillOfMaterial;
                    if (bom == null) 
                    {
                        Console.WriteLine($"[WARNING] Drawing for {member.Piecemark} has no BOM object attached.");
                        bomMismatchesCount++;
                        continue;
                    }

                    var bomLines = bom.GetLines();
                    bool foundMainMemberInBOM = false;

                    foreach (var line in bomLines)
                    {
                        if (line.UnitQuantity < 1)
                        {
                            Console.WriteLine($"   [ERROR] Invalid quantity ({line.UnitQuantity}) found on BOM for {member.Piecemark}");
                            bomMismatchesCount++;
                        }
                        
                        // Check if at least one line matches the major piece it belongs to
                        if (line.ToString().Contains(member.Piecemark))
                        {
                            foundMainMemberInBOM = true;
                        }
                    }

                    if (!foundMainMemberInBOM && bomLines.Count > 0)
                    {
                        Console.WriteLine($"[WARNING] The BOM for {member.Piecemark} exists, but the main piecemark label wasn't found in the line items.");
                        bomMismatchesCount++;
                    }
                }
            }

            Console.WriteLine($"[CHECKER 1 COMPLETE] Missing Drawings: {missingDrawingsCount} | BOM Discrepancies: {bomMismatchesCount}\n");
        }

        // =========================================================================
        // CHECKER 2: Verify Advanced Part BOM (Gather Sheets vs Detail Sheets)
        // Scope: Cross-references the detail sheet's required submaterials with the 
        //        actual gather sheets printed for the shop to ensure quantities match.
        // =========================================================================
        public static void VerifyGatherSheets(string repositoryName, string jobName, string targetSequenceName)
        {
            var job = OpenJobAndAuthenticate(repositoryName, jobName);
            if (job == null) return;

            Console.WriteLine($"[CHECKER 2] Starting Gather Sheet Verification for Sequence: {targetSequenceName}");
            int missingGatherSheets = 0;
            int gatherQuantityMismatches = 0;

            using (var transaction = new ReadOnlyTransaction(job))
            {
                foreach (var handle in job.Members)
                {
                    var member = MemberBrief.Get(handle);
                    if (member.Sequence == null || member.Sequence.ToString() != targetSequenceName)
                        continue;

                    var drawings = Drawing.Find(PiecemarkType.Major, member.Piecemark);
                    if (drawings == null || drawings.Count == 0) continue; // Handled by Checker 1

                    var bom = drawings[0].BillOfMaterial;
                    if (bom == null) continue; // Handled by Checker 1

                    var bomLines = bom.GetLines();
                    
                    foreach (var line in bomLines)
                    {
                        // MinorMark denotes a submaterial (e.g., a plate or angle attached to the beam)
                        if (!string.IsNullOrEmpty(line.MinorMark))
                        {
                            var gatherSheets = Drawing.Find(PiecemarkType.Minor, line.MinorMark);
                            
                            if (gatherSheets != null && gatherSheets.Count > 0)
                            {
                                var gatherSheet = gatherSheets[0];
                                uint gatherQty = gatherSheet.Status.Quantity;
                                
                                if (gatherQty < (uint)Math.Max(0, line.TotalQuantity))
                                {
                                    Console.WriteLine($"   [WARNING] Mismatch! Gather sheet for '{line.MinorMark}' quantifies {gatherQty} total, but detail sheet '{member.Piecemark}' dictates {line.TotalQuantity}!");
                                    gatherQuantityMismatches++;
                                }
                            }
                            else
                            {
                                Console.WriteLine($"   [WARNING] Submaterial '{line.MinorMark}' on '{member.Piecemark}' BOM is missing a Gather Sheet!");
                                missingGatherSheets++;
                            }
                        }
                    }
                }
            }

            Console.WriteLine($"[CHECKER 2 COMPLETE] Missing Gather Sheets: {missingGatherSheets} | Quantity Mismatches: {gatherQuantityMismatches}\n");
        }

        // =========================================================================
        // HELPER METHOD: Boilerplate encapsulation
        // =========================================================================
        private static Job OpenJobAndAuthenticate(string repositoryName, string jobName)
        {
            var repositories = Repository.GetAllRepositories();
            Identifier jobId = null;
            
            foreach (var repo in repositories)
            {
                if (repo.Name != repositoryName) continue;
                foreach (var id in repo.JobIdentifiers)
                {
                    if (id.Name == jobName)
                        jobId = id;
                }
            }
            
            if (jobId == null) 
            {
                Console.WriteLine($"Job {jobName} not found in {repositoryName}.");
                return null;
            }

            var job = Job.FindJob(jobId);
            if (job == null)
            {
                Console.WriteLine($"Could not find job '{jobName}'.");
                return null;
            }
            job.Open();
            return job;
        }
    }
}
