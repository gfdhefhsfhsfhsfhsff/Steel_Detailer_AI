using System;
using System.Collections.Generic;
using System.Linq;
using DesignData.SDS2.Database;
using DesignData.SDS2.Model;

namespace SDS2Workflow
{
    public class Automator1_BulkPropertyUpdater
    {
        [STAThread]
        public static void Main(string[] args)
        {
            try
            {
                DataDirectory.Open(DataDirectory.Default);

                if (args.Length > 0)
                {
                    RunSilentMode(args);
                }
                else
                {
                    RunInteractiveMode();
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"[FATAL ERROR] {ex.Message}");
            }
        }

        private static void RunSilentMode(string[] args)
        {
            string repoName = null;
            string jobName = null;
            List<string> targetHandles = new List<string>();
            string propName = null;
            string propValue = null;

            for (int i = 0; i < args.Length; i++)
            {
                if (args[i] == "--repo" && i + 1 < args.Length) repoName = args[++i];
                else if (args[i] == "--job" && i + 1 < args.Length) jobName = args[++i];
                else if (args[i] == "--handles" && i + 1 < args.Length)
                {
                    var splitHandles = args[++i].Split(',');
                    foreach(var h in splitHandles)
                    {
                        targetHandles.Add(h.Trim());
                    }
                }
                else if (args[i] == "--prop" && i + 1 < args.Length) propName = args[++i];
                else if (args[i] == "--val" && i + 1 < args.Length) propValue = args[++i];
            }

            if (string.IsNullOrEmpty(repoName) || string.IsNullOrEmpty(jobName) || targetHandles.Count == 0 || string.IsNullOrEmpty(propName))
            {
                Console.WriteLine("[ERROR] Missing required arguments for silent mode.");
                return;
            }

            Console.WriteLine($"[AUTOMATOR-SILENT] Received input to apply '{propName}'='{propValue}' to {targetHandles.Count} members.");

            var repo = Repository.GetAllRepositories().FirstOrDefault(r => r.Name == repoName);
            if (repo == null)
            {
                Console.WriteLine($"[ERROR] Repository '{repoName}' not found.");
                return;
            }

            var jobId = repo.JobIdentifiers.FirstOrDefault(j => j.Name == jobName);
            if (jobId == null)
            {
                Console.WriteLine($"[ERROR] Job '{jobName}' not found in repo '{repoName}'.");
                return;
            }

            var job = Job.FindJob(jobId);
            job.Open();

            List<MemberHandle> memberHandlesToModify = new List<MemberHandle>();

            using (var readTran = new ReadOnlyTransaction(job))
            {
                foreach (var handle in job.Members)
                {
                    if (targetHandles.Contains(handle.ToString()) || targetHandles.Contains(handle.Index.ToString()))
                    {
                        memberHandlesToModify.Add(handle);
                    }
                }
            }

            if (memberHandlesToModify.Count == 0)
            {
                Console.WriteLine("[INFO] No matching members found in the job to apply properties to.");
                return;
            }

            ExecuteTransaction(job, memberHandlesToModify, propName, propValue ?? "");
        }

        private static void RunInteractiveMode()
        {
            var repositories = Repository.GetAllRepositories();
            Console.WriteLine("\n==========================================================");
            Console.WriteLine("  Available Repositories:");
            for (int i = 0; i < repositories.Count; i++)
                Console.WriteLine($"  [{i + 1}] {repositories[i].Name}");

            Console.Write("\n  Select repository number: ");
            if (!int.TryParse(Console.ReadLine().Trim(), out int repoIndex) || repoIndex < 1 || repoIndex > repositories.Count) return;
            var selectedRepo = repositories[repoIndex - 1];

            var jobIds = selectedRepo.JobIdentifiers;
            Console.WriteLine($"\n  Jobs in '{selectedRepo.Name}':");
            for (int i = 0; i < jobIds.Count; i++)
                Console.WriteLine($"  [{i + 1}] {jobIds[i].Name}");

            Console.Write("\n  Select job number: ");
            if (!int.TryParse(Console.ReadLine().Trim(), out int jobIndex) || jobIndex < 1 || jobIndex > jobIds.Count) return;
            var selectedJobId = jobIds[jobIndex - 1];

            Console.Write("\n  Enter Sequence Name to update (e.g. '1', '2A', or 'ALL' to do the whole job): ");
            string targetSeq = Console.ReadLine().Trim();

            Console.Write("  Enter Custom Property Name EXACTLY: ");
            string propName = Console.ReadLine().Trim();

            Console.Write("  Enter Custom Property VALUE to uniformly apply: ");
            string propValue = Console.ReadLine().Trim();

            Console.WriteLine("\n[AUTOMATOR] Preparing to process model...");

            var job = Job.FindJob(selectedJobId);
            job.Open();

            var handlesToModify = new List<MemberHandle>();

            using (var transaction = new ReadOnlyTransaction(job))
            {
                foreach (var handle in job.Members)
                {
                    var memberBrief = MemberBrief.Get(handle);
                    if (targetSeq.ToUpper() == "ALL" || (memberBrief.Sequence != null && memberBrief.Sequence.ToString() == targetSeq))
                    {
                        handlesToModify.Add(handle);
                    }
                }
            }

            if (handlesToModify.Count == 0)
            {
                Console.WriteLine($"[INFO] No members found in Sequence '{targetSeq}'.");
                Console.WriteLine("\nPress Enter to return...");
                Console.ReadLine();
                return;
            }

            Console.WriteLine($"[AUTOMATOR] Found {handlesToModify.Count} members in sequence '{targetSeq}'.");
            ExecuteTransaction(job, handlesToModify, propName, propValue);

            Console.WriteLine("\nPress Enter to return...");
            Console.ReadLine();
        }

        private static void ExecuteTransaction(Job job, List<MemberHandle> handlesToModify, string propName, string propValue)
        {
            int appliedCount = 0;
            int errorCount = 0;

            Console.WriteLine($"[AUTOMATOR] Locking {handlesToModify.Count} members and applying '{propName}' = '{propValue}'...");

            ILockHandler lockHandler = new ImmediateLockHandler();
            using (var writeTransaction = new Transaction(job, lockHandler))
            {
                foreach (var handle in handlesToModify)
                {
                    writeTransaction.Add(handle);
                }

                if (!writeTransaction.Lock())
                {
                    Console.WriteLine("[ERROR] Could not acquire lock on all members. Ensure no one else is editing the job.");
                    return;
                }

                foreach (var handle in handlesToModify)
                {
                    try
                    {
                        var member = Member.Get(handle);
                        var propsHandle = member.CustomPropertyMapHandle;
                        var props = CustomPropertyMap.Get(propsHandle);
                        bool success = props.Set(propName, propValue);
                        if (success) appliedCount++;
                        else errorCount++;
                    }
                    catch (Exception)
                    {
                        errorCount++;
                    }
                }

                var commitStatus = writeTransaction.Commit();
                if (commitStatus)
                {
                    Console.WriteLine($"\n[SUCCESS] Successfully applied property '{propName}' = '{propValue}' to {appliedCount} members.");
                    if (errorCount > 0) Console.WriteLine($"[WARNING] {errorCount} members failed (likely because the property schema doesn't exist for that member type).");
                }
                else
                {
                    Console.WriteLine($"\n[ERROR] Transaction commit failed. Reason: {commitStatus.Reason}");
                }
            }
        }
    }
}
