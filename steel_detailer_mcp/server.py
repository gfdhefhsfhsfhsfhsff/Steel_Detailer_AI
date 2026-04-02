import os
import sys
import dataclasses

from mcp.server.fastmcp import FastMCP

_repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _repo_root not in sys.path:
    sys.path.insert(0, _repo_root)

from qa_qc_verify.kiss_parser import (
    parse_kiss_file,
    KISSFile,
    KISSAssembly,
    KISSMinorMark,
)
from qa_qc_verify.project_scanner import (
    scan_all_projects,
    get_statistics,
    find_stair_rail_projects,
    _scan_release,
    ReleasePackage,
)
from qa_qc_verify.cross_reference import CrossReferenceEngine, aggregate_results
from qa_qc_verify.statistics import (
    compute_project_metrics,
    compute_portfolio_baseline,
    detect_anomalies,
    ProjectMetrics,
    PortfolioBaseline,
    AnomalyReport,
)
from qa_qc_verify.config import Config

mcp = FastMCP("steel-detailer", json_response=True)


def _dataclass_to_dict(obj):
    if dataclasses.is_dataclass(obj) and not isinstance(obj, type):
        return dataclasses.asdict(obj)
    if isinstance(obj, list):
        return [_dataclass_to_dict(item) for item in obj]
    if isinstance(obj, dict):
        return {k: _dataclass_to_dict(v) for k, v in obj.items()}
    if isinstance(obj, tuple):
        return list(obj)
    return obj


@mcp.tool()
def parse_kiss(filepath: str) -> dict:
    """Parse a KISS .kss file and return header, assemblies, global BOM, member types, minor marks, and parse errors."""
    kiss = parse_kiss_file(filepath)
    if kiss is None:
        return {"error": f"File not found: {filepath}"}

    return {
        "path": kiss.path,
        "project_name": kiss.project_name,
        "release_name": kiss.release_name,
        "header": _dataclass_to_dict(kiss.header),
        "total_assemblies": kiss.total_assemblies,
        "total_minor_marks": kiss.total_minor_marks,
        "assemblies": {
            mark: _dataclass_to_dict(asm) for mark, asm in kiss.assemblies.items()
        },
        "global_bom": kiss.get_global_bom(),
        "member_types": kiss.get_member_types(),
        "unique_minor_marks": kiss.unique_minor_marks,
        "parse_errors": kiss.parse_errors,
    }


@mcp.tool()
def scan_portfolio(path: str, focus: str = "all") -> dict:
    """Scan all projects in a directory for releases, KISS files, and sheet PDFs. Use focus='stair_rail' to filter stair/rail/ladder projects."""
    catalogs = scan_all_projects(path)
    stats = get_statistics(catalogs)

    stair_rail_projects = None
    if focus == "stair_rail":
        stair_catalogs = find_stair_rail_projects(catalogs)
        stair_rail_projects = [
            {
                "project_name": c.project_name,
                "project_path": c.project_path,
                "releases": [_dataclass_to_dict(r) for r in c.releases],
            }
            for c in stair_catalogs
        ]

    projects = [
        {
            "project_name": c.project_name,
            "project_path": c.project_path,
            "release_count": len(c.releases),
            "releases": [
                {
                    "release_path": r.release_path,
                    "category": r.category,
                    "release_type": r.release_type,
                    "date": r.date,
                    "has_kiss": r.has_kiss,
                    "kiss_path": r.kiss_path,
                    "has_detail_sheets": r.has_detail_sheets,
                    "has_erection_sheets": r.has_erection_sheets,
                    "has_gather_sheets": r.has_gather_sheets,
                }
                for r in c.releases
            ],
        }
        for c in catalogs
    ]

    result = {
        "statistics": stats,
        "projects": projects,
        "total_projects": len(catalogs),
    }
    if stair_rail_projects is not None:
        result["stair_rail_projects"] = stair_rail_projects

    return result


