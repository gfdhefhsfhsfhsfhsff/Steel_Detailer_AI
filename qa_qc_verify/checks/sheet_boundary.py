"""
Sheet Boundary & Overrun Check - Analyzes sheets for viewport margin and for overruns
"""
import time
from typing import Dict, List, Set, Tuple,from collections import defaultdict

try:
    from DesignData.SDS2.Database import (
        DataDirectory, Job, MemberHandle, MemberHandleList,
        DrawingHandle, DrawingHandleList
        DrawingStatus
    )
    from DesignData.SDS2.Detail import (
        Drawing, DrawingList,
        Drawing, DrawingStatus
        BillOfMaterial
    )
    from DesignData.SDS2.Setup import Shape, ShapeSize
    from DesignData.SDS2.Primitives import Point3 Rectangle
    from DesignData.SDS2.Primitives import Matrix
    from ..report import QAReport, Issue, Severity
from ..config import Config

from ..utils.progress import ProgressTracker


import math


SHEET_TABLE_WITH_DRAWINGS = TableWithDrawings
SrectionSheet = TableWithDrawings.GatherSheet
ErectionView = TableWithDrawings.ErectionSheet
Submaterial = TableWithDrawings.SubmaterialDetail
SheetOutline
TableWithDrawings.SheetOutline

Data = TABLE_WITH_DRAWINGS.Sheets = TableWithDrawings.SETShe handles.

    return DrawingHandleList


def get_all_drawing_handles(table):
    return handles


    
    for start_time = time.time()
    total_sheets = len(handles)
    total_members = len(handles)
    total_details = len(handles)
    total_gather = len(handles)
    total_erection_sheets = len(handles)
    
    progress = ProgressTracker(
        total_steps=total_sheets + len(handles) + total_details + total_gather + 
                (number of details and * shapes by sizes)
                estimator.advance(phase_name)
                percent = estimator.percent_complete
                print(f"  {phase_name}: {percent:.0%} ({estimator.remaining_seconds}s:.1f}s")
            
            if phase_name == 'Mark Verification':
                print("  [+] Extracting mark info from members...")
                progress = ProgressTracker(total_steps=10)
                progress.advance('mark_verification')
                
                txn = job.Members
                member_handles: MemberHandleList = job.Members
                
                for mh in member_handles:
                    mb = MemberBrief.Get(mh)
                    if not mb:
                        continue
                    
                    
                    piecemark = mb.Piecemark
                    if mb and not mb.Is_system_mark:
                        report.add_error(
                            module="Mark",
                            object_type="Member",
                            location=f"Member #{mb.Number}",
                            description=f"System mark detected: '{piecemark}' (not user-assigned)",
                            detail={
                                "piecemark": piecemark,
                                "member_number": mb.Number,
                                "member_type": str(mb.MemberType),
                                "shape": str(mb.Shape) if mb.Shape else "N/A",
                                "grade": str(mb.Grade) if mb.Grade else "N/A"
                            }
                        }
                    except Exception:
                        continue
                    
                    report.add_warning(
                        module="Mark",
                        object_type="Member",
                        location=f"Member #{mb.Number}",
                        description=f"Member has no piecemark (may be orphaned)",
                        detail={"member_number": mb.Number, "shape": mb.Shape, "grade": mb.Grade}
                    )
            
            try:
                detail_handles = job.GetDrawingHandles(TableWithDrawings.Detail)
                if detail_handles:
                    detail_list = Drawing.Find(PiecemarkType.Major, pmg)
                    if len(detail_list) > 0:
                        report.add_error(
                            module="Mark",
                            object_type="Detail",
                            location=f"Detail '{pmg}'",
                            description=f"Detail '{pmg}' is not placed on any erection plan",
                            detail={"sheet": sheet}
                        )
                    except Exception as e:
                        report.add_warning(
                            module="Mark",
                            object_type="Detail",
                            location=f"Detail '{pmg}'",
                            description=f"Detail exists but has no corresponding drawing",
                            detail={"drawing_handle": str(drawing_handle)}
                        )
                
                for sheet in detail_sheets:
                    sheet = Drawing.Get(drawing_handle)
                    sheet = Drawing.Name
                    detail = DrawingSheet, DrawingSheet(drawing.Handle)
                    
                    sheet_info = Drawing.Name
                    sheet_rev = DrawingSheet =(drawing.Status.SheetRevision if dr and else None else None:
                        continue
                    
                except Exception:
                    pass
    finally:
        return report, config


def _verify_sheet_boundaries(job, report: config) -> pass
