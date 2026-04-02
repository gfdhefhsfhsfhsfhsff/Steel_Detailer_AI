"""
SDS/2 QA/QC Verification Plugin
================================
Evaluates the currently open SDS/2 model. No hardcoded paths or project lists.

Inside SDS/2 (toolbar / Run Script):
  - Auto-detects active job via DataDirectory.Default / Job.Default
  - Reads all members, drawings, BOMs from the live model
  - Runs 4 verification phases using DesignData.SDS2.* API
  - Generates HTML + JSON + CSV reports

Install as toolbar button:
  1. SDS/2 > Tools > Customize > Toolbar > Add Button
  2. Script: <path_to_this_file>
  3. Label: QA/QC

Author: John May
Version: 1.1.0
"""

import os
import sys
import time
from datetime import datetime

try:
    import sds2
    import selection

    IN_SDS2 = True
except ImportError:
    IN_SDS2 = False

_REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)


def _output_dir():
    d = os.path.join(_REPO_ROOT, "qa_output")
    os.makedirs(d, exist_ok=True)
    return d


def _ts():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def _fmt(seconds):
    if seconds < 60:
        return f"{seconds:.1f}s"
    if seconds < 3600:
        return f"{int(seconds / 60)}m {int(seconds % 60)}s"
    return f"{int(seconds / 3600)}h {int((seconds % 3600) / 60)}m"


import tkinter as tk
from tkinter import messagebox


