"""
KISS File Parser for SDS/2 Steel Detailing Data
Parses KISS v1.1 format files (.kss) exported from SDS/2
Author: John May
"""

import os
import re
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from collections import defaultdict


@dataclass
class KISSHeader:
    job_id: str = ""
    fabricator: str = ""
    date: str = ""
    time: str = ""
    status: str = ""


@dataclass
class KISSAssembly:
    major_mark: str
    revision: str = ""
    assembly_mark: str = ""
    main_mark: str = ""
    main_qty: int = 1
    main_type: str = ""
    main_size: str = ""
    main_grade: str = ""
    main_length_mm: float = 0.0
    main_location: str = ""
    main_remarks: str = ""
    member_description: str = ""
    detail_date: str = ""
    sds2_version: str = ""
    minor_marks: List["KISSMinorMark"] = field(default_factory=list)


@dataclass
class KISSMinorMark:
    major_mark: str
    revision: str
    assembly_mark: str
    minor_mark: str
    quantity: int
    material_type: str
    material_size: str
    grade: str
    length_mm: float
    location: str = ""
    remarks: str = ""

    @property
    def is_field_bolt(self) -> bool:
        return "field" in self.remarks.lower() if self.remarks else False

    @property
    def is_shop_bolt(self) -> bool:
        return "shop" in self.remarks.lower() if self.remarks else False

    @property
    def is_bolt(self) -> bool:
        return self.material_type in ("HS", "MB", "MX")

    @property
    def is_anchor(self) -> bool:
        return "embed" in self.remarks.lower() if self.remarks else False


@dataclass
class KISSFile:
    path: str
    project_name: str = ""
    release_name: str = ""
    header: KISSHeader = field(default_factory=KISSHeader)
    assemblies: Dict[str, KISSAssembly] = field(default_factory=dict)
    all_minor_marks: List[KISSMinorMark] = field(default_factory=list)
    parse_errors: List[str] = field(default_factory=list)

    @property
    def total_assemblies(self) -> int:
        return len(self.assemblies)

    @property
    def total_minor_marks(self) -> int:
        return len(self.all_minor_marks)

    @property
    def unique_minor_marks(self) -> List[str]:
        return list(set(m.minor_mark for m in self.all_minor_marks if m.minor_mark))

    @property
    def total_weight_kg(self) -> float:
        return sum(a.main_length_mm for a in self.assemblies.values())

    def get_assembly_bom(self, assembly_mark: str) -> Dict[str, int]:
        bom = {}
        for mm in self.all_minor_marks:
            if mm.assembly_mark == assembly_mark and mm.minor_mark:
                bom[mm.minor_mark] = bom.get(mm.minor_mark, 0) + mm.quantity
        return bom

    def get_global_bom(self) -> Dict[str, int]:
        bom = {}
        for mm in self.all_minor_marks:
            if mm.minor_mark and not mm.is_bolt:
                bom[mm.minor_mark] = bom.get(mm.minor_mark, 0) + mm.quantity
        return bom

    def get_all_marks(self) -> Dict[str, int]:
        bom = {}
        for mm in self.all_minor_marks:
            if mm.minor_mark:
                bom[mm.minor_mark] = bom.get(mm.minor_mark, 0) + mm.quantity
        return bom

    def get_member_types(self) -> Dict[str, int]:
        types = {}
        for asm in self.assemblies.values():
            desc = asm.member_description or "UNKNOWN"
            types[desc] = types.get(desc, 0) + asm.main_qty
        return types


