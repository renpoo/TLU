#!/usr/bin/env python3
import sys
import argparse
import pandas as pd
import collections
import json
import os

def main():
    parser = argparse.ArgumentParser(description="Generate Hybrid Thermodynamic Financial Statements")
    parser.add_argument("--mapping", required=True, help="Path to _account_mapping.csv")
    parser.add_argument("--output", required=True, help="Path to output markdown file")
    args, unknown = parser.parse_known_args()

    from src.filters.cli_parser import parse_projector_args
    mapping_config = parse_projector_args(unknown)
    col_time = mapping_config.get("col_time", "Trans_Date")
    col_src = mapping_config.get("col_src", "Src")
    col_tgt = mapping_config.get("col_tgt", "Tgt")
    col_val = mapping_config.get("col_val", "Amount")

    # Read mapping (3 columns: Account_Name, Custom_Label, Accounting_Category)
    try:
        mapping_df = pd.read_csv(args.mapping)
        # Handle both 2-column and 3-column for backward compatibility
        if 'Custom_Label' in mapping_df.columns and 'Accounting_Category' in mapping_df.columns:
            account_map = {}
            for _, r in mapping_df.iterrows():
                account_map[r['Account_Name']] = {
                    'label': r['Custom_Label'],
                    'category': r['Accounting_Category']
                }
        else:
            # Fallback to 2-column
            account_map = {}
            for _, r in mapping_df.iterrows():
                account_map[r['Account_Name']] = {
                    'label': 'Uncategorized',
                    'category': r.get('Category', 'Expense')
                }
    except Exception as e:
        print(f"Error reading mapping file: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input stream: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)
        
    weeks = sorted(df[col_time].unique())
    cum_debits = collections.defaultdict(float)
    cum_credits = collections.defaultdict(float)
    
    weekly_reports = []
    
    def get_balance(category, dr, cr):
        if category in ['Asset', 'Expense']:
            return dr - cr
        else:
            return cr - dr

    for w in weeks:
        week_df = df[df[col_time] == w]
        
        for _, row in week_df.iterrows():
            src = row[col_src]
            tgt = row[col_tgt]
            amt = row[col_val]
            
            cum_credits[src] += amt
            cum_debits[tgt] += amt
            
        assets = 0.0
        liabilities = 0.0
        equity = 0.0
        revenue = 0.0
        expense = 0.0
        unknown_leak = 0.0
        
        bs_items = collections.defaultdict(list)
        pl_items = collections.defaultdict(list)
        
        all_accounts = set(cum_debits.keys()) | set(cum_credits.keys())
        for acc in sorted(all_accounts):
            dr = cum_debits[acc]
            cr = cum_credits[acc]
            
            info = account_map.get(acc, {'label': 'Unmapped', 'category': 'External'})
            cat = info['category']
            label = info['label']
            
            if cat == 'External':
                # External nodes act as the environment. Their net interaction with the system is the LEAK.
                # If an external node has net Credit (Outflow), it injected energy INTO our system (Positive Leak)
                # If an external node has net Debit (Inflow), it extracted energy FROM our system (Negative Leak)
                net_external_flow = cr - dr
                unknown_leak += net_external_flow
                continue
                
            bal = get_balance(cat, dr, cr)
            
            if cat == 'Asset':
                if bal < 0:
                    liabilities += -bal
                    bs_items[label].append((acc, 'Liability (Short)', -bal))
                else:
                    assets += bal
                    bs_items[label].append((acc, cat, bal))
            elif cat == 'Liability':
                if bal < 0:
                    assets += -bal
                    bs_items[label].append((acc, 'Asset (Receivable)', -bal))
                else:
                    liabilities += bal
                    bs_items[label].append((acc, cat, bal))
            elif cat == 'Equity':
                equity += bal
                bs_items[label].append((acc, cat, bal))
            elif cat == 'Revenue':
                revenue += bal
                pl_items[label].append((acc, cat, bal))
            elif cat == 'Expense':
                expense += bal
                pl_items[label].append((acc, cat, bal))
        
        net_income = revenue - expense
        total_equity = equity + net_income
        total_liab_eq = liabilities + total_equity
        
        # System Balance = Assets - (Liabilities + Equity)
        # If there is a leak from the environment, the internal B/S will not balance!
        # internal_imbalance = assets - total_liab_eq
        # In a perfect double-entry system with an external environment, 
        # internal_imbalance exactly equals the net injection from the environment (unknown_leak).
        
        report = {
            'week': w,
            'assets': assets,
            'liabilities': liabilities,
            'equity': equity,
            'net_income': net_income,
            'total_liab_eq': total_liab_eq,
            'revenue': revenue,
            'expense': expense,
            'unknown_leak': unknown_leak,
            'internal_imbalance': assets - total_liab_eq,
            'bs_items': bs_items,
            'pl_items': pl_items
        }
        weekly_reports.append(report)

    with open(args.output, 'w') as f:
        f.write("# TLU Hybrid Thermodynamic Financial Statements\n\n")
        f.write("> *This report merges traditional double-entry bookkeeping (B/S, P/L) with thermodynamic custom labels, while exposing the UNKNOWN_LEAK from the external environment.*\n\n")
        
        final = weekly_reports[-1]
        f.write("## 1. System State Summary (Cumulative)\n\n")
        f.write(f"**Period End:** {final['week']}\n\n")
        
        f.write("### 🛑 UNKNOWN_LEAK (External Energy Transfer)\n")
        f.write(f"> **{final['unknown_leak']:,.2f}** (Positive = Energy Injected into System, Negative = Energy Extracted)\n\n")
        
        f.write("### Balance Sheet (B/S) - System State\n")
        for label, items in sorted(final['bs_items'].items()):
            f.write(f"#### [{label}]\n")
            f.write("| Node | Category | Balance |\n")
            f.write("|---|---|---|\n")
            for acc, cat, bal in items:
                f.write(f"| {acc} | {cat} | {bal:,.2f} |\n")
            f.write("\n")
            
        f.write(f"**Retained Earnings (Net Income):** {final['net_income']:,.2f} (Equity)\n\n")
        f.write(f"**Total Assets:** {final['assets']:,.2f}\n")
        f.write(f"**Total Liab & Equity:** {final['total_liab_eq']:,.2f}\n")
        f.write(f"**Internal Imbalance (Assets - Liab&Eq):** {final['internal_imbalance']:,.2f}\n\n")
        
        f.write("### Profit & Loss (P/L) - System Flux\n")
        for label, items in sorted(final['pl_items'].items()):
            f.write(f"#### [{label}]\n")
            f.write("| Node | Category | Balance |\n")
            f.write("|---|---|---|\n")
            for acc, cat, bal in items:
                f.write(f"| {acc} | {cat} | {bal:,.2f} |\n")
            f.write("\n")
            
        f.write(f"**Total Revenue:** {final['revenue']:,.2f}\n")
        f.write(f"**Total Expenses:** {final['expense']:,.2f}\n")
        f.write(f"**Net Income:** {final['net_income']:,.2f}\n\n")
        
        f.write("---\n")
        f.write("## 2. Weekly Trend\n\n")
        f.write("| Week | Total Assets | Total Liab&Eq | Net Income | UNKNOWN_LEAK |\n")
        f.write("|---|---|---|---|---|\n")
        for r in weekly_reports:
            f.write(f"| {r['week']} | {r['assets']:,.2f} | {r['total_liab_eq']:,.2f} | {r['net_income']:,.2f} | {r['unknown_leak']:,.2f} |\n")

    json_path = args.output.replace('.md', '.json')
    with open(json_path, 'w') as f:
        json.dump(weekly_reports, f, indent=2)

if __name__ == "__main__":
    main()
