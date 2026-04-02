import os
import re
from datetime import datetime, timezone
from typing import Optional

from mcp.server.fastmcp import FastMCP

MEMORY_DIR = "memory_docs"
CORE_FILES = [
    "projectbrief.md",
    "productContext.md",
    "activeContext.md",
    "systemPatterns.md",
    "techContext.md",
    "progress.md",
    "decisions.md",
    "codeMap_root.md",
]
INDEX_DIR = "indexes"
TASK_DIR = "tasks"
ARCHIVE_DIR = "archive"

_TEMPLATES = {
    "projectbrief.md": (
        "# Project Brief\ntimestamp: {ts}\n\n"
        "## Overview\n[Project scope and requirements]\n\n"
        "## Goals\n- [Goal 1]\n- [Goal 2]\n\n"
        "## Constraints\n- [Constraint 1]\n"
    ),
    "productContext.md": (
        "# Product Context\ntimestamp: {ts}\n\n"
        "## Problem Space\n[Describe the problem being solved]\n\n"
        "## Business Context\n[Business requirements and user needs]\n\n"
        "## Success Metrics\n- [Metric 1]\n"
    ),
    "activeContext.md": (
        "# Active Context\ntimestamp: {ts}\n\n"
        "## Current Focus\n[What is being worked on right now]\n\n"
        "## Priorities\n1. [Priority 1]\n\n"
        "## Active Components\n- [Component ID]: [Description]\n\n"
        "## Open Questions\n- [Question 1]\n"
    ),
    "systemPatterns.md": (
        "# System Patterns\ntimestamp: {ts}\n\n"
        "## Architecture\n[High-level architecture description]\n\n"
        "## Design Patterns\n- @pattern1: [Description]\n\n"
        "## Conventions\n- [Convention 1]\n"
    ),
    "techContext.md": (
        "# Technical Context\ntimestamp: {ts}\n\n"
        "## Technologies\n- [Tech 1]: [Version] - [Purpose]\n\n"
        "## Dependencies\n- [Dependency 1]\n\n"
        "## Development Environment\n[Setup instructions]\n"
    ),
    "progress.md": (
        "# Progress\ntimestamp: {ts}\n\n"
        "## Status\n- [Current milestone status]\n\n"
        "## Completed\n- [Completed item 1]\n\n"
        "## In Progress\n- [In-progress item 1]\n\n"
        "## Pending\n- [Pending item 1]\n\n"
        "## Blockers\n- [Blocker 1]\n"
    ),
    "decisions.md": (
        "# Decision Journal\ntimestamp: {ts}\n\n"
        "## Active Decisions\n"
        "(No decisions recorded yet)\n\n"
        "## Historical Decisions\n"
        "(No historical decisions yet)\n"
    ),
    "codeMap_root.md": (
        "# CodeMap Root\ntimestamp: {ts}\n\n"
        "## ACTIVE_MEMORY\n"
        "- Components: []\n"
        "- Decisions: []\n"
        "- Patterns: []\n"
        "- Tasks: []\n\n"
        "## CACHED_MEMORY\n"
        "- Components: []\n"
        "- Decisions: []\n"
        "- Tasks: []\n\n"
        "## ARCHIVED_MEMORY\n"
        "- [Archived items]\n\n"
        "## PROJECT_STRUCTURE\n"
        "[root_directory]/\n"
        "  [Describe project structure here]\n\n"
        "## FLOW_DIAGRAMS\n"
        "(No flow diagrams defined yet)\n"
    ),
    "tasks/task_registry.md": (
        "# Task Registry\ntimestamp: {ts}\n\n"
        "## Active Tasks\n"
        "(No active tasks)\n\n"
        "## Completed Tasks\n"
        "(No completed tasks)\n"
    ),
}


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _mb_root(project_path: str) -> str:
    return os.path.join(os.path.abspath(project_path), MEMORY_DIR)


