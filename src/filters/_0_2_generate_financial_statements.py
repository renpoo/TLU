#!/usr/bin/env python3
import sys
import argparse
import pandas as pd
import collections
import json
import os

def main():
    parser = argparse.ArgumentParser(description="Generate Financial Statements from TLU Graph Edges")
    parser.add_argument("--mapping", required=True, help="Path to _account_mapping.csv")
    parser.add_argument("--output", required=True, help="Path to output markdown file")
    args = parser.parse_args()

    # Read mapping
    try:
        mapping_df = pd.read_csv(args.mapping)
        account_map = dict(zip(mapping_df['Account_Name'], mapping_df['Category']))
    except Exception as e:
        print(f"Error reading mapping file: {e}", file=sys.stderr)
        sys.exit(1)

    # Read aggregated journal from stdin
    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input stream: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    # df has columns: Trans_Date, Src, Tgt, Amount
    # Src = Credit, Tgt = Debit
    
    # Process transactions by week
    weeks = sorted(df['Trans_Date'].unique())
    
    # Track cumulative debits and credits
    cum_debits = collections.defaultdict(float)
    cum_credits = collections.defaultdict(float)
    
    weekly_reports = []
    
    def get_balance(account, dr, cr):
        category = account_map.get(account, 'Expense') # Default to Expense if unknown
        if category in ['Asset', 'Expense']:
            return dr - cr
        else:
            return cr - dr

    for w in weeks:
        week_df = df[df['Trans_Date'] == w]
        
        # Accumulate period
        for _, row in week_df.iterrows():
            src = row['Src']
            tgt = row['Tgt']
            amt = row['Amount']
            
            cum_credits[src] += amt
            cum_debits[tgt] += amt
            
        # Calculate balances for this week
        assets = 0.0
        liabilities = 0.0
        equity = 0.0
        revenue = 0.0
        expense = 0.0
        
        bs_items = []
        pl_items = []
        
        all_accounts = set(cum_debits.keys()) | set(cum_credits.keys())
        for acc in sorted(all_accounts):
            dr = cum_debits[acc]
            cr = cum_credits[acc]
            bal = get_balance(acc, dr, cr)
            cat = account_map.get(acc, 'Expense')
            
            if cat == 'Asset':
                assets += bal
                bs_items.append((acc, cat, bal))
            elif cat == 'Liability':
                liabilities += bal
                bs_items.append((acc, cat, bal))
            elif cat == 'Equity':
                equity += bal
                bs_items.append((acc, cat, bal))
            elif cat == 'Revenue':
                revenue += bal
                pl_items.append((acc, cat, bal))
            elif cat == 'Expense':
                expense += bal
                pl_items.append((acc, cat, bal))
        
        net_income = revenue - expense
        total_equity = equity + net_income
        total_liab_eq = liabilities + total_equity
        
        is_balanced = abs(assets - total_liab_eq) < 0.01
        
        report = {
            'week': w,
            'assets': assets,
            'liabilities': liabilities,
            'equity': equity,
            'net_income': net_income,
            'total_liab_eq': total_liab_eq,
            'revenue': revenue,
            'expense': expense,
            'is_balanced': is_balanced,
            'bs_items': bs_items,
            'pl_items': pl_items
        }
        weekly_reports.append(report)

    # Generate Markdown Output
    with open(args.output, 'w') as f:
        f.write("# TLU Financial Statements Report\n\n")
        f.write("> *This report bridges TLU mathematical outputs with traditional accounting frameworks.*\n\n")
        
        # 1. Total Period Summary (Last Week)
        final = weekly_reports[-1]
        f.write("## 1. Total Period Summary (Cumulative)\n\n")
        f.write(f"**Period End:** {final['week']}\n")
        f.write(f"**Status:** {'✅ BALANCED' if final['is_balanced'] else '❌ UNBALANCED'}\n\n")
        
        f.write("### Balance Sheet (B/S)\n")
        f.write("| Account | Category | Balance |\n")
        f.write("|---|---|---|\n")
        for acc, cat, bal in final['bs_items']:
            f.write(f"| {acc} | {cat} | {bal:,.2f} |\n")
        f.write(f"| **Retained Earnings (Net Income)** | Equity | **{final['net_income']:,.2f}** |\n")
        f.write("|---|---|---|\n")
        f.write(f"| **Total Assets** | | **{final['assets']:,.2f}** |\n")
        f.write(f"| **Total Liabilities & Equity** | | **{final['total_liab_eq']:,.2f}** |\n\n")
        
        f.write("### Profit & Loss (P/L)\n")
        f.write("| Account | Category | Balance |\n")
        f.write("|---|---|---|\n")
        for acc, cat, bal in final['pl_items']:
            f.write(f"| {acc} | {cat} | {bal:,.2f} |\n")
        f.write("|---|---|---|\n")
        f.write(f"| **Total Revenue** | | **{final['revenue']:,.2f}** |\n")
        f.write(f"| **Total Expenses** | | **{final['expense']:,.2f}** |\n")
        f.write(f"| **Net Income** | | **{final['net_income']:,.2f}** |\n\n")
        
        f.write("---\n")
        f.write("## 2. Weekly Trend Summary\n\n")
        f.write("| Week | Total Assets | Total Liab. | Retained Earnings | Net Income | Balanced? |\n")
        f.write("|---|---|---|---|---|---|\n")
        for r in weekly_reports:
            status = '✅' if r['is_balanced'] else '❌'
            f.write(f"| {r['week']} | {r['assets']:,.2f} | {r['liabilities']:,.2f} | {r['net_income']:,.2f} | {r['net_income']:,.2f} | {status} |\n")

    # Generate JSON Output for Visualizer
    json_path = args.output.replace('.md', '.json')
    with open(json_path, 'w') as f:
        json.dump(weekly_reports, f, indent=2)

if __name__ == "__main__":
    main()
