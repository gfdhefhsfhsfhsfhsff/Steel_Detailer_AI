"""
PDF Text Extraction for Steel Detailing QA/QC
Extracts piecemark callouts, BOM data, and assembly info from erection, gather, and detail sheet PDFs.
Uses PyMuPDF (fitz) for text extraction and pdfplumber for table extraction.
"""

import logging
import os
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

try:
    import fitz

    FITZ_AVAILABLE = True
except ImportError:
    FITZ_AVAILABLE = False

try:
    import pdfplumber

    PDFPLUMBER_AVAILABLE = True
except ImportError:
    PDFPLUMBER_AVAILABLE = False


@dataclass
class GatherBOMItem:
    mark: str
    qty: int
    shape: str
    grade: str
    length: str = ""

    def to_dict(self) -> Dict:
        return {
            "mark": self.mark,
            "qty": self.qty,
            "shape": self.shape,
            "grade": self.grade,
            "length": self.length,
        }


@dataclass
class DetailSheetInfo:
    assembly_mark: str
    minor_marks: List[str] = field(default_factory=list)
    bom_items: List[Dict] = field(default_factory=list)
    section_refs: List[str] = field(default_factory=list)


_ASSEMBLY_PATTERN = re.compile(r"\b([A-Z]\d{2,5}[A-Z]{0,2}\d{0,2})\b")
_ERECTION_CALLOUT_PATTERN = re.compile(r"\b(M\d{2,5}[A-Z]?\d*)\b")
_BOLT_SPEC_PATTERN = re.compile(r"^A\d{3}[NX]$", re.IGNORECASE)
_MINOR_MARK_PATTERN = re.compile(r"\b([a-z]{1,3}\d{1,5})\b")
_GATHER_MATERIAL_LINE = re.compile(
    r"^(\d+)[^\S\n]+([A-Z][A-Z0-9x/\-.]+(?:[^\S\n]+[A-Z0-9x/\-.]+)*)[^\S\n]+([a-z]{1,3}\d{1,5})\s*$",
    re.MULTILINE,
)
_GRADE_LINE = re.compile(r"^GRADE:\s*(.+)$", re.MULTILINE)
_GATHER_HEADER_MARK = re.compile(r"\b([a-z]{1,3}\d{1,5})\b")
_DETAIL_SECTION_REF = re.compile(
    r"(?:DETAIL|Section|SEC)[\s\-]*(\d+)\s+([A-Z]\d+[A-Z]?\d*)"
)
_BOM_QTY_WORD_MAP = {
    "ONE": 1,
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9,
    "TEN": 10,
    "ELEVEN": 11,
    "TWELVE": 12,
}


def _safe_open_fitz(pdf_path: str) -> Optional[object]:
    if not FITZ_AVAILABLE:
        return None
    try:
        doc = fitz.open(pdf_path)
        return doc
    except Exception as e:
        logger.warning("fitz failed to open %s: %s", pdf_path, e)
        return None


def _safe_open_plumber(pdf_path: str) -> Optional[object]:
    if not PDFPLUMBER_AVAILABLE:
        return None
    try:
        pdf = pdfplumber.open(pdf_path)
        return pdf
    except Exception as e:
        logger.warning("pdfplumber failed to open %s: %s", pdf_path, e)
        return None


def _get_all_text_fitz(pdf_path: str) -> str:
    doc = _safe_open_fitz(pdf_path)
    if doc is None:
        return ""
    try:
        texts = []
        for page in doc:
            texts.append(page.get_text())
        return "\n".join(texts)
    except Exception as e:
        logger.warning("fitz text extraction failed for %s: %s", pdf_path, e)
        return ""
    finally:
        doc.close()


def _extract_pdf(pdf_path: str) -> Tuple[str, List[List[List[Optional[str]]]]]:
    text = _get_all_text_fitz(pdf_path)
    tables: List[List[List[Optional[str]]]] = []

    if PDFPLUMBER_AVAILABLE:
        pdf = _safe_open_plumber(pdf_path)
        if pdf is not None:
            try:
                for page in pdf.pages:
                    try:
                        page_tables = page.extract_tables()
                        if page_tables:
                            tables.extend(page_tables)
                    except Exception:
                        pass
            finally:
                pdf.close()

    return text, tables


