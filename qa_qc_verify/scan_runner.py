"""
Standalone QA/QC Scanner - Portfolio-wide scan from KISS files and filesystem data
Does NOT require SDS2 API. Processes all 424+ steel detailing projects from disk.
Version: 1.0.0-alpha
"""

import argparse
import json
import os
import statistics
import sys
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple

from .kiss_parser import parse_kiss_file, KISSFile
from .project_scanner import (
    scan_all_projects,
    scan_project,
    find_stair_rail_projects,
    get_statistics,
    ProjectCatalog,
    ReleasePackage,
)
from .cross_reference import (
    CrossReferenceEngine,
    aggregate_results,
    CrossReferenceResult,
    CrossReleaseRef,
    VerificationIssue,
)
from .statistics import (
    compute_project_metrics,
    compute_portfolio_baseline,
    detect_anomalies,
    ProjectMetrics,
    PortfolioBaseline,
    AnomalyReport,
)
from .utils import ProgressTracker


class ScanProgress:
    def __init__(self, total_phases: int = 6):
        self.total_phases = total_phases
        self.current_phase = 0
        self.start_time = time.time()
        self.phase_start: float = 0.0
        self.phase_times: Dict[str, float] = {}

    def start_phase(self, name: str) -> None:
        self.current_phase += 1
        self.phase_start = time.time()
        elapsed = self._fmt(time.time() - self.start_time)
        print(f"\n{'=' * 60}")
        print(f"  Phase {self.current_phase}/{self.total_phases}: {name}")
        print(f"  Elapsed: {elapsed}")
        print(f"{'=' * 60}")

    def end_phase(self, detail: str = "") -> None:
        dur = time.time() - self.phase_start
        name = f"phase_{self.current_phase}"
        self.phase_times[name] = dur
        msg = f"  Done in {self._fmt(dur)}"
        if detail:
            msg += f" - {detail}"
        print(msg)

    def print_progress(self, current: int, total: int, message: str) -> None:
        pct = (current / total * 100) if total > 0 else 0
        print(f"  [{current}/{total}] {pct:.1f}% - {message}")

    def finish(self) -> None:
        total = time.time() - self.start_time
        print(f"\n{'=' * 60}")
        print(f"  Scan complete. Total time: {self._fmt(total)}")
        print(f"{'=' * 60}")

    @staticmethod
    def _fmt(seconds: float) -> str:
        if seconds < 60:
            return f"{seconds:.1f}s"
        elif seconds < 3600:
            m = int(seconds / 60)
            s = int(seconds % 60)
            return f"{m}m {s}s"
        h = int(seconds / 3600)
        m = int((seconds % 3600) / 60)
        return f"{h}h {m}m"


def _focus_filter(catalogs: List[ProjectCatalog], focus: str) -> List[ProjectCatalog]:
    if focus == "all":
        return catalogs
    if focus in ("stair_rail", "stairs", "rails"):
        return find_stair_rail_projects(catalogs)
    return catalogs


