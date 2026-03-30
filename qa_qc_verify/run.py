"""
Main entry point for Runs all verification modules
Author: John May
Version: 1.0.0-alpha
"""

import sys
import time
from typing import Dict, List, Optional
from datetime import datetime

from .config import Config
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
        MemberHandleList,
        DrawingHandleList,
        TableWithDrawings,
        ReadOnlyTransaction,
    )
    from DesignData.SDS2.Detail import Drawing, DrawingList

    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False


def run_verification(config_path: Optional[str] = None) -> QAReport:
    """
    Main entry point for the QA/QC verification tool.
    Orchestrates all verification checks and generates a comprehensive discrepancy report.

    Args:
        config_path: Path to configuration JSON file (default: 'qa_config.json')
    """
    start_time = time.time()

    config = Config(config_path)

    if config.fabricator_id:
        db_connected = config.connect_db()
        if not db_connected:
            print_error("DB_001")

    report = QAReport(job_name=config.job_name, run_timestamp=datetime.now())

    if not API_AVAILABLE:
        print_error("API_001", "DesignData.SDS2 modules not found")
        report.add_error(
            module="Core",
            object_type="System",
            location="N/A",
            description="SDS/2 API not available - cannot perform verification",
            detail={"hint": "Run this script from within SDS/2"},
        )
        return report

    if not config.validate_paths():
        print_error("CFG_003", f"data_directory: {config.data_directory}")
        report.add_error(
            module="Core",
            object_type="Config",
            location="N/A",
            description="Configuration paths are invalid",
            detail={"data_directory": config.data_directory},
        )

    tracker = ProgressTracker(total_steps=5)

    try:
        print(f"Opening job: {config.job_name}")

        job = Job.Open(config.job_name)
        if not job:
            print_error("API_002", f"job_name: {config.job_name}")
            report.add_error(
                module="Core",
                object_type="Job",
                location="N/A",
                description=f"Could not open job: {config.job_name}",
                detail={"job_name": config.job_name},
            )
            return report

        member_handles = job.Members
        total_members = len(member_handles)

        if total_members == 0:
            print_error("API_003")
            report.add_warning(
                module="Core",
                object_type="Job",
                location="N/A",
                description="Job has no members to verify",
                detail={"job_name": config.job_name},
            )
            return report

        tracker = ProgressTracker(total_steps=total_members)
        print(f"Found {total_members} members to process")

        # Phase 1: Mark Verification
        print("\n=== Phase 1: Mark Verification ===")
        tracker.start_phase("Mark Verification")
        report = verify_marks(job, report, config)
        print(f"  {report.error_count} errors, {report.warning_count} warnings")

        # Phase 2: Sheet Boundary Check
        print("\n=== Phase 2: Sheet Boundary Check ===")
        tracker.start_phase("Sheet Boundary")
        report = verify_sheet_boundaries(job, report, config)
        print(f"  {report.error_count} errors, {report.warning_count} warnings")

        # Phase 3: Erection Plan Continuity
        print("\n=== Phase 3: Erection Plan Continuity ===")
        tracker.start_phase("Erection Plan Continuity")
        report = verify_erection_continuity(job, report, config)
        print(f"  {report.error_count} errors, {report.warning_count} warnings")

        # Phase 4: BOM Reconciliation
        print("\n=== Phase 4: BOM Reconciliation ===")
        tracker.start_phase("BOM Reconciliation")
        report = verify_bom_reconciliation(job, report, config)
        print(f"  {report.error_count} errors, {report.warning_count} warnings")

        # Phase 5: Generate Report
        print("\n=== Phase 5: Generate Report ===")
        tracker.print_status("Generating reports...")

        try:
            report.to_html(config.output_path)
            report.to_json(config.output_path.replace(".html", ".json"))
            report.to_csv(config.output_path.replace(".html", ".csv"))
        except OSError as e:
            print_error("RPT_001", str(e))

        elapsed = time.time() - start_time

        print(f"\n{'=' * 60}")
        print(f"Report saved to: {config.output_path}")
        print(f"  JSON: {config.output_path.replace('.html', '.json')}")
        print(f"  CSV:  {config.output_path.replace('.html', '.csv')}")
        print(f"\n{'=' * 60}")
        print(f"TOTAL Issues: {report.summary['total_issues']}")
        print(f"  Errors:   {report.error_count}")
        print(f"  Warnings: {report.warning_count}")
        print(f"  Duration: {tracker.format_time(elapsed)}s")

        import webbrowser

        webbrowser.open(f"file://{config.output_path}")

    except Exception as e:
        print_error("RPT_003", str(e))
        report.add_error(
            module="Core",
            object_type="System",
            location="Report Generation",
            description=str(e),
            detail={"error": str(e)},
        )

    config.disconnect_db()
    return report


if __name__ == "__main__":
    config_path = sys.argv[1] if len(sys.argv) > 1 else "qa_config.json"
    run_verification(config_path)
