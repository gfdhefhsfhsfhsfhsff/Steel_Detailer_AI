import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import glob

try:
    import sds2
    import selection

    IN_SDS2 = True
except ImportError:
    IN_SDS2 = False


def find_latest_report(output_dir):
    pattern = os.path.join(output_dir, "Checker1_*.xlsx")
    files = glob.glob(pattern)
    if not files:
        return None
    files.sort(key=os.path.getmtime, reverse=True)
    return files[0]


def show_color_legend(root, report_path, issues_count, colored_count, total_checked):
    legend = tk.Toplevel(root)
    legend.title("Checker 1 Results")
    legend.attributes("-topmost", True)
    legend.resizable(False, False)
    legend.configure(bg="#2c3e50")

    pad = {"padx": 16, "pady": 4}

    header = tk.Label(
        legend,
        text="Checker 1 Results",
        font=("Segoe UI", 16, "bold"),
        fg="white",
        bg="#2c3e50",
    )
    header.pack(pady=(16, 4), **{"padx": 16})

    sep = tk.Label(
        legend, text="=" * 40, fg="#95a5a6", bg="#2c3e50", font=("Consolas", 10)
    )
    sep.pack()

    summary_frame = tk.Frame(legend, bg="#2c3e50")
    summary_frame.pack(fill="x", **pad)

    summary_lines = [
        f"Members checked:  {total_checked}",
        f"Issues found:     {issues_count}",
        f"Members colored:  {colored_count}",
    ]
    for line in summary_lines:
        tk.Label(
            summary_frame,
            text=line,
            font=("Consolas", 10),
            fg="#ecf0f1",
            bg="#2c3e50",
            anchor="w",
        ).pack(fill="x")

    tk.Label(legend, text="", bg="#2c3e50").pack(pady=2)

    red_frame = tk.Frame(legend, bg="#2c3e50")
    red_frame.pack(fill="x", **pad)
    tk.Label(
        red_frame,
        text="  RED  ",
        bg="#e74c3c",
        fg="white",
        font=("Consolas", 10, "bold"),
    ).pack(side="left")
    tk.Label(
        red_frame,
        text="  Issues Found (see report)",
        font=("Consolas", 10),
        fg="#ecf0f1",
        bg="#2c3e50",
    ).pack(side="left", padx=8)

    tk.Label(legend, text="", bg="#2c3e50").pack(pady=2)

    checks_frame = tk.Frame(legend, bg="#34495e", relief="groove", bd=1)
    checks_frame.pack(fill="x", **pad)

    tk.Label(
        checks_frame,
        text="Checks performed:",
        font=("Segoe UI", 10, "bold"),
        fg="#ecf0f1",
        bg="#34495e",
        anchor="w",
    ).pack(fill="x", padx=8, pady=(8, 4))

    checks = [
        "Not Processed",
        "Not Model Complete",
        "No Shape Assigned",
        "Missing Field Bolts",
        "Missing Shop Bolts",
        "Mismatched Holes",
        "Missing Holes",
        "Galvanized Mismatch",
        "Missing Connection",
        "Forced Connection",
        "User Connection",
        "Base/Cap Plate Schedule",
        "Embeds",
        "Forced User Piecemarks",
        "Graphical Connections",
        "Moment Connections",
        "Shear Tab Connections",
        "Clip Angle Connections",
        "End Plate Connections",
        "VBrace User Entered Load",
        "Beam User Entered Load",
    ]
    for check in checks:
        tk.Label(
            checks_frame,
            text=f"  - {check}",
            font=("Consolas", 9),
            fg="#bdc3c7",
            bg="#34495e",
            anchor="w",
        ).pack(fill="x", padx=8)

    tk.Label(checks_frame, text="", bg="#34495e").pack(pady=2)

    btn_frame = tk.Frame(legend, bg="#2c3e50")
    btn_frame.pack(fill="x", pady=(8, 16), padx=16)

    def open_report():
        if report_path and os.path.exists(report_path):
            os.startfile(report_path)
        else:
            messagebox.showwarning(
                "Report Not Found",
                "No Checker1 Excel report was found in the output directory.",
                parent=legend,
            )

    if report_path:
        tk.Button(
            btn_frame,
            text="Open Report",
            command=open_report,
            font=("Segoe UI", 10),
            bg="#27ae60",
            fg="white",
            width=14,
            relief="flat",
        ).pack(side="left", padx=(0, 8))

    tk.Button(
        btn_frame,
        text="Close",
        command=legend.destroy,
        font=("Segoe UI", 10),
        bg="#7f8c8d",
        fg="white",
        width=14,
        relief="flat",
    ).pack(side="left")