def _parse_qty(val: Optional[str]) -> int:
    if val is None:
        return 0
    val = val.strip()
    if not val:
        return 0
    upper = val.upper()
    if upper in _BOM_QTY_WORD_MAP:
        return _BOM_QTY_WORD_MAP[upper]
    try:
        return int(float(val))
    except (ValueError, TypeError):
        return 0


def extract_erection_callouts(pdf_path: str) -> List[str]:
    if not os.path.isfile(pdf_path):
        logger.warning("PDF not found: %s", pdf_path)
        return []

    text, _ = _extract_pdf(pdf_path)
    if not text:
        return []

    found = set()

    for match in _ERECTION_CALLOUT_PATTERN.finditer(text):
        mark = match.group(1)
        if len(mark) >= 3:
            found.add(mark)

    for match in _ASSEMBLY_PATTERN.finditer(text):
        mark = match.group(1)
        if _BOLT_SPEC_PATTERN.match(mark):
            continue
        if re.match(r"^[A-Z]\d+[A-Z]+\d*$", mark) and len(mark) >= 4:
            found.add(mark)

    return sorted(found, key=lambda m: (len(m), m))


def extract_gather_bom(pdf_path: str) -> List[GatherBOMItem]:
    if not os.path.isfile(pdf_path):
        logger.warning("PDF not found: %s", pdf_path)
        return []

    basename = os.path.splitext(os.path.basename(pdf_path))[0]
    filename_mark = basename.lower()

    text, _ = _extract_pdf(pdf_path)
    if not text:
        return [GatherBOMItem(mark=filename_mark, qty=1, shape="", grade="")]

    items: List[GatherBOMItem] = []
    grade_match = _GRADE_LINE.search(text)
    grade = grade_match.group(1).strip() if grade_match else ""

    mat_match = _GATHER_MATERIAL_LINE.search(text)
    if mat_match:
        qty = int(mat_match.group(1))
        shape_desc = mat_match.group(2).strip()
        mark = mat_match.group(3)
        items.append(GatherBOMItem(mark=mark, qty=qty, shape=shape_desc, grade=grade))
    else:
        lines = text.split("\n")
        for line in lines:
            line = line.strip()
            if not line:
                continue
            minor_matches = _MINOR_MARK_PATTERN.findall(line)
            if filename_mark in [m.lower() for m in minor_matches]:
                qty = 1
                qty_word_match = re.match(
                    r"^\s*(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN)\b",
                    line,
                    re.IGNORECASE,
                )
                if qty_word_match:
                    qty = _BOM_QTY_WORD_MAP.get(qty_word_match.group(1).upper(), 1)
                else:
                    qty_match = re.match(r"^\s*(\d+)\s", line)
                    if qty_match:
                        qty = int(qty_match.group(1))
                shape = ""
                shape_match = re.search(
                    r"\b\d+\s+([A-Z][A-Z0-9x/\-.]+(?:\s[A-Z0-9x/\-.]+)*)",
                    line,
                )
                if not shape_match:
                    shape_match = re.search(
                        r"(?:ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN)\s+([A-Z][A-Z0-9x/\-.]+(?:\s[A-Z0-9x/\-.]+)*)",
                        line,
                        re.IGNORECASE,
                    )
                if shape_match:
                    shape = shape_match.group(1).strip()
                items.append(
                    GatherBOMItem(mark=filename_mark, qty=qty, shape=shape, grade=grade)
                )
                break

    if not items:
        items.append(GatherBOMItem(mark=filename_mark, qty=1, shape="", grade=grade))

    return items


