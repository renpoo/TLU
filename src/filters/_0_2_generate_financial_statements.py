#!/usr/bin/env python3
# ==========================================
# _0_2_generate_financial_statements.py
# TLU System: Utility & Simulation Layer
# Category: Financial Statement Generator
# Version: 6.0.0 (Refactored with AccountTaxonomy)
# ==========================================
import sys
import argparse
import pandas as pd
import collections
import json
import os

from src.core.core_accounting_taxonomy import AccountTaxonomy, AccountCategory

def main():
    parser = argparse.ArgumentParser(description="Generate Financial Statements from TLU Graph Edges")
    parser.add_argument("--mapping", required=True, help="Path to _account_mapping.csv")
    parser.add_argument("--output", required=True, help="Path to output markdown file")
    parser.add_argument("--initial_state", default="", help="Path to ephemeral/_initial_state_labels.csv")
    args, unknown = parser.parse_known_args()

    from src.filters.cli_parser import parse_projector_args
    mapping_config = parse_projector_args(unknown)
    col_time = mapping_config.get("col_time", "Trans_Date")
    col_src = mapping_config.get("col_src", "Src")
    col_tgt = mapping_config.get("col_tgt", "Tgt")
    col_val = mapping_config.get("col_val", "Amount")

    custom_map = {}
    try:
        mapping_df = pd.read_csv(args.mapping)
        custom_map = dict(zip(mapping_df['Account_Name'], mapping_df['Category']))
    except Exception as e:
        print(f"[WARN] Could not read mapping file: {e}. Using default taxonomy.", file=sys.stderr)

    taxonomy = AccountTaxonomy(custom_map)

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
    
    if args.initial_state and os.path.exists(args.initial_state):
        try:
            init_df = pd.read_csv(args.initial_state)
            for _, row in init_df.iterrows():
                acc = row.get("node_label", "")
                val = float(row.get("initial_X", 0.0))
                cat = taxonomy.classify_account(acc)
                if cat in (AccountCategory.ASSET, AccountCategory.EXPENSE):
                    cum_debits[acc] += val
                else:
                    cum_credits[acc] += val
        except Exception as e:
            print(f"[WARN] Failed to load initial state from {args.initial_state}: {e}", file=sys.stderr)
    
    def get_balance(account, dr, cr):
        cat = taxonomy.classify_account(account)
        if cat in (AccountCategory.ASSET, AccountCategory.EXPENSE):
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
        
        bs_items = []
        pl_items = []
        tb_items = []
        
        all_accounts = set(cum_debits.keys()) | set(cum_credits.keys())
        for acc in sorted(all_accounts):
            dr = cum_debits[acc]
            cr = cum_credits[acc]
            bal = get_balance(acc, dr, cr)
            cat_enum = taxonomy.classify_account(acc)
            cat_str = cat_enum.value
            
            tb_items.append((acc, cat_str, dr, cr, bal))
            
            if cat_enum == AccountCategory.ASSET:
                if bal < 0:
                    liabilities += -bal
                    bs_items.append((acc, 'Liability (Short/Overdraft)', -bal))
                else:
                    assets += bal
                    bs_items.append((acc, cat_str, bal))
            elif cat_enum == AccountCategory.LIABILITY:
                if bal < 0:
                    assets += -bal
                    bs_items.append((acc, 'Asset (Receivable)', -bal))
                else:
                    liabilities += bal
                    bs_items.append((acc, cat_str, bal))
            elif cat_enum == AccountCategory.EQUITY:
                equity += bal
                bs_items.append((acc, cat_str, bal))
            elif cat_enum == AccountCategory.REVENUE:
                revenue += bal
                pl_items.append((acc, cat_str, bal))
            elif cat_enum == AccountCategory.EXPENSE:
                expense += bal
                pl_items.append((acc, cat_str, bal))
            else:
                expense += bal
                pl_items.append((acc, cat_str, bal))
        
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
            'pl_items': pl_items,
            'tb_items': tb_items
        }
        weekly_reports.append(report)

    with open(args.output, 'w') as f:
        f.write("# TLU Financial Statements Report\n\n")
        f.write("> *This report bridges TLU mathematical outputs with traditional accounting frameworks.*\n\n")
        
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
        f.write("## 2. Gross Flow / Trial Balance (T/B)\n\n")
        f.write("> *Reveals the total trading volume and liquidity passing through the nodes (Debit = Outflow/Acquisition, Credit = Inflow/Disposition).*\n\n")
        f.write("| Account | Category | Gross Debit (Dr) | Gross Credit (Cr) | Net Balance |\n")
        f.write("|---|---|---|---|---|\n")
        for acc, cat, dr, cr, bal in final['tb_items']:
            f.write(f"| {acc} | {cat} | {dr:,.2f} | {cr:,.2f} | {bal:,.2f} |\n")
        f.write("\n---\n")

        f.write("## 3. Weekly Trend Summary\n\n")
        f.write("| Week | Total Assets | Total Liab. | Retained Earnings | Net Income | Balanced? |\n")
        f.write("|---|---|---|---|---|---|\n")
        for r in weekly_reports:
            status = '✅' if r['is_balanced'] else '❌'
            f.write(f"| {r['week']} | {r['assets']:,.2f} | {r['liabilities']:,.2f} | {r['equity']:,.2f} | {r['net_income']:,.2f} | {status} |\n")

    json_path = args.output.replace('.md', '.json')
    with open(json_path, 'w') as f:
        json.dump(weekly_reports, f, indent=2)

if __name__ == "__main__":
    main()