def _ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def _read(path: str) -> Optional[str]:
    if not os.path.isfile(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _write(path: str, content: str) -> None:
    d = os.path.dirname(path)
    if d:
        _ensure_dir(d)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def _parse_list_items(text: str, section_header: str) -> list[str]:
    in_section = False
    items: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("##"):
            if in_section:
                break
            if section_header.lower() in stripped.lower():
                in_section = True
            continue
        if in_section and stripped.startswith("- "):
            items.append(stripped[2:].strip())
    return items


def _parse_memory_section(text: str, section_name: str) -> dict:
    result: dict = {}
    in_section = False
    current_key = None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("##"):
            if in_section:
                break
            if section_name.upper() in stripped.upper():
                in_section = True
            continue
        if in_section:
            m = re.match(r"-\s*(\w+)\s*:\s*\[([^\]]*)\]", stripped)
            if m:
                key = m.group(1).lower()
                vals = [
                    v.strip().strip("'\"") for v in m.group(2).split(",") if v.strip()
                ]
                result[key] = vals
                current_key = key
            elif stripped.startswith("##"):
                break
    return result


def _replace_memory_section(
    content: str, section_name: str, new_lines: list[str]
) -> str:
    lines = content.splitlines(keepends=True)
    out: list[str] = []
    in_section = False
    section_replaced = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("##"):
            if in_section and not section_replaced:
                out.extend(ln + "\n" for ln in new_lines)
                section_replaced = True
            if section_name.upper() in stripped.upper():
                in_section = True
                out.append(line)
                continue
            elif in_section:
                in_section = False
            out.append(line)
            continue
        if in_section:
            continue
        out.append(line)

    if in_section and not section_replaced:
        out.extend(ln + "\n" for ln in new_lines)

    return "".join(out)


def _next_task_id(registry_content: str) -> str:
    nums = re.findall(r"TASK_(\d+)", registry_content)
    n = max(int(x) for x in nums) + 1 if nums else 1
    return f"TASK_{n:03d}"


mcp = FastMCP("memory-bank", json_response=True)


@mcp.tool()
def init_memory_bank(project_path: str, overwrite: bool = False) -> dict:
    """Initialize the memory_docs/ directory structure with template files. Set overwrite=True to reset existing files."""
    root = _mb_root(project_path)
    created: list[str] = []
    skipped: list[str] = []
    ts = _now_iso()

    _ensure_dir(root)
    _ensure_dir(os.path.join(root, INDEX_DIR))
    _ensure_dir(os.path.join(root, TASK_DIR))
    _ensure_dir(os.path.join(root, TASK_DIR, ARCHIVE_DIR))

    for filename, template in _TEMPLATES.items():
        fpath = os.path.join(root, filename)
        if os.path.isfile(fpath) and not overwrite:
            skipped.append(filename)
            continue
        _write(fpath, template.format(ts=ts))
        created.append(filename)

    return {
        "memory_bank_root": root,
        "created": created,
        "skipped": skipped,
        "directories": [
            os.path.join(root, INDEX_DIR),
            os.path.join(root, TASK_DIR),
            os.path.join(root, TASK_DIR, ARCHIVE_DIR),
        ],
    }


@mcp.tool()
def read_file(project_path: str, file_path: str) -> dict:
    """Read any file from the memory bank. file_path is relative to memory_docs/ (e.g. 'activeContext.md', 'tasks/task_registry.md')."""
    full = os.path.join(_mb_root(project_path), file_path)
    content = _read(full)
    if content is None:
        return {"error": f"File not found: {file_path}", "path": full}
    return {"file_path": file_path, "content": content}


@mcp.tool()
def write_file(project_path: str, file_path: str, content: str) -> dict:
    """Write or update any file in the memory bank. file_path is relative to memory_docs/."""
    full = os.path.join(_mb_root(project_path), file_path)
    _write(full, content)
    return {
        "file_path": file_path,
        "bytes_written": len(content.encode("utf-8")),
        "path": full,
    }


@mcp.tool()
def get_active_context(project_path: str) -> dict:
    """Read the current activeContext.md to understand what's in focus."""
    content = _read(os.path.join(_mb_root(project_path), "activeContext.md"))
    if content is None:
        return {"error": "activeContext.md not found. Run init_memory_bank first."}
    sections: dict[str, str] = {}
    current = None
    buf: list[str] = []
    for line in content.splitlines():
        if line.startswith("## "):
            if current:
                sections[current] = "\n".join(buf).strip()
            current = line[3:].strip()
            buf = []
        elif current:
            buf.append(line)
    if current:
        sections[current] = "\n".join(buf).strip()
    return {"raw": content, "sections": sections}


@mcp.tool()
def update_active_context(
    project_path: str,
    focus: Optional[str] = None,
    priorities: Optional[list[str]] = None,
    active_components: Optional[list[str]] = None,
    open_questions: Optional[list[str]] = None,
) -> dict:
    """Update specific sections of activeContext.md. Only provided fields are updated; others are preserved."""
    fpath = os.path.join(_mb_root(project_path), "activeContext.md")
    content = _read(fpath)
    if content is None:
        return {"error": "activeContext.md not found. Run init_memory_bank first."}

    if focus is not None:
        content = re.sub(
            r"(## Current Focus\n).*?(\n## )",
            lambda m: m.group(1) + focus + "\n" + m.group(2),
            content,
            count=1,
            flags=re.DOTALL,
        )

    def _replace_section(text: str, header: str, items: list[str]) -> str:
        numbered = "\n".join(f"{i + 1}. {item}" for i, item in enumerate(items))
        pattern = rf"(## {header}\n).*?(\n## )"
        return re.sub(
            pattern,
            lambda m: m.group(1) + numbered + "\n" + m.group(2),
            text,
            count=1,
            flags=re.DOTALL,
        )

    if priorities is not None:
        content = _replace_section(content, "Priorities", priorities)
    if active_components is not None:
        lines = "\n".join(f"- {c}" for c in active_components)
        pattern = r"(## Active Components\n).*?(\n## )"
        content = re.sub(
            pattern,
            lambda m: m.group(1) + lines + "\n" + m.group(2),
            content,
            count=1,
            flags=re.DOTALL,
        )
    if open_questions is not None:
        content = _replace_section(content, "Open Questions", open_questions)

    ts_line = f"timestamp: {_now_iso()}\n"
    content = re.sub(r"timestamp: [^\n]+\n", ts_line, content, count=1)

    _write(fpath, content)
    return {"updated": "activeContext.md", "timestamp": _now_iso()}


@mcp.tool()
def get_code_map(project_path: str) -> dict:
    """Read the codeMap_root.md navigation file with ACTIVE_MEMORY, CACHED_MEMORY, ARCHIVED_MEMORY, and PROJECT_STRUCTURE."""
    content = _read(os.path.join(_mb_root(project_path), "codeMap_root.md"))
    if content is None:
        return {"error": "codeMap_root.md not found. Run init_memory_bank first."}
    return {"raw": content}


@mcp.tool()
def get_memory_state(project_path: str) -> dict:
    """Parse the current memory paging state (ACTIVE_MEMORY, CACHED_MEMORY, ARCHIVED_MEMORY) from codeMap_root.md."""
    content = _read(os.path.join(_mb_root(project_path), "codeMap_root.md"))
    if content is None:
        return {"error": "codeMap_root.md not found. Run init_memory_bank first."}
    return {
        "ACTIVE_MEMORY": _parse_memory_section(content, "ACTIVE_MEMORY"),
        "CACHED_MEMORY": _parse_memory_section(content, "CACHED_MEMORY"),
        "ARCHIVED_MEMORY": _parse_memory_section(content, "ARCHIVED_MEMORY"),
    }


@mcp.tool()
def activate_components(
    project_path: str,
    components: list[str],
    decisions: Optional[list[str]] = None,
    patterns: Optional[list[str]] = None,
    tasks: Optional[list[str]] = None,
) -> dict:
    """Add component IDs, decision IDs, patterns, or task IDs to ACTIVE_MEMORY in codeMap_root.md."""
    fpath = os.path.join(_mb_root(project_path), "codeMap_root.md")
    content = _read(fpath)
    if content is None:
        return {"error": "codeMap_root.md not found. Run init_memory_bank first."}

    state = _parse_memory_section(content, "ACTIVE_MEMORY")

    def _merge(existing: list[str], additions: list[str]) -> list[str]:
        seen = set(existing)
        merged = list(existing)
        for a in additions:
            if a not in seen:
                merged.append(a)
                seen.add(a)
        return merged

    comps = _merge(state.get("components", []), components)
    decs = _merge(state.get("decisions", []), decisions or [])
    pats = _merge(state.get("patterns", []), patterns or [])
    tks = _merge(state.get("tasks", []), tasks or [])

    new_lines = [
        f"- Components: [{', '.join(comps)}]",
        f"- Decisions: [{', '.join(decs)}]",
        f"- Patterns: [{', '.join(pats)}]",
        f"- Tasks: [{', '.join(tks)}]",
    ]
    content = _replace_memory_section(content, "ACTIVE_MEMORY", new_lines)
    ts_line = f"timestamp: {_now_iso()}\n"
    content = re.sub(r"timestamp: [^\n]+\n", ts_line, content, count=1)
    _write(fpath, content)

    return {
        "ACTIVE_MEMORY": {
            "components": comps,
            "decisions": decs,
            "patterns": pats,
            "tasks": tks,
        }
    }


@mcp.tool()
def deactivate_components(project_path: str, components: list[str]) -> dict:
    """Move component IDs from ACTIVE_MEMORY to CACHED_MEMORY in codeMap_root.md."""
    fpath = os.path.join(_mb_root(project_path), "codeMap_root.md")
    content = _read(fpath)
    if content is None:
        return {"error": "codeMap_root.md not found. Run init_memory_bank first."}

    active = _parse_memory_section(content, "ACTIVE_MEMORY")
    cached = _parse_memory_section(content, "CACHED_MEMORY")

    active_comps = [c for c in active.get("components", []) if c not in components]
    cached_comps = cached.get("components", []) + components

    active_lines = [
        f"- Components: [{', '.join(active_comps)}]",
        f"- Decisions: [{', '.join(active.get('decisions', []))}]",
        f"- Patterns: [{', '.join(active.get('patterns', []))}]",
        f"- Tasks: [{', '.join(active.get('tasks', []))}]",
    ]
    cached_lines = [
        f"- Components: [{', '.join(cached_comps)}]",
        f"- Decisions: [{', '.join(cached.get('decisions', []))}]",
        f"- Tasks: [{', '.join(cached.get('tasks', []))}]",
    ]

    content = _replace_memory_section(content, "ACTIVE_MEMORY", active_lines)
    content = _replace_memory_section(content, "CACHED_MEMORY", cached_lines)
    ts_line = f"timestamp: {_now_iso()}\n"
    content = re.sub(r"timestamp: [^\n]+\n", ts_line, content, count=1)
    _write(fpath, content)

    return {
        "ACTIVE_MEMORY": {"components": active_comps},
        "CACHED_MEMORY": {"components": cached_comps},
    }


@mcp.tool()
def create_task(
    project_path: str,
    name: str,
    description: str,
    components: Optional[list[str]] = None,
    subtasks: Optional[list[str]] = None,
    confidence: str = "MEDIUM",
    task_id: Optional[str] = None,
) -> dict:
    """Create a new task file in tasks/ and register it in task_registry.md. Optionally provide subtask names and component IDs."""
    root = _mb_root(project_path)
    _ensure_dir(os.path.join(root, TASK_DIR))
    _ensure_dir(os.path.join(root, TASK_DIR, ARCHIVE_DIR))

    registry_path = os.path.join(root, TASK_DIR, "task_registry.md")
    registry = _read(registry_path) or _TEMPLATES["tasks/task_registry.md"].format(
        ts=_now_iso()
    )

    tid = task_id or _next_task_id(registry)
    ts = _now_iso()

    comp_ids = components or []
    subtask_lines: list[str] = []
    subtask_defs: list[str] = []
    for i, st_name in enumerate(subtasks or [], 1):
        sid = f"{tid}.{i}"
        subtask_lines.append(f'{sid}: "{st_name}" | Status: Not Started')
        subtask_defs.append(
            f'{i}. SUBTASK_{sid}: "{st_name}"\n'
            f"   - Goal: [TBD]\n"
            f"   - Required contexts: [TBD]\n"
            f"   - Output: [TBD]\n"
            f"   - Dependencies: None\n"
        )

    task_content = (
        f"# {tid}: {name}\n"
        f"timestamp: {ts}\n"
        f"status: Planning\n"
        f"components: [{', '.join(comp_ids)}]\n"
        f"implements_decisions: []\n"
        f"generated_decisions: []\n"
        f"confidence: {confidence}\n\n"
        f"## Task Definition\n{description}\n\n"
        f"## Subtasks\n"
        + ("\n".join(subtask_defs) if subtask_defs else "(No subtasks defined)\n")
        + f"\n## Generated Decisions\n(None yet)\n\n"
        f"## Integration Notes\n(TBD)\n"
    )

    safe_name = re.sub(r"[^a-zA-Z0-9_]+", "_", name).strip("_").lower()
    task_filename = f"{tid}_{safe_name}.md"
    task_path = os.path.join(root, TASK_DIR, task_filename)
    _write(task_path, task_content)

    subtask_summary = f" Subtasks: {len(subtask_lines)} total" if subtask_lines else ""
    task_entry = (
        f'- {tid}: "{name}" | Status: Planning | '
        f"Components: [{', '.join(comp_ids)}] | [Confidence: {confidence}]{subtask_summary} | "
        f"Started: {ts[:10]}\n"
    )

    active_marker = "## Active Tasks\n"
    if active_marker in registry:
        registry = registry.replace(active_marker, active_marker + task_entry, 1)
    else:
        registry += "\n" + task_entry

    ts_line = f"timestamp: {_now_iso()}\n"
    registry = re.sub(r"timestamp: [^\n]+\n", ts_line, registry, count=1)
    _write(registry_path, registry)

    return {
        "task_id": tid,
        "task_file": os.path.join(TASK_DIR, task_filename),
        "subtasks": subtask_lines,
        "status": "Planning",
    }


@mcp.tool()
def update_task(
    project_path: str,
    task_id: str,
    status: Optional[str] = None,
    subtask_id: Optional[str] = None,
    subtask_status: Optional[str] = None,
    confidence: Optional[str] = None,
    notes: Optional[str] = None,
) -> dict:
    """Update a task's status, a specific subtask's status, confidence level, or add integration notes."""
    root = _mb_root(project_path)
    registry_path = os.path.join(root, TASK_DIR, "task_registry.md")

    task_file = _find_task_file(root, task_id)
    if task_file is None:
        return {"error": f"Task file for {task_id} not found"}

    content = _read(task_file)
    if content is None:
        return {"error": f"Cannot read task file: {task_file}"}

    ts = _now_iso()

    if status is not None:
        content = re.sub(
            r"^status: .*$", f"status: {status}", content, count=1, flags=re.MULTILINE
        )

    if confidence is not None:
        content = re.sub(
            r"^confidence: .*$",
            f"confidence: {confidence}",
            content,
            count=1,
            flags=re.MULTILINE,
        )

    if subtask_id is not None and subtask_status is not None:
        subtask_line_pattern = (
            rf"(SUBTASK_{re.escape(subtask_id)}:.*?)(\s*-\s*Status:\s*)\S+"
        )
        m = re.search(subtask_line_pattern, content)
        if m:
            content = (
                content[: m.start(2)]
                + f"- Status: {subtask_status}"
                + content[m.end() :]
            )

    if notes is not None:
        content = re.sub(
            r"(## Integration Notes\n).*?(\n## |\Z)",
            lambda m: m.group(1) + notes + "\n" + m.group(2),
            content,
            count=1,
            flags=re.DOTALL,
        )

    _write(task_file, content)

    if status is not None:
        registry = _read(registry_path)
        if registry:
            registry = re.sub(
                rf"(- {re.escape(task_id)}:.*?\| Status: )\S+",
                rf"\g<1>{status}",
                registry,
            )
            ts_line = f"timestamp: {_now_iso()}\n"
            registry = re.sub(r"timestamp: [^\n]+\n", ts_line, registry, count=1)
            _write(registry_path, registry)

    return {
        "task_id": task_id,
        "updated_fields": {
            k: v
            for k, v in [
                ("status", status),
                ("confidence", confidence),
                (
                    "subtask_status",
                    {subtask_id: subtask_status} if subtask_id else None,
                ),
                ("notes_added", notes is not None),
            ]
            if v is not None
        },
    }


@mcp.tool()
def archive_task(project_path: str, task_id: str) -> dict:
    """Move a completed task file to tasks/archive/ and update the registry."""
    root = _mb_root(project_path)
    archive_dir = os.path.join(root, TASK_DIR, ARCHIVE_DIR)
    _ensure_dir(archive_dir)

    task_file = _find_task_file(root, task_id)
    if task_file is None:
        return {"error": f"Task file for {task_id} not found"}

    basename = os.path.basename(task_file)
    archive_path = os.path.join(archive_dir, basename)

    content = _read(task_file) or ""
    content = re.sub(
        r"^status: .*$", "status: Archived", content, count=1, flags=re.MULTILINE
    )
    _write(archive_path, content)
    os.remove(task_file)

    registry_path = os.path.join(root, TASK_DIR, "task_registry.md")
    registry = _read(registry_path)
    if registry:
        pattern = rf"- {re.escape(task_id)}:.*?\| Status: \S+"
        match = re.search(pattern, registry)
        if match:
            entry = match.group(0)
            entry = re.sub(r"\| Status: \S+", "| Status: Archived", entry)
            registry = registry.replace(match.group(0), "", 1)
            completed_marker = "## Completed Tasks\n"
            if completed_marker in registry:
                registry = registry.replace(
                    completed_marker,
                    completed_marker
                    + entry
                    + f" | Archive: {os.path.join(TASK_DIR, ARCHIVE_DIR, basename)}\n",
                    1,
                )
        ts_line = f"timestamp: {_now_iso()}\n"
        registry = re.sub(r"timestamp: [^\n]+\n", ts_line, registry, count=1)
        _write(registry_path, registry)

    return {
        "task_id": task_id,
        "archived_to": os.path.join(TASK_DIR, ARCHIVE_DIR, basename),
    }


@mcp.tool()
def list_tasks(project_path: str, include_archived: bool = False) -> dict:
    """List all tasks from the task registry. Optionally include archived tasks."""
    registry = _read(os.path.join(_mb_root(project_path), TASK_DIR, "task_registry.md"))
    if registry is None:
        return {"error": "task_registry.md not found. Run init_memory_bank first."}

    active: list[dict] = []
    completed: list[dict] = []

    for m in re.finditer(
        r"^- (TASK_\d+):\s*\"(.*?)\"\s*\|\s*Status:\s*(\w+)(.*?)$",
        registry,
        re.MULTILINE,
    ):
        entry = {
            "task_id": m.group(1),
            "name": m.group(2),
            "status": m.group(3),
            "details": m.group(4).strip(),
        }
        if "Archived" in m.group(3) or "Completed" in m.group(3):
            completed.append(entry)
        else:
            active.append(entry)

    result: dict = {"active_tasks": active, "active_count": len(active)}
    if include_archived:
        result["completed_tasks"] = completed
        result["completed_count"] = len(completed)
    return result


@mcp.tool()
def add_decision(
    project_path: str,
    decision_id: str,
    title: str,
    context: str,
    decision: str,
    components: Optional[list[str]] = None,
    options: Optional[list[str]] = None,
    confidence: str = "MEDIUM",
    source: Optional[str] = None,
    rationale: Optional[str] = None,
) -> dict:
    """Add a new decision to the decisions.md journal under Active Decisions."""
    fpath = os.path.join(_mb_root(project_path), "decisions.md")
    content = _read(fpath)
    if content is None:
        return {"error": "decisions.md not found. Run init_memory_bank first."}

    ts = _now_iso()
    date = ts[:10]
    comp_str = ", ".join(components or [])
    opts_str = "\n    - ".join(options) if options else "[Not specified]"

    entry = (
        f'\n- [{date}] #{decision_id} "{title}"\n'
        f"  - **Context**: {context}\n"
        f"  - **Options**:\n    - {opts_str}\n"
        f"  - **Decision**: {decision}\n"
    )
    if rationale:
        entry += f"  - **Rationale**: {rationale}\n"
    entry += f"  - **Components**: [{comp_str}]\n  - **Confidence**: {confidence}\n"
    if source:
        entry += f"  - **Source**: {source}\n"
    entry += f"  - **Status**: Active\n"

    active_marker = "## Active Decisions\n"
    if active_marker in content:
        content = content.replace(active_marker, active_marker + entry, 1)
    else:
        content += "\n## Active Decisions\n" + entry

    ts_line = f"timestamp: {_now_iso()}\n"
    content = re.sub(r"timestamp: [^\n]+\n", ts_line, content, count=1)
    _write(fpath, content)

    return {"decision_id": decision_id, "title": title, "confidence": confidence}


@mcp.tool()
def list_decisions(project_path: str, include_historical: bool = False) -> dict:
    """List active (and optionally historical) decisions from decisions.md."""
    content = _read(os.path.join(_mb_root(project_path), "decisions.md"))
    if content is None:
        return {"error": "decisions.md not found. Run init_memory_bank first."}

    def _parse_section(section_text: str) -> list[dict]:
        decisions: list[dict] = []
        for m in re.finditer(
            r"- \[(\d{4}-\d{2}-\d{2})\] #(\S+) \"(.*?)\"\n(.*?)(?=\n- \[|\Z)",
            section_text,
            re.DOTALL,
        ):
            body = m.group(4)
            dec = {
                "date": m.group(1),
                "decision_id": m.group(2),
                "title": m.group(3),
            }
            for field_name in (
                "Context",
                "Decision",
                "Rationale",
                "Confidence",
                "Status",
                "Source",
            ):
                fm = re.search(rf"\*\*{field_name}\*\*:\s*(.+?)(?:\n|$)", body)
                if fm:
                    dec[field_name.lower()] = fm.group(1).strip()
            comps_m = re.search(r"\*\*Components\*\*:\s*\[([^\]]*)\]", body)
            if comps_m:
                dec["components"] = [
                    c.strip() for c in comps_m.group(1).split(",") if c.strip()
                ]
            decisions.append(dec)
        return decisions

    parts = content.split("## Historical Decisions")
    active_text = (
        parts[0].split("## Active Decisions")[-1]
        if "## Active Decisions" in parts[0]
        else ""
    )
    active = _parse_section(active_text)

    result: dict = {"active_decisions": active, "active_count": len(active)}
    if include_historical and len(parts) > 1:
        historical = _parse_section(parts[1])
        result["historical_decisions"] = historical
        result["historical_count"] = len(historical)
    return result


@mcp.tool()
def retire_decision(
    project_path: str, decision_id: str, final_status: str = "Implemented"
) -> dict:
    """Move a decision from Active to Historical in decisions.md."""
    fpath = os.path.join(_mb_root(project_path), "decisions.md")
    content = _read(fpath)
    if content is None:
        return {"error": "decisions.md not found."}

    pattern = rf"(- \[\d{{4}}-\d{{2}}-\d{{2}}\] #{re.escape(decision_id)} .*?)(?=\n- \[|\n## )"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return {"error": f"Decision #{decision_id} not found in active decisions."}

    entry = match.group(1)
    entry = re.sub(r"\*\*Status\*\*:\s*\S+", f"**Status**: {final_status}", entry)

    content = content.replace(match.group(1), "", 1)

    hist_marker = "## Historical Decisions\n"
    if hist_marker in content:
        content = content.replace(hist_marker, hist_marker + entry + "\n", 1)
    else:
        content += "\n## Historical Decisions\n" + entry + "\n"

    ts_line = f"timestamp: {_now_iso()}\n"
    content = re.sub(r"timestamp: [^\n]+\n", ts_line, content, count=1)
    _write(fpath, content)

    return {
        "decision_id": decision_id,
        "moved_to": "Historical",
        "final_status": final_status,
    }


@mcp.tool()
def assess_confidence(
    project_path: str,
    item_type: str,
    item_id: str,
    level: str,
    rationale: str,
) -> dict:
    """Record a confidence assessment for a decision or task. item_type is 'decision' or 'task'. level is HIGH (>85%), MEDIUM (60-85%), or LOW (<60%)."""
    valid_levels = ("HIGH", "MEDIUM", "LOW")
    if level.upper() not in valid_levels:
        return {
            "error": f"Invalid confidence level '{level}'. Must be one of: {valid_levels}"
        }

    root = _mb_root(project_path)
    ts = _now_iso()

    if item_type.lower() == "decision":
        fpath = os.path.join(root, "decisions.md")
        content = _read(fpath)
        if content is None:
            return {"error": "decisions.md not found."}
        pattern = rf"(#{re.escape(item_id)}.*?\*\*Confidence\*\*:\s*)\S+"
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, rf"\g<1>{level.upper()}", content, count=1)
            _write(fpath, content)
            return {
                "item_type": "decision",
                "item_id": item_id,
                "confidence": level.upper(),
                "rationale": rationale,
            }
        return {"error": f"Decision #{item_id} not found."}

    elif item_type.lower() == "task":
        task_file = _find_task_file(root, item_id)
        if task_file is None:
            return {"error": f"Task {item_id} not found."}
        content = _read(task_file) or ""
        content = re.sub(
            r"^confidence: .*$",
            f"confidence: {level.upper()}",
            content,
            count=1,
            flags=re.MULTILINE,
        )
        _write(task_file, content)
        return {
            "item_type": "task",
            "item_id": item_id,
            "confidence": level.upper(),
            "rationale": rationale,
        }

    return {"error": f"Unknown item_type '{item_type}'. Use 'decision' or 'task'."}


