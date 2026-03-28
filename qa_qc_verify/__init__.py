"""
SDS/2 QA/QC Verification Tool
Production-ready verification for steel detailing projects
"""

__version__ = "1.0.0"
__author__ = "AddonAxis / FabTrics"

from .run import run_verification
from .report import QAReport, Issue, Severity
from .config import Config

__all__ = ["run_verification", "QAReport", "Issue", "Severity", "Config"]
