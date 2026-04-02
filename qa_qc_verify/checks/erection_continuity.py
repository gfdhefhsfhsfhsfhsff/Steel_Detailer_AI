"""
Erection Plan Continuity Module
Cross-references all details on detail sheets to ensure they are accurately called out and represented on erection plans
Flags any orphaned details.
Version: 1.0.0-alpha
"""

from __future__ import annotations

import re
from typing import List, Dict, Any, Optional
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
        PiecemarkType,
        BillOfMaterial,
    )
    from DesignData.SDS2.Model import MemberBrief

    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False


from ..config import Config
from ..report import QAReport, Issue, Severity
from ..utils import ProgressTracker


@dataclass
class DetailInfo:
    """Cached detail drawing information"""

    handle: Any
    name: str
    piecemark: str
    member_type: str
    shape: Optional[str]
    grade: Optional[str]
    quantity: int
    sheet: str
    erection_views: List[str] = field(default_factory=list)
    status: Optional[Any] = field(default=None)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "handle": str(self.handle),
            "name": self.name,
            "piecemark": self.piecemark,
            "member_type": self.member_type,
            "shape": self.shape,
            "grade": self.grade,
            "quantity": self.quantity,
            "sheet": self.sheet,
            "erection_views": self.erection_views,
            "status": self.status.to_dict()
            if self.status and hasattr(self.status, "to_dict")
            else None,
        }


@dataclass
class ErectionSheetInfo:
    """Cached erection sheet information"""

    handle: Any
    name: str
    views: List[str] = field(default_factory=list)
    details: List[str] = field(default_factory=list)
    bom_piecemarks: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "handle": str(self.handle),
            "name": self.name,
            "views": self.views,
            "details": self.details,
            "bom_piecemarks": self.bom_piecemarks,
        }


class DetailType:
    MAJOR = "Major"
    MINOR = "Minor"


