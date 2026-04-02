"""
Statistical Baseline Computation for Steel Detailing Portfolio
Computes baselines from all KISS projects to identify anomalies.
"""

import math
import statistics
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from collections import Counter

from .kiss_parser import KISSFile, KISSAssembly, KISSMinorMark


@dataclass
class ProjectMetrics:
    project_name: str
    total_assemblies: int = 0
    total_minor_marks: int = 0
    unique_marks: int = 0
    total_pieces: int = 0
    member_type_counts: Dict[str, int] = field(default_factory=dict)
    material_type_counts: Dict[str, int] = field(default_factory=dict)
    avg_assembly_size: float = 0.0
    max_assembly_size: int = 0
    min_assembly_size: int = 0
    stair_count: int = 0
    rail_count: int = 0
    ladder_count: int = 0
    bolt_count: int = 0
    anchor_count: int = 0
    total_weight_estimate: float = 0.0
    has_stairs: bool = False
    has_rails: bool = False


@dataclass
class PortfolioBaseline:
    total_projects: int = 0
    total_releases: int = 0
    mean_assemblies_per_release: float = 0.0
    median_assemblies: float = 0.0
    std_assemblies: float = 0.0
    mean_pieces_per_release: float = 0.0
    median_pieces: float = 0.0
    std_pieces: float = 0.0
    mean_minor_marks: float = 0.0
    median_minor_marks: float = 0.0
    std_minor_marks: float = 0.0
    member_type_distribution: Dict[str, float] = field(default_factory=dict)
    material_type_distribution: Dict[str, float] = field(default_factory=dict)
    stair_project_count: int = 0
    rail_project_count: int = 0
    percentile_5: Dict[str, float] = field(default_factory=dict)
    percentile_95: Dict[str, float] = field(default_factory=dict)
    anomaly_thresholds: Dict[str, Tuple[float, float]] = field(default_factory=dict)


@dataclass
class AnomalyReport:
    project_name: str
    release_name: str
    metric_name: str
    actual_value: float
    expected_range: Tuple[float, float]
    deviation_pct: float
    is_anomaly: bool
    severity: str = "INFO"


def safe_mean(values: List[float]) -> float:
    if not values:
        return 0.0
    return statistics.mean(values)


def safe_median(values: List[float]) -> float:
    if not values:
        return 0.0
    return statistics.median(values)


def safe_stdev(values: List[float]) -> float:
    if len(values) < 2:
        return 0.0
    return statistics.stdev(values)


def safe_percentile(values: List[float], pct: float) -> float:
    if not values:
        return 0.0
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    k = (pct / 100.0) * (n - 1)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_vals[int(k)]
    d0 = sorted_vals[int(f)] * (c - k)
    d1 = sorted_vals[int(c)] * (k - f)
    return d0 + d1


def compute_project_metrics(kiss: KISSFile) -> ProjectMetrics:
    assemblies = list(kiss.assemblies.values())
    total_assemblies = len(assemblies)

    total_minor_marks = kiss.total_minor_marks

    unique_marks = len(
        set(mm.minor_mark for mm in kiss.all_minor_marks if mm.minor_mark)
    )

    total_pieces = sum(asm.main_qty for asm in assemblies)

    member_type_counts: Dict[str, int] = dict(Counter(kiss.get_member_types()))

    material_counter: Counter = Counter()
    for mm in kiss.all_minor_marks:
        if mm.material_type:
            material_counter[mm.material_type] += mm.quantity
    material_type_counts = dict(material_counter)

    assembly_sizes = [len(asm.minor_marks) for asm in assemblies] if assemblies else [0]
    avg_assembly_size = safe_mean([float(s) for s in assembly_sizes])
    max_assembly_size = max(assembly_sizes) if assembly_sizes else 0
    min_assembly_size = min(assembly_sizes) if assembly_sizes else 0

    stair_keywords = ("STAIR",)
    rail_keywords = ("HANDRAIL", "RAIL", "WALL RAIL")
    ladder_keywords = ("LADDER",)

    stair_count = 0
    rail_count = 0
    ladder_count = 0
    for asm in assemblies:
        desc = (asm.member_description or "").upper()
        if any(kw in desc for kw in stair_keywords):
            stair_count += asm.main_qty
        if any(kw in desc for kw in rail_keywords):
            rail_count += asm.main_qty
        if any(kw in desc for kw in ladder_keywords):
            ladder_count += asm.main_qty

    bolt_count = sum(mm.quantity for mm in kiss.all_minor_marks if mm.is_bolt)
    anchor_count = sum(mm.quantity for mm in kiss.all_minor_marks if mm.is_anchor)

    total_weight_estimate = sum(asm.main_length_mm * asm.main_qty for asm in assemblies)

    has_stairs = stair_count > 0
    has_rails = rail_count > 0

    return ProjectMetrics(
        project_name=kiss.project_name or kiss.header.job_id or "",
        total_assemblies=total_assemblies,
        total_minor_marks=total_minor_marks,
        unique_marks=unique_marks,
        total_pieces=total_pieces,
        member_type_counts=member_type_counts,
        material_type_counts=material_type_counts,
        avg_assembly_size=avg_assembly_size,
        max_assembly_size=max_assembly_size,
        min_assembly_size=min_assembly_size,
        stair_count=stair_count,
        rail_count=rail_count,
        ladder_count=ladder_count,
        bolt_count=bolt_count,
        anchor_count=anchor_count,
        total_weight_estimate=total_weight_estimate,
        has_stairs=has_stairs,
        has_rails=has_rails,
    )


