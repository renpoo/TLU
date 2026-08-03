#!/usr/bin/env python3
# ==========================================
# 00_1_parse_journal_dept.py
# TLU System: Pre-processing Phase 0
# Category: Account+Dept Node Coupling Parser
# Version: 6.0.0 (Refactored with TemporalBinningEngine)
# ==========================================
"""
@file 00_1_parse_journal_dept.py
@brief Parses raw journals into fine-grained (Account_Dept) COO streams with temporal binning.
"""

import os
import sys
import argparse
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.core.core_temporal_binning import apply_temporal_binning

def parse_args():
    parser = argparse.ArgumentParser(
        description="TLU Journal Preprocessor with Account_Name + Dept_Name Node Coupling"
    )
    parser.add_argument("--interval", default="month", help="Aggregation time interval (e.g., month, week, day)")
    parser.add_argument("--col_time", default="Trans_Date", help="Transaction date column name")
    return parser.parse_args()

def main():
    args = parse_args()
    
    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"[ERROR] Failed to read CSV from stdin: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    req_cols = [args.col_time, "Entry_ID", "Account_Name", "Dept_Name", "Debit", "Credit"]
    for col in req_cols:
        if col not in df.columns:
            print(f"[CRITICAL] Column '{col}' missing from input stream. Found: {list(df.columns)}", file=sys.stderr)
            sys.exit(1)

    df["Dept_Name"] = df["Dept_Name"].fillna("General")
    df["Node_Label"] = "ACC_" + df["Account_Name"].astype(str) + "_" + df["Dept_Name"].astype(str)
    
    df["t_idx"] = apply_temporal_binning(df[args.col_time], args.interval)
    
    entries = []
    grouped = df.groupby("Entry_ID")

    for entry_id, group in grouped:
        t_idx = group["t_idx"].iloc[0]
        
        cr_rows = group[group["Credit"] > 0]
        dr_rows = group[group["Debit"] > 0]

        for _, cr in cr_rows.iterrows():
            src_node = cr["Node_Label"]
            amt = cr["Credit"]
            for _, dr in dr_rows.iterrows():
                tgt_node = dr["Node_Label"]
                entries.append({
                    "t_idx": t_idx,
                    "src_idx": src_node,
                    "tgt_idx": tgt_node,
                    "value": amt
                })

    if not entries:
        print("[WARN] No valid double-entry pairs found.", file=sys.stderr)
        sys.exit(0)

    paired_df = pd.DataFrame(entries)
    agg_df = paired_df.groupby(["t_idx", "src_idx", "tgt_idx"], as_index=False)["value"].sum()
    agg_df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
