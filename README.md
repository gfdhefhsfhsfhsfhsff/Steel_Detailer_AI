# Steel Detailer AI - QA/QC Verification Tool

Production-ready Python automation for SDS/2 steel detailing QA/QC verification.

## Overview

This tool automates the final QA/QC process for steel detailing projects by performing four critical verification checks:

1. **Mark Verification** - Scans all members and flags system-generated marks (e.g., `B_1`, `VB_1`, `p1`) that haven't been converted to user-assigned drawing marks.

2. **Sheet Boundary Check** - Analyzes detail and erection sheets to verify all content fits within established sheet borders without overrunning margins.

3. **Erection Plan Continuity** - Cross-references all details on detail sheets to ensure they are accurately called out and represented on erection plans. Flags orphaned details.

4. **BOM Reconciliation** - Compares Gather Sheets (global BOM) against aggregate Detail Sheet BOMs for exact matches on:
   - Quantities
   - Material Types
   - Sizes
   - Shapes
   - Steel Grades

## Architecture

```
qa_qc_verify/
├── __init__.py              # Package initialization
├── config.py                # Configuration & PostgreSQL standards repo
├── report.py                # Report generation (HTML, CSV, JSON)
├── run.py                   # Main entry point
├── utils/
│   └── helpers.py           # Utility functions
└── checks/
    ├── mark_verification.py
    ├── sheet_boundary.py
    ├── erection_continuity.py
    └── bom_reconciliation.py
```

## Configuration

Create a `config.json` file:

```json
{
    "data_directory": "C:/SDS2/Data",
    "job_name": "Project Name",
    "fabricator_id": "FAB001",
    "output_path": "./qa_qc_report.html",
    "page_margin_inches": 0.5,
    "db_host": "localhost",
    "db_port": 5432,
    "db_name": "sds2_standards",
    "db_user": "postgres",
    "db_password": "your_password"
}
```

## Database Schema (PostgreSQL)

```sql
CREATE TABLE fabricator_standards (
    fabricator_id VARCHAR(50) PRIMARY KEY,
    fabricator_name VARCHAR(100),
    major_prefixes JSONB,
    minor_prefixes JSONB,
    system_patterns JSONB,
    page_margin_inches FLOAT DEFAULT 0.5
);
```

## Usage

### Within SDS/2

```python
from qa_qc_verify import run_verification

report = run_verification(config_path="config.json")
```

### Command Line

```bash
python -m qa_qc_verify config.json
```

## Output

Generates a comprehensive HTML report with:
- Summary statistics by module and severity
- Detailed issue list with exact locations
- Expandable detail sections for each issue
- Filterable by severity, module, and object type

## Requirements

- SDS/2 Open API (DesignData.SDS2.*.dll)
- Python 3.8+
- psycopg2 (for PostgreSQL standards repository)

## License

Proprietary - AddonAxis / FabTrics
