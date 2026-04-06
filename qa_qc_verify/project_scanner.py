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


def _looks_like_release(path: str) -> bool:
    indicators = {
        "Detail Sheet",
        "Detail Sheets",
        "Erection Sheet",
        "Erection Sheets",
        "Gather Sheet",
        "Gather Sheets",
        "Reports",
        "CNC",
        "KISS",
        "Material Summary",
    }
    try:
        for entry in os.scandir(path):
            if entry.is_dir() and entry.name in indicators:
                return True
            if entry.is_file():
                low = entry.name.lower()
                if low.endswith(".kss") or low.startswith("material summary"):
                    return True
    except (PermissionError, OSError):
        pass
    return False


def _scan_release_files(release_dir: str):
    kiss_path = None
    detail_pdfs: List[str] = []
    erection_pdfs: List[str] = []
    gather_pdfs: List[str] = []
    material_paths: List[str] = []

    detail_variants = {"detail sheet", "detail sheets"}
    erection_variants = {"erection sheet", "erection sheets"}
    gather_variants = {"gather sheet", "gather sheets"}

    for root, dirs, files in os.walk(release_dir):
        dirname_lower = os.path.basename(root).lower()
        parent_lower = os.path.basename(os.path.dirname(root)).lower()

        if kiss_path is None:
            for f in files:
                if f.lower().endswith(".kss"):
                    kiss_path = os.path.join(root, f)
                    break

        if dirname_lower in detail_variants or parent_lower in detail_variants:
            detail_pdfs.extend(
                os.path.join(root, f) for f in files if f.lower().endswith(".pdf")
            )
        elif dirname_lower in erection_variants or parent_lower in erection_variants:
            erection_pdfs.extend(
                os.path.join(root, f) for f in files if f.lower().endswith(".pdf")
            )
        elif dirname_lower in gather_variants or parent_lower in gather_variants:
            gather_pdfs.extend(
                os.path.join(root, f) for f in files if f.lower().endswith(".pdf")
            )

        for f in files:
            low = f.lower()
            if low.startswith("material summary") and (
                low.endswith(".pdf") or low.endswith(".xlsx")
            ):
                material_paths.append(os.path.join(root, f))

    return kiss_path, detail_pdfs, erection_pdfs, gather_pdfs, material_paths


def _scan_release(release_dir: str, project_name: str, category: str) -> ReleasePackage:
    folder_name = os.path.basename(release_dir)
    release_type, date = _parse_release_info(folder_name)
    kiss_path, detail_pdfs, erection_pdfs, gather_pdfs, mat_paths = _scan_release_files(
        release_dir
    )
    return ReleasePackage(
        project_name=project_name,
        release_path=release_dir,
        category=category,
        release_type=release_type,
        date=date,
        has_kiss=kiss_path is not None,
        kiss_path=kiss_path,
        has_detail_sheets=bool(detail_pdfs),
        has_erection_sheets=bool(erection_pdfs),
        has_gather_sheets=bool(gather_pdfs),
        has_material_summary=bool(mat_paths),
        detail_sheet_paths=detail_pdfs,
        erection_sheet_paths=erection_pdfs,
        gather_sheet_paths=gather_pdfs,
        material_summary_paths=mat_paths,
    )


def _find_release_root(project_path: str) -> Tuple[Optional[str], bool]:
    release_root = None
    is_archive = False
    try:
        for entry in os.scandir(project_path):
            if not entry.is_dir():
                continue
            name_lower = entry.name.lower()
            if "release" in name_lower and release_root is None:
                return entry.path, False
            if entry.name == os.path.basename(project_path):
                inner_path = _find_release_root(entry.path)
                if inner_path[0]:
                    return inner_path[0], True
    except (PermissionError, OSError):
        pass

    if _looks_like_project_with_releases(project_path):
        return project_path, True

    return None, False


def _looks_like_project_with_releases(path: str) -> bool:
    try:
        for entry in os.scandir(path):
            if not entry.is_dir():
                continue
            name = entry.name
            if name in (
                "Detail Sheets",
                "Detail Sheet",
                "Erection Sheets",
                "Erection Sheet",
                "Gather Sheets",
                "Gather Sheet",
                "Reports",
                "CNC",
                "SDS2_Model",
                "Design",
            ):
                return True
            if entry.is_dir():
                for sub in os.scandir(entry.path):
                    if not sub.is_dir():
                        continue
                    if sub.name in (
                        "Detail Sheets",
                        "Detail Sheet",
                        "Erection Sheets",
                        "Erection Sheet",
                        "Gather Sheets",
                        "Gather Sheet",
                        "Reports",
                        "CNC",
                        "PDF",
                    ):
                        return True
                    break
        return False
    except (PermissionError, OSError):
        return False


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
                        if not sub.is_dir():
                            continue
                        if _looks_like_release(sub.path):
                            releases.append(
                                _scan_release(sub.path, project_name, category)
                            )
                        else:
                            try:
                                for inner in os.scandir(sub.path):
                                    if inner.is_dir():
                                        releases.append(
                                            _scan_release(
                                                inner.path, project_name, category
                                            )
                                        )
                            except (PermissionError, OSError):
                                pass
                except (PermissionError, OSError):
                    pass
        except (PermissionError, OSError):
            pass

    if not releases and not release_root:
        found_root, is_arch = _find_release_root(project_path)
        if found_root:
            try:
                for entry in os.scandir(found_root):
                    if not entry.is_dir():
                        continue
                    if _looks_like_release(entry.path):
                        releases.append(_scan_release(entry.path, project_name, ""))
                    else:
                        try:
                            for sub in os.scandir(entry.path):
                                if sub.is_dir():
                                    if _looks_like_release(sub.path):
                                        releases.append(
                                            _scan_release(
                                                sub.path, project_name, entry.name
                                            )
                                        )
                                    else:
                                        try:
                                            for inner in os.scandir(sub.path):
                                                if (
                                                    inner.is_dir()
                                                    and _looks_like_release(inner.path)
                                                ):
                                                    releases.append(
                                                        _scan_release(
                                                            inner.path,
                                                            project_name,
                                                            entry.name,
                                                        )
                                                    )
                                        except (PermissionError, OSError):
                                            pass
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