def run_full_scan(projects_root: str, output_dir: str, focus: str = "all") -> dict:
    start = time.time()
    progress = ScanProgress(total_phases=7)
    errors: List[str] = []

    if not os.path.isdir(projects_root):
        return {
            "success": False,
            "error": f"Projects root not found: {projects_root}",
            "timestamp": datetime.now().isoformat(),
        }

    os.makedirs(output_dir, exist_ok=True)

    # ── Phase 1: Scan project directories ─────────────────────────
    progress.start_phase("Scanning project directories")
    try:
        all_catalogs = scan_all_projects(projects_root)
    except Exception as e:
        errors.append(f"Project scan failed: {e}")
        all_catalogs = []

    scan_stats = get_statistics(all_catalogs)
    progress.end_phase(f"{len(all_catalogs)} projects found")
    print(f"  Total releases: {scan_stats.get('total_releases', 0)}")
    print(f"  With KISS files: {scan_stats.get('total_kiss_files', 0)}")

    filtered = _focus_filter(all_catalogs, focus)

    # ── Phase 2: Parse all KISS files ─────────────────────────────
    progress.start_phase("Parsing KISS files")
    kiss_files: Dict[str, KISSFile] = {}
    total_kiss = 0
    parse_errors_count = 0

    for catalog in filtered:
        for release in catalog.releases:
            if not release.has_kiss or not release.kiss_path:
                continue
            total_kiss += 1
            try:
                kf = parse_kiss_file(release.kiss_path)
                if kf is not None:
                    key = f"{catalog.project_name}::{release.release_path}"
                    kiss_files[key] = kf
                    if kf.parse_errors:
                        parse_errors_count += 1
                        errors.extend(kf.parse_errors)
                else:
                    errors.append(f"Parse returned None: {release.kiss_path}")
                    parse_errors_count += 1
            except Exception as e:
                errors.append(f"Parse error {release.kiss_path}: {e}")
                parse_errors_count += 1

    progress.end_phase(
        f"{len(kiss_files)}/{total_kiss} parsed, {parse_errors_count} errors"
    )

    # ── Phase 3: Compute portfolio baseline statistics ────────────
    progress.start_phase("Computing portfolio baseline statistics")
    all_metrics: List[ProjectMetrics] = []
    for key, kf in kiss_files.items():
        try:
            m = compute_project_metrics(kf)
            all_metrics.append(m)
        except Exception as e:
            errors.append(f"Metrics error for {key}: {e}")

    baseline: Optional[PortfolioBaseline] = None
    if all_metrics:
        try:
            baseline = compute_portfolio_baseline(all_metrics)
        except Exception as e:
            errors.append(f"Baseline computation failed: {e}")

    progress.end_phase(f"{len(all_metrics)} project metrics computed")

    # ── Phase 4: Cross-reference verification ─────────────────────
    progress.start_phase("Running cross-reference verification")
    engine = CrossReferenceEngine()
    xref_results: List[CrossReferenceResult] = []
    release_map: Dict[str, ReleasePackage] = {}

    for catalog in filtered:
        for release in catalog.releases:
            if release.has_kiss and release.kiss_path:
                rkey = f"{catalog.project_name}::{release.release_path}"
                release_map[rkey] = release

    done = 0
    total_verify = len(release_map)
    for key, release in release_map.items():
        done += 1
        if key not in kiss_files:
            continue
        try:
            result = engine.verify_release(kiss_files[key], release)
            xref_results.append(result)
        except Exception as e:
            errors.append(f"XRef error for {key}: {e}")
        if done % 50 == 0 or done == total_verify:
            progress.print_progress(done, total_verify, f"verifying releases")

    aggregated = aggregate_results(xref_results) if xref_results else {}
    progress.end_phase(f"{len(xref_results)} releases verified")

    # ── Phase 5: Cross-release reference detection ──────────────────
    progress.start_phase("Detecting cross-release references")
    cross_release_refs: List[CrossReleaseRef] = []
    if len(release_map) > 1:
        release_data: Dict[str, Tuple[KISSFile, ReleasePackage]] = {}
        for key, release in release_map.items():
            if key in kiss_files:
                release_data[key] = (kiss_files[key], release)
        try:
            cross_release_refs = engine.detect_cross_release_references(release_data)
        except Exception as e:
            errors.append(f"Cross-release detection failed: {e}")

    cross_release_serialized = [
        {
            "source_project": r.source_project,
            "source_release": r.source_release,
            "source_mark": r.source_mark,
            "target_project": r.target_project,
            "target_release": r.target_release,
            "target_assembly": r.target_assembly,
        }
        for r in cross_release_refs
    ]
    progress.end_phase(f"{len(cross_release_refs)} cross-release references found")

    # ── Phase 6: Detect anomalies ─────────────────────────────────
    progress.start_phase("Detecting anomalies across portfolio")
    anomalies: List[AnomalyReport] = []
    if baseline and all_metrics:
        try:
            anomalies = detect_anomalies(all_metrics, baseline)
        except Exception as e:
            errors.append(f"Anomaly detection failed: {e}")

    progress.end_phase(f"{len(anomalies)} anomalies detected")

    # ── Phase 7: Generate reports ─────────────────────────────────
    progress.start_phase("Generating reports")
    elapsed = time.time() - start

    total_issues = sum(r.total_assemblies or 0 for r in xref_results)
    total_orphans = sum(len(r.orphaned_details) for r in xref_results)
    total_mismatches = sum(len(r.quantity_mismatches) for r in xref_results)
    all_issues: List[Dict[str, Any]] = []
    for r in xref_results:
        for issue in r.issues or []:
            sev = issue.severity
            if hasattr(sev, "value"):
                sev = sev.value
            all_issues.append(
                {
                    "severity": str(sev) if sev is not None else "unknown",
                    "check_type": getattr(issue, "check_type", "unknown"),
                    "project": getattr(issue, "project", ""),
                    "release": getattr(issue, "release", ""),
                    "mark": getattr(issue, "mark", ""),
                    "description": getattr(issue, "description", ""),
                    "detail": getattr(issue, "detail", {}),
                }
            )

    summary = {
        "success": True,
        "timestamp": datetime.now().isoformat(),
        "elapsed_seconds": round(elapsed, 2),
        "focus": focus,
        "projects_root": projects_root,
        "projects_scanned": {
            "total": len(all_catalogs),
            "filtered": len(filtered),
        },
        "releases": {
            "total": scan_stats.get("total_releases", 0),
            "with_kiss": scan_stats.get("total_kiss_files", 0),
            "parsed_successfully": len(kiss_files),
            "parse_errors": parse_errors_count,
            "verified": len(xref_results),
        },
        "scan_statistics": scan_stats,
        "baseline": _serialize_baseline(baseline) if baseline else None,
        "cross_reference": {
            "total_issues": len(all_issues),
            "orphaned_details": total_orphans,
            "quantity_mismatches": total_mismatches,
            "by_severity": _count_by(all_issues, "severity"),
            "by_check_type": _count_by(all_issues, "check_type"),
            "by_project": _count_by(all_issues, "project"),
            "aggregated": aggregated,
        },
        "anomalies": {
            "total": len(anomalies),
            "items": [_serialize_anomaly(a) for a in anomalies],
        },
        "cross_release": {
            "total": len(cross_release_refs),
            "items": cross_release_serialized,
        },
        "issues": all_issues,
        "errors": errors,
        "phase_times": progress.phase_times,
    }

    html_path = os.path.join(output_dir, "qa_scan_report.html")
    json_path = os.path.join(output_dir, "qa_scan_report.json")

    try:
        generate_html_report(summary, html_path)
        summary["html_report"] = html_path
        print(f"  HTML: {html_path}")
    except Exception as e:
        errors.append(f"HTML report failed: {e}")

    try:
        generate_json_report(summary, json_path)
        summary["json_report"] = json_path
        print(f"  JSON: {json_path}")
    except Exception as e:
        errors.append(f"JSON report failed: {e}")

    progress.end_phase()

    progress.finish()
    print(f"\n  Projects:     {len(all_catalogs)}")
    print(f"  Releases:     {scan_stats.get('total_releases', 0)}")
    print(f"  KISS parsed:  {len(kiss_files)}")
    print(f"  Issues:       {len(all_issues)}")
    print(f"  X-Release:    {len(cross_release_refs)}")
    print(f"  Anomalies:    {len(anomalies)}")
    print(f"  Errors:       {len(errors)}")

    return summary