class QAQCPlugin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QA/QC Verification")
        self.root.attributes("-topmost", True)
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        self.root.protocol("WM_DELETE_WINDOW", self._close)
        self._running = False
        self._build()

    def _build(self):
        px = {"padx": 16, "pady": 4}

        tk.Label(
            self.root,
            text="QA/QC Verification",
            font=("Segoe UI", 16, "bold"),
            fg="white",
            bg="#2c3e50",
        ).pack(pady=(16, 2), padx=20)

        env = "Inside SDS/2" if IN_SDS2 else "Standalone (no SDS/2)"
        env_clr = "#27ae60" if IN_SDS2 else "#e67e22"
        tk.Label(
            self.root,
            text=env,
            font=("Segoe UI", 10),
            fg=env_clr,
            bg="#2c3e50",
        ).pack()

        tk.Label(
            self.root,
            text="\u2500" * 40,
            fg="#7f8c8d",
            bg="#2c3e50",
            font=("Consolas", 8),
        ).pack(pady=(4, 0))

        if IN_SDS2:
            self._build_inprocess(px)
        else:
            self._build_standalone(px)

    def _build_inprocess(self, px):
        try:
            repo = sds2.utility.GetRepositoryName()
            job = sds2.utility.GetJobName()
        except Exception:
            repo, job = "Unknown", "Unknown"

        info = tk.Frame(self.root, bg="#34495e", relief="groove", bd=1)
        info.pack(fill="x", **px)
        for lbl, val in [("Job", job), ("Repository", repo)]:
            tk.Label(
                info,
                text=lbl,
                font=("Segoe UI", 9, "bold"),
                fg="#bdc3c7",
                bg="#34495e",
                anchor="w",
            ).pack(fill="x", padx=10, pady=(6, 0))
            tk.Label(
                info,
                text=f"  {val}",
                font=("Consolas", 10),
                fg="#ecf0f1",
                bg="#34495e",
                anchor="w",
            ).pack(fill="x", padx=10)

        try:
            sel = selection.MemberSelection()
            self._sel_handles = [str(m.handle.id) for m in sel]
            n = len(self._sel_handles)
        except Exception:
            self._sel_handles = []
            n = 0

        sel_txt = f"  {n} members selected" if n else "  No selection (will verify ALL)"
        sel_clr = "#27ae60" if n else "#95a5a6"
        tk.Label(
            info,
            text=sel_txt,
            font=("Consolas", 10),
            fg=sel_clr,
            bg="#34495e",
            anchor="w",
        ).pack(fill="x", padx=10, pady=(0, 8))

        ckbx = tk.Frame(self.root, bg="#2c3e50")
        ckbx.pack(fill="x", **px)
        tk.Label(
            ckbx,
            text="Checks:",
            font=("Segoe UI", 10, "bold"),
            fg="#ecf0f1",
            bg="#2c3e50",
            anchor="w",
        ).pack(fill="x")
        self._chk = {}
        for key, label in [
            ("marks", "Mark Verification (system marks)"),
            ("sheets", "Sheet Boundary Check"),
            ("erection", "Erection Plan Continuity"),
            ("bom", "BOM Reconciliation"),
        ]:
            v = tk.BooleanVar(value=True)
            self._chk[key] = v
            tk.Checkbutton(
                ckbx,
                text=label,
                variable=v,
                font=("Consolas", 9),
                fg="#ecf0f1",
                bg="#2c3e50",
                selectcolor="#34495e",
                activebackground="#2c3e50",
                activeforeground="#ecf0f1",
                anchor="w",
            ).pack(fill="x", padx=8)

        bf = tk.Frame(self.root, bg="#2c3e50")
        bf.pack(fill="x", pady=(12, 16), padx=16)
        self._run_btn = tk.Button(
            bf,
            text="Run Verification",
            command=self._run_inprocess,
            font=("Segoe UI", 11, "bold"),
            bg="#27ae60",
            fg="white",
            width=22,
            relief="flat",
            cursor="hand2",
        )
        self._run_btn.pack(side="left", padx=(0, 8))
        tk.Button(
            bf,
            text="Close",
            command=self._close,
            font=("Segoe UI", 10),
            bg="#7f8c8d",
            fg="white",
            width=10,
            relief="flat",
            cursor="hand2",
        ).pack(side="left")

        self._status = tk.Label(
            self.root,
            text="Ready",
            font=("Segoe UI", 9),
            fg="#bdc3c7",
            bg="#2c3e50",
            anchor="w",
        )
        self._status.pack(fill="x", padx=16, pady=(0, 12))

    def _build_standalone(self, px):
        info = tk.Frame(self.root, bg="#34495e", relief="groove", bd=1)
        info.pack(fill="x", **px)
        tk.Label(
            info,
            text="Standalone portfolio scan (KISS-based)",
            font=("Segoe UI", 10, "bold"),
            fg="#ecf0f1",
            bg="#34495e",
            anchor="w",
        ).pack(fill="x", padx=10, pady=(8, 4))
        tk.Label(
            info,
            text="Point scan_runner at any project root.\nNo hardcoded paths.",
            font=("Consolas", 9),
            fg="#bdc3c7",
            bg="#34495e",
            anchor="w",
            wraplength=400,
            justify="left",
        ).pack(fill="x", padx=10, pady=(0, 8))

        bf = tk.Frame(self.root, bg="#2c3e50")
        bf.pack(fill="x", pady=(12, 16), padx=16)

        tk.Label(
            bf, text="Projects root:", font=("Segoe UI", 9), fg="#bdc3c7", bg="#2c3e50"
        ).pack(side="left")
        self._root_var = tk.StringVar(value=os.getcwd())
        tk.Entry(bf, textvariable=self._root_var, width=40, font=("Consolas", 9)).pack(
            side="left", padx=4
        )

        bf2 = tk.Frame(self.root, bg="#2c3e50")
        bf2.pack(fill="x", pady=(0, 16), padx=16)

        self._run_btn = tk.Button(
            bf2,
            text="Run Scan",
            command=self._run_standalone,
            font=("Segoe UI", 11, "bold"),
            bg="#3498db",
            fg="white",
            width=18,
            relief="flat",
            cursor="hand2",
        )
        self._run_btn.pack(side="left", padx=(0, 8))
        tk.Button(
            bf2,
            text="Close",
            command=self._close,
            font=("Segoe UI", 10),
            bg="#7f8c8d",
            fg="white",
            width=10,
            relief="flat",
            cursor="hand2",
        ).pack(side="left")

        self._status = tk.Label(
            self.root,
            text="Ready",
            font=("Segoe UI", 9),
            fg="#bdc3c7",
            bg="#2c3e50",
            anchor="w",
        )
        self._status.pack(fill="x", padx=16, pady=(0, 12))

    def _msg(self, text):
        self._status.config(text=text)
        self.root.update_idletasks()

    def _close(self):
        if not self._running:
            try:
                self.root.destroy()
            except Exception:
                pass

    def _run_inprocess(self):
        if self._running:
            return
        self._running = True
        self._run_btn.config(state="disabled", bg="#95a5a6")

        out = _output_dir()
        ts = _ts()
        html = os.path.join(out, f"qaqc_{ts}.html")
        json = os.path.join(out, f"qaqc_{ts}.json")

        try:
            self._msg("Connecting to SDS/2...")
            from qa_qc_verify.run import run_verification

            checks = [k for k, v in self._chk.items() if v.get()]
            if not checks:
                checks = ["marks", "sheets", "erection", "bom"]

            report = run_verification(
                output_dir=out,
                checks=checks,
            )

            errors = report.error_count
            warnings = report.warning_count
            total = report.total_issues

            self._show_results(
                html,
                json,
                report.job_name,
                report.summary.get("total_issues", total),
                errors,
                warnings,
            )

        except Exception as e:
            messagebox.showerror(
                "Error", f"Verification failed:\n\n{e}", parent=self.root
            )
        finally:
            self._running = False
            self._run_btn.config(state="normal", bg="#27ae60")
            self._msg("Ready")

    def _run_standalone(self):
        if self._running:
            return
        self._running = True
        self._run_btn.config(state="disabled", bg="#95a5a6")

        root = self._root_var.get().strip()
        out = _output_dir()

        try:
            if not os.path.isdir(root):
                messagebox.showerror(
                    "Not Found", f"Directory does not exist:\n{root}", parent=self.root
                )
                return

            self._msg("Scanning...")
            from qa_qc_verify.scan_runner import run_full_scan

            results = run_full_scan(root, out)

            if not results.get("success"):
                messagebox.showerror(
                    "Failed", f"Scan error: {results.get('error')}", parent=self.root
                )
                return

            self._show_scan_results(results, out)

        except Exception as e:
            messagebox.showerror("Error", f"Scan failed:\n\n{e}", parent=self.root)
        finally:
            self._running = False
            self._run_btn.config(state="normal", bg="#3498db")
            self._msg("Ready")

    def _show_results(self, html, json, job, total, errors, warnings):
        w = tk.Toplevel(self.root)
        w.title("Results")
        w.attributes("-topmost", True)
        w.resizable(False, False)
        w.configure(bg="#2c3e50")

        tk.Label(
            w,
            text="Verification Complete",
            font=("Segoe UI", 16, "bold"),
            fg="white",
            bg="#2c3e50",
        ).pack(pady=(16, 4), padx=20)
        tk.Label(
            w, text=f"Job: {job}", font=("Consolas", 10), fg="#bdc3c7", bg="#2c3e50"
        ).pack()

        sf = tk.Frame(w, bg="#2c3e50")
        sf.pack(fill="x", padx=20, pady=12)
        for val, lbl, clr in [
            (str(total), "Issues", "#e74c3c" if total else "#27ae60"),
            (str(errors), "Errors", "#e74c3c" if errors else "#27ae60"),
            (str(warnings), "Warnings", "#f39c12" if warnings else "#27ae60"),
        ]:
            c = tk.Frame(sf, bg="#34495e", relief="groove", bd=1)
            c.pack(side="left", expand=True, fill="x", padx=4)
            tk.Label(
                c, text=val, font=("Segoe UI", 18, "bold"), fg=clr, bg="#34495e"
            ).pack(pady=(8, 0))
            tk.Label(
                c, text=lbl, font=("Segoe UI", 9), fg="#bdc3c7", bg="#34495e"
            ).pack(pady=(0, 8))

        bf = tk.Frame(w, bg="#2c3e50")
        bf.pack(fill="x", pady=(4, 16), padx=20)

        def _open(p):
            if os.path.exists(p):
                os.startfile(p)

        def _folder():
            d = os.path.dirname(html)
            if os.path.isdir(d):
                os.startfile(d)

        for txt, cmd, bg in [
            ("Open Report", lambda: _open(html), "#27ae60"),
            ("Open JSON", lambda: _open(json), "#3498db"),
            ("Open Folder", _folder, "#8e44ad"),
            ("Close", w.destroy, "#7f8c8d"),
        ]:
            tk.Button(
                bf,
                text=txt,
                command=cmd,
                font=("Segoe UI", 10),
                bg=bg,
                fg="white",
                width=12,
                relief="flat",
                cursor="hand2",
            ).pack(side="left", padx=3)

    def _show_scan_results(self, results, out):
        w = tk.Toplevel(self.root)
        w.title("Scan Results")
        w.attributes("-topmost", True)
        w.resizable(False, False)
        w.configure(bg="#2c3e50")

        tk.Label(
            w,
            text="Scan Complete",
            font=("Segoe UI", 16, "bold"),
            fg="white",
            bg="#2c3e50",
        ).pack(pady=(16, 4), padx=20)

        p = results.get("projects_scanned", {})
        r = results.get("releases", {})
        iss = results.get("issues", [])

        sf = tk.Frame(w, bg="#2c3e50")
        sf.pack(fill="x", padx=20, pady=12)
        for val, lbl, clr in [
            (str(p.get("total", 0)), "Projects", "#2c3e50"),
            (str(r.get("parsed_successfully", 0)), "Parsed", "#27ae60"),
            (str(len(iss)), "Issues", "#e74c3c" if iss else "#27ae60"),
        ]:
            c = tk.Frame(sf, bg="#34495e", relief="groove", bd=1)
            c.pack(side="left", expand=True, fill="x", padx=4)
            tk.Label(
                c, text=val, font=("Segoe UI", 14, "bold"), fg=clr, bg="#34495e"
            ).pack(pady=(6, 0))
            tk.Label(
                c, text=lbl, font=("Segoe UI", 8), fg="#bdc3c7", bg="#34495e"
            ).pack(pady=(0, 6))

        html = results.get("html_report", "")
        json = results.get("json_report", "")
        bf = tk.Frame(w, bg="#2c3e50")
        bf.pack(fill="x", pady=(8, 16), padx=20)

        def _open(p):
            if os.path.exists(p):
                os.startfile(p)

        for txt, cmd, bg in [
            ("Open Report", lambda: _open(html), "#27ae60"),
            ("Open JSON", lambda: _open(json), "#3498db"),
            (
                "Open Folder",
                lambda: os.startfile(out) if os.path.isdir(out) else None,
                "#8e44ad",
            ),
            ("Close", w.destroy, "#7f8c8d"),
        ]:
            tk.Button(
                bf,
                text=txt,
                command=cmd,
                font=("Segoe UI", 10),
                bg=bg,
                fg="white",
                width=12,
                relief="flat",
                cursor="hand2",
            ).pack(side="left", padx=3)

    def run(self):
        self.root.mainloop()


def _cli():
    if len(sys.argv) > 1 and sys.argv[1].lower().strip("-/") == "scan":
        root = sys.argv[2] if len(sys.argv) > 2 else "./qa_output"
        out = sys.argv[0]
        from qa_qc_verify.scan_runner import main

        main()
    else:
        QAQCPlugin().run()


if __name__ == "__main__":
    _cli()
