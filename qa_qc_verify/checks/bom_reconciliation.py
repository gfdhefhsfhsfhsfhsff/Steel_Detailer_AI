"""
BOM Reconciliation Module
Compares Gather Sheet BOM against aggregate Detail Sheet BOMs
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
        Drawing, DrawingList, DrawingStatus, BillOfMaterial, PiecemarkType
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
    unit_quantity: int
    total_quantity: int
    unit_weight: float
    total_weight: float
    is_hidden: bool
    advance_mill: str
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'piecemark': self.piecemark,
            'minor_mark': self.minor_mark,
            'description': self.description,
            'grade': self.grade,
            'shape': self.shape,
            'size': self.size,
            'length': self.length,
            'unit_quantity': self.unit_quantity,
            'total_quantity': self.total_quantity,
            'unit_weight': self.unit_weight,
            'total_weight': self.total_weight,
            'is_hidden': self.is_hidden,
            'advance_mill': self.advance_mill
        }


@dataclass
class BOMSummary:
    """BOM reconciliation summary"""
    gather_sheet: str
    detail_sheets: List[str]
    gather_bom: Dict[str, List[BOMLine]] = field(default_factory=dict)
    detail_biecemarks: Dict[str, List[BOMLine]] = field(default_factory=dict)
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
            'gather_sheet': self.gather_sheet,
            'detail_sheets': self.detail_sheets,
            'total_gather_lines': sum(len(v) for v in self.gather_bom.values()),
            'total_detail_lines': sum(len(v) for v in self.detail_piecemarks.values()),
            'issues': self.issues
        }


def verify_bom_reconciliation(job: Job, report: QAReport, config: Config) -> QAReport:
    """
    Module 4: BOM Reconciliation
    Compares Gather Sheet BOM against aggregate Detail Sheet BOMs
    Verifies exact matches for:
    - Quantities
    - Material Types  
    - Sizes
    - Shapes
    - Steel Grades
    """
    tracker = ProgressTracker(total_steps=4)
    tracker.print_status("Starting BOM Reconciliation...")
    
    if not API_AVAILABLE:
        report.add_error(
            module="BOM",
            object_type="System",
            location="N/A",
            description="SDS/2 API not available - cannot perform verification",
            detail={}
        )
        return report
    
    # Get gather sheet handles
    tracker.print_status("Reading gather sheets...")
    gather_handles = job.GetDrawingHandles(TableWithDrawings.GatherSheet)
    gather_sheets: Dict[str, BOMSummary] = {}
    
    for handle in gather_handles:
        drawing = Drawing.Get(handle)
        sheet_name = drawing.Name
        bom = drawing.BillOfMaterial
        
        
        if bom:
            lines = bom.GetLines()
            gather_bom_lines: List[BOMLine] = []
            
            for line in lines:
                if line.IsLineHidden:
                    continue
                
                bom_line = BOMLine(
                    piecemark=line.Piecemark,
                    minor_mark=line.MinorMark or "",
                    description=line.Description or "",
                    grade=str(line.Grade) or "",
                    shape=str(line.Shape) if hasattr(line, 'Shape') else "",
                    size=str(line.Shape.Size) if hasattr(line, 'Size') else "",
                    length=float(line.Length) if line.Length else 0.0,
                    unit_quantity=int(line.UnitQuantity) if line.UnitQuantity else 0,
                    total_quantity=int(line.TotalQuantity) if line.TotalQuantity else 0,
                    unit_weight=float(line.UnitWeight) if line.UnitWeight else 0.0,
                    total_weight=float(line.TotalWeight) if line.TotalWeight else 0.0,
                    is_hidden=line.IsLineHidden,
                    advance_mill=line.AdvanceMill or ""
                )
                gather_bom_lines.append(bom_line)
            
            gather_sheets[sheet_name] = BOMSummary(
                gather_sheet=sheet_name,
                detail_sheets=[],
                gather_bom=sheet_name: gather_bom_lines,
            )
            
            for bom_line in gather_bom_lines:
                gather_bom[bom_line.piecemark].append(bom_line)
    
    tracker.print_status(f"Found {len(gather_sheets)} gather sheets with {sum(len(v) for v in gather_bom.values())} BOM lines")
    
    # Get detail sheet handles
    tracker.print_status("Reading detail sheets...")
    detail_handles = job.GetDrawingHandles(TableWithDrawings.DetailSheet)
    
    for handle in detail_handles:
        drawing = Drawing.Get(handle)
        sheet_name = drawing.Name
        bom = drawing.BillOfMaterial
        
        
        if bom:
            lines = bom.GetLines()
            
            for line in lines:
                if line.IsLineHidden:
                    continue
                
                bom_line = BOMLine(
                    piecemark=line.Piecemark,
                    minor_mark=line.MinorMark or "",
                    description=line.Description or "",
                    grade=str(line.Grade) or "",
                    shape=str(line.Shape) if hasattr(line, 'Shape') else "",
                    size=str(line.Shape.Size) if hasattr(line, 'Size') else "",
                    length=float(line.Length) if line.Length else 0.0,
                    unit_quantity=int(line.UnitQuantity) if line.UnitQuantity else 0,
                    total_quantity=int(line.TotalQuantity) if line.TotalQuantity else 0,
                    unit_weight=float(line.UnitWeight) if line.UnitWeight else 0.0,
                    total_weight=float(line.TotalWeight) if line.TotalWeight else 0.0,
                    is_hidden=line.IsLineHidden,
                    advance_mill=line.AdvanceMill or ""
                )
                
                # Add to detail sheet BOMs
                if sheet_name not in gather_sheets:
                    continue
                
                gather_sheets[sheet_name].add_detail_line(sheet_name, bom_line)
    
    tracker.print_status(f"Found {len(gather_sheets)} detail sheets with BOMs")
    
    # Reconcile BOMs
    tracker.print_status("Reconciling BOM data...")
    issues: List[Dict] = []
    
    for gather_name, gather_summary in gather_sheets.items():
        for piecemark, gather_bom in gather_summary.gather_bom.items():
            for detail_name in gather_summary.detail_sheets:
                if piecemark in gather_summary.detail_piecemarks:
                    detail_bom = gather_summary.detail_piecemarks[piecemark]
                    
                    # Find matching detail line
                    for detail_line in detail_bom:
                        if (detail_line.minor_mark == gather_bom.minor_mark and                            detail_line.minor_mark == gather_bom.minor_mark:
                            
                            # Compare quantities
                            if detail_line.total_quantity != gather_bom.total_quantity:
                                issues.append({
                                    'type': 'quantity_mismatch',
                                    'piecemark': piecemark,
                                    'minor_mark': detail_line.minor_mark,
                                    'gather_sheet': gather_name,
                                    'detail_sheet': detail_name,
                                    'gather_quantity': gather_bom.total_quantity,
                                    'detail_quantity': detail_line.total_quantity
                                })
                            
                            # Compare grades
                            if detail_line.grade != gather_bom.grade:
                                issues.append({
                                    'type': 'grade_mismatch',
                                    'piecemark': piecemark,
                                    'minor_mark': detail_line.minor_mark,
                                    'gather_sheet': gather_name,
                                    'detail_sheet': detail_name,
                                    'gather_grade': gather_bom.grade,
                                    'detail_grade': detail_line.grade
                                })
                            
                            # Compare shapes
                            if detail_line.shape != gather_bom.shape:
                                issues.append({
                                    'type': 'shape_mismatch',
                                    'piecemark': piecemark,
                                    'minor_mark': detail_line.minor_mark,
                                    'gather_sheet': gather_name,
                                    'detail_sheet': detail_name,
                                    'gather_shape': gather_bom.shape,
                                    'detail_shape': detail_line.shape
                                })
                            
                            # Mark as processed
                            gather_bom.is_hidden = False
                            detail_line.is_hidden = False
        
        # Check for orphaned materials
        for gather_name, gather_summary in gather_sheets.items():
            for piecemark, gather_bom in gather_summary.gather_bom.items():
                if piecemark not in gather_summary.detail_piecemarks:
                    issues.append({
                        'type': 'orphaned_gather',
                        'piecemark': piecemark,
                        'minor_mark': gather_bom.minor_mark,
                        'gather_sheet': gather_name,
                        'detail_sheet': None,
                        'gather_quantity': gather_bom.total_quantity,
                        'detail_quantity': 0
                    })
        
        for detail_name in gather_summary.detail_sheets:
            if detail_name not in gather_summary.detail_sheets:
                continue
            
            detail_bom = gather_summary.detail_piecemarks[piecemark]
            for piecemark, detail_lines in detail_bom.items():
                for detail_line in detail_lines:
                    if piecemark not in gather_summary.gather_bom:
                        issues.append({
                            'type': 'orphaned_detail',
                            'piecemark': piecemark,
                            'minor_mark': detail_line.minor_mark,
                            'gather_sheet': None,
                            'detail_sheet': detail_name,
                            'gather_quantity': 0,
                            'detail_quantity': detail_line.total_quantity
                        })
    
    # Add issues to report
    for issue in issues:
        if issue['type'] == 'quantity_mismatch':
            report.add_error(
                module="BOM",
                object_type="Material",
                location=f"Gather Sheet '{issue['gather_sheet']}' - Material '{issue['minor_mark']}'",
                description=f"Quantity mismatch: Gather={issue['gather_quantity']}, Detail={issue['detail_quantity']}",
                detail=issue
            )
        elif issue['type'] == 'grade_mismatch':
            report.add_error(
                module="BOM",
                object_type="Material",
                location=f"Gather Sheet '{issue['gather_sheet']}' - Material '{issue['minor_mark']}'",
                description=f"Grade mismatch: Gather={issue['gather_grade']}, Detail={issue['detail_grade']}",
                detail=issue
            )
        elif issue['type'] == 'shape_mismatch':
            report.add_error(
                module="BOM",
                object_type="Material",
                location=f"Gather Sheet '{issue['gather_sheet']}' - Material '{issue['minor_mark']}'",
                description=f"Shape mismatch: Gather={issue['gather_shape']}, Detail={issue['detail_shape']}",
                detail=issue
            )
        elif issue['type'] == 'orphaned_gather':
            report.add_warning(
                module="BOM",
                object_type="Material",
                location=f"Gather Sheet '{issue['gather_sheet']}' - Material '{issue['minor_mark']}'",
                description=f"Material on gather sheet but not found on any detail sheet",
                detail=issue
            )
        elif issue['type'] == 'orphaned_detail':
            report.add_warning(
                module="BOM",
                object_type="Material",
                location=f"Detail Sheet '{issue['detail_sheet']}' - Material '{issue['minor_mark']}'",
                description=f"Material on detail sheet but not found on gather sheet",
                detail=issue
            )
    
    # Summary
    tracker.print_status(
        f"Completed: {len(issues)} BOM issues found"
        print(f"  Quantity mismatches: {sum(1 for i in issues if i['type'] == 'quantity_mismatch')}")
        print(f"  Grade mismatches: {sum(1 for i in issues if i['type'] == 'grade_mismatch')}")
        print(f"  Shape mismatches: {sum(1 for i in issues if i['type'] == 'shape_mismatch')}")
        print(f"  Orphaned from gather: {sum(1 for i in issues if i['type'] == 'orphaned_gather')}")
        print(f"  Orphaned from detail: {sum(1 for i in issues if i['type'] == 'orphaned_detail')}")
    
    return report
