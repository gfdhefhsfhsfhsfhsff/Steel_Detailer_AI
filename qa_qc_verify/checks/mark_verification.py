"""
Mark Verification Module
Verifies all member piecemarks are user-assigned drawing marks
Version: 1.0.0-alpha
"""

from __future__ import annotations

import re
from typing import List, Set, Dict, Any, Optional
from dataclasses import dataclass, field

try:
    from DesignData.SDS2.Database import (
        Job,
        MemberHandle,
        MemberHandleList,
        DrawingHandle,
        DrawingHandleList,
        TableWithDrawings,
        ReadOnlyTransaction,
    )
    from DesignData.SDS2.Model import MemberBrief, Member
    from DesignData.SDS2.Detail import (
        Drawing,
        DrawingList,
        DrawingStatus,
        PiecemarkType,
    )

    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False


from ..config import Config
from ..report import QAReport, Issue, Severity


from ..utils import ProgressTracker


@dataclass
class MemberInfo:
    """Cached member information"""

    handle: MemberHandle
    number: int
    piecemark: str
    member_type: str
    shape: Optional[str]
    grade: Optional[str]
    is_system_mark: bool = False
    sheets: List[str] = field(default_factory=list)

    detail_handle: Optional[DrawingHandle] = field(default=None)

    revision: Optional[str] = field(default=None)

    is_held: bool = False
    held_date: Optional[str] = field(default=None)

    held_description: Optional[str] = field(default=None)

    is_existing: bool = False
    surface_finish: Optional[str] = field(default=None)
    is_galvanized: bool = False
    category: Optional[str] = field(default=None)
    sequence: Optional[str] = field(default=None)

    route1: Optional[str] = field(default=None)
    route2: Optional[str] = field(default=None)
    route3: Optional[str] = field(default=None)
    route4: Optional[str] = field(default=None)

    left_end: Optional[str] = field(default=None)
    right_end: Optional[str] = field(default=None)
    guid: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)

    swap_ends: bool = False
    model_complete_date: Optional[str] = field(default=None)
    fabrication_projected_date: Optional[str] = field(default=None)
    fabrication_shop_date: Optional[str] = field(default=None)
    fabrication_complete_date: Optional[str] = field(default=None)
    ship_date: Optional[str] = field(default=None)
    projected_ship_date: Optional[str] = field(default=None)
    received_on_job_site: Optional[str] = field(default=None)
    erected_date: Optional[str] = field(default=None)

    submitted_for_approval: Optional[str] = field(default=None)
    received_for_approval: Optional[str] = field(default=None)
    approval: Optional[str] = field(default=None)

    approval_status: Optional[str] = field(default=None)

    group_handle: Optional[str] = field(default=None)
    custom_property_handle: Optional[str] = field(default=None)

    model_complete_mode: Optional[str] = field(default=None)

    to_global_coordinates: Optional[Any] = field(default=None)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "number": self.number,
            "piecemark": self.piecemark,
            "member_type": self.member_type,
            "shape": self.shape,
            "grade": self.grade,
            "is_system_mark": self.is_system_mark,
            "sheets": self.sheets,
            "detail_handle": str(self.detail_handle) if self.detail_handle else None,
            "revision": self.revision,
            "is_held": self.is_held,
            "held_date": str(self.held_date) if self.held_date else None,
            "held_description": self.held_description,
            "is_existing": self.is_existing,
            "surface_finish": str(self.surface_finish) if self.surface_finish else None,
            "is_galvanized": self.is_galvanized,
            "category": str(self.category) if self.category else None,
            "sequence": str(self.sequence) if self.sequence else None,
            "routes": {
                "route1": str(self.route1) if self.route1 else None,
                "route2": str(self.route2) if self.route2 else None,
                "route3": str(self.route3) if self.route3 else None,
                "route4": str(self.route4) if self.route4 else None,
            },
            "ends": {
                "left_end": str(self.left_end) if self.left_end else None,
                "right_end": str(self.right_end) if self.right_end else None,
            },
            "dates": {
                "model_complete_date": str(self.model_complete_date)
                if self.model_complete_date
                else None,
                "fabrication_projected_date": str(self.fabrication_projected_date)
                if self.fabrication_projected_date
                else None,
                "fabrication_shop_date": str(self.fabrication_shop_date)
                if self.fabrication_shop_date
                else None,
                "fabrication_complete_date": str(self.fabrication_complete_date)
                if self.fabrication_complete_date
                else None,
                "ship_date": str(self.ship_date) if self.ship_date else None,
                "projected_ship_date": str(self.projected_ship_date)
                if self.projected_ship_date
                else None,
                "received_on_job_site": str(self.received_on_job_site)
                if self.received_on_job_site
                else None,
                "erected_date": str(self.erected_date) if self.erected_date else None,
                "submitted_for_approval": str(self.submitted_for_approval)
                if self.submitted_for_approval
                else None,
                "received_for_approval": str(self.received_for_approval)
                if self.received_for_approval
                else None,
            },
            "other": {
                "description": self.description,
                "swap_ends": self.swap_ends,
                "model_complete_mode": str(self.model_complete_mode)
                if self.model_complete_mode
                else None,
                "approval_status": str(self.approval_status)
                if self.approval_status
                else None,
                "group_handle": str(self.group_handle) if self.group_handle else None,
                "custom_property_handle": str(self.custom_property_handle)
                if self.custom_property_handle
                else None,
                "guid": str(self.guid) if self.guid else None,
                "to_global_coordinates": str(self.to_global_coordinates)
                if self.to_global_coordinates
                else None,
            },
        }


