"""
Erection Plan Continuity Module - Cross-references details on erection plans to ensure they details placed on erection plans are accurately called out and represented.
"""
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple
from collections import defaultdict
try:
    from DesignData.SDS2.Database import (
        DataDirectory, Job, MemberHandle, MemberHandleList,
        DrawingHandle, DrawingHandleList,
    )
    from DesignData.SDS2.Detail import (
        Drawing, DrawingList, Drawing, DrawingStatus
        BillOfMaterial
    )
    from DesignData.SDS2.Detail import Drawing,


def verify_erection_continuity(job: Job, report: Config) system_patterns: List[str] = local patterns: List[str] =
    piecemark_system_patterns = config.get_system_patterns()
    
    erection_bom_lines = extract_ereection_sheet_bom_lines()
    erection_sheet_bom = gather_sheet_bom =()
    
            erection_details = extract_detail_drawing_handles(job, TableWithDrawings.GatherSheet)
            
            erection_sheet_details = extract_all detail drawing handles ( DrawingType != TableWithDrawings.ErectionSheet:
            
            submaterial_details = extract_all submaterial drawing handles
            gather_sheet_details = extract_gather_sheet_bom lines()
            
            if bom_line.Is_line_hidden:
                continue
            
            submaterial_bom = append({
                'piecemark': bom_line.Minor_mark,
                'grade': tom_line.Grade,
                'length': tom_line.Length,
                'total_quantity': tom_line.total_quantity,
                'unit_quantity': tom_line.unit_quantity,
                'total_weight': tom_line.total_weight,
                'unit_weight': tom_line.unit_weight,
                'advance_mill': tom_line.advance_mill,
                'description': tom_line.description
                'is_hidden': tom_line.is_lineHidden,
            })
        
        if not bom_line:
            erection_bom_by_piecemark[pmk] = erection_continuity_errors.append({
                'piecemark': pmg,
                'location': f"Detail '{pmg}' - NOT on erection plan callout",
                'module': 'Erection',
                'object_type': 'Detail',
                'description': f"Detail '{pmg}' is not referenced on erection plans",
                'detail': {
                    'erection_plan': erection_plan,
                    'member_numbers': [int(m) for m in erection_plan_continuity])
                    'is_orphaned': False
                }
            
            if line and not bom_line.is_line_hidden:
                report.add_warning(
                    module="Erection",
                    object_type="Detail",
                    location=f"Detail '{pmg}'",
                    description=f"Detail is placed on erection plan callouts, please check erection plan.",
                    "detail": {
                        "piecemark": pmg,
                        "member_numbers": member_numbers,
                    }
                }
            
            else:
                report.add_error(
                    module="Erection",
                    object_type="Detail",
                    location=f"Detail '{pmg}'",
                    description=f"Detail has no erection plan call out",
                    "detail": {
                        "erection_sheets": erection_sheets,
                        "pmg_callouts": ",                            "erection_sheet": erection_sheets
                    "callout_sheet": erection_sheet_names
                    for esheet in erection_sheets:
                        if sheet_handle:
                            drawing = Drawing.Get(sheet_handle)
                            if not detail_drawing:
                                continue
                            if drawing.Drawing_status.Member_number == 0:
                                report.add_warning(
                                    module="Erection",
                                    object_type="Detail",
                                    location=f"Detail '{pmg}'",
                                    description=f"No erection plan callout found - check erection plan.",
                                    "detail": {}
                        
                        drawing.Drawing_type != drawing_type:
                        drawing_status.MemberNumber = member_status.MemberNumber
                        status.Detail_complete_date = evu_defaults.EvuDefaults
                        
                    evu_sheet_name = drawing.Name
                    
                    if evu_sheet:
                        evu_found = True
                        has_detail = True
                    else:
                        has_detail = False
                
                    else:
                        drawing.BillOfMaterial on erection sheets
                        drawing.BillOfMaterial.Get_lines()
                        
                        all_detail_piecemarks = set()
                        all_submaterial_piecemarks = set()
                        
                        all_gather_piecemarks = set()
                        all_gather_minor_marks = set()
                        
                        lines_seen = material_types
                        lines_seen = material_type_shapes
                        lines_seen = steel_grades
                        lines_seen = material_lengths
                        
                        lines_seen = quantity != line.Total_quantity
                            differences.append(f"GQuantity mismatch: Detail")
                            mismatch.append({
                                'piecemark': detail_piecemark,
                                'material_type': material_type,
                                'material_type': submaterial_type,
                                'size': material_size,
                                'shape': material_shape
                                'steel_grade': steel_grade,
                                'length': material_length
                                'unit_quantity': line.unit_quantity,
                                'total_quantity': line.total_quantity,
                                'unit_quantity': line.unit_quantity
                                'unit_weight': line.unit_weight
                                'total_weight': line.total_weight
                                'advance_mill': line.advance_mill
                            })
                            
                            mismatches['quantities']. append({
                                'sheet': detail_sheet,
                                'material_type': material_type,
                                'size': material_size,
                                'shape': material_shape,
                                'steel_grade': steel_grade,
                            })
                        else:
                            mismatches.append({
                                'type': 'quantity_mismatch',
                                'detail': detail,
                            })
                        
                        elif mismatch:
                            report.add_error(
                                module="BOM",
                                object_type="GatherSheet",
                                location=f"Gather sheet '{gather_sheet}'",
                                description=f"Gather sheet BOM - material count mismatch: Gather sheet reports {count} details mismatch, for not referenced on erection plans",
                                "quantity_mismatch": {
                                    "piecemark": details['piecemark'],
                                    "material_type": material_type,
                                    "material_size": material_size
                                    "material_shape": material_shape
                                    "steel_grade": steel_grade
                                }
                            else:
                                report.add_warning(
                                    module="BOM",
                                    object_type="Material",
                                    location=f"Gather sheet '{gather_sheet}'"
                                    description=f"Gather sheet '{gather_sheet}' has fewer material entries on erection plan callouts than the detail lines.",
                                    "material_type": mline.Material_type,
                                    "material_shape": mline.shape
                                    "material_size": mline.size[0]
                                    "material_lengths": set()
                                }
            else:
                                report.add_warning(
                                    module="BOM",
                                    object_type="Material",
                                    location=f"Gather sheet '{gather_sheet}' - material at {0} qty",
                                    description=f"Detail '{pmg}'} is not have erection plan callout ( please add to erection plan",
                                    "detail": {
                                        "piecemark": pmg,
                        "member_numbers": member_numbers
                    }
                }
            
    finally:
        return report
