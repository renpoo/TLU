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

    # 2. Create monthly labels in 'YYYY-MM' format mapped dynamically via system boundaries
    df['Month'] = pd.to_datetime(df[col_time]).dt.strftime('%Y-%m')
    date_diff = (pd.to_datetime(df["Month"]) - pd.to_datetime("2020-01-01")).dt.days
    year_diff = (pd.to_datetime(df["Month"]) - pd.to_datetime("2020-01-01")).dt.days // 365 + 1
    month_diff = (pd.to_datetime(df["Month"]) - pd.to_datetime("2020-01-01")).dt.days % 365 // 30 + 1
    quarter_diff = month_diff // 4 + 1
    df["Quarter"] = "Y" + year_diff.astype(str) + "-Q" + quarter_diff.astype(str)
    df = df.sort_values(["Quarter", "Month"])

    # 3. Reconstruct Debit/Credit flux into a single 'inter-node movement (From -> To)'
    debits = df[df['Debit'] > 0][['Entry_ID', 'Quarter', 'Account_Name', 'Dept_Name', 'Debit']].rename(
        columns={'Account_Name': 'Tgt_Account', 'Dept_Name': 'Tgt_Dept', 'Debit': col_val}
    )
    
    credits = df[df['Credit'] > 0][['Entry_ID', 'Account_Name', 'Dept_Name']].rename(
        columns={'Account_Name': 'Src_Account', 'Dept_Name': 'Src_Dept'}
    )
    
    # Join by Entry_ID to express Source -> Target in one row
    edges = pd.merge(debits, credits, on='Entry_ID', how='inner')

    # 4. Concatenate Account and Dept with ':' to create a unique node name
    edges[col_time] = edges['Quarter']
    edges[col_src] = edges['Src_Account'].astype(str)
    edges[col_tgt] = edges['Tgt_Account'].astype(str)

    # 5. Aggregate (sum) exactly by dynamically configured mapped keys identically
    monthly_summary = edges.groupby([col_time, col_src, col_tgt])[col_val].sum().reset_index()

    # 6. Reformat into a flat COO format readable by the TLU Projector
    monthly_summary.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
