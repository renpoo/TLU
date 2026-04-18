#!/usr/bin/env python3
# ==========================================
# _0_1_preprocess_monthly_summary.py
# TLU System: Pre-filtering Layer
# Action: Monthly Aggregation of Journal Entries (Account:Dept Level)
# ==========================================
import sys
import pandas as pd

def main():
    try:
        # 1. Read stream from standard input
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    # 2. Create monthly labels in 'YYYY-MM' format from Trans_Date
    df['Month'] = pd.to_datetime(df['Trans_Date']).dt.strftime('%Y-%m')
    date_diff = (pd.to_datetime(df["Month"]) - pd.to_datetime("2020-01-01")).dt.days
    year_diff = (pd.to_datetime(df["Month"]) - pd.to_datetime("2020-01-01")).dt.days // 365 + 1
    month_diff = (pd.to_datetime(df["Month"]) - pd.to_datetime("2020-01-01")).dt.days % 365 // 30 + 1
    quarter_diff = month_diff // 4 + 1
    df["Quarter"] = "Y" + year_diff.astype(str) + "-Q" + quarter_diff.astype(str)
    df = df.sort_values(["Quarter", "Month"])

    # 3. Reconstruct Debit/Credit flux into a single 'inter-node movement (From -> To)'
    debits = df[df['Debit'] > 0][['Entry_ID', 'Quarter', 'Account_Name', 'Dept_Name', 'Debit']].rename(
        columns={'Account_Name': 'Tgt_Account', 'Dept_Name': 'Tgt_Dept', 'Debit': 'Amount'}
    )
    
    credits = df[df['Credit'] > 0][['Entry_ID', 'Account_Name', 'Dept_Name']].rename(
        columns={'Account_Name': 'Src_Account', 'Dept_Name': 'Src_Dept'}
    )
    
    # Join by Entry_ID to express Source -> Target in one row
    edges = pd.merge(debits, credits, on='Entry_ID', how='inner')

    # 4. Concatenate Account and Dept with ':' to create a unique node name
    edges['Trans_Date'] = edges['Quarter']
    edges['Src'] = edges['Src_Account'].astype(str)
    edges['Tgt'] = edges['Tgt_Account'].astype(str)
    # edges['Src'] = edges['Src_Dept'].astype(str)
    # edges['Tgt'] = edges['Tgt_Dept'].astype(str)
    # edges['Src'] = edges['Src_Account'].astype(str) + ':' + edges['Src_Dept'].astype(str)
    # edges['Tgt'] = edges['Tgt_Account'].astype(str) + ':' + edges['Tgt_Dept'].astype(str)

    # 5. Aggregate (sum) the Amount by Month, Source node, and Target node combination
    monthly_summary = edges.groupby(['Trans_Date', 'Src', 'Tgt'])['Amount'].sum().reset_index()

    # 6. Reformat into a flat COO format readable by the TLU Projector
    monthly_summary.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
