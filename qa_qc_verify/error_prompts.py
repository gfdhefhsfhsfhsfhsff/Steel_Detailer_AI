"""
Steel Detailer AI - Error Prompts
Easy-to-understand error messages with causes and fixes for every failure point.
Author: John May
Version: 1.0.0-alpha
"""

from enum import Enum
from dataclasses import dataclass
from typing import Optional


class ErrorCategory(Enum):
    SETUP = "Setup"
    DATABASE = "Database"
    API = "SDS/2 API"
    CONFIG = "Configuration"
    FILE_SYSTEM = "File System"
    VERIFICATION = "Verification"
    REPORT = "Report Generation"


@dataclass
class ErrorPrompt:
    code: str
    category: ErrorCategory
    short_message: str
    explanation: str
    likely_cause: str
    suggested_fix: str

    def format(self, detail: str = "") -> str:
        lines = [
            f"\n{'=' * 60}",
            f"  ERROR [{self.code}] - {self.category.value}",
            f"{'=' * 60}",
            f"",
            f"  {self.short_message}",
            f"",
            f"  What happened:",
            f"    {self.explanation}",
            f"",
            f"  Likely cause:",
            f"    {self.likely_cause}",
            f"",
            f"  How to fix it:",
            f"    {self.suggested_fix}",
        ]
        if detail:
            lines += [
                f"",
                f"  Technical detail:",
                f"    {detail}",
            ]
        lines += [f"{'=' * 60}\n"]
        return "\n".join(lines)


