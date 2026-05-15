#!/usr/bin/env python3
"""
@file 00_1_parse_journal.py
@brief TLU/WMU Pre-processing Phase 0: Parses raw double-entry accounting journals into standard COO stream.
@details
This script acts as a "Thin Adapter" specifically for accounting data.
It reads raw journal entries (with Debits and Credits), matches them by Entry_ID,
and flattens them into a 1-to-1 transaction network (COO format).

@pre Input must be CSV via stdin containing at least: ['Trans_Date', 'Entry_ID', 'Debit', 'Credit', 'Account_Name']
@post Output is CSV via stdout containing: ['t_idx', 'src_idx', 'tgt_idx', 'value']
@note This script does NOT perform temporal aggregation. It preserves the original Trans_Date.
"""

import sys
import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Parse raw journal to COO stream.")
    parser.add_argument("--col_time", default="Trans_Date", help="Name of time column")
    parser.add_argument("--col_src", default="Src", help="Output source column name")
    parser.add_argument("--col_tgt", default="Tgt", help="Output target column name")
    parser.add_argument("--col_val", default="Amount", help="Output value column name")
    return parser.parse_args()

def main():
    args = parse_args()

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"[ERROR] Failed to read input: {e}\n")
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    # Validate contract
    required = [args.col_time, 'Entry_ID', 'Debit', 'Credit', 'Account_Name']
    for req in required:
        if req not in df.columns:
            sys.stderr.write(f"[ERROR] Missing required column: {req}\n")
            sys.exit(1)

    # Extract debits and credits
    agg_dict_dr = {'Account_Name': 'first', 'Debit': 'sum'}
    agg_dict_cr = {'Account_Name': 'first', 'Credit': 'sum'}
    
    if args.col_time != 'Entry_ID':
        agg_dict_dr[args.col_time] = 'first'
        agg_dict_cr[args.col_time] = 'first'

    debits = df[df['Debit'] > 0].groupby('Entry_ID').agg(agg_dict_dr).reset_index()
    debits = debits.rename(columns={'Account_Name': 'Tgt_Account', 'Debit': 'Debit_Amt'})

    credits = df[df['Credit'] > 0].groupby('Entry_ID').agg(agg_dict_cr).reset_index()
    credits = credits.rename(columns={'Account_Name': 'Src_Account', 'Credit': 'Credit_Amt'})

    # Bipartite matching on Entry_ID
    edges = pd.merge(debits, credits, on='Entry_ID', how='outer', suffixes=('_dr', '_cr'))
    edges['Debit_Amt'] = edges['Debit_Amt'].fillna(0)
    edges['Credit_Amt'] = edges['Credit_Amt'].fillna(0)
    
    # Resolve time
    if args.col_time == 'Entry_ID':
        edges['Time_Resolved'] = edges['Entry_ID']
    else:
        edges['Time_Resolved'] = edges[f"{args.col_time}_dr"].combine_first(edges[f"{args.col_time}_cr"])
    
    # Resolve Amount (Min of Debit/Credit for matching, excess goes to UNKNOWN_LEAK)
    edges['Base_Amount'] = edges[['Debit_Amt', 'Credit_Amt']].min(axis=1)

    final_edges = []
    for _, row in edges.iterrows():
        base_amt = row['Base_Amount']
        dr = row['Debit_Amt']
        cr = row['Credit_Amt']
        
        t_val = row.get('Time_Resolved', None)
        if pd.isna(t_val):
            continue 

        src = str(row['Src_Account']) if pd.notna(row['Src_Account']) else 'UNKNOWN_LEAK'
        tgt = str(row['Tgt_Account']) if pd.notna(row['Tgt_Account']) else 'UNKNOWN_LEAK'

        # Ensure ACC_ prefix for TLU compatibility
        if src != 'UNKNOWN_LEAK' and not src.startswith('ACC_'):
            src = f"ACC_{src}"
        if tgt != 'UNKNOWN_LEAK' and not tgt.startswith('ACC_'):
            tgt = f"ACC_{tgt}"

        # Main matched flow
        if base_amt > 0:
            final_edges.append({'t_idx': t_val, 'src_idx': src, 'tgt_idx': tgt, 'value': base_amt})
        
        # Discrepancy leaks
        diff_cr = cr - base_amt
        if diff_cr > 0:
            final_edges.append({'t_idx': t_val, 'src_idx': src, 'tgt_idx': 'UNKNOWN_LEAK', 'value': diff_cr})
            
        diff_dr = dr - base_amt
        if diff_dr > 0:
            final_edges.append({'t_idx': t_val, 'src_idx': 'UNKNOWN_LEAK', 'tgt_idx': tgt, 'value': diff_dr})

    if not final_edges:
        sys.exit(0)

    final_df = pd.DataFrame(final_edges)
    final_df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
