import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import os

try:
    import sds2
    import selection
    IN_SDS2 = True
except ImportError:
    IN_SDS2 = False

def run_automator():
    root = tk.Tk()
    root.withdraw() # Hide the main window
    root.attributes("-topmost", True)
    
    if not IN_SDS2:
        messagebox.showerror("Environment Error", "This script must be launched from INSIDE the SDS/2 application via 'Run Script' or a Toolbar Button.")
        return

    # Get active Job and Repo from SDS2
    repo_name = sds2.utility.GetRepositoryName()
    job_name = sds2.utility.GetJobName()
    
    # 1. Ask what property they want
    prop_name = simpledialog.askstring("Bulk Updater", "Enter the Custom Property name EXACTLY as it appears:", parent=root)
    if not prop_name:
        return
        
    prop_val = simpledialog.askstring("Bulk Updater", f"Enter the value to apply for '{prop_name}':", parent=root)
    if prop_val is None:
        return
        
    # 2. Get Highligted Selection natively from SDS/2
    handles = []
    try:
        sel = selection.MemberSelection()
        handles = [str(m.handle.id) for m in sel]
    except Exception as e:
        messagebox.showerror("Selection Error", f"Could not read native SDS/2 selection: {e}")
        return
            
    if not handles:
        messagebox.showinfo("Bulk Updater", "No members are currently highlighted in your 3D Model.\n\nPlease highlight the members you wish to apply the Custom Property to and try again.")
        return
        
    handles_str = ",".join(handles)
    
    # 3. Path to the C# execution
    # We use 'dotnet run' natively pointing to the C# project
    project_path = r"d:\Steel_Detailer_AI\Steel Detailer AI.csproj"
    
    cmd = [
        "dotnet", "run",
        "--project", project_path,
        "--", 
        "--repo", repo_name,
        "--job", job_name,
        "--handles", handles_str,
        "--prop", prop_name,
        "--val", prop_val
    ]
    
    messagebox.showinfo("Bulk Updater", f"Applying '{prop_name}' = '{prop_val}'\n\nTargeting {len(handles)} highlighted members...\n\n(This may take a moment. Click OK to begin.)", parent=root)
    
    try:
        # Run process seamlessly in the background
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=r"d:\Steel_Detailer_AI")
        
        # Check standard success outputs
        if "SUCCESS" in result.stdout:
            messagebox.showinfo("Success", f"Update completed successfully!\n\nConsole Result:\n{result.stdout.split('[SUCCESS]')[1].strip()}", parent=root)
        else:
            messagebox.showwarning("Notice", f"Tool executed but might have encountered an issue:\n\n{result.stdout}", parent=root)
            
    except Exception as e:
        messagebox.showerror("Execution Error", f"Failed to launch background C# Automator:\n{str(e)}", parent=root)

if __name__ == "__main__":
    run_automator()
