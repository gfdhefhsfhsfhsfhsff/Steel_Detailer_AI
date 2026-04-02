from __future__ import annotations

"""
Main entry point for QA/QC verification.
Works on whatever job is currently open in SDS/2.
No config file required — auto-detects job from the active SDS/2 session.
Version: 1.1.0
"""

import os
import sys
import time
from typing import Dict, List, Optional, Any
from datetime import datetime

from .report import QAReport
from .checks.mark_verification import verify_marks
from .checks.sheet_boundary import verify_sheet_boundaries
from .checks.erection_continuity import verify_erection_continuity
from .checks.bom_reconciliation import verify_bom_reconciliation
from .utils import ProgressTracker
from .error_prompts import print_error

try:
    from DesignData.SDS2.Database import (
        Job,
        DataDirectory,
        ReadOnlyTransaction,
    )
    from DesignData.SDS2.Detail import Drawing, DrawingList

    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False


def _auto_open_job() -> tuple:
    try:
        DataDirectory.Open(DataDirectory.Default)
    except Exception as e:
        return None, str(e)

    try:
        job_id = Job.Default
        job = Job.FindJob(job_id)
        if job:
            return job, None
    except Exception:
        pass

    return None, "No default job found"


def run_verification(
    config_path: Optional[str] = None,
    output_dir: Optional[str] = None,
    checks: Optional[List[str]] = None,
    page_margin_inches: float = 0.5,
    system_patterns: Optional[List[str]] = None,
) -> QAReport:
    """
    Run QA/QC verification on the currently open SDS/2 job.

    No config file or hardcoded paths needed. Auto-detects the active job
    from the SDS/2 session and evaluates whatever model is loaded.

    Args:
        config_path: Optional path to config JSON (overrides auto-detect)
        output_dir: Where to write reports (default: ./qa_output)
        checks: List of check names to run. Default: all.
                     Options: 'marks', 'sheets', 'erection', 'bom'
        page_margin_inches: Sheet margin for boundary check (default: 0.5)
        system_patterns: Regex patterns for system mark detection
    """
    start_time = time.time()

    if output_dir is None:
        output_dir = os.path.join(os.getcwd(), "qa_output")
    os.makedirs(output_dir, exist_ok=True)

    if checks is None:
        checks = ["marks", "sheets", "erection", "bom"]

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    html_path = os.path.join(output_dir, f"qaqc_{ts}.html")
    json_path = os.path.join(output_dir, f"qaqc_{ts}.json")
    csv_path = os.path.join(output_dir, f"qaqc_{ts}.csv")

    if not API_AVAILABLE:
        report = QAReport(job_name="Unknown", run_timestamp=datetime.now())
        report.add_error(
            module="Core",
            object_type="System",
            location="N/A",
            description="SDS/2 API not available. This tool must run inside SDS/2.",
            detail={"hint": "Launch via Run Script or a toolbar button inside SDS/2"},
        )
        return report

    job, job_error = _auto_open_job()
    if job_error:
        report = QAReport(job_name="Unknown", run_timestamp=datetime.now())
        report.add_error(
            module="Core",
            object_type="Job",
            location="N/A",
            description=f"Could not open job: {job_error}",
            detail={},
        )
        return report

    job_name = str(job) if job else "Unknown"
    report = QAReport(job_name=job_name, run_timestamp=datetime.now())

    from .config import Config

    config = Config.from_dict(
        {
            "job_name": job_name,
            "output_path": html_path,
            "page_margin_inches": page_margin_inches,
        }
    )
    if system_patterns:
        config._raw_config["system_patterns"] = system_patterns

    if config_path and os.path.exists(config_path):
        try:
            config = Config(config_path)
        except Exception:
            pass

    member_handles = job.Members
    total_members = len(member_handles)

    if total_members == 0:
        report.add_warning(
            module="Core",
            object_type="Job",
            location="N/A",
            description="Job has no members to verify",
            detail={"job_name": job_name},
        )
        return report

    print(f"QA/QC Verification: {job_name}")
    print(f"  Members: {total_members}")
    print(f"  Checks: {', '.join(checks)}")
    print()

    tracker = ProgressTracker(total_steps=total_members)

    if "marks" in checks:
        print("Phase 1: Mark Verification")
        report = verify_marks(job, report, config)
        print(f"  {report.error_count} errors, {report.warning_count} warnings")

    if "sheets" in checks:
        print("Phase 2: Sheet Boundary Check")
        report = verify_sheet_boundaries(job, report, config)
        print(f"  {report.error_count} errors, {report.warning_count} warnings")

    if "erection" in checks:
        print("Phase 3: Erection Plan Continuity")
        report = verify_erection_continuity(job, report, config)
        print(f"  {report.error_count} errors, {report.warning_count} warnings")

    if "bom" in checks:
        print("Phase 4: BOM Reconciliation")
        report = verify_bom_reconciliation(job, report, config)
        print(f"  {report.error_count} errors, {report.warning_count} warnings")

    print("Generating reports...")
    try:
        report.to_html(html_path)
        report.to_json(json_path)
        try:
            report.to_csv(csv_path)
        except Exception:
            pass
    except Exception as e:
        print(f"Report generation error: {e}")

    elapsed = time.time() - start_time
    summary = report.summary
    print()
    print(f"{'=' * 50}")
    print(f"Job: {job_name}")
    print(f"Members checked: {total_members}")
    print(f"Total issues: {summary['total_issues']}")
    print(f"  Errors:   {report.error_count}")
    print(f"  Warnings: {report.warning_count}")
    print(f"Duration: {tracker.format_time(elapsed)}")
    print(f"Report: {html_path}")
    print(f"{'=' * 50}")

    return report


if __name__ == "__main__":
    run_verification()
