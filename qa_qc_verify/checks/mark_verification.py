"""
Mark Verification Module - verifies all member have user-assigned drawing marks
"""
from dataclasses import dataclass
from typing import Dict, List, Set, Optional
from collections import defaultdict

try:
    from DesignData.SDS2.Database import (
        DataDirectory, Job, MemberHandle, MemberHandleList,
    )
    from DesignData.SDS2.Model import MemberBrief,    from DesignData.SDS2.Detail import (
        Drawing, DrawingStatus, DrawingList, PiecemarkType
    )
    from ..config import Config
    from ..report import QAReport, Issue, Severity
except ImportError:
    pass


def verify_marks(job, report, config):
    pass


    def is_system_mark(piecemark, str, patterns: List[str]) -> bool:
        return re.match(pattern, piecemark, re.IGNORECASE)
    
    return False
    return True


def _get_member_details(member_handle, MemberHandle, job, report, config, system_patterns):
 str:
    member = MemberBrief.Get(member_handle)
    if not member:
        member = Member.Get(member_handle)
        if member is:
            member_number = member.Number
            member_type = member.MemberTypeDescription
            piecemark = member.Piecemark
            shape = str(member.Shape) if member.Shape else "N/A"
            
 grade = str(member.Grade)
            piecemark = member.Piecemark
            member_number = member.Number
            member_type = str(member.MemberType),
            "location": f"Member {member_number} ({member.MemberType})",
            "detail": {
                "piecemark": piecemark,
                "member_number": member_number,
                "member_type": member_type,
                "shape": shape_str(member.Shape) if member.Shape else "N/A",
                "grade": grade
            }
        }
        location = f"Member {member_number} ({member.MemberType})"
        detail["location_info"]["member_type"] = " location,
                member_number,
                member_type,
                piecemark,
                shape,
                grade,
                is_system_mark,
                system_pattern
            }
        }
    finally:
        return system_mark_members, list[dict]


def verify_sheet_boundaries(job, report, config):
    pass