def show_progress(root, title, message):
    progress_win = tk.Toplevel(root)
    progress_win.title(title)
    progress_win.attributes("-topmost", True)
    progress_win.resizable(False, False)
    progress_win.configure(bg="#2c3e50")

    tk.Label(
        progress_win,
        text=title,
        font=("Segoe UI", 14, "bold"),
        fg="white",
        bg="#2c3e50",
    ).pack(pady=(20, 8), padx=30)

    msg_label = tk.Label(
        progress_win,
        text=message,
        font=("Segoe UI", 10),
        fg="#bdc3c7",
        bg="#2c3e50",
        wraplength=400,
        justify="left",
    )
    msg_label.pack(pady=(0, 20), padx=30)

    progress_win.update()
    return progress_win


def run_standalone():
    _script_dir = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.join(_script_dir, "Checker1", "Checker1.csproj")

    if not os.path.exists(project_path):
        print(f"ERROR: Checker1 project not found at:\n  {project_path}")
        print("Please build the project first.")
        return

    cmd = ["dotnet", "run", "--project", project_path]

    try:
        subprocess.run(cmd, cwd=os.path.dirname(project_path))
    except Exception as e:
        print(f"Failed to launch Checker1: {e}")


def run_checker():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    if not IN_SDS2:
        print(
            "Not running inside SDS/2. Launching Checker1 in standalone console mode...\n"
        )
        root.destroy()
        run_standalone()
        return

    _script_dir = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.join(_script_dir, "Checker1", "Checker1.csproj")

    if not os.path.exists(project_path):
        messagebox.showerror(
            "Missing Executable",
            f"Checker1 project not found at:\n\n{project_path}\n\n"
            "Please build the C# Checker1 project first.",
            parent=root,
        )
        return

    repo_name = sds2.utility.GetRepositoryName()
    job_name = sds2.utility.GetJobName()

    members_str = ""
    selected_handles = []

    try:
        sel = selection.MemberSelection()
        selected_handles = [str(m.handle.id) for m in sel]
    except Exception:
        selected_handles = []

    if selected_handles:
        members_str = ",".join(selected_handles)
        confirm = messagebox.askyesno(
            "Checker 1: Selection Found",
            f"{len(selected_handles)} members are highlighted in the 3D model.\n\n"
            f"Run Checker 1 on these members only?\n\n"
            "Click 'No' to check ALL members in the job.",
            parent=root,
        )
        if not confirm:
            members_str = ""
    else:
        confirm = messagebox.askyesno(
            "Checker 1: No Selection",
            "No members are highlighted in the 3D model.\n\n"
            "Run Checker 1 on ALL members in the job?",
            parent=root,
        )
        if not confirm:
            return

    target_label = (
        f"{len(selected_handles)} selected members" if members_str else "ALL members"
    )

    cmd = [
        "dotnet",
        "run",
        "--project",
        project_path,
        "--",
        "--repo",
        repo_name,
        "--job",
        job_name,
        "--apply-colors",
        "--color",
        "red",
    ]
    if members_str:
        cmd.extend(["--members", members_str])

    progress_win = show_progress(
        root,
        "Checker 1 Running...",
        f"Running Pre-Detail Model Verification...\n\n"
        f"Job: {job_name}\n"
        f"Target: {target_label}\n"
        f"Color: RED for issues\n\n"
        "Please wait, this may take a moment.",
    )

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=os.path.dirname(project_path)
        )
        progress_win.destroy()

        issues_count = 0
        colored_count = 0
        total_checked = 0

        for line in result.stdout.splitlines():
            stripped = line.strip()
            if "Issues Found:" in stripped or "issues found" in stripped.lower():
                parts = stripped.split(":")
                if len(parts) > 1:
                    try:
                        issues_count = int(parts[-1].strip())
                    except ValueError:
                        pass
            if "Members colored:" in stripped or "colored" in stripped.lower():
                parts = stripped.split(":")
                if len(parts) > 1:
                    try:
                        colored_count = int(parts[-1].strip())
                    except ValueError:
                        pass
            if (
                "Total members checked:" in stripped
                or "members checked" in stripped.lower()
            ):
                parts = stripped.split(":")
                if len(parts) > 1:
                    try:
                        total_checked = int(parts[-1].strip())
                    except ValueError:
                        pass

        if total_checked == 0 and "Total members checked:" in result.stdout:
            for line in result.stdout.splitlines():
                stripped = line.strip()
                if "Total members checked" in stripped:
                    try:
                        total_checked = int(stripped.split()[-1])
                    except ValueError:
                        pass

        output_dir = os.path.join(os.path.dirname(project_path), "bin")
        report_path = find_latest_report(output_dir)

        if not report_path:
            bin_debug = os.path.join(output_dir, "Debug")
            report_path = find_latest_report(bin_debug)

        if not report_path:
            bin_release = os.path.join(output_dir, "Release")
            report_path = find_latest_report(bin_release)

        if not report_path:
            report_path = find_latest_report(os.path.dirname(project_path))

        show_color_legend(root, report_path, issues_count, colored_count, total_checked)
        root.mainloop()

    except Exception as e:
        try:
            progress_win.destroy()
        except Exception:
            pass
        messagebox.showerror(
            "Execution Error",
            f"Failed to launch Checker1:\n{str(e)}",
            parent=root,
        )


if __name__ == "__main__":
    run_checker()
