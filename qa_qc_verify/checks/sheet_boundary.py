"""
Sheet Boundary & Overrun Check
Analyzes all detail and erection sheets for content that fits within sheet borders
Version: 1.0.0-alpha
"""

from __future__ import annotations

import math
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field

try:
    from DesignData.SDS2.Database import (
        Job,
        DrawingHandle,
        DrawingHandleList,
        TableWithDrawings,
    )
    from DesignData.SDS2.Detail import Drawing, DrawingStatus

    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False


from ..config import Config
from ..report import QAReport, Issue, Severity
from ..utils import ProgressTracker


@dataclass
class SheetInfo:
    """Cached sheet information"""

    handle: DrawingHandle
    name: str
    drawing_type: str
    length: float
    height: float
    scale: float
    rotation: float
    revision: Optional[str]
    detail_count: int
    has_bom: bool

    views: List[str] = field(default_factory=list)
    details: List[str] = field(default_factory=list)
    issues: List[Dict] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "drawing_type": self.drawing_type,
            "length": self.length,
            "height": self.height,
            "scale": self.scale,
            "rotation": self.rotation,
            "detail_count": self.detail_count,
            "has_bom": self.has_bom,
            "views": self.views,
            "details": self.details,
            "issues": self.issues,
        }


@dataclass
class ViewportInfo:
    """Information about a single viewport on a sheet"""

    name: str
    x: float
    y: float
    width: float
    height: float
    scale: float
    rotation: float
    overlaps_margin: bool

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "scale": self.scale,
            "rotation": self.rotation,
            "overlaps_margin": self.overlaps_margin,
        }


