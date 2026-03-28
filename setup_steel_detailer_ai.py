#!/usr/bin/env python3
"""
Steel Detailer AI - Project Generator

This script creates the complete project structure for the Steel Detailer AI application.
Run this script to generate all necessary files and folders.

Usage:
    python setup_steel_detailer_ai.py
"""

import os


def create_project():
    base_dir = "steel-detailer-ai"

    folders = [
        f"{base_dir}/app",
        f"{base_dir}/frontend/src",
        f"{base_dir}/.github/workflows",
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    print("\nProject structure created successfully!")
    print(f"\nNext steps:")
    print(f"1. cd {base_dir}/app")
    print(f"2. cp .env.example .env")
    print(f"3. Edit .env with your API keys")
    print(f"4. pip install -r requirements.txt")
    print(f"5. uvicorn main:app --reload")


if __name__ == "__main__":
    create_project()