ERRORS = {
    # ── Setup Errors ──────────────────────────────────────────────
    ErrorCategory.SETUP: {
        "SETUP_001": ErrorPrompt(
            code="SETUP_001",
            category=ErrorCategory.SETUP,
            short_message="Python version is too old",
            explanation=(
                "This tool requires Python 3.8 or newer. "
                "The version currently on your system is older than that."
            ),
            likely_cause="An older version of Python is installed on this machine.",
            suggested_fix=(
                "1. Download Python 3.8+ from https://www.python.org/downloads/\n"
                "    2. Install it (check 'Add to PATH' during install)\n"
                "    3. Restart your terminal and run the tool again"
            ),
        ),
        "SETUP_002": ErrorPrompt(
            code="SETUP_002",
            category=ErrorCategory.SETUP,
            short_message="Required Python packages are missing",
            explanation=(
                "One or more libraries this tool depends on could not be found. "
                "The tool cannot run without them."
            ),
            likely_cause="Dependencies were never installed or the virtual environment is not activated.",
            suggested_fix=(
                "1. Open a terminal in the project folder\n"
                "    2. Run: pip install -r requirements.txt\n"
                "    3. If using a virtual environment, activate it first:\n"
                "       - Windows: .venv\\Scripts\\activate\n"
                "       - Mac/Linux: source .venv/bin/activate"
            ),
        ),
        "SETUP_003": ErrorPrompt(
            code="SETUP_003",
            category=ErrorCategory.SETUP,
            short_message="psycopg2 database driver is not installed",
            explanation=(
                "The PostgreSQL database driver (psycopg2) is not available. "
                "The tool will fall back to default settings and cannot load "
                "fabricator-specific piecemark standards from the database."
            ),
            likely_cause=(
                "psycopg2 was not included in your pip install, or "
                "the build tools needed to compile it are missing."
            ),
            suggested_fix=(
                "Option A (recommended): pip install psycopg2-binary\n"
                "    Option B (if you need native performance): Install PostgreSQL client "
                "libraries, then: pip install psycopg2\n"
                "    Note: The tool will still work with defaults if you skip this."
            ),
        ),
    },
    # ── SDS/2 API Errors ─────────────────────────────────────────
    ErrorCategory.API: {
        "API_001": ErrorPrompt(
            code="API_001",
            category=ErrorCategory.API,
            short_message="SDS/2 API is not available",
            explanation=(
                "The tool cannot find the SDS/2 API libraries (DesignData.SDS2). "
                "All four verification modules require this API to read member data, "
                "drawings, and bills of material."
            ),
            likely_cause=(
                "The script is being run outside of the SDS/2 environment. "
                "The SDS/2 API is only accessible when Python is launched from "
                "within SDS/2 (e.g., via the SDS/2 scripting console or by running "
                "a script inside the SDS/2 installation)."
            ),
            suggested_fix=(
                "1. Open SDS/2 on your machine\n"
                "    2. Launch this script from within the SDS/2 scripting environment\n"
                "    3. If SDS/2 is not installed, contact your IT department for a license\n"
                "    4. Check that the SDS/2 Python path is in your PYTHONPATH"
            ),
        ),
        "API_002": ErrorPrompt(
            code="API_002",
            category=ErrorCategory.API,
            short_message="Cannot open the SDS/2 job",
            explanation=(
                "The tool connected to SDS/2 but could not open the specified job. "
                "The job name in your config file does not match any job in SDS/2."
            ),
            likely_cause=(
                "The 'job_name' in qa_config.json is misspelled, or the job has not "
                "been created in SDS/2 yet."
            ),
            suggested_fix=(
                "1. Open SDS/2 and verify the exact job name\n"
                "    2. Open qa_config.json in a text editor\n"
                "    3. Update 'job_name' to match exactly (case-sensitive)\n"
                "    4. Save and re-run the tool"
            ),
        ),
        "API_003": ErrorPrompt(
            code="API_003",
            category=ErrorCategory.API,
            short_message="SDS/2 job has no members",
            explanation=(
                "The job opened successfully but contains zero members. "
                "There is nothing to verify."
            ),
            likely_cause=(
                "The job is empty because members have not been modeled yet, "
                "or the wrong job was opened."
            ),
            suggested_fix=(
                "1. Open the job in SDS/2 and confirm members exist\n"
                "    2. If the job is new, model members first, then re-run\n"
                "    3. Double-check the job_name in your config"
            ),
        ),
        "API_004": ErrorPrompt(
            code="API_004",
            category=ErrorCategory.API,
            short_message="Failed to read a member from SDS/2",
            explanation=(
                "While scanning members, one member could not be read. "
                "The tool skipped it and continued with the rest."
            ),
            likely_cause=(
                "The member data may be corrupted, locked by another user, "
                "or reference a deleted object."
            ),
            suggested_fix=(
                "1. Note the member number shown in the report\n"
                "    2. Open that member in SDS/2 and check for errors\n"
                "    3. If the member was deleted, refresh the job and re-run\n"
                "    4. This is a warning - the rest of the verification is still valid"
            ),
        ),
        "API_005": ErrorPrompt(
            code="API_005",
            category=ErrorCategory.API,
            short_message="Cannot read drawing / sheet data",
            explanation=(
                "The tool could not retrieve drawing information for one or more "
                "sheets. Some boundary checks may be incomplete."
            ),
            likely_cause=(
                "The drawing may be locked, corrupted, or not yet generated in SDS/2."
            ),
            suggested_fix=(
                "1. In SDS/2, regenerate drawings for the affected sheets\n"
                "    2. Make sure no other user has the drawings open\n"
                "    3. Re-run the verification tool"
            ),
        ),
    },
    # ── Configuration Errors ──────────────────────────────────────
    ErrorCategory.CONFIG: {
        "CFG_001": ErrorPrompt(
            code="CFG_001",
            category=ErrorCategory.CONFIG,
            short_message="Configuration file not found",
            explanation=(
                "The tool cannot find the configuration file (qa_config.json). "
                "It needs this file to know which job to check and where to save results."
            ),
            likely_cause=(
                "The config file was deleted, moved, or never created. "
                "Or the path passed to the tool is incorrect."
            ),
            suggested_fix=(
                "1. Check that qa_config.json exists in the project folder\n"
                "    2. If it is missing, create it with these minimum settings:\n"
                "       {\n"
                '         "job_name": "Your Job Name",\n'
                '         "fabricator_id": "DEFAULT",\n'
                '         "output_path": "./qa_qc_report.html"\n'
                "       }\n"
                "    3. Or run: python -m qa_qc_verify --create-config"
            ),
        ),
        "CFG_002": ErrorPrompt(
            code="CFG_002",
            category=ErrorCategory.CONFIG,
            short_message="Configuration file has invalid JSON",
            explanation=(
                "The config file contains a syntax error. JSON requires double quotes "
                "around keys and string values, and does not allow trailing commas."
            ),
            likely_cause=(
                "A missing comma, extra comma, single quotes instead of double quotes, "
                "or an unclosed brace/bracket in the JSON file."
            ),
            suggested_fix=(
                "1. Open qa_config.json in a text editor\n"
                "    2. Look for these common mistakes:\n"
                "       - Missing comma between entries\n"
                "       - Extra comma after the last entry\n"
                "       - Single quotes (') instead of double quotes (\")\n"
                "       - Missing closing } or ]\n"
                "    3. Use a JSON validator (jsonlint.com) to find the exact error\n"
                "    4. Save and re-run"
            ),
        ),
        "CFG_003": ErrorPrompt(
            code="CFG_003",
            category=ErrorCategory.CONFIG,
            short_message="Data directory does not exist",
            explanation=(
                "The 'data_directory' path in your config points to a folder that "
                "does not exist on this computer."
            ),
            likely_cause=(
                "The path is wrong, or the SDS/2 data folder has been moved "
                "to a different location."
            ),
            suggested_fix=(
                "1. Verify the correct path to your SDS/2 data folder\n"
                "    2. Open qa_config.json and update 'data_directory'\n"
                "    3. Use forward slashes (/) or escaped backslashes (\\\\) in the path\n"
                '       Example: "C:/SDS2/Data" or "C:\\\\SDS2\\\\Data"'
            ),
        ),
        "CFG_004": ErrorPrompt(
            code="CFG_004",
            category=ErrorCategory.CONFIG,
            short_message="Page margin value is invalid",
            explanation=(
                "The 'page_margin_inches' value must be a positive number (e.g., 0.5). "
                "The current value is zero, negative, or not a number."
            ),
            likely_cause="The value was accidentally set to 0, a negative number, or text.",
            suggested_fix=(
                "1. Open qa_config.json\n"
                '    2. Set "page_margin_inches" to a positive number (typical: 0.5 or 1.0)\n'
                "    3. Save and re-run"
            ),
        ),
    },
    # ── Database Errors ───────────────────────────────────────────
    ErrorCategory.DATABASE: {
        "DB_001": ErrorPrompt(
            code="DB_001",
            category=ErrorCategory.DATABASE,
            short_message="Cannot connect to the PostgreSQL database",
            explanation=(
                "The tool tried to connect to the PostgreSQL database to load "
                "fabricator-specific standards but the connection was refused."
            ),
            likely_cause=(
                "PostgreSQL is not running, or the host/port/credentials in the "
                "config file are incorrect."
            ),
            suggested_fix=(
                "1. Make sure PostgreSQL is installed and running:\n"
                "       - Windows: Open 'Services' and check 'postgresql'\n"
                "       - Mac: brew services start postgresql\n"
                "       - Linux: sudo systemctl start postgresql\n"
                "    2. Verify the connection settings in qa_config.json:\n"
                '       - "db_host" (usually "localhost")\n'
                '       - "db_port" (usually 5432)\n'
                '       - "db_name" (usually "sds2_standards")\n'
                '       - "db_user" and "db_password"\n'
                "    3. Test manually: psql -h localhost -U postgres -d sds2_standards\n"
                "    4. The tool will use default patterns if the database is unavailable"
            ),
        ),
        "DB_002": ErrorPrompt(
            code="DB_002",
            category=ErrorCategory.DATABASE,
            short_message="Database authentication failed",
            explanation=(
                "The database rejected the username or password provided in the "
                "configuration file."
            ),
            likely_cause=(
                "The db_user or db_password in qa_config.json is incorrect, "
                "or the user does not have access to the sds2_standards database."
            ),
            suggested_fix=(
                "1. Verify the username and password in qa_config.json\n"
                "    2. Try connecting manually with the same credentials:\n"
                "       psql -h localhost -U postgres -d sds2_standards\n"
                "    3. If the database does not exist, create it:\n"
                "       createdb -U postgres sds2_standards\n"
                "    4. Then run the database setup script (database_schema.sql)"
            ),
        ),
        "DB_003": ErrorPrompt(
            code="DB_003",
            category=ErrorCategory.DATABASE,
            short_message="Fabricator standards table not found",
            explanation=(
                "The database is connected but the 'fabricator_standards' table "
                "does not exist. The tool will fall back to default piecemark patterns."
            ),
            likely_cause=(
                "The database schema has not been set up yet. The table needs to "
                "be created before fabricator-specific standards can be loaded."
            ),
            suggested_fix=(
                "1. Run the schema setup script:\n"
                "       psql -U postgres -d sds2_standards -f database_schema.sql\n"
                "    2. If you do not have a database, the tool will use built-in defaults\n"
                "    3. To add a custom fabricator, insert a row into fabricator_standards"
            ),
        ),
        "DB_004": ErrorPrompt(
            code="DB_004",
            category=ErrorCategory.DATABASE,
            short_message="Fabricator ID not found in database",
            explanation=(
                "The fabricator_id in your config does not match any entry in the "
                "fabricator_standards table. The tool will use default patterns instead."
            ),
            likely_cause=(
                "The fabricator_id is misspelled, or this fabricator has not been "
                "added to the database yet."
            ),
            suggested_fix=(
                "1. Check the fabricator_id in qa_config.json\n"
                "    2. View available fabricators:\n"
                '       psql -U postgres -d sds2_standards -c "SELECT fabricator_id, fabricator_name FROM fabricator_standards;"\n'
                '    3. Add your fabricator if it is missing, or set fabricator_id to "DEFAULT"'
            ),
        ),
    },
    # ── File System Errors ────────────────────────────────────────
    ErrorCategory.FILE_SYSTEM: {
        "FS_001": ErrorPrompt(
            code="FS_001",
            category=ErrorCategory.FILE_SYSTEM,
            short_message="Cannot create the output directory",
            explanation=(
                "The tool tried to create the folder for the output report but "
                "was denied permission."
            ),
            likely_cause=(
                "The output_path in the config points to a location that requires "
                "administrator access, or the path contains invalid characters."
            ),
            suggested_fix=(
                "1. Change 'output_path' in qa_config.json to a writable location\n"
                '       Example: "./qa_qc_report.html" or "C:/Users/YourName/Desktop/report.html"\n'
                "    2. Avoid system-protected folders like C:\\Windows or C:\\Program Files\n"
                "    3. Run the terminal as administrator if you must write to a protected location"
            ),
        ),
        "FS_002": ErrorPrompt(
            code="FS_002",
            category=ErrorCategory.FILE_SYSTEM,
            short_message="Cannot write the report file",
            explanation=(
                "The tool generated the report data but could not save it to disk. "
                "The report was not written."
            ),
            likely_cause=(
                "The file may be open in another program (e.g., the HTML report is "
                "open in a browser or the CSV is open in Excel), or the disk is full."
            ),
            suggested_fix=(
                "1. Close any program that might have the file open\n"
                "    2. Check that you have free disk space\n"
                "    3. If the file is read-only, right-click > Properties > uncheck Read-only\n"
                "    4. Try saving to a different location by updating output_path"
            ),
        ),
        "FS_003": ErrorPrompt(
            code="FS_003",
            category=ErrorCategory.FILE_SYSTEM,
            short_message="Could not open the report in the browser",
            explanation=(
                "The report was saved successfully but the tool could not "
                "automatically open it in your web browser."
            ),
            likely_cause=(
                "No default browser is configured, or the file path contains "
                "special characters that the browser cannot handle."
            ),
            suggested_fix=(
                "1. Open the report manually by navigating to the output path\n"
                "    2. The file path is shown in the tool output - copy it into your browser\n"
                "    3. This does not affect the report itself - the data is still saved"
            ),
        ),
    },
    # ── Verification Errors / Warnings ────────────────────────────
    ErrorCategory.VERIFICATION: {
        "VER_001": ErrorPrompt(
            code="VER_001",
            category=ErrorCategory.VERIFICATION,
            short_message="System marks detected (unconverted piecemarks)",
            explanation=(
                "Some members still have system-generated piecemarks (like B_1, VB_1, "
                "p1, m1) instead of user-assigned drawing marks. These members have not "
                "been properly piecemarked and will cause issues in fabrication."
            ),
            likely_cause=(
                "The detailer has not yet assigned drawing marks to these members, "
                "or the auto-piecemarking process was not completed."
            ),
            suggested_fix=(
                "1. Open the job in SDS/2\n"
                "    2. For each system mark listed in the report:\n"
                "       a. Locate the member by its number\n"
                "       b. Assign a proper drawing mark (e.g., 1B, 2C, 3VB)\n"
                "    3. Follow your fabricator's naming convention\n"
                "    4. Re-run the verification to confirm all marks are converted"
            ),
        ),
        "VER_002": ErrorPrompt(
            code="VER_002",
            category=ErrorCategory.VERIFICATION,
            short_message="Detail content overruns the sheet boundary",
            explanation=(
                "One or more detail views extend beyond the sheet margin. This means "
                "part of the detail may be cut off when the sheet is printed."
            ),
            likely_cause=(
                "Too many details are placed on one sheet, or a detail is too large "
                "for the sheet size at the current scale."
            ),
            suggested_fix=(
                "1. In SDS/2, open the affected sheet\n"
                "    2. Options to fix:\n"
                "       a. Move some details to another sheet\n"
                "       b. Reduce the drawing scale\n"
                "       c. Use a larger sheet size\n"
                "    3. Adjust the 'page_margin_inches' in qa_config.json if needed (default: 0.5)\n"
                "    4. Re-run the verification"
            ),
        ),
        "VER_003": ErrorPrompt(
            code="VER_003",
            category=ErrorCategory.VERIFICATION,
            short_message="Orphaned detail found (not on any erection plan)",
            explanation=(
                "A detail drawing exists on a detail sheet but is not called out "
                "or referenced on any erection plan. Fabricators and erectors will "
                "not know where this piece goes."
            ),
            likely_cause=(
                "The erection plan was created before all details were added, or "
                "the erection view callouts were accidentally deleted."
            ),
            suggested_fix=(
                "1. Open the erection plans in SDS/2\n"
                "    2. Find the location where each orphaned detail should be shown\n"
                "    3. Add the detail callout to the appropriate erection view\n"
                "    4. Verify that the callout text matches the piecemark exactly\n"
                "    5. Re-run the verification"
            ),
        ),
        "VER_004": ErrorPrompt(
            code="VER_004",
            category=ErrorCategory.VERIFICATION,
            short_message="BOM quantity mismatch between gather sheet and detail sheets",
            explanation=(
                "The quantity of a material on the gather sheet does not match the "
                "quantity shown on the detail sheets. This could lead to ordering "
                "the wrong amount of material."
            ),
            likely_cause=(
                "A member was added or removed after the gather sheet was last "
                "updated, or a manual edit changed the quantity on one sheet but "
                "not the other."
            ),
            suggested_fix=(
                "1. Compare the gather sheet and detail sheet side by side\n"
                "    2. For the mismatched piecemark listed in the report:\n"
                "       a. Count the actual members in the SDS/2 model\n"
                "       b. Update whichever sheet has the wrong count\n"
                "    3. Regenerate BOMs in SDS/2 if available\n"
                "    4. Re-run the verification"
            ),
        ),
        "VER_005": ErrorPrompt(
            code="VER_005",
            category=ErrorCategory.VERIFICATION,
            short_message="BOM grade mismatch detected",
            explanation=(
                "The steel grade for a material differs between the gather sheet "
                "and the detail sheet. This could result in fabricating with the "
                "wrong grade of steel."
            ),
            likely_cause=(
                "The grade was changed on one sheet but the change was not propagated "
                "to all related sheets."
            ),
            suggested_fix=(
                "1. Check the material grade in the SDS/2 model (this is the source of truth)\n"
                "    2. Update the gather sheet or detail sheet to match\n"
                "    3. Common grades: A36, A572 Gr.50, A992, A500 Gr. B\n"
                "    4. Re-run the verification"
            ),
        ),
        "VER_006": ErrorPrompt(
            code="VER_006",
            category=ErrorCategory.VERIFICATION,
            short_message="BOM shape mismatch detected",
            explanation=(
                "The member shape (e.g., W12x26, L4x4x1/2) differs between the "
                "gather sheet and the detail sheet."
            ),
            likely_cause=(
                "The member shape was edited in the model but the BOM was not refreshed."
            ),
            suggested_fix=(
                "1. Check the member shape in the SDS/2 model\n"
                "    2. Update the incorrect BOM entry to match\n"
                "    3. Regenerate drawings if SDS/2 supports it\n"
                "    4. Re-run the verification"
            ),
        ),
        "VER_007": ErrorPrompt(
            code="VER_007",
            category=ErrorCategory.VERIFICATION,
            short_message="Material on gather sheet but missing from detail sheets",
            explanation=(
                "A material line item appears on the gather sheet but has no matching "
                "entry on any detail sheet. This material may have been removed from "
                "the model but not from the gather sheet."
            ),
            likely_cause=(
                "A member was deleted from the model but the gather sheet BOM was not updated."
            ),
            suggested_fix=(
                "1. Verify whether this material still exists in the SDS/2 model\n"
                "    2. If it was deleted, remove it from the gather sheet BOM\n"
                "    3. If it still exists, check that the detail sheet includes it\n"
                "    4. Re-run the verification"
            ),
        ),
        "VER_008": ErrorPrompt(
            code="VER_008",
            category=ErrorCategory.VERIFICATION,
            short_message="Material on detail sheet but missing from gather sheet",
            explanation=(
                "A material appears on a detail sheet but is not listed on the gather "
                "sheet. This material might not be ordered for fabrication."
            ),
            likely_cause=(
                "A member was added to the model but the gather sheet BOM was not regenerated."
            ),
            suggested_fix=(
                "1. Verify that this material should be in the project\n"
                "    2. If yes, regenerate or update the gather sheet BOM in SDS/2\n"
                "    3. If no, remove the detail from the detail sheet\n"
                "    4. Re-run the verification"
            ),
        ),
        "VER_009": ErrorPrompt(
            code="VER_009",
            category=ErrorCategory.VERIFICATION,
            short_message="Erection view has no associated detail callout",
            explanation=(
                "An erection view on an erection plan does not reference any detail "
                "drawings. The view may be a placeholder or was not properly set up."
            ),
            likely_cause=(
                "The erection view was created but detail callouts were never added."
            ),
            suggested_fix=(
                "1. Open the erection sheet in SDS/2\n"
                "    2. Select the affected erection view\n"
                "    3. Add the correct detail callouts\n"
                "    4. Re-run the verification"
            ),
        ),
    },
    # ── Report Generation Errors ──────────────────────────────────
    ErrorCategory.REPORT: {
        "RPT_001": ErrorPrompt(
            code="RPT_001",
            category=ErrorCategory.REPORT,
            short_message="HTML report generation failed",
            explanation=(
                "The tool finished verifying the job but crashed while trying to "
                "generate the HTML report file."
            ),
            likely_cause=(
                "A file permission issue, a path with special characters, or a "
                "unicode error in the member data."
            ),
            suggested_fix=(
                "1. Check the output_path in qa_config.json for special characters\n"
                '    2. Try saving to a simpler path like "./report.html"\n'
                "    3. Run the terminal as administrator\n"
                "    4. The JSON report may still have been generated - check for that file"
            ),
        ),
        "RPT_002": ErrorPrompt(
            code="RPT_002",
            category=ErrorCategory.REPORT,
            short_message="CSV report generation failed",
            explanation=(
                "The HTML report was created but the CSV export failed. "
                "You still have the HTML report."
            ),
            likely_cause=(
                "The CSV file path is invalid, or another program has the file locked."
            ),
            suggested_fix=(
                "1. Close any program that might have the CSV open (e.g., Excel)\n"
                "    2. Check the output_path and ensure the directory exists\n"
                "    3. The HTML report contains the same data and can be used instead"
            ),
        ),
        "RPT_003": ErrorPrompt(
            code="RPT_003",
            category=ErrorCategory.REPORT,
            short_message="Verification crashed unexpectedly",
            explanation=(
                "An unexpected error occurred during the verification process. "
                "Partial results may have been generated."
            ),
            likely_cause=(
                "A bug in the tool, corrupted data in the SDS/2 job, or an "
                "unexpected API response."
            ),
            suggested_fix=(
                "1. Check the error message shown above for details\n"
                "    2. Try running the tool again - it may be a transient issue\n"
                "    3. If the error persists, report it with:\n"
                "       - The error message\n"
                "       - Your qa_config.json (remove any passwords)\n"
                "       - The SDS/2 version you are running\n"
                "    4. Any partial report that was saved is still valid for completed modules"
            ),
        ),
    },
}