def parse_kiss_file(filepath: str) -> Optional[KISSFile]:
    if not os.path.exists(filepath):
        return None

    kiss = KISSFile(path=filepath)
    path_parts = filepath.replace("\\", "/").split("/")
    for i, part in enumerate(path_parts):
        if "_Release" in part or "Release" in part:
            kiss.project_name = part
            break
    for i, part in enumerate(path_parts):
        if "FSF" in part or "OFA" in part or "REV" in part:
            kiss.release_name = part
            break

    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
    except Exception as e:
        kiss.parse_errors.append(f"Cannot read file: {e}")
        return kiss

    current_assembly_mark = None
    current_major_mark = None
    current_revision = "0"

    for line_num, raw_line in enumerate(lines, 1):
        line = raw_line.strip()
        if not line:
            continue

        parts = line.split(",")
        record_type = parts[0].strip() if parts else ""

        if record_type == "KISS":
            continue

        elif record_type == "H":
            if len(parts) >= 6:
                kiss.header = KISSHeader(
                    job_id=parts[1].strip() if len(parts) > 1 else "",
                    fabricator=parts[2].strip() if len(parts) > 2 else "",
                    date=parts[4].strip() if len(parts) > 4 else "",
                    time=parts[5].strip() if len(parts) > 5 else "",
                    status=parts[6].strip() if len(parts) > 6 else "",
                )

        elif record_type == "*":
            current_assembly_mark = None
            current_major_mark = None

        elif record_type == "W":
            if len(parts) >= 4:
                major = parts[1].strip()
                rev = parts[2].strip() if len(parts) > 2 else "0"
                desc = parts[3].strip() if len(parts) > 3 else ""
                if major in kiss.assemblies:
                    kiss.assemblies[major].member_description = desc
                    kiss.assemblies[major].detail_date = (
                        parts[4].strip() if len(parts) > 4 else ""
                    )
                    kiss.assemblies[major].sds2_version = (
                        parts[5].strip() if len(parts) > 5 else ""
                    )

        elif record_type == "M":
            if len(parts) >= 4:
                asm_mark = parts[1].strip()
                qty = _safe_int(parts[2].strip())
                desc = parts[3].strip() if len(parts) > 3 else ""
                current_assembly_mark = asm_mark
                if asm_mark not in kiss.assemblies:
                    kiss.assemblies[asm_mark] = KISSAssembly(
                        major_mark=current_major_mark or asm_mark,
                        assembly_mark=asm_mark,
                        main_qty=qty,
                        member_description=desc,
                    )

        elif record_type == "D":
            if len(parts) < 9:
                continue

            major_mark = parts[1].strip()
            revision = parts[2].strip() if len(parts) > 2 else "0"
            asm_mark = parts[3].strip() if len(parts) > 3 else ""
            minor_mark = parts[4].strip() if len(parts) > 4 else ""
            qty = _safe_int(parts[5].strip()) if len(parts) > 5 else 1
            mat_type = parts[6].strip() if len(parts) > 6 else ""
            mat_size = parts[7].strip() if len(parts) > 7 else ""
            grade = parts[8].strip() if len(parts) > 8 else ""
            length_mm = _safe_float(parts[9].strip()) if len(parts) > 9 else 0.0
            location = parts[10].strip() if len(parts) > 10 else ""
            remarks1 = parts[11].strip() if len(parts) > 11 else ""
            remarks2 = parts[12].strip() if len(parts) > 12 else ""
            remarks = remarks1
            if remarks2:
                remarks = f"{remarks1} {remarks2}".strip()

            current_major_mark = major_mark
            current_revision = revision

            if not minor_mark and not asm_mark:
                continue

            if asm_mark and minor_mark and asm_mark != minor_mark:
                mm = KISSMinorMark(
                    major_mark=major_mark,
                    revision=revision,
                    assembly_mark=asm_mark,
                    minor_mark=minor_mark,
                    quantity=qty,
                    material_type=mat_type,
                    material_size=mat_size,
                    grade=grade,
                    length_mm=length_mm,
                    location=location,
                    remarks=remarks,
                )
                kiss.all_minor_marks.append(mm)

                if asm_mark in kiss.assemblies:
                    kiss.assemblies[asm_mark].minor_marks.append(mm)
                else:
                    asm = KISSAssembly(
                        major_mark=major_mark,
                        revision=revision,
                        assembly_mark=asm_mark,
                    )
                    asm.minor_marks.append(mm)
                    kiss.assemblies[asm_mark] = asm

            elif asm_mark and not minor_mark:
                if asm_mark in kiss.assemblies:
                    kiss.assemblies[asm_mark].main_qty = qty
                else:
                    kiss.assemblies[asm_mark] = KISSAssembly(
                        major_mark=major_mark,
                        revision=revision,
                        assembly_mark=asm_mark,
                        main_qty=qty,
                    )

    return kiss


def _safe_int(val: str) -> int:
    try:
        return int(float(val))
    except (ValueError, TypeError):
        return 0


def _safe_float(val: str) -> float:
    try:
        return float(val)
    except (ValueError, TypeError):
        return 0.0
