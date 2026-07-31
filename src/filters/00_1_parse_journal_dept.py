#!/usr/bin/env python3
# ==========================================
# parse_and_aggregate_journal_dept.py
# TLU System: ERP Preprocessing Filter (Scratch Extension)
# Action: Combines Account_Name and Dept_Name into fine-grained nodes (Account_Dept)
#         and aggregates monthly transaction streams into Hodgepodge COO format.
# ==========================================

import sys
import argparse
import pandas as pd

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

    # Ensure required columns exist
    req_cols = [args.col_time, "Entry_ID", "Account_Name", "Dept_Name", "Debit", "Credit"]
    for col in req_cols:
        if col not in df.columns:
            print(f"[CRITICAL] Column '{col}' missing from input stream. Found: {list(df.columns)}", file=sys.stderr)
            sys.exit(1)

    # Construct combined node label: ACC_{Account_Name}_{Dept_Name}
    # For UNKNOWN_LEAK or special nodes without Dept_Name, handle gracefully
    df["Dept_Name"] = df["Dept_Name"].fillna("General")
    df["Node_Label"] = "ACC_" + df["Account_Name"].astype(str) + "_" + df["Dept_Name"].astype(str)
    
    # Parse transaction date and extract period
    df["parsed_time"] = pd.to_datetime(df[args.col_time], errors="coerce")
    df = df.dropna(subset=["parsed_time"])
    
    if args.interval == "month":
        df["t_idx"] = df["parsed_time"].dt.strftime("%Y-%m")
    elif args.interval == "week":
        df["t_idx"] = df["parsed_time"].dt.strftime("%G-W%V")
    elif args.interval == "day":
        df["t_idx"] = df["parsed_time"].dt.strftime("%Y-%m-%d")
    else:
        df["t_idx"] = df["parsed_time"].dt.strftime("%Y-%m")

    # Double-entry pairing by Entry_ID
    # Group by Entry_ID to pair Credit (Src) and Debit (Tgt)
    # Credit row has Credit > 0 (Outflow/Src), Debit row has Debit > 0 (Inflow/Tgt)
    entries = []
    grouped = df.groupby("Entry_ID")

    for entry_id, group in grouped:
        t_idx = group["t_idx"].iloc[0]
        
        # Credit rows (Source)
        cr_rows = group[group["Credit"] > 0]
        # Debit rows (Destination)
        dr_rows = group[group["Debit"] > 0]

        for _, cr in cr_rows.iterrows():
            src_node = cr["Node_Label"]
            amt = cr["Credit"]
            for _, dr in dr_rows.iterrows():
                tgt_node = dr["Node_Label"]
                # In double entry, amount transfers from src_node to tgt_node
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
    
    # Group by (t_idx, src_idx, tgt_idx) and sum values
    agg_df = paired_df.groupby(["t_idx", "src_idx", "tgt_idx"], as_index=False)["value"].sum()
    
    # Output to stdout as CSV
    agg_df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