def verify_sheet_boundaries(job: Job, report: QAReport, config: Config) -> QAReport:
    """
    Module 2: Sheet Boundary & Overrun Check
    Analyzes all detail and erection sheets and verifies that all content fits within
    established sheet borders without overrunning margins.
    """
    tracker = ProgressTracker(total_steps=4)
    tracker.print_status("Starting Sheet Boundary Check...")

    if not API_AVAILABLE:
        report.add_error(
            module="Sheet",
            object_type="System",
            location="N/A",
            description="SDS/2 API not available - cannot perform verification",
            detail={},
        )
        return report

    sheets_data: List[SheetInfo] = []
    margin_inches = config.page_margin_inches

    # Get all detail sheets
    try:
        detail_sheet_handles = job.GetDrawingHandles(TableWithDrawings.DetailSheet)
        tracker = ProgressTracker(total_steps=len(detail_sheet_handles))

        for handle in detail_sheet_handles:
            try:
                drawing = Drawing.Get(handle)
                if not drawing:
                    continue

                status = drawing.Status

                sheet_info = SheetInfo(
                    handle=handle,
                    name=drawing.Name,
                    drawing_type="DetailSheet",
                    length=status.Length if status else 0,
                    height=status.Height if status else 0,
                    scale=status.DrawingScale if status else 1.0,
                    rotation=math.degrees(status.DetailRotation)
                    if status and status.DetailRotation
                    else 0,
                    revision=str(status.SheetRevision)
                    if status and status.SheetRevision
                    else None,
                    detail_count=0,
                    has_bom=drawing.BillOfMaterial is not None,
                    views=[],
                    details=[],
                    issues=[],
                )

                # Calculate effective sheet area (minus margins)
                margin_units = (
                    margin_inches * status.DrawingScale if status else margin_inches
                )
                effective_length = sheet_info.length - (2 * margin_units)
                effective_height = sheet_info.height - (2 * margin_units)

                # Check each detail on this sheet
                detail_handles = job.GetDrawingHandles(TableWithDrawings.Detail)
                for detail_handle in detail_handles:
                    try:
                        detail_drawing = Drawing.Get(detail_handle)
                        if not detail_drawing:
                            continue

                        detail_status = detail_drawing.Status

                        # Check if this detail is on this sheet
                        sheet_list = (
                            detail_status.Sheet.split(",")
                            if detail_status.Sheet
                            else ""
                        )
                        if drawing.Name not in sheet_list:
                            continue

                        sheet_info.detail_count += 1
                        sheet_info.details.append(detail_drawing.Name)

                        # Check viewport bounds
                        viewport_length = detail_status.Length
                        viewport_height = detail_status.Height
                        viewport_scale = detail_status.DrawingScale

                        # Calculate viewport position relative to sheet
                        # This is a heuristic check based on API metadata
                        # For precise checking, PDF analysis would be needed

                        # Convert to same units
                        viewport_length_scaled = viewport_length / viewport_scale
                        viewport_height_scaled = viewport_height / viewport_scale
                        sheet_length_scaled = sheet_info.length / sheet_info.scale

                        # Simple overlap check
                        if (
                            viewport_length_scaled > effective_length
                            or viewport_height_scaled > effective_height
                        ):
                            issue = {
                                "type": "viewport_overlap",
                                "detail": detail_drawing.Name,
                                "viewport_length": viewport_length_scaled,
                                "viewport_height": viewport_height_scaled,
                                "sheet_effective_length": effective_length,
                                "sheet_effective_height": effective_height,
                            }
                            sheet_info.issues.append(issue)

                            report.add_warning(
                                module="Sheet",
                                object_type="Detail",
                                location=f"Sheet '{drawing.Name}' - Detail '{detail_drawing.Name}'",
                                description=f"Detail viewport may exceed sheet margins (length: {viewport_length_scaled:.2f}, height: {viewport_height_scaled:.2f})",
                                detail=issue,
                            )
                    except Exception as e:
                        report.add_warning(
                            module="Sheet",
                            object_type="Detail",
                            location=f"Sheet '{drawing.Name}'",
                            description=f"Error checking detail: {str(e)}",
                            detail={"error": str(e)},
                        )

                sheets_data.append(sheet_info)

                # Check for any issues found on this sheet
                if sheet_info.issues:
                    report.add_warning(
                        module="Sheet",
                        object_type="Sheet",
                        location=f"Sheet '{sheet_info.name}'",
                        description=f"Sheet has {len(sheet_info.issues)} viewport(s) that may exceed margins",
                        detail={
                            "issues": sheet_info.issues,
                            "detail_count": sheet_info.detail_count,
                        },
                    )

            except Exception as e:
                report.add_warning(
                    module="Sheet",
                    object_type="Sheet",
                    location=f"Unknown Sheet",
                    description=f"Error processing sheet: {str(e)}",
                    detail={"error": str(e)},
                )
    except Exception as e:
        report.add_warning(
            module="Sheet",
            object_type="DetailSheet",
            location="N/A",
            description=f"Error processing detail sheets: {str(e)}",
            detail={"error": str(e)},
        )

    # Get all erection sheets
    try:
        erection_sheet_handles = job.GetDrawingHandles(TableWithDrawings.ErectionSheet)
        tracker = ProgressTracker(total_steps=len(erection_sheet_handles))

        for handle in erection_sheet_handles:
            try:
                drawing = Drawing.Get(handle)
                if not drawing:
                    continue

                status = drawing.Status

                sheet_info = SheetInfo(
                    handle=handle,
                    name=drawing.Name,
                    drawing_type="ErectionSheet",
                    length=status.Length if status else 0,
                    height=status.Height if status else 0,
                    scale=status.DrawingScale if status else 1.0,
                    rotation=math.degrees(status.DetailRotation)
                    if status and status.DetailRotation
                    else 0,
                    revision=str(status.SheetRevision)
                    if status and status.SheetRevision
                    else None,
                    detail_count=0,
                    has_bom=drawing.BillOfMaterial is not None,
                    views=[],
                    details=[],
                    issues=[],
                )

                # Calculate effective sheet area
                margin_units = (
                    margin_inches * status.DrawingScale if status else margin_inches
                )
                effective_length = sheet_info.length - (2 * margin_units)
                effective_height = sheet_info.height - (2 * margin_units)

                # Check erection views on this sheet
                erection_view_handles = job.GetDrawingHandles(
                    TableWithDrawings.ErectionView
                )
                for view_handle in erection_view_handles:
                    try:
                        view_drawing = Drawing.Get(view_handle)
                        if not view_drawing:
                            continue

                        view_status = view_drawing.Status

                        # Check if this view is on this erection sheet
                        sheet_list = (
                            view_status.Sheet.split(",") if view_status.Sheet else ""
                        )
                        if drawing.Name not in sheet_list:
                            continue

                        sheet_info.views.append(view_drawing.Name)

                        # Check view bounds
                        view_length = view_status.Length
                        view_height = view_status.Height
                        view_scale = view_status.DrawingScale

                        # Convert units
                        view_length_scaled = view_length / view_scale
                        view_height_scaled = view_height / view_scale

                        if (
                            view_length_scaled > effective_length
                            or view_height_scaled > effective_height
                        ):
                            issue = {
                                "type": "view_overlap",
                                "view": view_drawing.Name,
                                "view_length": view_length_scaled,
                                "view_height": view_height_scaled,
                            }
                            sheet_info.issues.append(issue)

                            report.add_warning(
                                module="Sheet",
                                object_type="ErectionView",
                                location=f"Erection Sheet '{drawing.Name}' - View '{view_drawing.Name}'",
                                description=f"Erection view may exceed sheet margins",
                                detail=issue,
                            )
                    except Exception as e:
                        report.add_warning(
                            module="Sheet",
                            object_type="ErectionView",
                            location=f"Erection Sheet '{drawing.Name}'",
                            description=f"Error checking view: {str(e)}",
                            detail={"error": str(e)},
                        )

                sheets_data.append(sheet_info)

                if sheet_info.issues:
                    report.add_warning(
                        module="Sheet",
                        object_type="Sheet",
                        location=f"Erection Sheet '{sheet_info.name}'",
                        description=f"Erection sheet has {len(sheet_info.issues)} view(s) that may exceed margins",
                        detail={
                            "issues": sheet_info.issues,
                            "view_count": len(sheet_info.views),
                        },
                    )

            except Exception as e:
                report.add_warning(
                    module="Sheet",
                    object_type="Sheet",
                    location=f"Unknown Erection Sheet",
                    description=f"Error processing erection sheet: {str(e)}",
                    detail={"error": str(e)},
                )
    except Exception as e:
        report.add_warning(
            module="Sheet",
            object_type="ErectionSheet",
            location="N/A",
            description=f"Error processing erection sheets: {str(e)}",
            detail={"error": str(e)},
        )

    # Summary
    detail_sheets_with_issues = sum(
        1 for s in sheets_data if s.issues and s.drawing_type == "DetailSheet"
    )
    erection_sheets_with_issues = sum(
        1 for s in sheets_data if s.issues and s.drawing_type == "ErectionSheet"
    )

    tracker.print_status(
        f"Completed: {detail_sheets_with_issues} detail sheets, {erection_sheets_with_issues} erection sheets with potential issues"
    )

    return report