def _merge_split_header(
    table: List[List[Optional[str]]], header_idx: int
) -> List[Optional[str]]:
    row1 = table[header_idx]
    ncols = len(row1)
    merged = list(row1)

    if header_idx + 1 < len(table):
        row2 = table[header_idx + 1]
        row1_str = " ".join(c or "" for c in row1).upper()
        row2_str = " ".join(c or "" for c in row2).upper()

        is_split = (
            ("QTY" in row2_str and "QTY" not in row1_str)
            or ("DESCRIPTION" in row2_str and "DESCRIPTION" not in row1_str)
            or ("MARK" in row1_str and "MARK" in row2_str)
        )

        if is_split:
            for i in range(min(ncols, len(row2))):
                val2 = (row2[i] or "").strip()
                if val2:
                    existing = (merged[i] or "").strip()
                    if existing:
                        merged[i] = f"{existing} {val2}"
                    else:
                        merged[i] = val2

    return merged


def extract_detail_sheet_info(pdf_path: str) -> DetailSheetInfo:
    if not os.path.isfile(pdf_path):
        logger.warning("PDF not found: %s", pdf_path)
        return DetailSheetInfo(assembly_mark="")

    basename = os.path.splitext(os.path.basename(pdf_path))[0]
    filename_mark = basename.strip("_").split("_")[0]

    text, tables = _extract_pdf(pdf_path)
    info = DetailSheetInfo(assembly_mark=filename_mark)

    if not text and not tables:
        return info

    if text:
        assembly_matches = _ASSEMBLY_PATTERN.findall(text)
        m_style = [m for m in assembly_matches if re.match(r"^M\d+", m)]
        if m_style:
            info.assembly_mark = m_style[0]

        for match in _DETAIL_SECTION_REF.finditer(text):
            info.section_refs.append(f"DETAIL {match.group(1)}-{match.group(2)}")

        for match in _ASSEMBLY_PATTERN.finditer(text):
            mark = match.group(1)
            if re.match(r"^M\d+[A-Z]?\d*$", mark):
                info.section_refs.append(mark)

    bom_table_found = False
    for table in tables:
        if not table or len(table) < 3:
            continue

        header_idx = None
        for idx, row in enumerate(table):
            row_str = " ".join(c or "" for c in row).upper()
            if "QTY" in row_str and ("MARK" in row_str or "MINOR" in row_str):
                header_idx = idx
                break
            if "BILL OF MATERIAL" in row_str and idx + 2 < len(table):
                candidate = " ".join(c or "" for c in table[idx + 1]).upper()
                candidate2 = " ".join(c or "" for c in table[idx + 2]).upper()
                if "QTY" in candidate or "QTY" in candidate2:
                    header_idx = idx + 1
                    break

        if header_idx is None:
            continue

        merged_header = _merge_split_header(table, header_idx)
        col_map = _identify_bom_columns(merged_header)
        if not col_map:
            continue

        data_start = header_idx + 1
        if header_idx + 1 < len(table):
            next_row_str = " ".join(c or "" for c in table[header_idx + 1]).upper()
            if any(h in next_row_str for h in ("QTY", "MARK", "DESCRIPTION")):
                if "QTY" not in " ".join(c or "" for c in table[header_idx]).upper():
                    data_start = header_idx + 2

        bom_table_found = True
        for row in table[data_start:]:
            row_str = " ".join(c or "" for c in row)
            if not row_str.strip():
                continue
            if "BILL OF MATERIAL" in row_str.upper():
                continue
            if "FIELD BOLTS" in row_str.upper():
                break

            minor_mark = _get_col(row, col_map.get("minor_mark"))
            if not minor_mark or not minor_mark.strip():
                continue
            minor_mark = minor_mark.strip()

            if not re.match(r"^[a-zA-Z]\w{1,10}$", minor_mark):
                continue

            qty = _parse_qty(_get_col(row, col_map.get("qty")))
            shape = _get_col(row, col_map.get("description")) or ""
            grade = _get_col(row, col_map.get("grade")) or ""
            length = _get_col(row, col_map.get("length")) or ""

            info.minor_marks.append(minor_mark)
            info.bom_items.append(
                {
                    "minor_mark": minor_mark,
                    "qty": qty,
                    "shape": shape.strip(),
                    "grade": grade.strip(),
                    "length": length.strip(),
                }
            )

    if not bom_table_found and text:
        _parse_bom_from_text(text, info)

    return info


