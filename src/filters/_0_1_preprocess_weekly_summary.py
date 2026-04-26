#!/usr/bin/env python3
# ==========================================
# _0_1_preprocess_weekly_summary.py
# TLU System: Pre-filtering Layer
# Action: Weekly Aggregation of Journal Entries (Account:Dept Level)
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
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    # 2. Create weekly labels
    dt_col = pd.to_datetime(df[col_time])
    df['Week'] = dt_col.dt.isocalendar().year.astype(str) + "-W" + dt_col.dt.isocalendar().week.astype(str).str.zfill(2)

    # 3. Aggregate Debits and Credits by Entry_ID
    debits = df[df['Debit'] > 0].groupby('Entry_ID').agg({'Account_Name': 'first', 'Dept_Name': 'first', 'Debit': 'sum', 'Week': 'first'}).reset_index()
    debits = debits.rename(columns={'Account_Name': 'Tgt_Account', 'Dept_Name': 'Tgt_Dept', 'Debit': 'Debit_Amt'})

    credits = df[df['Credit'] > 0].groupby('Entry_ID').agg({'Account_Name': 'first', 'Dept_Name': 'first', 'Credit': 'sum'}).reset_index()
    credits = credits.rename(columns={'Account_Name': 'Src_Account', 'Dept_Name': 'Src_Dept', 'Credit': 'Credit_Amt'})

    # Join on Entry_ID (Outer join to catch unmatched entries)
    edges = pd.merge(debits, credits, on='Entry_ID', how='outer')
    edges['Debit_Amt'] = edges['Debit_Amt'].fillna(0)
    edges['Credit_Amt'] = edges['Credit_Amt'].fillna(0)

    # Resolve Base Amount (Min of Debit and Credit)
    edges['Base_Amount'] = edges[['Debit_Amt', 'Credit_Amt']].min(axis=1)

    # Reconstruct edges including UNKNOWN_LEAK for discrepancies
    final_edges = []
    for _, row in edges.iterrows():
        base_amt = row['Base_Amount']
        dr = row['Debit_Amt']
        cr = row['Credit_Amt']
        
        t_val = row.get('Week', None)
        if pd.isna(t_val):
            continue 

        src = str(row['Src_Account']) if pd.notna(row['Src_Account']) else 'UNKNOWN_LEAK'
        tgt = str(row['Tgt_Account']) if pd.notna(row['Tgt_Account']) else 'UNKNOWN_LEAK'

        if base_amt > 0:
            final_edges.append({col_time: t_val, col_src: src, col_tgt: tgt, col_val: base_amt})
        
        diff_cr = cr - base_amt
        if diff_cr > 0:
            final_edges.append({col_time: t_val, col_src: src, col_tgt: 'UNKNOWN_LEAK', col_val: diff_cr})
            
        diff_dr = dr - base_amt
        if diff_dr > 0:
            final_edges.append({col_time: t_val, col_src: 'UNKNOWN_LEAK', col_tgt: tgt, col_val: diff_dr})

    if not final_edges:
        sys.exit(0)

    final_df = pd.DataFrame(final_edges)

    # 5. Sum (aggregate) Amount by combination
    summary = final_df.groupby([col_time, col_src, col_tgt])[col_val].sum().reset_index()

    # 6. Reformat into a flat COO format
    summary.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
