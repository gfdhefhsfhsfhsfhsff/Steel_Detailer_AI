"""
BOM Reconciliation Module
Compares Gather Sheet BOM against aggregate Detail Sheet BOMs
Version: 1.0.0-alpha
"""

from __future__ import annotations

import re
from typing import List, Set, Dict, Any, Optional
from collections import defaultdict
from dataclasses import dataclass, field

try:
    from DesignData.SDS2.Database import (
        Job,
        DrawingHandle,
        DrawingHandleList,
        TableWithDrawings,
    )
    from DesignData.SDS2.Detail import (
        Drawing,
        DrawingList,
        DrawingStatus,
        BillOfMaterial,
        PiecemarkType,
    )
    from DesignData.SDS2.Model import MemberBrief

    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False


from ..config import Config
from ..report import QAReport, Issue, Severity
from ..utils import ProgressTracker


@dataclass
class BOMLine:
    """Represents a single BOM line"""

    piecemark: str
    minor_mark: str
    description: str
    grade: str
    shape: str
    size: str
    length: float
    unit_qty: int
    total_qty: int
    unit_weight: float
    total_weight: float
    is_hidden: bool
    advance_mill: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "piecemark": self.piecemark,
            "minor_mark": self.minor_mark,
            "description": self.description,
            "grade": self.grade,
            "shape": self.shape,
            "size": self.size,
            "length": self.length,
            "unit_qty": self.unit_qty,
            "total_qty": self.total_qty,
            "unit_weight": self.unit_weight,
            "total_weight": self.total_weight,
            "is_hidden": self.is_hidden,
            "advance_mill": self.advance_mill,
        }


@dataclass
class BOMSummary:
    """BOM reconciliation summary"""

    gather_sheet: str
    detail_sheets: List[str]
    gather_bom: Dict[str, List[BOMLine]] = field(default_factory=dict)
    detail_piecemarks: Dict[str, List[BOMLine]] = field(default_factory=dict)
    detail_only_piecemarks: Set[str] = field(default_factory=set)
    total_quantities: Dict[str, int] = field(default_factory=dict)
    material_types: Dict[str, int] = field(default_factory=dict)
    shapes: Dict[str, int] = field(default_factory=dict)
    grades: Dict[str, int] = field(default_factory=dict)
    issues: List[Dict] = field(default_factory=list)

    def add_gather_line(self, line: BOMLine) -> None:
        if line.piecemark not in self.gather_bom:
            self.gather_bom[line.piecemark] = []
        self.gather_bom[line.piecemark].append(line)

    def add_detail_line(self, sheet: str, piecemark: str, line: BOMLine) -> None:
        if piecemark not in self.detail_piecemarks:
            self.detail_piecemarks[piecemark] = []
        self.detail_piecemarks[piecemark].append(line)

    def add_issue(self, issue: Dict) -> None:
        self.issues.append(issue)

    def get_gather_summary(self) -> Dict[str, Any]:
        return {
            "gather_sheet": self.gather_sheet,
            "detail_sheets": self.detail_sheets,
            "total_gather_lines": sum(len(v) for v in self.gather_bom.values()),
            "total_detail_lines": sum(len(v) for v in self.detail_piecemarks.values()),
            "issues": self.issues,
        }