def _identify_bom_columns(header_row: List[Optional[str]]) -> Optional[Dict[str, int]]:
    col_map = {}
    header_upper = [(c or "").upper().strip() for c in header_row]
    for i, h in enumerate(header_upper):
        if h in ("PIECE", "PIECE MARK", "MARK"):
            if "piece_mark" not in col_map:
                col_map["piece_mark"] = i
        elif h in ("QTY",):
            col_map["qty"] = i
        elif h in ("MINOR", "MINOR MARK"):
            col_map["minor_mark"] = i
        elif h in ("DESCRIPTION", "MATERIAL"):
            col_map["description"] = i
        elif h in ("LENGTH",):
            col_map["length"] = i
        elif h in ("WEIGHT",):
            col_map["weight"] = i
        elif h in ("REMARKS",):
            col_map["remarks"] = i
        elif h in ("GRADE", "STEEL"):
            col_map["grade"] = i

    if "minor_mark" in col_map:
        return col_map
    return None


def _get_col(row: List[Optional[str]], idx: Optional[int]) -> Optional[str]:
    if idx is None or idx >= len(row):
        return None
    return row[idx]


def _parse_bom_from_text(text: str, info: DetailSheetInfo) -> None:
    lines = text.split("\n")
    in_bom = False
    for line in lines:
        line = line.strip()
        if "BILL OF MATERIAL" in line.upper():
            in_bom = True
            continue
        if in_bom and "FIELD BOLTS" in line.upper():
            break
        if not in_bom:
            continue
        if not line:
            continue

        parts = line.split()
        if len(parts) < 3:
            continue

        minor_mark = None
        qty = 0
        shape = ""

        for i, part in enumerate(parts):
            if _MINOR_MARK_PATTERN.match(part):
                minor_mark = part
                if i > 0:
                    qty = _parse_qty(parts[i - 1])
                if i + 1 < len(parts):
                    shape = " ".join(parts[i + 1 : i + 3])
                break

        if minor_mark:
            info.minor_marks.append(minor_mark)
            info.bom_items.append(
                {
                    "minor_mark": minor_mark,
                    "qty": qty or 1,
                    "shape": shape,
                    "grade": "",
                    "length": "",
                }
            )


def extract_batch(
    erection_paths: Optional[List[str]] = None,
    gather_paths: Optional[List[str]] = None,
    detail_paths: Optional[List[str]] = None,
) -> Dict[str, Dict]:
    results: Dict[str, Dict] = {}

    if erection_paths:
        for path in erection_paths:
            try:
                callouts = extract_erection_callouts(path)
                results[path] = {"type": "erection", "callouts": callouts}
            except Exception as e:
                logger.error("Error extracting erection %s: %s", path, e)
                results[path] = {"type": "erection", "callouts": [], "error": str(e)}

    if gather_paths:
        for path in gather_paths:
            try:
                bom_items = extract_gather_bom(path)
                results[path] = {
                    "type": "gather",
                    "bom_items": [item.to_dict() for item in bom_items],
                }
            except Exception as e:
                logger.error("Error extracting gather %s: %s", path, e)
                results[path] = {"type": "gather", "bom_items": [], "error": str(e)}

    if detail_paths:
        for path in detail_paths:
            try:
                detail_info = extract_detail_sheet_info(path)
                results[path] = {
                    "type": "detail",
                    "assembly_mark": detail_info.assembly_mark,
                    "minor_marks": detail_info.minor_marks,
                    "bom_items": detail_info.bom_items,
                }
            except Exception as e:
                logger.error("Error extracting detail %s: %s", path, e)
                results[path] = {
                    "type": "detail",
                    "assembly_mark": "",
                    "minor_marks": [],
                    "bom_items": [],
                    "error": str(e),
                }

    return results


def is_pdf_text_extractable(pdf_path: str, min_chars: int = 50) -> bool:
    text = _get_all_text_fitz(pdf_path)
    return len(text.strip()) >= min_chars