@mcp.tool()
def update_progress(
    project_path: str,
    completed: Optional[list[str]] = None,
    in_progress: Optional[list[str]] = None,
    pending: Optional[list[str]] = None,
    blockers: Optional[list[str]] = None,
) -> dict:
    """Update the progress.md file with completed, in-progress, pending, and blocker items."""
    fpath = os.path.join(_mb_root(project_path), "progress.md")
    content = _read(fpath)
    if content is None:
        return {"error": "progress.md not found. Run init_memory_bank first."}

    ts = _now_iso()

    def _update_list_section(text: str, header: str, items: list[str]) -> str:
        lines = "\n".join(f"- {item}" for item in items)
        pattern = rf"(## {header}\n).*?(\n## |\Z)"
        replacement = rf"\g<1>{lines}\n\g<2>"
        new_text, count = re.subn(pattern, replacement, text, count=1, flags=re.DOTALL)
        if count == 0:
            new_text += f"\n## {header}\n{lines}\n"
        return new_text

    if completed is not None:
        content = _update_list_section(content, "Completed", completed)
    if in_progress is not None:
        content = _update_list_section(content, "In Progress", in_progress)
    if pending is not None:
        content = _update_list_section(content, "Pending", pending)
    if blockers is not None:
        content = _update_list_section(content, "Blockers", blockers)

    ts_line = f"timestamp: {_now_iso()}\n"
    content = re.sub(r"timestamp: [^\n]+\n", ts_line, content, count=1)
    _write(fpath, content)

    return {"updated": "progress.md", "timestamp": ts}