def compute_portfolio_baseline(all_metrics: List[ProjectMetrics]) -> PortfolioBaseline:
    if not all_metrics:
        return PortfolioBaseline()

    n = len(all_metrics)

    assembly_counts = [float(m.total_assemblies) for m in all_metrics]
    piece_counts = [float(m.total_pieces) for m in all_metrics]
    minor_mark_counts = [float(m.total_minor_marks) for m in all_metrics]

    mean_asm = safe_mean(assembly_counts)
    median_asm = safe_median(assembly_counts)
    std_asm = safe_stdev(assembly_counts)

    mean_pcs = safe_mean(piece_counts)
    median_pcs = safe_median(piece_counts)
    std_pcs = safe_stdev(piece_counts)

    mean_mm = safe_mean(minor_mark_counts)
    median_mm = safe_median(minor_mark_counts)
    std_mm = safe_stdev(minor_mark_counts)

    member_type_total: Counter = Counter()
    for m in all_metrics:
        for mt, count in m.member_type_counts.items():
            if count > 0:
                member_type_total[mt] += 1
    member_type_distribution = {k: v / n for k, v in member_type_total.items()}

    material_type_total: Counter = Counter()
    for m in all_metrics:
        for mt, count in m.material_type_counts.items():
            if count > 0:
                material_type_total[mt] += 1
    material_type_distribution = {k: v / n for k, v in material_type_total.items()}

    stair_project_count = sum(1 for m in all_metrics if m.has_stairs)
    rail_project_count = sum(1 for m in all_metrics if m.has_rails)

    percentile_5 = {
        "assemblies": safe_percentile(assembly_counts, 5),
        "pieces": safe_percentile(piece_counts, 5),
        "minor_marks": safe_percentile(minor_mark_counts, 5),
        "avg_assembly_size": safe_percentile(
            [m.avg_assembly_size for m in all_metrics], 5
        ),
    }
    percentile_95 = {
        "assemblies": safe_percentile(assembly_counts, 95),
        "pieces": safe_percentile(piece_counts, 95),
        "minor_marks": safe_percentile(minor_mark_counts, 95),
        "avg_assembly_size": safe_percentile(
            [m.avg_assembly_size for m in all_metrics], 95
        ),
    }

    anomaly_thresholds: Dict[str, Tuple[float, float]] = {
        "assemblies": (mean_asm - 2 * std_asm, mean_asm + 2 * std_asm),
        "pieces": (mean_pcs - 2 * std_pcs, mean_pcs + 2 * std_pcs),
        "minor_marks": (mean_mm - 2 * std_mm, mean_mm + 2 * std_mm),
    }

    return PortfolioBaseline(
        total_projects=n,
        total_releases=n,
        mean_assemblies_per_release=mean_asm,
        median_assemblies=median_asm,
        std_assemblies=std_asm,
        mean_pieces_per_release=mean_pcs,
        median_pieces=median_pcs,
        std_pieces=std_pcs,
        mean_minor_marks=mean_mm,
        median_minor_marks=median_mm,
        std_minor_marks=std_mm,
        member_type_distribution=member_type_distribution,
        material_type_distribution=material_type_distribution,
        stair_project_count=stair_project_count,
        rail_project_count=rail_project_count,
        percentile_5=percentile_5,
        percentile_95=percentile_95,
        anomaly_thresholds=anomaly_thresholds,
    )


def _classify_severity(deviation_pct: float) -> str:
    abs_dev = abs(deviation_pct)
    if abs_dev >= 100.0:
        return "CRITICAL"
    if abs_dev >= 50.0:
        return "HIGH"
    if abs_dev >= 25.0:
        return "MEDIUM"
    return "LOW"


