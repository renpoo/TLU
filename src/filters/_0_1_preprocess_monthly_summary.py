#!/usr/bin/env python3
# ==========================================
# _0_1_preprocess_monthly_summary.py
# TLU System: Pre-filtering Layer
# Action: Monthly Aggregation of Journal Entries (Account:Dept Level)
# ==========================================
import sys
import pandas as pd
from src.filters.cli_parser import parse_projector_args

def main():
    mapping_config = parse_projector_args(sys.argv[1:])
    col_time = mapping_config.get("col_time", "Trans_Date")
    col_src = mapping_config.get("col_src", "Src")
    col_tgt = mapping_config.get("col_tgt", "Tgt")
    col_val = mapping_config.get("col_val", "Amount")
    try:
        # 1. Read stream from standard input
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    # 2. Create monthly label mapping dynamically to defined col_time
    df['Month'] = pd.to_datetime(df[col_time]).dt.strftime('%Y-%m')

    # 3. Reconstruct debit / credit flux into a single "movement between nodes (From -> To)"
    debits = df[df['Debit'] > 0][['Entry_ID', 'Month', 'Account_Name', 'Dept_Name', 'Debit']].rename(
        columns={'Account_Name': 'Tgt_Account', 'Dept_Name': 'Tgt_Dept', 'Debit': col_val}
    )
    
    credits = df[df['Credit'] > 0][['Entry_ID', 'Account_Name', 'Dept_Name']].rename(
        columns={'Account_Name': 'Src_Account', 'Dept_Name': 'Src_Dept'}
    )
    
    # Join on Entry_ID and represent Source -> Target in 1 row
    edges = pd.merge(debits, credits, on='Entry_ID', how='inner')

    # 4. Concatenate Account and Dept with ':' to create a unique node name
    edges[col_time] = edges['Month']
    edges[col_src] = edges['Src_Account'].astype(str)
    edges[col_tgt] = edges['Tgt_Account'].astype(str)

    # 5. Sum (aggregate) Amount by combination of Month, Source Node, Target Node
    monthly_summary = edges.groupby([col_time, col_src, col_tgt])[col_val].sum().reset_index()

    # 6. Reformat into a flat COO format readable by TLU Projector
    monthly_summary.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
