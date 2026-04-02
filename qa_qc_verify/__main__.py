"""
Entry point for standalone QA/QC scanner.
Usage: python -m qa_qc_verify [projects_root] [output_dir] [--focus all|stairs|rails|stair_rail]
"""

from .scan_runner import main

if __name__ == "__main__":
    main()