def _count_by(items: List[Dict[str, Any]], key: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for item in items:
        val = str(item.get(key, "unknown"))
        counts[val] = counts.get(val, 0) + 1
    return counts


def _serialize_baseline(baseline: PortfolioBaseline) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for attr in (
        "mean_assemblies_per_release",
        "median_assemblies",
        "std_assemblies",
        "mean_pieces_per_release",
        "median_pieces",
        "std_pieces",
        "mean_minor_marks",
        "median_minor_marks",
        "std_minor_marks",
        "total_projects",
        "total_releases",
        "stair_project_count",
        "rail_project_count",
        "mean_assemblies",
        "mean_pieces",
        "mean_minor_marks",
    ):
        val = getattr(baseline, attr, None)
        if val is not None:
            result[attr] = val
    return result


def _serialize_anomaly(anomaly: AnomalyReport) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for attr in (
        "project_name",
        "release_name",
        "metric_name",
        "actual_value",
        "expected_range",
        "deviation_pct",
        "severity",
        "is_anomaly",
    ):
        val = getattr(anomaly, attr, None)
        if isinstance(val, tuple):
            val = list(val)
        result[attr] = val
    return result


def generate_json_report(results: dict, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    serializable = _make_serializable(results)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=2, default=str)


def _make_serializable(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {str(k): _make_serializable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_make_serializable(v) for v in obj]
    if isinstance(obj, (int, float, str, bool)) or obj is None:
        return obj
    if isinstance(obj, datetime):
        return obj.isoformat()
    try:
        return asdict(obj)
    except (TypeError, ValueError):
        return str(obj)


def generate_html_report(results: dict, output_path: str) -> None:
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    html = _build_html(results)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)


def _build_html(results: dict) -> str:
    timestamp = results.get("timestamp", datetime.now().isoformat())
    focus = results.get("focus", "all")
    elapsed = results.get("elapsed_seconds", 0)
    projects_total = results.get("projects_scanned", {}).get("total", 0)
    projects_filtered = results.get("projects_scanned", {}).get("filtered", 0)
    releases = results.get("releases", {})
    xref = results.get("cross_reference", {})
    anomaly_data = results.get("anomalies", {})
    cross_release_data = results.get("cross_release", {})
    issues = results.get("issues", [])
    errors = results.get("errors", [])
    baseline_data = results.get("baseline")

    errors_count = sum(
        1 for i in issues if str(i.get("severity", "")).lower() == "error"
    )
    warnings_count = sum(
        1 for i in issues if str(i.get("severity", "")).lower() == "warning"
    )
    info_count = sum(1 for i in issues if str(i.get("severity", "")).lower() == "info")
    total_issues = len(issues)

    baseline_rows = ""
    if baseline_data:
        labels = {
            "mean_assemblies": "Mean Assemblies",
            "median_assemblies": "Median Assemblies",
            "std_assemblies": "Std Dev Assemblies",
            "mean_pieces": "Mean Pieces",
            "median_pieces": "Median Pieces",
            "std_pieces": "Std Dev Pieces",
            "mean_minor_marks": "Mean Minor Marks",
            "median_minor_marks": "Median Minor Marks",
            "std_minor_marks": "Std Dev Minor Marks",
            "total_projects": "Projects in Baseline",
            "total_assemblies": "Total Assemblies",
            "total_pieces": "Total Pieces",
        }
        for key, label in labels.items():
            val = baseline_data.get(key)
            if val is not None:
                baseline_rows += f"""
                <tr>
                    <td>{label}</td>
                    <td>{_fmt_num(val)}</td>
                </tr>"""

    anomaly_rows = ""
    for idx, anom in enumerate(anomaly_data.get("items", [])):
        sev = str(anom.get("severity", "unknown")).lower()
        anomaly_rows += f"""
                <tr class="issue-row {sev}">
                    <td>{_esc(anom.get("project_name", ""))}</td>
                    <td>{_esc(anom.get("metric_name", ""))}</td>
                    <td>{_fmt_num(anom.get("actual_value", ""))}</td>
                    <td>{_esc(str(anom.get("expected_range", "")))}</td>
                    <td>{_fmt_num(anom.get("deviation_pct", ""))}</td>
                    <td><span class="badge {sev}">{_esc(anom.get("severity", ""))}</span></td>
                    <td>{_esc(str(anom.get("is_anomaly", "")))}</td>
                </tr>"""

    severity_breakdown = ""
    for sev, count in xref.get("by_severity", {}).items():
        sev_cls = str(sev).lower()
        severity_breakdown += f"""
                <tr>
                    <td><span class="badge {sev_cls}">{_esc(sev)}</span></td>
                    <td>{count}</td>
                </tr>"""

    check_type_breakdown = ""
    for ct, count in sorted(xref.get("by_check_type", {}).items(), key=lambda x: -x[1]):
        check_type_breakdown += f"""
                <tr>
                    <td>{_esc(ct)}</td>
                    <td>{count}</td>
                </tr>"""

    project_issue_rows = ""
    for proj, count in sorted(xref.get("by_project", {}).items(), key=lambda x: -x[1])[
        :25
    ]:
        project_issue_rows += f"""
                <tr>
                    <td class="location">{_esc(proj)}</td>
                    <td>{count}</td>
                </tr>"""

    cross_release_rows = ""
    for cr in cross_release_data.get("items", [])[:500]:
        cross_release_rows += f"""
                <tr class="issue-row warning">
                    <td class="location">{_esc(cr.get("source_project", ""))}</td>
                    <td class="location">{_esc(cr.get("source_release", ""))}</td>
                    <td class="location">{_esc(cr.get("source_mark", ""))}</td>
                    <td class="location">{_esc(cr.get("target_project", ""))}</td>
                    <td class="location">{_esc(cr.get("target_release", ""))}</td>
                    <td class="location">{_esc(cr.get("target_assembly", ""))}</td>
                </tr>"""

    issue_rows = ""
    display_issues = issues[:500]
    for issue in display_issues:
        sev = str(issue.get("severity", "unknown")).lower()
        detail_json = json.dumps(issue.get("detail", {}), indent=2)
        issue_rows += f"""
                <tr class="issue-row {sev}">
                    <td><span class="badge {sev}">{_esc(issue.get("severity", ""))}</span></td>
                    <td>{_esc(issue.get("check_type", ""))}</td>
                    <td class="location">{_esc(issue.get("project", ""))}</td>
                    <td class="location">{_esc(issue.get("release", ""))}</td>
                    <td class="location">{_esc(issue.get("mark", ""))}</td>
                    <td>{_esc(issue.get("description", ""))}</td>
                    <td><pre class="detail-json">{_esc(detail_json)}</pre></td>
                </tr>"""

    truncated_msg = ""
    if len(issues) > 500:
        truncated_msg = f'<p class="truncated">Showing 500 of {len(issues)} issues. See JSON report for full data.</p>'

    focus_section = ""
    if focus != "all":
        focus_section = f"""
        <div class="section">
            <h2>Focus Mode: {_esc(focus.title())}</h2>
            <p>Scanned {projects_filtered} of {projects_total} projects matching filter "{_esc(focus)}".</p>
        </div>"""

    error_rows = ""
    if errors:
        for err in errors[:50]:
            error_rows += f"""
                <tr class="issue-row error">
                    <td>{_esc(str(err))}</td>
                </tr>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QA/QC Portfolio Scan Report</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            color: #333;
            padding: 20px;
        }}
        .container {{ max-width: 1600px; margin: 0 auto; }}
        .header {{
            background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            color: #fff;
        }}
        .header h1 {{ margin-bottom: 5px; font-size: 1.8em; }}
        .header .meta {{ opacity: 0.9; font-size: 0.9em; }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 12px;
            margin-bottom: 20px;
        }}
        .summary-card {{
            background: #fff;
            padding: 18px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .summary-card h2 {{ font-size: 2em; margin-bottom: 4px; }}
        .summary-card p {{ color: #666; font-size: 0.85em; }}
        .summary-card.projects h2 {{ color: #2c3e50; }}
        .summary-card.releases h2 {{ color: #8e44ad; }}
        .summary-card.parsed h2 {{ color: #27ae60; }}
        .summary-card.issues h2 {{ color: #e74c3c; }}
        .summary-card.warnings h2 {{ color: #f39c12; }}
        .summary-card.anomalies h2 {{ color: #e67e22; }}
        .section {{
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .section h2 {{
            color: #2c3e50;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }}
        .section h3 {{
            color: #34495e;
            margin: 15px 0 10px 0;
        }}
        table {{ width: 100%; border-collapse: collapse; font-size: 0.9em; }}
        th, td {{ padding: 10px 12px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background: #f8f9fa; font-weight: 600; position: sticky; top: 0; }}
        tr:hover {{ background: #f0f4f8; }}
        .badge {{
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.8em;
            font-weight: 600;
            display: inline-block;
        }}
        .badge.error {{ background: #e74c3c; color: #fff; }}
        .badge.warning {{ background: #f39c12; color: #fff; }}
        .badge.info {{ background: #3498db; color: #fff; }}
        .badge.unknown {{ background: #95a5a6; color: #fff; }}
        .location {{
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 0.85em;
        }}
        .detail-json {{
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 0.75em;
            background: #f8f9fa;
            padding: 6px;
            border-radius: 4px;
            max-width: 250px;
            overflow-x: auto;
            white-space: pre-wrap;
        }}
        .issue-row.error {{ background: #fdf2f2; }}
        .issue-row.warning {{ background: #fef9e7; }}
        .issue-row.info {{ background: #ebf5fb; }}
        .no-issues {{ text-align: center; padding: 30px; color: #27ae60; }}
        .truncated {{
            text-align: center;
            padding: 10px;
            color: #7f8c8d;
            font-style: italic;
        }}
        .two-col {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }}
        .scroll-table {{
            max-height: 400px;
            overflow-y: auto;
        }}
        .footer {{
            text-align: center;
            color: #666;
            margin-top: 20px;
            font-size: 0.85em;
            padding: 15px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>QA/QC Portfolio Scan Report</h1>
            <div class="meta">
                <strong>Root:</strong> {_esc(results.get("projects_root", ""))} |
                <strong>Focus:</strong> {_esc(focus)} |
                <strong>Run:</strong> {timestamp} |
                <strong>Duration:</strong> {_fmt_elapsed(elapsed)}
            </div>
        </div>

        <div class="summary">
            <div class="summary-card projects">
                <h2>{projects_total}</h2>
                <p>Projects</p>
            </div>
            <div class="summary-card releases">
                <h2>{releases.get("total", 0)}</h2>
                <p>Total Releases</p>
            </div>
            <div class="summary-card parsed">
                <h2>{releases.get("parsed_successfully", 0)}</h2>
                <p>KISS Parsed</p>
            </div>
            <div class="summary-card issues">
                <h2>{total_issues}</h2>
                <p>Total Issues</p>
            </div>
            <div class="summary-card warnings">
                <h2>{cross_release_data.get("total", 0)}</h2>
                <p>Cross-Release Refs</p>
            </div>
            <div class="summary-card anomalies">
                <h2>{anomaly_data.get("total", 0)}</h2>
                <p>Anomalies</p>
            </div>
            <div class="summary-card" style="">
                <h2>{len(errors)}</h2>
                <p>Errors</p>
            </div>
        </div>

        {focus_section}

        <div class="section">
            <h2>Issue Summary</h2>
            <div class="summary" style="grid-template-columns: repeat(3, 1fr); margin-bottom: 0;">
                <div class="summary-card" style="padding: 12px;">
                    <h2 style="color: #e74c3c;">{errors_count}</h2>
                    <p>Errors</p>
                </div>
                <div class="summary-card" style="padding: 12px;">
                    <h2 style="color: #f39c12;">{warnings_count}</h2>
                    <p>Warnings</p>
                </div>
                <div class="summary-card" style="padding: 12px;">
                    <h2 style="color: #3498db;">{info_count}</h2>
                    <p>Info</p>
                </div>
            </div>
        </div>

        <div class="section">
            <h2>Portfolio Baseline Statistics</h2>
            {f"<table><thead><tr><th>Metric</th><th>Value</th></tr></thead><tbody>{baseline_rows}</tbody></table>" if baseline_rows else '<p class="no-issues">No baseline data available.</p>'}
        </div>

        <div class="section">
            <h2>Cross-Reference Results</h2>
            <div class="two-col">
                <div>
                    <h3>By Severity</h3>
                    <div class="scroll-table">
                        <table>
                            <thead><tr><th>Severity</th><th>Count</th></tr></thead>
                            <tbody>{severity_breakdown or '<tr><td colspan="2" class="no-issues">No issues</td></tr>'}</tbody>
                        </table>
                    </div>
                </div>
                <div>
                    <h3>By Check Type</h3>
                    <div class="scroll-table">
                        <table>
                            <thead><tr><th>Check Type</th><th>Count</th></tr></thead>
                            <tbody>{check_type_breakdown or '<tr><td colspan="2" class="no-issues">No issues</td></tr>'}</tbody>
                        </table>
                    </div>
                </div>
            </div>
            <h3>Top 25 Projects by Issue Count</h3>
            <table>
                <thead><tr><th>Project</th><th>Issues</th></tr></thead>
                <tbody>{project_issue_rows or '<tr><td colspan="2" class="no-issues">No issues</td></tr>'}</tbody>
            </table>
        </div>

        <div class="section">
            <h2>Anomaly Detection ({anomaly_data.get("total", 0)} found)</h2>
            {f'<div class="scroll-table"><table><thead><tr><th>Project</th><th>Metric</th><th>Value</th><th>Expected Range</th><th>Deviation %</th><th>Severity</th><th>Anomaly</th></tr></thead><tbody>{anomaly_rows}</tbody></table></div>' if anomaly_rows else '<p class="no-issues">No anomalies detected.</p>'}
        </div>

        <div class="section">
            <h2>Cross-Release References ({cross_release_data.get("total", 0)} found)</h2>
            {f'<div class="scroll-table"><table><thead><tr><th>Source Project</th><th>Source Release</th><th>Source Mark</th><th>Target Project</th><th>Target Release</th><th>Target Assembly</th></tr></thead><tbody>{cross_release_rows}</tbody></table></div>' if cross_release_rows else '<p class="no-issues">No cross-release references detected.</p>'}
        </div>

        <div class="section">
            <h2>All Issues ({total_issues})</h2>
            {truncated_msg}
            {f'<div class="scroll-table"><table><thead><tr><th>Severity</th><th>Check</th><th>Project</th><th>Release</th><th>Mark</th><th>Description</th><th>Detail</th></tr></thead><tbody>{issue_rows}</tbody></table></div>' if issue_rows else '<p class="no-issues">No issues found across the portfolio.</p>'}
        </div>

        {'<div class="section"><h2>Processing Errors</h2><table><thead><tr><th>Error</th></tr></thead><tbody>' + error_rows + "</tbody></table></div>" if error_rows else ""}

        <div class="footer">
            Generated by QA/QC Portfolio Scanner v1.0.0-alpha | {timestamp}
        </div>
    </div>
</body>
</html>"""


def _esc(text: str) -> str:
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _fmt_num(val: Any) -> str:
    if val is None:
        return ""
    try:
        n = float(val)
        if n == int(n):
            return str(int(n))
        return f"{n:.2f}"
    except (ValueError, TypeError):
        return str(val)


def _fmt_elapsed(seconds: Any) -> str:
    try:
        s = float(seconds)
    except (ValueError, TypeError):
        return str(seconds)
    if s < 60:
        return f"{s:.1f}s"
    elif s < 3600:
        return f"{int(s / 60)}m {int(s % 60)}s"
    return f"{int(s / 3600)}h {int((s % 3600) / 60)}m"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="QA/QC Portfolio Scanner - Scan all steel detailing projects from disk"
    )
    parser.add_argument(
        "projects_root",
        nargs="?",
        default=".",
        help="Root directory containing all project folders",
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default="./qa_output",
        help="Output directory for reports",
    )
    parser.add_argument(
        "--focus",
        choices=["all", "stairs", "rails", "stair_rail"],
        default="all",
        help="Filter projects by type (default: all)",
    )

    args = parser.parse_args()

    if not os.path.isdir(args.projects_root):
        print(f"Error: Projects root not found: {args.projects_root}")
        sys.exit(1)

    print(f"QA/QC Portfolio Scanner v1.0.0-alpha")
    print(f"  Root:   {args.projects_root}")
    print(f"  Output: {args.output_dir}")
    print(f"  Focus:  {args.focus}")

    results = run_full_scan(args.projects_root, args.output_dir, args.focus)

    if not results.get("success"):
        print(f"\nScan failed: {results.get('error', 'Unknown error')}")
        sys.exit(1)

    html_path = results.get("html_report", "")
    if html_path and os.path.exists(html_path):
        print(f"\nOpen report: {html_path}")


if __name__ == "__main__":
    main()
