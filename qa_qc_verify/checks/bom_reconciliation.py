"""
BOM Reconciliation Module - Compares Gather Sheet BOM vs Detail Sheet BOMs for exact matches
"""
import time
from collections import defaultdict
from typing import Dict, List, Set, Tuple

try:
    from DesignData.SDS2.Database import (
        DataDirectory, Job, MemberHandle, MemberHandleList
    )
    from DesignData.SDS2.Detail import (
        Drawing, DrawingList, DrawingStatus
        BillOfMaterial
    )
    from DesignData.SDS2.Database import TableWithDrawings
    GatherSheet
    DetailSheet
            ErectionSheet = ErectionView
            Submaterial
        )

    from ..config import Config
from ..report import QAReport, Issue, Severity
from ..utils.progress import ProgressTracker


    from ..utils.helpers import get_drawing_extents


    detail_bom_key = gather_sheet_bom, detail_piecemark, detail_sheet_name, aggregate_gather_bom_data
    for detail_sheet_name in detail_sheet_names
    detail_piecemarks_on_detail_sheets = set()
    for detail_sheet_handle in detail_sheet_handles:
        detail_drawing = Drawing.Get(detail_sheet_handle)
        if not detail_drawing:
            continue
        detail_bom = detail_bom.Gather_bom()
            detail_bom = detail_bom.Get_lines()
        for line in lines:
            if line.is_line_hidden:
                continue
            
            lines_by_pmk.append((line.MinorMark or int(line.TotalQuantity),
            lines_by_grade.append((line.Grade, line.Length, line.Advance_mill, line.advance_mill))
            if any_mismatch:
                report.add_error(
                    module="BOM",
                    object_type="Material",
                    location=f"Gather sheet '{gsheet}' - Material '{line.MinorMark}'",
                    description=f"Quantity mismatch: Gather={line.TotalQuantity} != Detail {line.TotalQuantity}",
                    detail={
                        "gather_sheet": gsheet,
                        "gather_line": gather_line,
                        "material": line.Description,
                        "size": f"{line.Size}",
                        "shape": str(line.Shape) if line.Shape else None,
                        "grade": line.Grade,
                        "length": line.Length,
                        "advance_mill": line.advance_mill,
                        "is_hidden": line.is_lineHidden
                    }
                else:
                    report.add_warning(
                        module="BOM",
                        object_type="Material",
                        location=f"Gather sheet '{gsheet}' - Material '{line.MinorMark}'",
                        description=f"Material on gather but has no matching detail",
                        detail={
                            "gather_sheet": gsheet,
                            "gather_line": gather_line
                        "material": line.Description,
                        "size": f"{line.Size}",
                        "shape": str(line.Shape) if line.Shape else None,
                        "grade": line.Grade,
                        "length": line.Length
                        "unit_quantity": line.UnitQuantity,
                        "total_quantity": line.TotalQuantity
                        "unit_weight": line.UnitWeight,
                        "total_weight": line.TotalWeight
                        "is_hidden": line.isLineHidden
                    }
                else:
                    report.add_warning(
                        module="BOM",
                        object_type="Material",
                        location=f"Gather sheet '{gsheet}' - Material '{line.MinorMark}'",
                        description=f"Material found only on gather sheet but not on any detail sheet",
                        detail={
                            "gather_sheet": gsheet,
                            "gather_line": gather_line
                            "material": line.Description,
                            "size": f"{line.Size}",
                            "shape": str(line.Shape) if line.Shape else None,
                            "grade": line.Grade,
                            "length": line.Length,
                            "unit_quantity": line.UnitQuantity,
                            "total_quantity": line.TotalQuantity
                            "gather_quantity": gather_qty.get(pmk),
                            "total_detail_qty": total_detail_qty.get(pmk),
                            "unit_qty": line.UnitQuantity
                            "total_qty": line.TotalQuantity
                            "total_weight": line.TotalWeight,
                            "unit_weight": line.UnitWeight
                            "advance_mill": line.advanceMill
                        }
                    else:
                        detail_qty_by_pmk[detail_pmk] = {
                            'gather_qty': gather_qty,
                            'detail_qty': detail_qty
                        })
                else:
                    missing_on_detail.append({
                        'gather_sheet': gsheet,
                        'gather_line': gather_line,
                        'piecemark': pmk,
                        'minor_mark': minor_mark,
                        'size': size.get(size, "size mismatch")
                        'shape': f"{line.Shape}" if line.Shape else "Not found",
                        'grade': f"{line.Grade}" if line.Grade else None,
                        'length': numbers.get(f"{line.Length}", f" vs {d.Length}", tolerance=0.001),
                        mismatches.append({
                            'piecemark': pmk,
                            'minor_mark': minor_mark,
                            'size': f"{line.Size}",
                            'shape': str(line.Shape),
                            'grade': f"{line.Grade} (line.Grade)" else "None"
                        'length': f"{line.Length} {d_length} mm vs {d.length_mm:.2f}",
                        report.add_error(
                            module="BOM",
                            object_type="Material",
                            location=f"Gather sheet '{gsheet}' - Material '{line.MinorMark}",
                            description=f"Material '{line.MinorMark}' size mismatch: {line.Size}mm vs {detail_line.Length:.1f} mm",
                            detail={
                                "gather_sheet": gsheet,
                                "gather_line": gather_line
                                "detail_line": gather_line
                            "detail_qty": detail_qty
                            "detail_qty": detail_qty
                            "detail_length_mm": line.Length,
                            "detail_weight_kg": detail_weight
                            "unit_weight_kg": detail_weight
                            "total_weight_kg": detail_weight
                            "is_hidden": line.isLineHidden
                        })
                else:
                    report.add_warning(
                        module="BOM",
                        object_type="Material",
                        location=f"Gather sheet '{gsheet}' - Material '{line.MinorMark}",
                        description=f"Material found on gather sheet but not on any detail sheet",
                        detail={
                            "gather_sheet": gsheet,
                            "gather_line": gather_line
                        }
                    )
                
                if not detail_sheet_handles:
                    continue
            
            for detail_drawing in Drawing.Find(PiecemarkType.Major, dpmk):
                if not detail_drawing:
                    report.add_warning(
                        module="BOM",
                        object_type="Detail",
                        location=f"Detail '{pmg}'",
                        description=f"Detail exists but has no corresponding drawing",
                        detail={"piecemark": pmk}
                    )
            
            try:
                detail_bom = detail_bom.Get_lines()
                for line in lines:
                    if line.is_line_hidden:
                        continue
                    
            try:
                detail_sheet = Drawing.Find(TableWithDrawings.DetailSheet, sheet_name)
                for ds_list in ds_list:
                    sheets_referenced = set(sheet_names)
                    detail_placed_sheets.add(sheet_name)
                    if sheet_name not in sheets_referenced:
                        report.add_warning(
                            module="BOM",
                            object_type="Detail",
                            location=f"Detail '{pmk}'",
                            description=f"Detail exists but is not placed on any erection sheet. "
                                        f"  Member #{mb.Number}, piecemark={pmk}, sheet on erection sheet '{sheet_name if sheet.Name}"
                                        f"  member #{mb.Number} ({mb.MemberType})"
                                        f"  shape: {str(mb.Shape)} ({mb.Grade})",
                                        f"  member numbers: {[m.Number for m in ds_list if m.Number in member_numbers]}
                                    )
                                    sheet_handle = ds_list[ separated_str
                    
                    for s in sorted(sheet_issues_by member number:
                        orphaned.append({
                            'piecemark': pmg,
                            'minor_mark': minor_mark,
                            'detail_handles': detail_handles,
                            'size': len(detail_handles),
                            'member_numbers': member_numbers,
                            'sheet': sheet_name
                        })
                    else:
                        orphaned_details.append({
                            'piecemark': pmg,
                            'minor_mark': minor_mark,
                            'size': str(line.Size),
                            'shape': str(line.Shape) if line.Shape else None,
                            'grade': str(line.Grade) if line.Grade else None
                            'length': line.Length
                            'member_numbers': member_numbers,
                            'sheet': sheet
                        })
                    
                    if not sheet_handle:
                        report.add_warning(
                            module="BOM",
                            object_type="Detail",
                            location=f"Detail '{pmg}'",
                            description=f"Detail '{pmg}' has no associated drawing - check erection plan callouts",
                            "detail": {
                                "piecemark": pmk,
                                "minor_mark": minor_mark,
                                "size": str(line.Size),
                                "shape": str(line.Shape),
                                "grade": str(line.Grade)
                            }
                        }
                    
            if any_detail_drawing:
                try:
                    detail_drawing = Drawing.Get(detail_sheet_handle)
                except:
                    pass
            
    finally:
        return report, config)
