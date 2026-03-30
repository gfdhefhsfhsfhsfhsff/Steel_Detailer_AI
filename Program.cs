using System;
using System.Diagnostics;
using SDS2Workflow;

while (true)
{
    Console.Clear();
    Console.WriteLine("==========================================================");
    Console.WriteLine("  Steel Detailer AI - Main Menu");
    Console.WriteLine("==========================================================\n");
    Console.WriteLine("  1. Pre-Detail Model Checker");
    Console.WriteLine("  2. Post-Detail Sheet Checker");
    Console.WriteLine("  3. Verify BOM & Gather Sheets (Basic)");
    Console.WriteLine("  4. Run QA/QC Verification (Python tool)");
    Console.WriteLine("  5. Bulk Custom Property Updater (Automator)");
    Console.WriteLine("  Q. Quit");
    Console.Write("\n  Enter choice: ");
    
    var choice = Console.ReadLine()?.Trim().ToUpper();
    
    Console.WriteLine();
    
    switch(choice)
    {
        case "1":
            PreDetailModelChecker.Main(new string[0]);
            break;
        case "2":
            PostDetailSheetChecker.Main(new string[0]);
            break;
        case "3":
            CheckingScripts.Main(new string[0]);
            break;
        case "4":
            Console.WriteLine("Starting QA/QC Verification script...");
            try
            {
                var process = new Process();
                process.StartInfo.FileName = "python";
                // Assumes "qa_qc_verify\run.py" exists relative to the executable or working dir
                process.StartInfo.Arguments = "\"qa_qc_verify\\run.py\"";
                process.StartInfo.UseShellExecute = false;
                process.Start();
                process.WaitForExit();
            }
            catch(Exception ex)
            {
                Console.WriteLine($"Failed to start Python script: {ex.Message}");
            }
            Console.WriteLine("\nPress Enter to return...");
            Console.ReadLine();
            break;
        case "5":
            Automator1_BulkPropertyUpdater.Main(new string[0]);
            break;
        case "Q":
            Console.WriteLine("Exiting.");
            return;
        default:
            Console.WriteLine("Invalid choice. Press Enter to try again.");
            Console.ReadLine();
            break;
    }
}
