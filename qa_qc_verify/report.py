"""
Report generation for QA/QC verification results
Version: 1.0.0-alpha
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime
from enum import Enum
import json
import os


class Severity(Enum):
    ERROR = "Error"
    WARNING = "Warning"
    INFO = "Info"


@dataclass
class Issue:
    """Represents a single verification issue"""

    severity: Severity
    module: str
    object_type: str
    location: str
    description: str
    detail: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "severity": self.severity.value,
            "module": self.module,
            "object_type": self.object_type,
            "location": self.location,
            "description": self.description,
            "detail": self.detail,
        }


class QAReport:
    """Aggregates all verification issues into a structured report"""

    def __init__(self, job_name: str = "Unknown Job", run_timestamp: datetime = None):
        self.job_name = job_name
        self.run_timestamp = run_timestamp or datetime.now()
        self._issues: List[Issue] = []

    @property
    def issues(self) -> List[Issue]:
        return self._issues.copy()

    @property
    def total_issues(self) -> int:
        return len(self._issues)

    @property
    def error_count(self) -> int:
        return sum(1 for i in self._issues if i.severity == Severity.ERROR)

    @property
    def warning_count(self) -> int:
        return sum(1 for i in self._issues if i.severity == Severity.WARNING)

    @property
    def info_count(self) -> int:
        return sum(1 for i in self._issues if i.severity == Severity.INFO)

    @property
    def summary(self) -> Dict[str, Any]:
        """Get summary statistics by module"""
        modules = {}
        for issue in self._issues:
            if issue.module not in modules:
                modules[issue.module] = {"errors": 0, "warnings": 0, "info": 0}
            if issue.severity == Severity.ERROR:
                modules[issue.module]["errors"] += 1
            elif issue.severity == Severity.WARNING:
                modules[issue.module]["warnings"] += 1
            else:
                modules[issue.module]["info"] += 1

        return {
            "total_issues": self.total_issues,
            "errors": self.error_count,
            "warnings": self.warning_count,
            "info": self.info_count,
            "by_module": modules,
        }

    def add_issue(self, issue: Issue) -> None:
        """Add an issue to the report"""
        self._issues.append(issue)

    def add_error(
        self,
        module: str,
        object_type: str,
        location: str,
        description: str,
        detail: Dict = None,
    ) -> None:
        """Convenience method to add an error"""
        self.add_issue(
            Issue(
                severity=Severity.ERROR,
                module=module,
                object_type=object_type,
                location=location,
                description=description,
                detail=detail or {},
            )
        )

    def add_warning(
        self,
        module: str,
        object_type: str,
        location: str,
        description: str,
        detail: Dict = None,
    ) -> None:
        """Convenience method to add a warning"""
        self.add_issue(
            Issue(
                severity=Severity.WARNING,
                module=module,
                object_type=object_type,
                location=location,
                description=description,
                detail=detail or {},
            )
        )

    def add_info(
        self,
        module: str,
        object_type: str,
        location: str,
        description: str,
        detail: Dict = None,
    ) -> None:
        """Convenience method to add info"""
        self.add_issue(
            Issue(
                severity=Severity.INFO,
                module=module,
                object_type=object_type,
                location=location,
                description=description,
                detail=detail or {},
            )
        )

    def get_issues_by_module(self, module: str) -> List[Issue]:
        """Get all issues for a specific module"""
        return [i for i in self._issues if i.module == module]

    def get_issues_by_severity(self, severity: Severity) -> List[Issue]:
        """Get all issues of a specific severity"""
        return [i for i in self._issues if i.severity == severity]

    def to_dict(self) -> Dict[str, Any]:
        """Convert report to dictionary"""
        return {
            "job_name": self.job_name,
            "run_timestamp": self.run_timestamp.isoformat(),
            "summary": self.summary,
            "issues": [i.to_dict() for i in self._issues],
        }

    def to_json(self, path: str) -> None:
        """Export report to JSON file"""
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2)

    def to_csv(self, path: str) -> None:
        """Export report to CSV file"""
        import csv

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    "Severity",
                    "Module",
                    "Object Type",
                    "Location",
                    "Description",
                    "Details",
                ]
            )
            for issue in self._issues:
                writer.writerow(
                    [
                        issue.severity.value,
                        issue.module,
                        issue.object_type,
                        issue.location,
                        issue.description,
                        json.dumps(issue.detail) if issue.detail else "",
                    ]
                )

    def to_html(self, path: str) -> None:
        """Export report to HTML file"""
        html = self._generate_html()
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)

    def _generate_html(self) -> str:
        """Generate HTML report content"""
        summary = self.summary
        timestamp = self.run_timestamp.strftime("%Y-%m-%d %H:%M:%S")

        # Build module summary rows
        module_rows = ""
        for module, counts in summary["by_module"].items():
            module_rows += f"""
                <tr>
                    <td>{module}</td>
                    <td class="error-count">{counts["errors"]}</td>
                    <td class="warning-count">{counts["warnings"]}</td>
                </tr>"""

        # Build issue rows
        issue_rows = ""
        for issue in self._issues:
            severity_class = issue.severity.value.lower()
            detail_json = json.dumps(issue.detail, indent=2) if issue.detail else "{}"
            issue_rows += f"""
                <tr class="issue-row {severity_class}">
                    <td><span class="badge {severity_class}">{issue.severity.value}</span></td>
                    <td>{issue.module}</td>
                    <td>{issue.object_type}</td>
                    <td class="location">{issue.location}</td>
                    <td>{issue.description}</td>
                    <td><pre class="detail-json">{detail_json}</pre></td>
                </tr>"""

        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QA/QC Report - {self.job_name}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            color: #333;
            padding: 20px;
        }}
        .container {{ max-width: 1400px; margin: 0 auto; }}
        .header {{
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .header h1 {{ color: #2c3e50; margin-bottom: 10px; }}
        .header .meta {{ color: #666; font-size: 0.9em; }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin-bottom: 20px;
        }}
        .summary-card {{
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .summary-card h2 {{ font-size: 2.5em; margin-bottom: 5px; }}
        .summary-card p {{ color: #666; }}
        .summary-card.total h2 {{ color: #2c3e50; }}
        .summary-card.errors h2 {{ color: #dc3545; }}
        .summary-card.warnings h2 {{ color: #ffc107; }}
        .summary-card.info h2 {{ color: #17a2b8; }}
        .section {{
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .section h2 {{
            color: #2c3e50;
            border-bottom: 2px solid #e0e0e0;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
        th {{ background: #f8f9fa; font-weight: 600; }}
        tr:hover {{ background: #f8f9fa; }}
        .badge {{
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.85em;
            font-weight: 600;
        }}
        .badge.error {{ background: #dc3545; color: #fff; }}
        .badge.warning {{ background: #ffc107; color: #333; }}
        .badge.info {{ background: #17a2b8; color: #fff; }}
        .location {{
            font-family: 'Consolas', monospace;
            background: #f0f0f0;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 0.9em;
        }}
        .detail-json {{
            font-family: 'Consolas', monospace;
            font-size: 0.8em;
            background: #f8f9fa;
            padding: 8px;
            border-radius: 4px;
            max-width: 300px;
            overflow-x: auto;
            white-space: pre-wrap;
        }}
        .issue-row.error {{ background: #fff5f5; }}
        .issue-row.warning {{ background: #fffdf0; }}
        .no-issues {{ text-align: center; padding: 40px; color: #28a745; }}
        .footer {{ text-align: center; color: #666; margin-top: 20px; font-size: 0.9em; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>QA/QC Verification Report</h1>
            <div class="meta">
                <strong>Job:</strong> {self.job_name} | <strong>Run:</strong> {timestamp}
            </div>
        </div>
        
        <div class="summary">
            <div class="summary-card total">
                <h2>{summary["total_issues"]}</h2>
                <p>Total Issues</p>
            </div>
            <div class="summary-card errors">
                <h2>{summary["errors"]}</h2>
                <p>Errors</p>
            </div>
            <div class="summary-card warnings">
                <h2>{summary["warnings"]}</h2>
                <p>Warnings</p>
            </div>
            <div class="summary-card info">
                <h2>{summary["info"]}</h2>
                <p>Info</p>
            </div>
        </div>
        
        <div class="section">
            <h2>Issues by Module</h2>
            <table>
                <thead>
                    <tr>
                        <th>Module</th>
                        <th>Errors</th>
                        <th>Warnings</th>
                    </tr>
                </thead>
                <tbody>
                    {module_rows}
                </tbody>
            </table>
        </div>
        
        <div class="section">
            <h2>All Issues</h2>
            {f"<table><thead><tr><th>Severity</th><th>Module</th><th>Object</th><th>Location</th><th>Description</th><th>Details</th></tr></thead><tbody>{issue_rows}</tbody></table>" if self._issues else '<p class="no-issues">No issues found!</p>'}
        </div>
        
        <div class="footer">
            Generated by QA/QC Verification Tool v1.0.0-alpha | {timestamp}
        </div>
    </div>
</body>
</html>"""
