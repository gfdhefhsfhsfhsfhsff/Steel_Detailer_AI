"""
SDS/2 QA/QC Verification Tool
Author: John May
Version: 1.0.0-alpha
"""

__version__ = "1.0.0-alpha"
__author__ = "John May"

try:
    from .run import run_verification
except Exception:
    run_verification = None

try:
    from .report import QAReport, Issue, Severity
except Exception:
    QAReport = None
    Issue = None
    Severity = None

try:
    from .config import Config
except Exception:
    Config = None

__all__ = ["run_verification", "QAReport", "Issue", "Severity", "Config"]
