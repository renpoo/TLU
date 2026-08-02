#!/usr/bin/env python3
"""
TLU Standalone Math Engine CLI for Tauri Sidecar
Input: Path to financial CSV file or directory
Output: JSON output to stdout or output file
"""
import sys
import os
import json
import argparse
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.utils._99_export_json_summary import export_summary_json

def main():
    parser = argparse.ArgumentParser(description="TLU Core Math Analysis Engine")
    parser.add_argument("--csv", type=str, help="Path to input financial CSV file")
    parser.add_argument("--outdir", type=str, help="Path to output directory containing analysis CSVs")
    parser.add_argument("--nodemap", type=str, help="Path to _node_map.csv")
    parser.add_argument("--timemap", type=str, help="Path to _time_map.csv")

    args = parser.parse_args()

    out_dir = args.outdir
    if not out_dir and args.csv:
        out_dir = os.path.dirname(args.csv)

    if not out_dir or not os.path.exists(out_dir):
        out_dir = "samples/Sample_0_Healthy/output_data"

    try:
        summary = export_summary_json(out_dir, args.nodemap, args.timemap)
        print(json.dumps(summary, ensure_ascii=False))
        sys.exit(0)
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
