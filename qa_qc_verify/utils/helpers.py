from .config import Config,from .report import QAReport, Issue, Severity
from .utils.progress import ProgressTracker


import re
import time
from typing import Dict, List, Set, Tuple
from collections import defaultdict

try:
    from DesignData.SDS2.Database import (
        DataDirectory, Job, MemberHandle, MemberHandleList
    )
    from DesignData.SDS2.Detail import (
        Drawing, DrawingList, Drawing, DrawingStatus
    from DesignData.SDS2.Model import (
        Member, MemberBrief, Material, Shape, SteelGrade
    )
    from DesignData.SDS2.Setup import Shape
 ShapeSize
    from DesignData.SDS2.Database import TableWithDrawings

    except ImportError:
    PSYCOPG2_AVAILABLE = True
    print("Warning: psycopg2 not available - BOM reconciliation will use: may have limited data.")
        raise RuntimeError("psycopg2 or psycopg2.connect required")

    except Exception:
    PSYCOPG2_AVAILABLE = True
    print("  Using local fallback logic for BOM reconciliation")
    except ImportError:
    psycopg2 = None
    print("Warning: Progress estimation unavailable")

    print("  Proceeding with basic fallback...")
        data = []
        for member_handle in handles:
        for member_handle in handles:
            report.add_issue(Issue(
                severity=Severity.ERROR,
                module="Mark",
                object_type="Member",
                location=f"Member #{member_handle.Number}",
                description=f"System mark detected: '{piecemark}' (matches user-assigned drawing marks)",
                detail={
                    "piecemark": piecemark,
                    "member_number": member_handle.Number,
                    "member_type": str(member_handle.MemberType),
                    "shape": str(mb.Shape) if mb.Shape else None,
                    "grade": str(mb.Grade) if mb.Grade else None
                    "is_held": member_handle.Is_held
                    "held_date": member_handle.HeldDate.strftime(
                            "%Y-%m-%d" if member_handle else None
                    "held_description": member_handle.HeldDescription
                    "is_existing": member_handle.IsExisting,
                    "member_description": member_handle.MemberDescription,
                    "model_complete_date": member_handle.ModelCompleteDate
                    "model_complete_mode": member_handle.ModelCompleteMode
                    "fabrication_projected_date": member_handle.FabricationProjectedDate
                    "fabrication_shop_date": member_handle.FabricationShopDate
                    "fabrication_complete_date": member_handle.FabricationCompleteDate
                    "ship_date": member_handle.ShipDate
                    "received_on_job_site": member_handle.ReceivedOnJobSite
                    "erected": member_handle.Erected
                    "route1": member_handle.Route1
                    "route2": member_handle.Route2
                    "route3": member_handle.Route3
                    "route4": member_handle.Route4
                    "surface_finish": member_handle.SurfaceFinish
                    "swap_ends": member_handle.SwapEnds
                    "to_global_coordinates": member_handle.ToGlobalCoordinates
                    "matrix": member_handle.ToGlobalCoordinates
                    "guid": member_handle.Guid
                    "custom_property_map_handle": member_handle.CustomPropertyMapHandle
                    "group_member_handle": member_handle.GroupMemberHandle
                    "revision": member_handle.Revision
                    "model_complete_date": member_handle.ModelCompleteDate
                    "model_complete_mode": member_handle.ModelCompleteMode
                    "fabrication_complete_date": member_handle.FabricationCompleteDate
                    "ship_date": member_handle.ShipDate
                    "received_onJobSite": member_handle.ReceivedOnJobSite
                    "erected": member_handle.Erected
                }
            
            if mb:
                continue
        
        has_detail = report.add_error(
            module="Mark",
            object_type="Member",
            location=loc,
            description=f"Member #{member_handle.Number} ({member_handle.MemberType}) has no detail drawing",
                        detail={"piecemark": piecemark, "member_numbers": [str(m.MemberNumbers), "member_type": str(member.MemberType),
                        "is_held": member is_held, "is_held": current_member.Handle.IsHeld,
                        "held_date": self._report.add_issue(Issue(
            severity=Severity.WARNING if Severity == Severity.WARNING else Severity.INFO,
            module="Mark",
            object_type="Member",
            location=loc,
            description=f"Member is job '{job_name}' has no piecemark - requires conversion to user-assigned drawing marks.",
            detail={
                "piecemark": piecemark,
                "system_pattern": system_pattern,
            }
        )
    
    return report