def verify_marks(job: Job, report: QAReport, config: Config) -> QAReport:
    """
    Module 1: Mark Verification
    Scans all members in the model and verifies that all system marks
    have been successfully converted to user-assigned drawing marks.
    Flags any remaining system marks (e.g., B_1, VB_1, p1, C_1, M_1)
    """
    tracker = ProgressTracker(total_steps=4)
    tracker.print_status("Starting Mark Verification...")

    if not API_AVAILABLE:
        report.add_error(
            module="Mark",
            object_type="System",
            location="N/A",
            description="SDS/2 API not available - cannot perform verification",
            detail={},
        )
        return report

    # Get all member handles
    member_handles = job.Members
    total_members = len(member_handles)
    tracker = ProgressTracker(total_steps=total_members)

    system_patterns = config.get_system_patterns()
    members_data: List[MemberInfo] = []

    for i in range(total_members):
        handle = member_handles[i]

        # Update progress
        info = tracker.advance(f"Member {i + 1}/{total_members}")
        if i % 50 == 0 or (i + 1) % 100 == 0:
            tracker.print_status(f"Processing member {i + 1}/{total_members}")

        try:
            # Get member brief for fast access
            member_brief = MemberBrief.Get(handle)

            if not member_brief:
                continue

            # Build member info
            member_info = MemberInfo(
                handle=handle,
                number=member_brief.Number,
                piecemark=member_brief.Piecemark or "",
                member_type=str(member_brief.MemberType)
                if member_brief.MemberType
                else "Unknown",
                shape=str(member_brief.Shape) if member_brief.Shape else None,
                grade=str(member_brief.Grade) if member_brief.Grade else None,
                is_system_mark=config.is_system_mark(member_brief.Piecemark),
                sheets=[],
                detail_handle=None,
                revision=str(member_brief.Revision) if member_brief.Revision else None,
                is_held=member_brief.IsHeld,
                held_date=str(member_brief.HeldDate) if member_brief.HeldDate else None,
                held_description=member_brief.HeldDescription,
                is_existing=member_brief.IsExisting,
                surface_finish=str(member_brief.SurfaceFinish)
                if member_brief.Surface_finish
                else None,
                is_galvanized=member_brief.IsGalvanized,
                category=str(member_brief.Category) if member_brief.Category else None,
                sequence=str(member_brief.Sequence) if member_brief.Sequence else None,
                route1=str(member_brief.Route1) if member_brief.Route1 else None,
                route2=str(member_brief.Route2) if member_brief.Route2 else None,
                route3=str(member_brief.Route3) if member_brief.Route3 else None,
                route4=str(member_brief.Route4) if member_brief.Route4 else None,
                left_end=str(member_brief.Left) if member_brief.Left else None,
                right_end=str(member_brief.Right) if member_brief.Right else None,
                description=member_brief.MemberDescription,
                swap_ends=member_brief.SwapEnds,
                model_complete_date=str(member_brief.ModelCompleteDate)
                if member_brief.ModelCompleteDate
                else None,
                model_complete_mode=str(member_brief.ModelCompleteMode)
                if member_brief.ModelCompleteMode
                else None,
                fabrication_projected_date=str(member_brief.FabricationProjectedDate)
                if member_brief.FabricationProjectedDate
                else None,
                fabrication_shop_date=str(member_brief.FabricationShopDate)
                if member_brief.FabricationShopDate
                else None,
                fabrication_complete_date=str(member_brief.FabricationCompleteDate)
                if member_brief.FabricationCompleteDate
                else None,
                ship_date=str(member_brief.ShipDate) if member_brief.ShipDate else None,
                projected_ship_date=str(member_brief.ProjectedShipDate)
                if member_brief.ProjectedShipDate
                else None,
                received_on_job_site=str(member_brief.ReceivedOnJobSite)
                if member_brief.ReceivedOnJobSite
                else None,
                erected_date=str(member_brief.Erected)
                if member_brief.Erected
                else None,
                submitted_for_approval=str(member_brief.SubmittedForApproval)
                if member_brief.SubmittedForApproval
                else None,
                received_for_approval=str(member_brief.ReceivedForApproval)
                if member_brief.ReceivedForApproval
                else None,
                guid=str(member_brief.Guid) if member_brief.Guid else None,
            )

            # Get detail drawing if exists
            try:
                drawing_list = Drawing.Find(PiecemarkType.Major, member_info.piecemark)
                if drawing_list and len(drawing_list) > 0:
                    drawing = drawing_list[0]
                    member_info.detail_handle = drawing.Handle
                    member_info.sheets = (
                        drawing.Status.Sheet.split(",") if drawing.Status.Sheet else []
                    )
                    member_info.revision = (
                        str(drawing.Status.SheetRevision)
                        if drawing.Status.SheetRevision
                        else None
                    )
            except Exception:
                pass

            members_data.append(member_info)

            # Check for system marks
            if member_info.is_system_mark:
                # Build location string with exact detail
                sheet_info = ""
                if member_info.sheets:
                    sheet_info = f" on sheet(s): {', '.join(member_info.sheets)}"
                else:
                    sheet_info = "(not on any sheet)"

                location = f"Member #{member_info.number} ({member_info.member_type})"
                if sheet_info:
                    location += f" {sheet_info}"

                report.add_error(
                    module="Mark",
                    object_type="Member",
                    location=location,
                    description=f"System mark detected: '{member_info.piecemark}' has not been converted to user-assigned drawing mark",
                    detail=member_info.to_dict(),
                )
        except Exception as e:
            report.add_warning(
                module="Mark",
                object_type="Member",
                location=f"Member index {i + 1}",
                description=f"Error processing member: {str(e)}",
                detail={"error": str(e)},
            )

    # Summary
    error_count = sum(1 for m in members_data if m.is_system_mark)
    warning_count = len(members_data) - error_count

    tracker.print_status(
        f"Completed: {error_count} system marks found, {warning_count} warnings"
    )

    return report