def get_prompt(code: str) -> Optional[ErrorPrompt]:
    """Look up an error prompt by its code (e.g., 'API_001')."""
    for category_errors in ERRORS.values():
        if code in category_errors:
            return category_errors[code]
    return None


def print_error(code: str, detail: str = "") -> None:
    """Print a user-friendly error message to the console."""
    prompt = get_prompt(code)
    if prompt:
        print(prompt.format(detail=detail))
    else:
        print(f"\n  Unknown error code: {code}")
        if detail:
            print(f"  Detail: {detail}\n")


def check_setup() -> bool:
    """
    Validate the runtime environment before the tool runs.
    Checks Python version, required packages, and psycopg2.

    Returns True if all checks pass (or only non-critical warnings).
    Returns False if a critical check fails (tool cannot run).
    """
    all_ok = True
    critical_failure = False

    # ── SETUP_001: Python version ──
    import sys

    min_version = (3, 8)
    if sys.version_info < min_version:
        print_error(
            "SETUP_001",
            f"Current version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        )
        critical_failure = True

    # ── SETUP_002: Required packages ──
    required_packages = {
        "dataclasses": "dataclasses",
    }
    missing = []
    for module_name in required_packages:
        try:
            __import__(module_name)
        except ImportError:
            missing.append(module_name)

    if sys.version_info < (3, 7):
        try:
            __import__("dataclasses")
        except ImportError:
            missing.append("dataclasses")

    if missing:
        print_error(
            "SETUP_002",
            f"Missing packages: {', '.join(missing)}",
        )
        critical_failure = True

    # ── SETUP_003: psycopg2 ──
    try:
        import psycopg2  # noqa: F401
    except ImportError:
        print_error("SETUP_003")
        all_ok = False

    if critical_failure:
        return False

    return all_ok


def list_all_errors() -> None:
    """Print a summary of all known error codes."""
    print("\nSteel Detailer AI - All Known Error Codes")
    print("=" * 60)
    for category, errors in ERRORS.items():
        print(f"\n  [{category.value}]")
        for code, prompt in errors.items():
            print(f"    {code}: {prompt.short_message}")
    print(f"\n{'=' * 60}\n")


if __name__ == "__main__":
    list_all_errors()
