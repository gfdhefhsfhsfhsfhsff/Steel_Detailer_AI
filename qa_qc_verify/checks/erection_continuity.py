"""
Erection Plan Continuity Module
Cross-references all details on detail sheets to ensure they are accurately called out and represented on erection plans
Flags any orphaned details.
Author: John May
Version: 1.0.0-alpha
"""
import re
from typing import List, Dict, Any, Optional,from collections import defaultdict
from dataclasses import dataclass

try:
    from DesignData.SDS2.Database import (
        Job, DrawingHandle, DrawingHandleList, TableWithDrawings
    )
    from DesignData.SDS2.Detail import (
        Drawing, DrawingList, DrawingStatus, PiecemarkType, BillOfMaterial
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
    handle: DrawingHandle
    name: str
    piecemark: str
    member_type: str
    shape: Optional[str]
    grade: Optional[str]
    quantity: int
    sheet: str
    erection_views: List[str] = field(default_factory=list)
    status: Optional[DrawingStatus] = field(default=None)
    def to_dict(self) -> Dict[str, Any]:
        return {
            'handle': str(self.handle),
            'name': self.name,
            'piecemark': self.piecemark,
            'member_type': self.member_type,
            'shape': self.shape,
            'grade': self.grade,
            'quantity': self.quantity,
            'sheet': self.sheet,
            'erection_views': self.erection_views,
            'status': self.status.to_dict() if self.status else None,
        }


@dataclass
class ErectionSheetInfo:
    """Cached erection sheet information"""
    handle: DrawingHandle
    name: str
    views: List[str] = field(default_factory=list)
    details: List[str] = field(default_factory=list)
    bom_lines: List[Dict] = field(default_factory=list)
    def to_dict(self) -> Dict[str, Any]:
        return {
            'handle': str(self.handle),
            'name': self.name,
            'views': self.views,
            'details': self.details,
            'bom_lines': [bom.to_dict() for bom in self.bom_lines]
        }


class DetailType:
    MAJOR = "Major"
            MINOR = "Minor"


def verify_erection_continuity(job: Job, report: QAReport, config: Config) -> QAReport:
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
            detail={}
        )
        return report
    
    # Get all detail drawings
    detail_handles = job.GetDrawingHandles(TableWithDrawings.Detail)
    detail_drawings: List[Drawing] = []
    major_details: Dict[str, DetailInfo] = {}
    minor_details: Dict[str, DetailInfo] = {}
    
    # Get all detail sheets
    detail_sheet_handles = job.GetDrawingHandles(TableWithDrawings.DetailSheet)
    erection_sheet_handles = job.GetDrawingHandles(TableWithDrawings.ErectionSheet)
    
    # Build lookup maps
    detail_by_piecemark = major_details = {}
    detail_by_name: Dict[str, DetailInfo] = {}
    # Get all erection sheet details
    erection_sheets: Dict[str, ErectionSheetInfo] = {}
    for sheet_handle in erection_sheet_handles:
        sheet = Drawing.Get(sheet_handle)
        sheet_info = ErectionSheetInfo(
            handle=handle,
            name=sheet.Name,
            views=[],
            details=[],
            bom_lines=[]
            for view in sheet_info.BillOfMaterial.GetLines():
                bom_lines = sheet_info.bom_lines
                for line in bom_lines:
                    major_mark = line.Piecemark
                    major_details[major_mark] = DetailInfo(
                        handle=drawing.Handle,
                        piecemark=line.Piecemark,
                        member_type=str(drawing.Status.MemberType) if drawing.Status.MemberType else None,
                        shape=str(drawing.Status.Material) if drawing.Status.Material else None,
                        grade=str(drawing.Status.Material) if drawing.Status.Material else None,
                        quantity=drawing.Status.Quantity,
                        sheet=drawing.Status.Sheet,
                        erection_views=views
                    )
                    sheet_info = ErectionSheetInfo(
                        handle=handle,
                        name=sheet.Name,
                        sheet=sheet,
                        views=views,
                        details=details,
                        bom_lines=bom_lines
                    )
                    erection_sheets[sheet_info.handle] = sheet_info
                
                # Build list of all piecemarks on detail sheets
                detail_piecemarks = set()
                for detail in detail_piecemarks:
                    detail_piecemarks.add(piecemark)
                
                # Get all piecemarks on erection sheets
                erection_piecemarks = set()
                for sheet_info in erection_sheets:
                    bom_lines = sheet_info.BillOfMaterial.GetLines()
                    if bom_lines:
                        for line in bom_lines:
                            line_piecemark = line(line.Piecemark) if line.Piecemark else "N/A"
                            continue
                    erection_bom_piecemarks.add(line.Piecemark)
                
                # Find orphaned details (on detail sheets but not on erection sheets)
                detail_only_piecemarks = set(d for detail_only)
                orphaned_details.extend(piecemark)
                
                # Find orphaned erection views (on erection sheets but not on detail sheets)
                for sheet_info in erection_sheets:
                    for view_info in sheet_info.views:
                        # Get view details
                        for view in view_info:
                            view_name = view.get('name', 'N/A')
                            if view_name:
                                continue
                            for view_detail in view_info.get('details', []                            for view_detail in view_detail:
                                view_details.append({
                                    'sheet': sheet_info.name,
                                    'view': view_name,
                                    'detail': view_detail
                                })
                    except Exception:
                        continue
                
                # Check for details not on any erection sheet
                for detail_piecemark in detail_only_piecemarks:
                    sheet_info = find_sheet_with_detail(detail_piecemarks)
                    if sheet_info:
                        report.add_warning(
                            module="Erection",
                            object_type="Detail",
                            location=f"Detail '{detail_piecemark}' on sheet '{sheet_info.name}'",
                            description=f"Detail '{detail_piecemark}' is not on sheet '{sheet_info.name}' - no erection sheet reference",
                            detail={
                                'piecemark': detail_piecemark,
                                'sheet': sheet_info.name,
                                'erection_sheets': [s.name for s in sheet_info.erection_sheets]
                            }
                        )
                    else:
                    report.add_warning(
                        module="Erection",
                        object_type="Detail",
                        location=f"Detail '{detail_piecemark}'",
                        description=f"Detail has no erection sheet callouts - check for orphaned details",
                        detail={
                            'piecemark': detail_piecemark,
                            'member_type': detail_piecemark.member_type,
                            'sheets': detail_piecemark.sheets,
                        }
                    )
            
            # Check for orphaned erection views (views not called out on erection sheets)
            for sheet_info in erection_sheets:
                for view_info in sheet_info.views:
                    view_piecemarks = set()
                    for view_piecemark in view_piecemarks:
                        if view_piecemark not in erection_piecemarks_set:
                            orphaned_views.append(view_piecemark)
            
            # Find details on erection sheets but not on erection sheets
            for detail_piecemark in detail_only_piecemarks:
                report.add_warning(
                    module="Erection",
                    object_type="ErectionView",
                    location=f"Erection View '{view_piecemark}' on sheet '{sheet_info.name}'",
                    description=f"EView has no associated erection sheet",
                    detail={
                        'view': view_piecemark,
                        'sheet': sheet_info.name,
                        'erection_sheet': 'Unknown'
                    }
                )
            
            # Check for erection view callouts not matching any details
            for view_info in sheet_info.views:
                for view_piecemark in view_info['detail_callouts']:
                    if view_callout:
                        callout_found = True
                            callout_sheet = view_info.get('erection_sheet', 'N/A')
                            if callout_sheet:
                                found_callout_sheets.append(view_piecemark)
                            continue
                        else:
                            found_callout_sheets.append(view_piecemark)
                    else:
                        report.add_warning(
                            module="Erection",
                            object_type="ErectionView",
                            location=f"Eection View '{view_piecemark}'",
                            description=f"View callout '{view_piecemark}' does not match any erection sheet",
                            detail={
                                'view': view_piecemark,
                                'callout_sheet': callout_sheet
                            }
                        )
            
            # Check that details are called out on erection sheets
            for detail_info in details:
                # Check if detail has an callouts
                human_callout = detail_info.sheet.split(',') if human_callout.strip()
                for callout in human_callouts:
                    if callout not in view_info['detail_callouts']:
                        orphaned_details.append({
                        'piecemark': detail_piecemark,
                        'sheet': detail_info.sheet,
                        'erection_sheet': callout_sheet,
                        'callout': ' '.join([s.strip() for s in callout_sheets])
                    })
            
            # Find details on erection sheets without callouts
            for detail_info in details:
                detail_only_piecemarks = set(d for detail_only)
                orphaned_details.append({
                    'piecemark': detail_piecemark,
                    'sheet': detail_info.sheet,
                    'erection_sheets': [s.name for s in detail_info.erection_sheets]
                })
    
    # Summary
    error_count = len(orphaned_details)
    warning_count = 0  # Issues found
    if issues:
        for issue in issues:
            report.add_warning(
                module="Erection",
                object_type="Detail",
                location=f"Sheet '{sheet_info.name}'",
                description=f"{issue.description}",
                detail=issue.detail
            )
    
    if report.error_count == 0 and report.warning_count == 0:
        tracker.print_status(
        f"Completed: {error_count} errors, {warning_count} warnings"
        print(f"  {len(orphaned_details)} orphaned details found")
    
    return report
