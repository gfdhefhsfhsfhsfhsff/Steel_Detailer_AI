# Steel Detailer AI - Development Handoff (03/31/2026)

## Session Summary

This session had two parallel workstreams:
1. **SDS/2 Detailing Templates** — Discovered, cataloged, and backed up the "Detailing with Templates" JSON files for both SDS2 2025-1 and 2026
2. **QA/QC Portfolio Scanner** — Built a standalone KISS-based verification tool that cross-references Detail/Erection/Gather sheets across all 424+ projects

---

## 1. SDS/2 Detailing Templates

### Discovery

The "Detailing with Templates" system stores templates as **plain JSON files** at:

```
F:\ProgramData\SDS2_2026\detailing\SDS2\          ← 268 base templates
F:\ProgramData\SDS2_2026\detailing\SDS2\US\        ← 268 US-imperial overrides
F:\ProgramData\SDS2_2026\detailing\SDS2\US_FitUp\  ← 211 fit-up drawing variants
F:\ProgramData\SDS2_2025\detailing\SDS2\US\        ← 267 US-imperial (2025)
F:\ProgramData\SDS2_2025\detailing\SDS2\US_FitUp\  ← 211 fit-up (2025)
```

The `fabs\` folder (per-fabricator overrides) is currently empty at both versions — this is where customized templates should be deployed.

### Backups Created

```
F:\ProgramData\SDS2_2026\detailing_old\   ← exact copy of 2026 detailing/
F:\ProgramData\SDS2_2025\detailing_old\   ← exact copy of 2025 detailing/
```

### Template File Format

Each template is JSON with this structure:
```json
{
  "Conditions": [{ "Member types": [0,2,5], "Material types": [] }],
  "Priority": 1001,
  "Template disabled": false,
  "Template version": 10,
  "Type": 0,
  "Rules": [
    {
      "Description": "workpoint symbol upwards",
      "Constraints": [
        { "Type": "Require location", "Value": { "Location": 0 } },
        { "Type": "Python: Condition", "Value": { "Expression": "detail_lib.fge(...)" } }
      ],
      "Locations": [ { "Type": "Named", "Value": { "Properties": {...} } } ],
      "DrawingItems": [ { "Type": "Workpoint|Snapline|Dimension|...", "Value": {...} } ],
      "Priority": 9,
      "Setup options": ["bm_flgs.show_ext_orig==Yes"],
      "Rule disabled": false,
      "Rotate with member": true,
      "View priority order": [0]
    }
  ]
}
```

### Member Type IDs
| ID | Member Type |
|----|-------------|
| 0  | Beam        |
| 2  | Column      |
| 3  | Horizontal Brace |
| 5  | Vertical Brace |
| 6  | Stair (tread sub-material) |
| 7  | Stair (main member) |
| 9  | Miscellaneous |
| 16 | Custom Hand Rail |
| 19 | Custom Hand Rail (piece mark) |

### Stair & Rail Template Files (9 files, in US/ and US_FitUp/ as well)

| File | Purpose | Member Types |
|------|---------|--------------|
| `Stair_0000.json` | Main stair workpoints & locations | 7 |
| `Stair_broken_apart_0100.json` | Broken-apart stair connections | 7 |
| `stair_treads_0200.json` | Stair tread detailing | 6 |
| `0001_StairSnapLines.json` | Stair snaplines | 7, 6 |
| `8913_StairMemb_Pcmk.json` | Stair member piecemarks | 7 |
| `6030_Custom_Handrail.json` | Custom handrail dimensions | 16, 19 |
| `8910_CustomHandRail_Pcmk.json` | Custom handrail piecemarks | 19 |
| `6090_Custom_Ladder.json` | Custom ladder detailing | - |
| `1380_Beam_HandRail_Material.json` | Beam handrail material | 0 |

**Important**: The 2025-1 base `detailing\SDS2\` directory has NO JSON files (only `US\` and `US_FitUp\` subdirectories). All 2025 templates live in the `US\` subfolder. The 2026 version has templates in the base directory.

### Supporting Files
- `detail_lib.py` (2,633 lines) — shared Python library with helper functions for bolt callouts, piecemarks, geometry, filtering. Referenced by Python expressions inside template constraints.
- Templates use `${Variable}` syntax for runtime substitution (e.g., `${MN}`, `${MtrlNumber}`, `${ViewType}`, `${WorkpointID}`)

### Template Revision Priorities (for Stair cleanup)
1. `Stair_0000.json` — foundation, defines named locations and workpoints
2. `0001_StairSnapLines.json` — snapline grid for dimension placement
3. `stair_treads_0200.json` — tread-specific dimensioning
4. `8913_StairMemb_Pcmk.json` — piecemark placement
5. `Stair_broken_apart_0100.json` — connection details for broken-apart views

---

## 2. QA/QC Portfolio Scanner

### Project Data Landscape

Source: `F:\WD Projects (total company)\` — 424 project folders

| Metric | Count |
|--------|-------|
| Total PDFs | 160,746 |
| KISS files (.kss) | 1,637 |
| Gather Sheet folders | 1,637 |
| Detail Sheet folders | 2,179 |
| Erection Sheet folders | 1,788 |
| Material Summaries | 2,835 |

### Directory Structure (typical project)
```
F:\WD Projects (total company)\
├── 2202 Project Elephant\
│   ├── PE_Design\                    ← design/architectural PDFs
│   └── PE_Release\
│       └── 004 Misc\
│           └── 07 Cage Ladder FSF_102222\
│               ├── Detail Sheet\      or Detail Sheets\PDF\
│               ├── Erection Sheet\    or Erection Sheets\PDF\
│               ├── Gather Sheets\     or Gather Sheets\PDF\
│               └── Reports\
│                   ├── CNC\DSTV\
│                   ├── Material Summary*.pdf/.xlsx
│                   ├── Field Bolt Summary*.pdf/.xlsx
│                   └── KISS\Kiss.kss  or Kiss File\Kiss.kss
```

### KISS File Format (machine-readable source of truth)
```
KISS,1.1,SDS/2 from Design Data
H,JobID,Fabricator,,Date,Time,Status,
*
D,M129,,M129L1,a466,2,L,3x3x1/4,A36,63.50,,,,
W,M129,,LADDER,10/21/22,SDS7.708
M,M129L1,1,LADDER,,,,
D,M129,,M129L1,a464,1,L,3x2x1/4,A36,5829.30,,,,
D,M129,,M129L1,rb106,19,HS,3/4x2-0-1/4,ROUND BAR,615.95,,Shop::(SLIP RESI.RUNGS),,
```

Record types: `H`=header, `D`=detail line, `W`=worksheet, `M`=member, `*`=separator

### New Modules Written

All in `C:\Users\test\source\repos\Steel_Detailer_AI\qa_qc_verify\`:

| File | Size | Purpose |
|------|------|---------|
| `kiss_parser.py` | 9.3 KB | Parses KISS .kss files into structured data (KISSFile, KISSAssembly, KISSMinorMark) |
| `project_scanner.py` | 8.1 KB | Walks all 424 project directories and catalogs every release package |
| `cross_reference.py` | 12.1 KB | Cross-reference engine: detail↔erection verification, BOM qty checks, orphan detection |
| `statistics.py` | 13.9 KB | Portfolio baseline statistics, anomaly detection across all projects |
| `scan_runner.py` | 29.7 KB | Main entry point: 6-phase pipeline + HTML/JSON report generation |

### Existing Modules (SDS2 API-dependent, unchanged)

| File | Purpose |
|------|---------|
| `__init__.py` | Package init (imports run.py which needs SDS2 API) |
| `run.py` | SDS2-in-process runner (needs DesignData.SDS2 modules) |
| `config.py` | Config + PostgreSQL fabricator standards |
| `report.py` | HTML/JSON/CSV report generator |
| `utils.py` | ProgressTracker utility |
| `error_prompts.py` | User-friendly error messages |
| `command.py` | CLI argument parser |
| `checks/mark_verification.py` | System mark detection (SDS2 API) |
| `checks/bom_reconciliation.py` | BOM gather vs detail (SDS2 API) |
| `checks/erection_continuity.py` | Detail↔erection cross-ref (SDS2 API) |
| `checks/sheet_boundary.py` | Sheet margin overrun check (SDS2 API) |

### KISS Parser — Verified Working
```python
# Test: parsed Elephant Cage Ladder KISS file
Assemblies: 1
Minor marks: 8
GlobalBOM: {'a466': 2, 'a464': 1, 'a465': 1, 'p652': 8, 'p647': 1, 'p145': 3, 'p646': 7}
```

### Project Scanner — Verified Working
```python
# Test: scanned GP Stairs project
Project: 2267 GP Stairs
Releases: 3
# Each release correctly identified with has_kiss, has_detail_sheets, etc.
```

### Architecture: Two Modes of Operation

**Mode 1 — Standalone (new):** `scan_runner.py`
- Runs outside SDS2 using only KISS files + filesystem
- Processes all 424 projects in one pass
- Cross-references via filename matching (no PDF OCR)
- Generates HTML + JSON reports
- Command: `python -m qa_qc_verify.scan_runner "F:\WD Projects (total company)" ./qa_output`

**Mode 2 — In-Process (existing):** `run.py`
- Runs inside SDS2 via its .NET/Python API
- Accesses live BOM data, drawing handles, sheet geometry
- More precise (actual drawing data vs filename heuristics)
- Command: `python -m qa_qc_verify qa_config.json`

---

## 3. Detailed PDF Analysis Results

### Elephant Cage Ladder (Project 2202, Release 07)
- **1 assembly**: M129L1 (Ladder, 398 lbs)
- **8 minor marks**: a464, a465, a466, rb106, p145, p646, p647, p652
- **42 total parts**, 10 field anchors (HILTI KB-TZ2)
- KISS data matches Material Summary exactly

### FedEx Ladders (Project 2144, Release 04)
- **10 members**: 3 ladders, 4 guardrails, 2 columns, 1 angle
- **35 PDFs** across detail/erection/gather/reports
- **55 round bar rungs** total across 3 ladders
- 3,013 lbs total weight
- Note: p214 references M122M4 from a different release (cross-package reference)

### Elephant Misc (Project 2202, Releases 04 & 05)
- **Package 1**: 51 assemblies, 29 detail sheets, 11 erection sheets, 109 gather sheets
- **Package 2**: 26 assemblies, 12 detail sheets, 4 erection sheets, 65 gather sheets
- **5 quantity mismatches found**:
  - `hss1299`: BOM=2, Gather=4
  - `p322`: BOM=6, Gather=8
  - `rb134`: BOM=1, Gather=5
  - `p261`: BOM=3, Gather=4
  - `CP2`: cross-package conflict (4 vs 12)
- Cross-package shared marks: BP1, CP2, p322, hss1299

### FedEx Anchor Bolts (Project 2144, Release AB)
- 476 total anchor bolt assemblies (456 AB1 + 20 AB2)
- 7 erection sheets (AB1.1–AB1.7)
- 114 Section A locations, 5 Section B locations

---

## 4. Critical Issues to Fix (Next Session)

### Issue 1: Package Import Circular Dependency
The `__init__.py` imports `run.py` which imports `checks/mark_verification.py` which uses `MemberHandle` (SDS2 API type). This causes `NameError` when importing any sub-module from outside SDS2.

**Fix needed**: Make `__init__.py` conditional — only import SDS2-dependent modules when the API is available:
```python
try:
    from .run import run_verification
