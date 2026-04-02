import os
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class ReleasePackage:
    project_name: str
    release_path: str
    category: str
    release_type: str
    date: Optional[str]
    has_kiss: bool
    kiss_path: Optional[str]
    has_detail_sheets: bool
    has_erection_sheets: bool
    has_gather_sheets: bool
    has_material_summary: bool
    detail_sheet_paths: List[str] = field(default_factory=list)
    erection_sheet_paths: List[str] = field(default_factory=list)
    gather_sheet_paths: List[str] = field(default_factory=list)
    material_summary_paths: List[str] = field(default_factory=list)


@dataclass
class ProjectCatalog:
    project_name: str
    project_path: str
    design_path: Optional[str]
    release_path: Optional[str]
    releases: List[ReleasePackage] = field(default_factory=list)


def _parse_release_info(name: str) -> Tuple[str, Optional[str]]:
    release_type = ""
    upper = name.upper()
    for rt in ("OFA", "FSF", "REV"):
        if rt in upper:
            release_type = rt
            break
    date_match = re.search(r"_(\d{6})$", name)
    date = date_match.group(1) if date_match else None
    return release_type, date


def _collect_pdfs(directory: str) -> List[str]:
    pdfs: List[str] = []
    try:
        for entry in os.scandir(directory):
            if entry.is_file() and entry.name.lower().endswith(".pdf"):
                pdfs.append(entry.path)
    except (PermissionError, OSError):
        pass
    return pdfs


def _find_sheet_pdfs(release_dir: str, base_name: str) -> Tuple[bool, List[str]]:
    variants = [base_name.lower(), base_name.lower() + "s"]
    try:
        for entry in os.scandir(release_dir):
            if not entry.is_dir():
                continue
            if entry.name.lower() in variants:
                pdf_sub = os.path.join(entry.path, "PDF")
                if os.path.isdir(pdf_sub):
                    return True, _collect_pdfs(pdf_sub)
                return True, _collect_pdfs(entry.path)
    except (PermissionError, OSError):
        pass
    return False, []


def _find_kiss(release_dir: str) -> Tuple[bool, Optional[str]]:
    search_dirs: List[str] = []
    reports_dir = os.path.join(release_dir, "Reports")
    if os.path.isdir(reports_dir):
        try:
            for entry in os.scandir(reports_dir):
                if entry.is_dir():
                    search_dirs.append(entry.path)
        except (PermissionError, OSError):
            pass
        search_dirs.append(reports_dir)
    search_dirs.append(release_dir)

    for d in search_dirs:
        try:
            for entry in os.scandir(d):
                if entry.is_file() and entry.name.lower().endswith(".kss"):
                    return True, entry.path
        except (PermissionError, OSError):
            pass
    return False, None


def _find_material_summary(release_dir: str) -> Tuple[bool, List[str]]:
    paths: List[str] = []
    search_dirs = [release_dir]
    reports_dir = os.path.join(release_dir, "Reports")
    if os.path.isdir(reports_dir):
        search_dirs.append(reports_dir)
    for d in search_dirs:
        try:
            for entry in os.scandir(d):
                if not entry.is_file():
                    continue
                low = entry.name.lower()
                if low.startswith("material summary") and (
                    low.endswith(".pdf") or low.endswith(".xlsx")
                ):
                    paths.append(entry.path)
        except (PermissionError, OSError):
            pass
    return bool(paths), paths


def _scan_release(release_dir: str, project_name: str, category: str) -> ReleasePackage:
    folder_name = os.path.basename(release_dir)
    release_type, date = _parse_release_info(folder_name)
    has_kiss, kiss_path = _find_kiss(release_dir)
    has_detail, detail_pdfs = _find_sheet_pdfs(release_dir, "Detail Sheet")
    has_erection, erection_pdfs = _find_sheet_pdfs(release_dir, "Erection Sheet")
    has_gather, gather_pdfs = _find_sheet_pdfs(release_dir, "Gather Sheet")
    has_mat, mat_paths = _find_material_summary(release_dir)
    return ReleasePackage(
        project_name=project_name,
        release_path=release_dir,
        category=category,
        release_type=release_type,
        date=date,
        has_kiss=has_kiss,
        kiss_path=kiss_path,
        has_detail_sheets=has_detail,
        has_erection_sheets=has_erection,
        has_gather_sheets=has_gather,
        has_material_summary=has_mat,
        detail_sheet_paths=detail_pdfs,
        erection_sheet_paths=erection_pdfs,
        gather_sheet_paths=gather_pdfs,
        material_summary_paths=mat_paths,
    )


def scan_project(project_path: str) -> ProjectCatalog:
    project_name = os.path.basename(project_path.rstrip("\\/"))
    design_path: Optional[str] = None
    release_root: Optional[str] = None
    releases: List[ReleasePackage] = []

    try:
        for entry in os.scandir(project_path):
            if not entry.is_dir():
                continue
            name_lower = entry.name.lower()
            if "design" in name_lower and design_path is None:
                design_path = entry.path
            elif "release" in name_lower and release_root is None:
                release_root = entry.path
    except (PermissionError, OSError):
        pass

    if release_root:
        try:
            for entry in os.scandir(release_root):
                if not entry.is_dir():
                    continue
                category = entry.name
                try:
                    for sub in os.scandir(entry.path):
                        if sub.is_dir():
                            releases.append(
                                _scan_release(sub.path, project_name, category)
                            )
                except (PermissionError, OSError):
                    pass
        except (PermissionError, OSError):
            pass

    return ProjectCatalog(
        project_name=project_name,
        project_path=project_path,
        design_path=design_path,
        release_path=release_root,
        releases=releases,
    )


def scan_all_projects(root_dir: str) -> List[ProjectCatalog]:
    catalogs: List[ProjectCatalog] = []
    try:
        for entry in os.scandir(root_dir):
            if entry.is_dir():
                catalogs.append(scan_project(entry.path))
    except (PermissionError, OSError):
        pass
    return catalogs


def get_statistics(catalogs: List[ProjectCatalog]) -> Dict[str, int]:
    total_releases = 0
    total_kiss = 0
    total_detail = 0
    total_erection = 0
    total_gather = 0
    total_mat = 0

    for cat in catalogs:
        for rel in cat.releases:
            total_releases += 1
            if rel.has_kiss:
                total_kiss += 1
            total_detail += len(rel.detail_sheet_paths)
            total_erection += len(rel.erection_sheet_paths)
            total_gather += len(rel.gather_sheet_paths)
            total_mat += len(rel.material_summary_paths)

    return {
        "total_projects": len(catalogs),
        "total_releases": total_releases,
        "total_kiss_files": total_kiss,
        "total_detail_pdfs": total_detail,
        "total_erection_pdfs": total_erection,
        "total_gather_pdfs": total_gather,
        "total_material_summaries": total_mat,
    }


def find_stair_rail_projects(catalogs: List[ProjectCatalog]) -> List[ProjectCatalog]:
    keywords = ("stair", "rail", "ladder", "handrail")
    results: List[ProjectCatalog] = []

    for cat in catalogs:
        name_lower = cat.project_name.lower()
        if any(kw in name_lower for kw in keywords):
            results.append(cat)
            continue
        found = False
        for rel in cat.releases:
            rel_text = (rel.category + " " + os.path.basename(rel.release_path)).lower()
            if any(kw in rel_text for kw in keywords):
                results.append(cat)
                found = True
                break
        if found:
            continue

    return results
