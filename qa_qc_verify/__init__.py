"""
SDS/2 QA/QC Verification Tool
Author: John May
Version: 1.0.0-alpha
"""

__version__ = "1.0.0-alpha"
__author__ = "John May"

from .run import run_verification
from .report import QAReport, Issue, Severity
from .config import Config

__all__ = ["run_verification", "QAReport", "Issue", "Severity", "Config"]
