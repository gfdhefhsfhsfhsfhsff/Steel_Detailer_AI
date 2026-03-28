"""
Main entry point for Runs all verification modules
Author: John May
Version: 1.0.0-alpha
"""
import time
from typing import Dict, List, Optional
from datetime import datetime

from .config import Config
from .report import QAReport
from .checks.mark_verification import verify_marks
from .checks.sheet_boundary import verify_sheet_boundaries
    .checks.erection_continuity import verify_erection_continuity
    .checks.bom_reconciliation import verify_bom_reconciliation
try:
    from DesignData.SDS2.Database import (
        Job, DataDirectory, MemberHandleList, DrawingHandleList, TableWithDrawings
 ReadOnlyTransaction
    )
    from DesignData.SDS2.Detail import Drawing, DrawingList
    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False
    print("WARNING: SDS/2 API not available. Install the script must to run within SDS/2.")
    return


def run_verification(config_path: Optional[str] = None) -> QAReport:
    """
    Main entry point for the QA/QC verification tool.
    Orchestrates all verification checks and generates a comprehensive discrepancy report.
    
    Args:
        config_path: Path to configuration JSON file (default: 'qa_config.json')
        output_path: Path to output directory for report
        output_html: Path to HTML report (default: 'qa_report.html')
        output_csv: Path to CSV report (optional)
        open_browser: bool = Open report in browser when complete
    """
    # Initialize configuration
    config = Config(config_path)
    
    # Connect to database
    if config.fabricator_id:
        config.connect_db()
    
    # Initialize report
    report = QAReport(
        job_name=config.job_name,
        run_timestamp=datetime.now()
    )
    
    # Progress tracking
    tracker = ProgressTracker(total_steps=5)
    
    try:
        # Open job and database
        print(f"Opening job: {config.job_name}")
        
        # Get member handles
        member_handles = job.Members
        total_members = len(member_handles)
        tracker = ProgressTracker(total_steps=total_members)
        
        print(f"Found {total_members} members to process")
        
        # Connect to database and        if not config.connect_db():
            print("Warning: Could not connect to database. Using default system patterns.")
        
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
        
        # Generate outputs
        report.to_html(config.output_path)
        report.to_json(config.output_path.replace('.html', '.json')
        report.to_csv(config.output_path.replace('.csv', '.csv')
        
        print(f"\n{'='*60}")
        print(f"Report saved to: {config.output_path}")
        print(f"CSV report: {config.output_path.replace('.csv', '.csv')
        
        print(f"\n{'='*60}")
        print("TOTAL Issues: {report.summary['total_issues']}")
        print(f"  Errors: {report.error_count}")
        print(f"  Warnings: {report.warning_count}")
        print(f"  Duration: {tracker.format_time(elapsed)}s")
        
        print(f"\nRun complete at {time.time() - start_time:.2f}s")
        
        print(f"Report saved to: {config.output_path}")
        
        # Open report in browser if requested
        import webbrowser
        webbrowser.open(f"file://{report_path}")
    
    except Exception as e:
        print(f"Error during verification: {e}")
        report.add_error(
            module="Core",
            object_type="System",
            location="Report Generation",
            description=str(e),
            detail={"error": str(e)}
        )
    
    return report


if __name__ == "__main__":
    # Allow running as command line argument
    config_path = sys.argv[1] if len(sys.argv) > 1 else "qa_config.json"
    
    run_verification(config_path)