except ImportError:
    pass
```
Or create a separate `__init_standalone__.py` for the new modules.

### Issue 2: scan_runner.py relative imports fail when loaded via `importlib`
The `scan_runner.py`, `cross_reference.py`, and `statistics.py` use relative imports (`from .kiss_parser import ...`). These fail when importing outside the package context.

**Fix needed**: Either:
- Add a `__main__.py` entry point that handles the package context
- Or add try/except fallback for both relative and absolute imports in each module
- Or create a standalone runner script at the repo root that does `from qa_qc_verify.scan_runner import run_full_scan`

### Issue 3: cross_reference.py references scanner fields
The cross-reference engine references `ReleasePackage` fields. The scanner was written by a different agent and field names need to be verified as matching:
- `release_path`, `kiss_path`, `detail_sheet_paths`, `erection_sheet_paths`, `gather_sheet_paths`, `has_kiss`, `has_detail_sheets`, `has_erection_sheets`, `has_gather_sheets` — confirmed these exist.

### Issue 4: Full Integration Test Needed
Individual modules tested OK (kiss_parser, project_scanner) but the full pipeline has not been run end-to-end:
```
scan_all_projects → parse all KISS → compute baseline → cross-reference → detect anomalies → generate reports
```

### Issue 5: Statistics module may need kiss_parser injection
The `statistics.py` uses `from .kiss_parser import KISSFile` — verify this import resolves correctly when the package __init__ is fixed.

---

## 5. Next Steps (Priority Order)

### A. Fix imports and run full scan (HIGH)
1. Fix `__init__.py` to be import-safe
2. Create `__main__.py` with standalone entry point
3. Run full scan across all 424 projects: `python -m qa_qc_verify`
4. Review generated HTML report for issues

### B. Stair template revision (HIGH)
1. Start with `Stair_0000.json` — modify named locations, workpoint placement
2. Then `0001_StairSnapLines.json` — adjust snapline distances
3. Then `stair_treads_0200.json` — tread dimensioning rules
4. Deploy revised templates to `fabs\` folder
5. Test in SDS2 2026 on a stair member

### C. Cross-package reference detection (MEDIUM)
The tool should flag cases where a piecemark in one release references a member from a different release (like p214 → M122M4). This requires cross-release mark tracking.

### D. PDF OCR integration (MEDIUM)
Currently cross-referencing uses filename matching only. For deeper verification (reading actual callout text on erection sheets), integrate PyMuPDF or pdfplumber:
- `extract_pdfs.py` already exists (uses `fitz`/PyMuPDF)
- `extract_tables.py` already exists (uses `pdfplumber`)

### E. Handrail/ladder template revision (MEDIUM)
After stair templates are validated, move to:
1. `6030_Custom_Handrail.json` — handrail dimensioning
2. `6090_Custom_Ladder.json` — ladder detailing
3. `8910_CustomHandRail_Pcmk.json` — handrail piecemarks
4. `1380_Beam_HandRail_Material.json` — beam-mounted rail material

---

## 6. Key File Paths Reference

### Project Repository
```
C:\Users\test\source\repos\Steel_Detailer_AI\
├── qa_qc_verify\               ← Main tool package
│   ├── kiss_parser.py           ← NEW: KISS file parser
│   ├── project_scanner.py       ← NEW: Directory scanner
│   ├── cross_reference.py       ← NEW: Verification engine
│   ├── statistics.py            ← NEW: Portfolio baseline
│   ├── scan_runner.py           ← NEW: Standalone runner + reports
│   ├── run.py                   ← SDS2-in-process runner
│   ├── config.py                ← Config + DB
│   ├── report.py                ← Report generator (SDS2 mode)
│   ├── utils.py                 ← ProgressTracker
│   ├── error_prompts.py         ← Error messages
│   ├── command.py               ← CLI parser
│   └── checks\                  ← SDS2 API-dependent checks
├── extracted_data\              ← PDF extraction results from agents
├── sds2_scraper\                ← SDS2 developer docs scraper
├── sds tooling\                 ← SDS2 tooling scripts
└── Steel Detailer AI.sln        ← C# solution
```

### SDS2 Installation
```
F:\Program Files\SDS2_2026\2026-1\bin\     ← SDS2 2026 binaries
F:\Program Files\SDS2_2025\2025-1\bin\     ← SDS2 2025 binaries
F:\ProgramData\SDS2_2026\detailing\         ← 2026 templates (ACTIVE)
F:\ProgramData\SDS2_2026\detailing_old\     ← 2026 templates (BACKUP)
F:\ProgramData\SDS2_2026\fabs\              ← 2026 fabricator overrides (EMPTY)
F:\ProgramData\SDS2_2025\detailing\         ← 2025 templates (ACTIVE)
F:\ProgramData\SDS2_2025\detailing_old\     ← 2025 templates (BACKUP)
```

### Project Data
```
F:\WD Projects (total company)\             ← 424 project folders
├── 2267 GP Stairs\                         ← Stair-only project
├── 2230 Medtronic Stair\                   ← Stair-only project
├── 25014 Carver HS Rails\                  ← Rail-only project
├── 2202 Project Elephant\                  ← Full building (stair + rail + misc)
├── 2144 Fed Ex\                            ← Full building (ladders + AB + structural)
└── ... (419 more)
```

### Scraped Documentation
```
C:\Users\test\source\repos\Steel_Detailer_AI\sds2_scraper\output\
├── 2026\API\DesignData\SDS2\              ← 1,511 scraped API docs
└── 2025-1\API\DesignData\SDS2\            ← Same for 2025-1
```

---

## 7. Data Dictionaries

### Template DrawingItem Types
`Workpoint`, `Snapline`, `Dimension`, `Label`, `Weld Symbol`, `Piecemark`, `Callout`, `Hole Pointer`, `Named Location`, `Named Rotation`, `Section Mark`

### Template Constraint Types
`Require location`, `Python: Condition`, `Python: Minimize`, `Python: Maximize`, `Apply only once`, `Variable equal`, `Variable not equal`, `Named rotation`

### Template Location Types
`Named` (property-matched), `Line mapped` (offset from base), `Between` (midpoint of two locations)

### KISS Material Types
`L`=Angle, `PL`=Plate, `HSS`=Hollow Structural, `W`=Wide Flange, `C`=Channel, `HS`=Bolt, `MB`=Machine Bolt, `RB`=Round Bar, `GR`=Grating, `GT`=Grating, `MC`=Misc Channel, `MX`=Misc Material, `WT`=Tee, `BLT`=Bolt, `SS`=Stainless

### KISS Record Prefixes
`D`=detail line, `M`=member definition, `W`=worksheet, `H`=header, `*`=assembly separator