@mcp.tool()
def cross_reference(
    kiss_path: str, release_path: str, use_pdf_verification: bool = False
) -> dict:
    """Cross-reference a KISS file against a release directory to find orphaned gathers, missing erection marks, and quantity mismatches."""
    kiss = parse_kiss_file(kiss_path)
    if kiss is None:
        return {"error": f"KISS file not found: {kiss_path}"}

    release = _scan_release(
        release_path,
        os.path.basename(os.path.dirname(release_path.rstrip("\\/"))),
        os.path.basename(release_path),
    )

    engine = CrossReferenceEngine()
    result = engine.verify_release(
        kiss, release, use_pdf_verification=use_pdf_verification
    )

    return {
        "project_name": result.project_name,
        "release_name": result.release_name,
        "total_assemblies": result.total_assemblies,
        "total_minor_marks": result.total_minor_marks,
        "verified_details": result.verified_details,
        "orphaned_details": result.orphaned_details,
        "missing_from_erection": result.missing_from_erection,
        "quantity_mismatches": result.quantity_mismatches,
        "pdf_verified": result.pdf_verified,
        "pdf_callout_mismatches": result.pdf_callout_mismatches,
        "pdf_bom_mismatches": result.pdf_bom_mismatches,
        "error_count": result.error_count,
        "warning_count": result.warning_count,
        "info_count": result.info_count,
        "issues": [
            {
                "severity": i.severity.value,
                "check_type": i.check_type,
                "project": i.project,
                "release": i.release,
                "mark": i.mark,
                "description": i.description,
                "detail": i.detail,
            }
            for i in result.issues
        ],
    }


@mcp.tool()
def detect_portfolio_anomalies(path: str) -> dict:
    """Scan a portfolio directory, parse all KISS files, compute baselines, and detect statistical anomalies across projects."""
    catalogs = scan_all_projects(path)
    all_metrics: list[ProjectMetrics] = []

    for cat in catalogs:
        for rel in cat.releases:
            if rel.has_kiss and rel.kiss_path:
                kiss = parse_kiss_file(rel.kiss_path)
                if kiss is not None:
                    metrics = compute_project_metrics(kiss)
                    all_metrics.append(metrics)

    if not all_metrics:
        return {"error": "No KISS files found in portfolio", "path": path}

    baseline = compute_portfolio_baseline(all_metrics)
    anomalies = detect_anomalies(all_metrics, baseline)

    return {
        "baseline": _dataclass_to_dict(baseline),
        "total_projects_analyzed": len(all_metrics),
        "anomaly_count": len(anomalies),
        "anomalies": _dataclass_to_dict(anomalies),
    }


@mcp.tool()
def validate_piecemark(mark: str) -> dict:
    """Validate a piecemark against standard SDS/2 system mark patterns. Returns match status and classification."""
    config = Config()
    is_system = config.is_system_mark(mark)

    classification = "unknown"
    mark_upper = mark.upper() if mark else ""
    if any(kw in mark_upper for kw in ("BEAM", "B_")):
        classification = "beam"
    elif any(kw in mark_upper for kw in ("COLUMN", "C_")):
        classification = "column"
    elif any(kw in mark_upper for kw in ("BRACE", "VB_", "V")):
        classification = "brace"
    elif any(kw in mark_upper for kw in ("STAIR", "S_")):
        classification = "stair"
    elif any(kw in mark_upper for kw in ("HANDRAIL", "HR_", "RAIL")):
        classification = "handrail"
    elif any(kw in mark_upper for kw in ("LADDER", "L_")):
        classification = "ladder"
    elif is_system:
        classification = "minor"

    return {
        "mark": mark,
        "is_system_mark": is_system,
        "classification": classification,
    }


@mcp.tool()
def get_assembly_bom(kiss_path: str, assembly_mark: str) -> dict:
    """Get the bill of materials for a specific assembly mark from a KISS file."""
    kiss = parse_kiss_file(kiss_path)
    if kiss is None:
        return {"error": f"KISS file not found: {kiss_path}"}

    asm = kiss.assemblies.get(assembly_mark)
    if asm is None:
        return {
            "error": f"Assembly mark '{assembly_mark}' not found",
            "available_assemblies": list(kiss.assemblies.keys())[:50],
        }

    bom = kiss.get_assembly_bom(assembly_mark)

    return {
        "assembly_mark": asm.assembly_mark,
        "major_mark": asm.major_mark,
        "revision": asm.revision,
        "main_qty": asm.main_qty,
        "main_type": asm.main_type,
        "main_size": asm.main_size,
        "main_grade": asm.main_grade,
        "member_description": asm.member_description,
        "bom": bom,
        "minor_marks": [
            {
                "minor_mark": mm.minor_mark,
                "quantity": mm.quantity,
                "material_type": mm.material_type,
                "material_size": mm.material_size,
                "grade": mm.grade,
                "length_mm": mm.length_mm,
                "location": mm.location,
                "remarks": mm.remarks,
            }
            for mm in asm.minor_marks
        ],
    }


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
