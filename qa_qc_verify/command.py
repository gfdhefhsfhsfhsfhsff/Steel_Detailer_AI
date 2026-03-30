#!/usr/bin/env python3
"""
Command-line entry point for QA/QC Verification Tool
Author: John May
Version: 1.0.0-alpha

Usage:
    python -m qa_qc_verify [config_path]
    python -m qa_qc_verify --no-browser
"""

import argparse
import json
import sys
import os

from .error_prompts import check_setup, print_error
from .config import Config, create_default_config
from .run import run_verification


def main():
    parser = argparse.ArgumentParser(
        description="QA/QC Verification Tool - SDS/2 Steel Detailing QA/QC"
    )
    parser.add_argument(
        "config",
        nargs="?",
        help="Path to configuration file",
        default="qa_config.json",
    )
    parser.add_argument(
        "--output", "-o", default="./qa_qc_report.html", help="Output path for report"
    )
    parser.add_argument(
        "--open-browser",
        action="store_true",
        help="Open HTML report in browser after completion",
    )
    parser.add_argument(
        "--no-db",
        action="store_true",
        help="Skip database connection and use default patterns",
    )
    parser.add_argument(
        "--create-config",
        action="store_true",
        help="Create a default config file and exit",
    )

    args = parser.parse_args()

    if not check_setup():
        sys.exit(1)

    config_path = args.config

    if args.create_config:
        default_config = create_default_config(config_path)
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=4)
        print(f"Created config: {config_path}")
        return

    if not os.path.exists(config_path):
        print_error("CFG_001", f"Looked for: {os.path.abspath(config_path)}")
        sys.exit(1)

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError as e:
        print_error("CFG_002", str(e))
        sys.exit(1)

    report = run_verification(config_path)
    return report


if __name__ == "__main__":
    main()