@mcp.tool()
def update_code_map(
    project_path: str,
    project_structure: Optional[str] = None,
    flow_diagrams: Optional[str] = None,
) -> dict:
    """Update the PROJECT_STRUCTURE or FLOW_DIAGRAMS sections of codeMap_root.md."""
    fpath = os.path.join(_mb_root(project_path), "codeMap_root.md")
    content = _read(fpath)
    if content is None:
        return {"error": "codeMap_root.md not found. Run init_memory_bank first."}

    if project_structure is not None:
        content = re.sub(
            r"(## PROJECT_STRUCTURE\n).*?(\n## )",
            lambda m: m.group(1) + project_structure + "\n" + m.group(2),
            content,
            count=1,
            flags=re.DOTALL,
        )

    if flow_diagrams is not None:
        marker = "## FLOW_DIAGRAMS\n"
        if marker in content:
            idx = content.index(marker)
            content = content[: idx + len(marker)] + flow_diagrams + "\n"
        else:
            content += "\n" + marker + flow_diagrams + "\n"

    ts_line = f"timestamp: {_now_iso()}\n"
    content = re.sub(r"timestamp: [^\n]+\n", ts_line, content, count=1)
    _write(fpath, content)

    return {"updated": "codeMap_root.md", "timestamp": _now_iso()}


def _find_task_file(root: str, task_id: str) -> Optional[str]:
    task_dir = os.path.join(root, TASK_DIR)
    if not os.path.isdir(task_dir):
        return None
    for entry in os.scandir(task_dir):
        if (
            entry.is_file()
            and entry.name.startswith(task_id)
            and entry.name.endswith(".md")
        ):
            return entry.path
    return None


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
