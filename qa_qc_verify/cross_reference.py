"""
Cross-Reference Verification Engine for Steel Detailing QA/QC
Verifies detail marks, gather quantities, and orphan detection across KISS data and PDF sheets.
"""

import os
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple

from .kiss_parser import KISSFile, KISSAssembly, KISSMinorMark
from .project_scanner import ReleasePackage


class Severity(Enum):
    ERROR = "Error"
    WARNING = "Warning"
    INFO = "Info"


@dataclass
class VerificationIssue:
    severity: Severity
    check_type: str
    project: str
    release: str
    mark: str
    description: str
    detail: Dict = field(default_factory=dict)


@dataclass
class CrossReferenceResult:
    project_name: str
    release_name: str
    total_assemblies: int = 0
    total_minor_marks: int = 0
    verified_details: int = 0
    orphaned_details: List[str] = field(default_factory=list)
    missing_from_erection: List[str] = field(default_factory=list)
    quantity_mismatches: List[Dict] = field(default_factory=list)
    issues: List[VerificationIssue] = field(default_factory=list)

    @property
    def has_errors(self) -> bool:
        return any(i.severity == Severity.ERROR for i in self.issues)

    @property
    def error_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == Severity.ERROR)

    @property
    def warning_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == Severity.WARNING)

    @property
    def info_count(self) -> int:
        return sum(1 for i in self.issues if i.severity == Severity.INFO)


_MARK_PATTERN = re.compile(r"^([A-Za-z]*\d+(?:\.\d+)?)")
_FILENAME_MARK_PATTERN = re.compile(r"^(.+?)_?\d*\.pdf$", re.IGNORECASE)


def _extract_marks_from_pdfs(pdf_paths: List[str]) -> List[str]:
    marks: List[str] = []
    for path in pdf_paths:
        basename = os.path.splitext(os.path.basename(path))[0]
        match = re.match(r"^(.+?)_?\d*$", basename)
        if match:
            mark = match.group(1).strip()
            marks.append(mark)
        else:
            mark = basename.strip()
            if mark:
                marks.append(mark)
    return marks


def _match_detail_to_erection(detail_mark: str, erection_marks: List[str]) -> bool:
    normalized = detail_mark.upper().strip()
    for em in erection_marks:
        em_normalized = em.upper().strip()
        if normalized == em_normalized:
            return True
        if normalized in em_normalized or em_normalized in normalized:
            return True
    return False