def _check_threshold(
    anomalies: List[AnomalyReport],
    project_name: str,
    release_name: str,
    metric_name: str,
    actual_value: float,
    low: float,
    high: float,
) -> None:
    mean_val = (low + high) / 2.0
    if actual_value < low:
        dev_pct = ((actual_value - mean_val) / mean_val * 100.0) if mean_val else 0.0
        anomalies.append(
            AnomalyReport(
                project_name=project_name,
                release_name=release_name,
                metric_name=metric_name,
                actual_value=actual_value,
                expected_range=(low, high),
                deviation_pct=dev_pct,
                is_anomaly=True,
                severity=_classify_severity(dev_pct),
            )
        )
    elif actual_value > high:
        dev_pct = ((actual_value - mean_val) / mean_val * 100.0) if mean_val else 0.0
        anomalies.append(
            AnomalyReport(
                project_name=project_name,
                release_name=release_name,
                metric_name=metric_name,
                actual_value=actual_value,
                expected_range=(low, high),
                deviation_pct=dev_pct,
                is_anomaly=True,
                severity=_classify_severity(dev_pct),
            )
        )


def _detect_single_anomalies(
    metrics: ProjectMetrics,
    baseline: PortfolioBaseline,
    release_name: str = "",
) -> List[AnomalyReport]:
    anomalies: List[AnomalyReport] = []
    proj = metrics.project_name
    rel = release_name

    for key in ("assemblies", "pieces", "minor_marks"):
        if key not in baseline.anomaly_thresholds:
            continue
        low, high = baseline.anomaly_thresholds[key]
        if key == "assemblies":
            actual = float(metrics.total_assemblies)
        elif key == "pieces":
            actual = float(metrics.total_pieces)
        else:
            actual = float(metrics.total_minor_marks)
        _check_threshold(anomalies, proj, rel, key, actual, low, high)

    if (
        metrics.max_assembly_size > 0
        and baseline.percentile_95.get("avg_assembly_size", 0) > 0
    ):
        p95_size = baseline.percentile_95["avg_assembly_size"]
        mean_size = baseline.mean_assemblies_per_release
        if metrics.max_assembly_size > p95_size * 2:
            dev_pct = (
                ((metrics.max_assembly_size - p95_size) / p95_size * 100.0)
                if p95_size
                else 0.0
            )
            anomalies.append(
                AnomalyReport(
                    project_name=proj,
                    release_name=rel,
                    metric_name="max_assembly_size",
                    actual_value=float(metrics.max_assembly_size),
                    expected_range=(0.0, p95_size * 2),
                    deviation_pct=dev_pct,
                    is_anomaly=True,
                    severity=_classify_severity(dev_pct),
                )
            )

    if baseline.total_projects > 5:
        for mt, freq in baseline.member_type_distribution.items():
            if freq > 0.5 and mt not in metrics.member_type_counts:
                anomalies.append(
                    AnomalyReport(
                        project_name=proj,
                        release_name=rel,
                        metric_name=f"missing_member_type:{mt}",
                        actual_value=0.0,
                        expected_range=(1.0, float("inf")),
                        deviation_pct=-100.0,
                        is_anomaly=True,
                        severity="MEDIUM",
                    )
                )

    for mt, count in metrics.member_type_counts.items():
        expected_freq = baseline.member_type_distribution.get(mt, 0.0)
        if expected_freq > 0 and count > 0:
            baseline_projects_with_type = int(expected_freq * baseline.total_projects)
            if baseline_projects_with_type > 0:
                avg_count = count
                if (
                    avg_count
                    > baseline.percentile_95.get("assemblies", float("inf")) * 3
                ):
                    dev_pct = (
                        (avg_count - baseline.percentile_95.get("assemblies", 0))
                        / baseline.percentile_95.get("assemblies", 1)
                        * 100.0
                    )
                    anomalies.append(
                        AnomalyReport(
                            project_name=proj,
                            release_name=rel,
                            metric_name=f"member_type_count:{mt}",
                            actual_value=float(count),
                            expected_range=(
                                0.0,
                                baseline.percentile_95.get("assemblies", 0) * 3,
                            ),
                            deviation_pct=dev_pct,
                            is_anomaly=True,
                            severity=_classify_severity(dev_pct),
                        )
                    )

    return anomalies


def detect_anomalies(
    metrics_list: List[ProjectMetrics],
    baseline: PortfolioBaseline,
) -> List[AnomalyReport]:
    all_anomalies: List[AnomalyReport] = []
    for metrics in metrics_list:
        project_anomalies = _detect_single_anomalies(metrics, baseline, release_name="")
        all_anomalies.extend(project_anomalies)
    return all_anomalies