class BOMReconciliationChecker:
    """Compares Gather Sheet BOM against aggregate Detail Sheet BOMs"""

    def __init__(self, job, report: QAReport, config: Config):
        self.job = job
        self.report = report
        self.config = config
        self.tracker = ProgressTracker(total_steps=4)
        self.gather_summaries: Dict[str, BOMSummary] = {}

    def run(self) -> QAReport:
        """
        Run BOM reconciliation checks.
        Compares Gather Sheet BOM against aggregate Detail Sheet BOMs.
        Verifies exact matches for:
        - Quantities
        - Material Types
        - Sizes
        - Shapes
        - Steel Grades
        """
        self.tracker.print_status("Starting BOM Reconciliation...")

        if not API_AVAILABLE:
            self.report.add_error(
                module="BOM",
                object_type="System",
                location="N/A",
                description="SDS/2 API not available - cannot perform verification",
                detail={},
            )
            return self.report

        self._read_gather_sheets()
        self._read_detail_sheets()
        self._reconcile()

        return self.report

    def _parse_bom_line(self, line) -> BOMLine:
        """Parse an API BOM line into a BOMLine dataclass"""
        return BOMLine(
            piecemark=line.Piecemark,
            minor_mark=line.MinorMark or "",
            description=line.Description or "",
            grade=str(line.Grade) or "",
            shape=str(line.Shape) if hasattr(line, "Shape") else "",
            size=str(line.Shape.Size) if hasattr(line, "Size") else "",
            length=float(line.Length) if line.Length else 0.0,
            unit_qty=int(line.UnitQuantity) if line.UnitQuantity else 0,
            total_qty=int(line.TotalQuantity) if line.TotalQuantity else 0,
            unit_weight=float(line.UnitWeight) if line.UnitWeight else 0.0,
            total_weight=float(line.TotalWeight) if line.TotalWeight else 0.0,
            is_hidden=line.IsLineHidden,
            advance_mill=line.AdvanceMill or "",
        )

    def _read_gather_sheets(self) -> None:
        """Read all gather sheet BOM data"""
        self.tracker.print_status("Reading gather sheets...")
        gather_handles = self.job.GetDrawingHandles(TableWithDrawings.GatherSheet)

        for handle in gather_handles:
            drawing = Drawing.Get(handle)
            sheet_name = drawing.Name
            bom = drawing.BillOfMaterial

            if not bom:
                continue

            lines = bom.GetLines()
            summary = BOMSummary(
                gather_sheet=sheet_name,
                detail_sheets=[],
            )

            for line in lines:
                if line.IsLineHidden:
                    continue
                bom_line = self._parse_bom_line(line)
                summary.add_gather_line(bom_line)

            self.gather_summaries[sheet_name] = summary

        total_lines = sum(
            sum(len(v) for v in s.gather_bom.values())
            for s in self.gather_summaries.values()
        )
        self.tracker.print_status(
            f"Found {len(self.gather_summaries)} gather sheets with {total_lines} BOM lines"
        )

    def _read_detail_sheets(self) -> None:
        """Read all detail sheet BOM data"""
        self.tracker.print_status("Reading detail sheets...")
        detail_handles = self.job.GetDrawingHandles(TableWithDrawings.DetailSheet)

        for handle in detail_handles:
            drawing = Drawing.Get(handle)
            sheet_name = drawing.Name
            bom = drawing.BillOfMaterial

            if not bom:
                continue

            lines = bom.GetLines()

            for line in lines:
                if line.IsLineHidden:
                    continue

                bom_line = self._parse_bom_line(line)

                for gather_name, summary in self.gather_summaries.items():
                    summary.add_detail_line(sheet_name, bom_line.piecemark, bom_line)
                    if sheet_name not in summary.detail_sheets:
                        summary.detail_sheets.append(sheet_name)

        self.tracker.print_status(
            f"Found {len(self.gather_summaries)} detail sheets with BOMs"
        )

    def _reconcile(self) -> None:
        """Compare gather BOMs against detail BOMs and report issues"""
        self.tracker.print_status("Reconciling BOM data...")
        issues: List[Dict] = []

        for gather_name, summary in self.gather_summaries.items():
            # Check matched and orphaned-from-gather
            for piecemark, gather_lines in summary.gather_bom.items():
                if piecemark in summary.detail_piecemarks:
                    detail_lines = summary.detail_piecemarks[piecemark]

                    for gather_line in gather_lines:
                        matched = False
                        for detail_line in detail_lines:
                            if detail_line.minor_mark == gather_line.minor_mark:
                                matched = True

                                detail_sheet = (
                                    summary.detail_sheets[0]
                                    if summary.detail_sheets
                                    else "N/A"
                                )

                                if detail_line.total_qty != gather_line.total_qty:
                                    issues.append(
                                        {
                                            "type": "quantity_mismatch",
                                            "piecemark": piecemark,
                                            "minor_mark": detail_line.minor_mark,
                                            "gather_sheet": gather_name,
                                            "detail_sheet": detail_sheet,
                                            "gather_quantity": gather_line.total_qty,
                                            "detail_quantity": detail_line.total_qty,
                                        }
                                    )

                                if detail_line.grade != gather_line.grade:
                                    issues.append(
                                        {
                                            "type": "grade_mismatch",
                                            "piecemark": piecemark,
                                            "minor_mark": detail_line.minor_mark,
                                            "gather_sheet": gather_name,
                                            "detail_sheet": detail_sheet,
                                            "gather_grade": gather_line.grade,
                                            "detail_grade": detail_line.grade,
                                        }
                                    )

                                if detail_line.shape != gather_line.shape:
                                    issues.append(
                                        {
                                            "type": "shape_mismatch",
                                            "piecemark": piecemark,
                                            "minor_mark": detail_line.minor_mark,
                                            "gather_sheet": gather_name,
                                            "detail_sheet": detail_sheet,
                                            "gather_shape": gather_line.shape,
                                            "detail_shape": detail_line.shape,
                                        }
                                    )
                                break

                        if not matched:
                            issues.append(
                                {
                                    "type": "orphaned_gather",
                                    "piecemark": piecemark,
                                    "minor_mark": gather_line.minor_mark,
                                    "gather_sheet": gather_name,
                                    "gather_quantity": gather_line.total_qty,
                                }
                            )
                else:
                    for gather_line in gather_lines:
                        issues.append(
                            {
                                "type": "orphaned_gather",
                                "piecemark": piecemark,
                                "minor_mark": gather_line.minor_mark,
                                "gather_sheet": gather_name,
                                "gather_quantity": gather_line.total_qty,
                            }
                        )

            # Check orphaned from detail (in detail but not gather)
            for piecemark, detail_lines in summary.detail_piecemarks.items():
                if piecemark not in summary.gather_bom:
                    for detail_line in detail_lines:
                        detail_sheet = (
                            summary.detail_sheets[0] if summary.detail_sheets else "N/A"
                        )
                        issues.append(
                            {
                                "type": "orphaned_detail",
                                "piecemark": piecemark,
                                "minor_mark": detail_line.minor_mark,
                                "detail_sheet": detail_sheet,
                                "detail_quantity": detail_line.total_qty,
                            }
                        )

        for issue in issues:
            self._add_issue_to_report(issue)

        self.print_status(issues)

    def _add_issue_to_report(self, issue: Dict) -> None:
        """Add a reconciliation issue to the QA report"""
        issue_type = issue["type"]

        if issue_type == "quantity_mismatch":
            self.report.add_error(
                module="BOM",
                object_type="Material",
                location=f"Gather Sheet '{issue['gather_sheet']}' - Material '{issue['minor_mark']}'",
                description=f"Quantity mismatch: Gather={issue['gather_quantity']}, Detail={issue['detail_quantity']}",
                detail=issue,
            )
        elif issue_type == "grade_mismatch":
            self.report.add_error(
                module="BOM",
                object_type="Material",
                location=f"Gather Sheet '{issue['gather_sheet']}' - Material '{issue['minor_mark']}'",
                description=f"Grade mismatch: Gather={issue['gather_grade']}, Detail={issue['detail_grade']}",
                detail=issue,
            )
        elif issue_type == "shape_mismatch":
            self.report.add_error(
                module="BOM",
                object_type="Material",
                location=f"Gather Sheet '{issue['gather_sheet']}' - Material '{issue['minor_mark']}'",
                description=f"Shape mismatch: Gather={issue['gather_shape']}, Detail={issue['detail_shape']}",
                detail=issue,
            )
        elif issue_type == "orphaned_gather":
            self.report.add_warning(
                module="BOM",
                object_type="Material",
                location=f"Gather Sheet '{issue['gather_sheet']}' - Material '{issue['minor_mark']}'",
                description="Material on gather sheet but not found on any detail sheet",
                detail=issue,
            )
        elif issue_type == "orphaned_detail":
            self.report.add_warning(
                module="BOM",
                object_type="Material",
                location=f"Detail Sheet '{issue['detail_sheet']}' - Material '{issue['minor_mark']}'",
                description="Material on detail sheet but not found on gather sheet",
                detail=issue,
            )

    def print_status(self, issues: List[Dict]) -> None:
        """Print reconciliation summary"""
        qty = sum(1 for i in issues if i["type"] == "quantity_mismatch")
        grade = sum(1 for i in issues if i["type"] == "grade_mismatch")
        shape = sum(1 for i in issues if i["type"] == "shape_mismatch")
        orphan_g = sum(1 for i in issues if i["type"] == "orphaned_gather")
        orphan_d = sum(1 for i in issues if i["type"] == "orphaned_detail")

        self.tracker.print_status(f"Completed: {len(issues)} BOM issues found")
        print(f"  Quantity mismatches: {qty}")
        print(f"  Grade mismatches: {grade}")
        print(f"  Shape mismatches: {shape}")
        print(f"  Orphaned from gather: {orphan_g}")
        print(f"  Orphaned from detail: {orphan_d}")


def verify_bom_reconciliation(job, report: QAReport, config: Config) -> QAReport:
    """Module 4: BOM Reconciliation entry point"""
    checker = BOMReconciliationChecker(job, report, config)
    return checker.run()