class CrossReferenceEngine:
    def __init__(self) -> None:
        self._results: List[CrossReferenceResult] = []

    @property
    def results(self) -> List[CrossReferenceResult]:
        return list(self._results)

    def verify_release(
        self, kiss_file: KISSFile, release: ReleasePackage
    ) -> CrossReferenceResult:
        result = CrossReferenceResult(
            project_name=release.project_name,
            release_name=os.path.basename(release.release_path),
            total_assemblies=kiss_file.total_assemblies,
            total_minor_marks=kiss_file.total_minor_marks,
        )

        self._check_all_details_on_erection(kiss_file, release, result)
        self._check_gather_quantities(kiss_file, release, result)
        self._check_orphaned_gathers(kiss_file, release, result)
        self._check_missing_gathers(kiss_file, release, result)

        self._results.append(result)
        return result

    def _check_all_details_on_erection(
        self,
        kiss: KISSFile,
        release: ReleasePackage,
        result: CrossReferenceResult,
    ) -> None:
        detail_marks_from_pdfs = _extract_marks_from_pdfs(release.detail_sheet_paths)
        erection_marks_from_pdfs = _extract_marks_from_pdfs(
            release.erection_sheet_paths
        )

        detail_mark_set = set(m.upper() for m in detail_marks_from_pdfs)

        for asm_mark, assembly in kiss.assemblies.items():
            major = assembly.major_mark or asm_mark
            major_upper = major.upper()
            asm_upper = asm_mark.upper()

            found_detail = any(
                dm == major_upper
                or dm == asm_upper
                or major_upper in dm
                or asm_upper in dm
                for dm in detail_mark_set
            )

            if not found_detail:
                if not any(
                    dm == major_upper or dm == asm_upper for dm in detail_mark_set
                ):
                    issue = VerificationIssue(
                        severity=Severity.WARNING,
                        check_type="detail_sheet_missing",
                        project=release.project_name,
                        release=result.release_name,
                        mark=major,
                        description=f"Assembly '{major}' has no corresponding detail sheet PDF",
                        detail={"assembly_mark": asm_mark, "major_mark": major},
                    )
                    result.issues.append(issue)

            found_on_erection = _match_detail_to_erection(
                major, erection_marks_from_pdfs
            ) or _match_detail_to_erection(asm_mark, erection_marks_from_pdfs)

            if not found_on_erection:
                result.missing_from_erection.append(major)
                issue = VerificationIssue(
                    severity=Severity.ERROR,
                    check_type="missing_from_erection",
                    project=release.project_name,
                    release=result.release_name,
                    mark=major,
                    description=f"Assembly '{major}' not found on any erection sheet",
                    detail={"assembly_mark": asm_mark},
                )
                result.issues.append(issue)
            else:
                result.verified_details += 1

    def _check_gather_quantities(
        self,
        kiss: KISSFile,
        release: ReleasePackage,
        result: CrossReferenceResult,
    ) -> None:
        global_bom = kiss.get_global_bom()
        gather_marks_from_pdfs = _extract_marks_from_pdfs(release.gather_sheet_paths)

        gather_mark_counts: Dict[str, int] = {}
        for gm in gather_marks_from_pdfs:
            key = gm.upper()
            gather_mark_counts[key] = gather_mark_counts.get(key, 0) + 1

        for minor_mark, kiss_qty in global_bom.items():
            minor_upper = minor_mark.upper()
            pdf_count = gather_mark_counts.get(minor_upper, 0)

            if pdf_count == 0:
                continue

            if pdf_count != kiss_qty:
                mismatch = {
                    "minor_mark": minor_mark,
                    "kiss_quantity": kiss_qty,
                    "gather_pdf_count": pdf_count,
                }
                result.quantity_mismatches.append(mismatch)
                issue = VerificationIssue(
                    severity=Severity.WARNING,
                    check_type="quantity_mismatch",
                    project=release.project_name,
                    release=result.release_name,
                    mark=minor_mark,
                    description=(
                        f"Quantity mismatch for '{minor_mark}': "
                        f"KISS={kiss_qty}, gather PDFs={pdf_count}"
                    ),
                    detail=mismatch,
                )
                result.issues.append(issue)

    def _check_orphaned_gathers(
        self,
        kiss: KISSFile,
        release: ReleasePackage,
        result: CrossReferenceResult,
    ) -> None:
        global_bom = kiss.get_global_bom()
        all_marks = kiss.get_all_marks()
        kiss_mark_set = set(m.upper() for m in all_marks.keys())

        gather_marks_from_pdfs = _extract_marks_from_pdfs(release.gather_sheet_paths)
        seen_gather = set()

        for gm in gather_marks_from_pdfs:
            gm_upper = gm.upper()
            if gm_upper in seen_gather:
                continue
            seen_gather.add(gm_upper)

            if gm_upper not in kiss_mark_set:
                result.orphaned_details.append(gm)
                issue = VerificationIssue(
                    severity=Severity.ERROR,
                    check_type="orphaned_gather",
                    project=release.project_name,
                    release=result.release_name,
                    mark=gm,
                    description=f"Gather sheet '{gm}' has no corresponding KISS entry",
                    detail={"pdf_mark": gm},
                )
                result.issues.append(issue)

    def _check_missing_gathers(
        self,
        kiss: KISSFile,
        release: ReleasePackage,
        result: CrossReferenceResult,
    ) -> None:
        global_bom = kiss.get_global_bom()
        gather_marks_from_pdfs = _extract_marks_from_pdfs(release.gather_sheet_paths)
        gather_mark_set = set(m.upper() for m in gather_marks_from_pdfs)

        for minor_mark in global_bom:
            minor_upper = minor_mark.upper()
            if minor_upper not in gather_mark_set:
                issue = VerificationIssue(
                    severity=Severity.WARNING,
                    check_type="missing_gather_sheet",
                    project=release.project_name,
                    release=result.release_name,
                    mark=minor_mark,
                    description=f"Minor mark '{minor_mark}' has no gather sheet PDF",
                    detail={
                        "minor_mark": minor_mark,
                        "kiss_quantity": global_bom[minor_mark],
                    },
                )
                result.issues.append(issue)


def aggregate_results(results: List[CrossReferenceResult]) -> Dict:
    total_assemblies = sum(r.total_assemblies for r in results)
    total_minor_marks = sum(r.total_minor_marks for r in results)
    total_verified = sum(r.verified_details for r in results)
    total_errors = sum(r.error_count for r in results)
    total_warnings = sum(r.warning_count for r in results)
    total_infos = sum(r.info_count for r in results)
    all_orphaned: List[str] = []
    all_missing_erection: List[str] = []
    all_qty_mismatches: List[Dict] = []
    all_issues: List[Dict] = []

    for r in results:
        all_orphaned.extend(r.orphaned_details)
        all_missing_erection.extend(r.missing_from_erection)
        all_qty_mismatches.extend(r.quantity_mismatches)
        for issue in r.issues:
            all_issues.append(
                {
                    "severity": issue.severity.value,
                    "check_type": issue.check_type,
                    "project": issue.project,
                    "release": issue.release,
                    "mark": issue.mark,
                    "description": issue.description,
                    "detail": issue.detail,
                }
            )

    issues_by_type: Dict[str, int] = {}
    for issue in all_issues:
        key = issue["check_type"]
        issues_by_type[key] = issues_by_type.get(key, 0) + 1

    issues_by_severity: Dict[str, int] = {}
    for issue in all_issues:
        key = issue["severity"]
        issues_by_severity[key] = issues_by_severity.get(key, 0) + 1

    return {
        "total_releases": len(results),
        "total_assemblies": total_assemblies,
        "total_minor_marks": total_minor_marks,
        "total_verified_details": total_verified,
        "total_orphaned": len(set(all_orphaned)),
        "total_missing_from_erection": len(set(all_missing_erection)),
        "total_quantity_mismatches": len(all_qty_mismatches),
        "total_errors": total_errors,
        "total_warnings": total_warnings,
        "total_infos": total_infos,
        "issues_by_type": issues_by_type,
        "issues_by_severity": issues_by_severity,
        "releases_with_errors": [r.release_name for r in results if r.has_errors],
        "orphaned_details": sorted(set(all_orphaned)),
        "missing_from_erection": sorted(set(all_missing_erection)),
    }