def verify_erection_continuity(job: Any, report: QAReport, config: Config) -> QAReport:
    """
    Module 3: Erection Plan Continuity
    Cross-references all details on detail sheets to ensure they are accurately
    called out and represented on erection plans.
    Flags any orphaned details.
    """
    tracker = ProgressTracker(total_steps=4)
    tracker.print_status("Starting Erection Plan Continuity...")

    if not API_AVAILABLE:
        report.add_error(
            module="Erection",
            object_type="System",
            location="N/A",
            description="SDS/2 API not available - cannot perform verification",
            detail={},
        )
        return report

    major_details: Dict[str, DetailInfo] = {}
    minor_details: Dict[str, DetailInfo] = {}
    detail_by_piecemark: Dict[str, DetailInfo] = {}

    erection_sheets: Dict[str, ErectionSheetInfo] = {}
    erection_piecemarks: set = set()
    detail_piecemarks: set = set()

    tracker.print_status("Scanning detail drawings...")

    detail_handles = job.GetDrawingHandles(TableWithDrawings.Detail)
    for i in range(len(detail_handles)):
        handle = detail_handles[i]
        try:
            drawing = Drawing.Get(handle)
            if not drawing:
                continue

            piecemark = drawing.Piecemark or ""
            if not piecemark:
                continue

            member_type = (
                str(drawing.Status.MemberType)
                if drawing.Status and drawing.Status.MemberType
                else "Unknown"
            )
            shape = (
                str(drawing.Status.Material)
                if drawing.Status and drawing.Status.Material
                else None
            )
            grade = shape
            quantity = (
                drawing.Status.Quantity
                if drawing.Status and hasattr(drawing.Status, "Quantity")
                else 0
            )
            sheet = (
                drawing.Status.Sheet
                if drawing.Status and hasattr(drawing.Status, "Sheet")
                else ""
            )

            detail_info = DetailInfo(
                handle=handle,
                name=drawing.Name or "",
                piecemark=piecemark,
                member_type=member_type,
                shape=shape,
                grade=grade,
                quantity=quantity,
                sheet=sheet or "",
                erection_views=[],
                status=drawing.Status if drawing.Status else None,
            )

            detail_by_piecemark[piecemark] = detail_info
            detail_piecemarks.add(piecemark)

            try:
                drawing_list = Drawing.Find(PiecemarkType.Major, piecemark)
                if drawing_list and len(drawing_list) > 0:
                    major_details[piecemark] = detail_info
            except Exception:
                pass

            try:
                drawing_list = Drawing.Find(PiecemarkType.Minor, piecemark)
                if drawing_list and len(drawing_list) > 0:
                    minor_details[piecemark] = detail_info
            except Exception:
                pass

        except Exception as e:
            report.add_warning(
                module="Erection",
                object_type="Detail",
                location=f"Detail handle index {i}",
                description=f"Error processing detail: {str(e)}",
                detail={"error": str(e)},
            )

    tracker.print_status("Scanning erection sheets...")

    erection_sheet_handles = job.GetDrawingHandles(TableWithDrawings.ErectionSheet)
    for i in range(len(erection_sheet_handles)):
        handle = erection_sheet_handles[i]
        try:
            drawing = Drawing.Get(handle)
            if not drawing:
                continue

            sheet_info = ErectionSheetInfo(
                handle=handle,
                name=drawing.Name or "",
                views=[],
                details=[],
                bom_piecemarks=[],
            )

            try:
                bom = drawing.BillOfMaterial
                if bom:
                    bom_lines = bom.GetLines()
                    for line in bom_lines:
                        pm = (
                            line.Piecemark
                            if hasattr(line, "Piecemark") and line.Piecemark
                            else None
                        )
                        if pm:
                            sheet_info.bom_piecemarks.append(pm)
                            erection_piecemarks.add(pm)
            except Exception:
                pass

            erection_sheets[str(handle)] = sheet_info

        except Exception as e:
            report.add_warning(
                module="Erection",
                object_type="ErectionSheet",
                location=f"Erection sheet handle index {i}",
                description=f"Error processing erection sheet: {str(e)}",
                detail={"error": str(e)},
            )

    tracker.print_status("Checking detail-to-erection continuity...")

    orphaned_details: List[DetailInfo] = []
    missing_details: List[str] = []

    for piecemark, detail_info in detail_by_piecemark.items():
        found_on_erection = False
        for sheet_key, sheet_info in erection_sheets.items():
            if piecemark in sheet_info.bom_piecemarks:
                found_on_erection = True
                detail_info.erection_views.append(sheet_info.name)
                if piecemark not in sheet_info.details:
                    sheet_info.details.append(piecemark)

        if not found_on_erection:
            orphaned_details.append(detail_info)
            report.add_warning(
                module="Erection",
                object_type="Detail",
                location=f"Detail '{piecemark}' on sheet '{detail_info.sheet}'",
                description=f"Detail '{piecemark}' is not referenced on any erection sheet - possible orphaned detail",
                detail={
                    "piecemark": piecemark,
                    "sheet": detail_info.sheet,
                    "member_type": detail_info.member_type,
                    "detail": detail_info.to_dict(),
                },
            )

    tracker.print_status("Checking erection-to-detail continuity...")

    for sheet_key, sheet_info in erection_sheets.items():
        for pm in sheet_info.bom_piecemarks:
            if pm not in detail_piecemarks:
                missing_details.append(pm)
                report.add_warning(
                    module="Erection",
                    object_type="ErectionView",
                    location=f"Erection sheet '{sheet_info.name}'",
                    description=f"Piecemark '{pm}' on erection sheet '{sheet_info.name}' has no matching detail drawing",
                    detail={
                        "piecemark": pm,
                        "erection_sheet": sheet_info.name,
                    },
                )

    tracker.print_status(
        f"Completed: {len(orphaned_details)} orphaned details, {len(missing_details)} missing details found"
    )

    return report
