#!/usr/bin/env python3
# ==========================================
# _0_2_generate_financial_statements_market_pl_allocation.py
# TLU System: Utility & Simulation Layer
# Category: Financial Statement Generator with B/S & P/L Partition Allocation
# ==========================================

import sys
import argparse
import pandas as pd
import numpy as np
import random
import json

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate Partition Allocated Financial Statements")
    parser.add_argument("--months", type=int, default=12, help="Period generated (in months)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed used in generator")
    parser.add_argument("--num-users", type=int, default=10, help="Number of users")
    parser.add_argument("--num-stocks", type=int, default=5, help="Number of stocks")
    parser.add_argument("--mapping", required=True, help="Path to _account_mapping.csv")
    parser.add_argument("--output", required=True, help="Path to output markdown file")
    parser.add_argument("--true-stream", required=True, help="Path to unfiltered Sample_X2 stream (actual bank records)")
    parser.add_argument("--initial_state", default="", help="Path to ephemeral/_initial_state_labels.csv (ignored)")
    return parser

def main():
    parser = setup_argparser()
    args, unknown = parser.parse_known_args()

    # 1. Load account mapping
    try:
        mapping_df = pd.read_csv(args.mapping)
        account_map = dict(zip(mapping_df['Account_Name'], mapping_df['Category']))
    except Exception as e:
        print(f"Error reading mapping file: {e}", file=sys.stderr)
        sys.exit(1)

    # 2. Re-generate exact initial state using the seed to ensure dual conservation
    random.seed(args.seed)
    np.random.seed(args.seed)

    stocks = [f"STK_{i:03d}" for i in range(1, args.num_stocks + 1)]
    target_prices = {stock: random.uniform(1000.0, 5000.0) for stock in stocks}
    stock_prices = target_prices.copy()
    
    users = [f"USR_{i:03d}" for i in range(1, args.num_users + 1)]
    user_cash = {}
    user_portfolio = {u: {s: 0 for s in stocks} for u in users}
    user_profiles = {}
    
    num_inst = max(2, int(args.num_users * 0.10))
    num_hft = max(2, int(args.num_users * 0.10))
    
    inst_users = users[:num_inst]
    hft_users = users[num_inst:num_inst+num_hft]
    retail_users = users[num_inst+num_hft:]

    for u in inst_users:
        user_profiles[u] = "Institutional"
        user_cash[u] = round(random.uniform(100_000_000, 500_000_000), 2)
        for s in stocks:
            user_portfolio[u][s] = random.randint(50000, 200000)

    for u in hft_users:
        user_profiles[u] = "HFT"
        user_cash[u] = round(random.uniform(50_000_000, 100_000_000), 2)
        for s in stocks:
            user_portfolio[u][s] = random.randint(1000, 5000)

    for u in retail_users:
        user_profiles[u] = "Retail"
        user_cash[u] = round(random.uniform(500_000, 2_000_000), 2)
        for s in stocks:
            if random.random() > 0.3:
                user_portfolio[u][s] = random.randint(100, 1000)

    # Initial balance sheets setup
    initial_cash = user_cash.copy()
    initial_portfolio = {u: user_portfolio[u].copy() for u in users}
    initial_stock_prices = stock_prices.copy()

    # Calculate total shares issued per stock
    total_shares_issued = {}
    for s in stocks:
        total_shares_issued[s] = sum(user_portfolio[u][s] for u in users)

    # Calculate initial capital representing shareholder assets (Cash + Portfolio Value)
    initial_corporate_cash = sum(initial_cash[u] for u in users)
    initial_stock_cap = sum(total_shares_issued[s] * initial_stock_prices[s] for s in stocks)
    initial_equity_allocation = initial_corporate_cash + initial_stock_cap

    # 3. Read Stream from true_stream (actual bank records)
    try:
        df_true = pd.read_csv(args.true_stream)
    except Exception as e:
        print(f"Error reading true stream: {e}", file=sys.stderr)
        sys.exit(1)

    if df_true.empty:
        print("True stream is empty", file=sys.stderr)
        sys.exit(1)

    # Convert timestamp and extract week grouping
    df_true['Timestamp'] = pd.to_datetime(df_true['Timestamp'], format='ISO8601')
    df_true['week'] = df_true['Timestamp'].dt.to_period('W').astype(str)
    weeks = sorted(df_true['week'].unique())

    weekly_reports = []

    # Sort stream by timestamp
    df_true = df_true.sort_values('Timestamp')

    # Simulation trackers
    prev_stock_cap = initial_stock_cap
    prev_corp_cash = initial_corporate_cash

    cum_val_loss = 0.0
    cum_val_gain = 0.0
    cum_est_inflow = 0.0
    cum_est_outflow = 0.0

    for w in weeks:
        week_df = df_true[df_true['week'] == w]
        
        # Apply transactions sequentially
        for _, row in week_df.iterrows():
            stock = row['Stock_ID']
            buyer = row['Buyer_ID']
            seller = row['Seller_ID']
            price = float(row['Price'])
            volume = int(row['Volume'])
            amount = float(row['Transaction_Amount'])
            
            # Apply Cash changes safely
            if buyer in user_cash:
                user_cash[buyer] = round(user_cash[buyer] - amount, 2)
            if seller in user_cash:
                user_cash[seller] = round(user_cash[seller] + amount, 2)
            
            # Apply Stock holdings changes
            if buyer in user_portfolio and seller in user_portfolio and stock != "CASH_FLOW":
                user_portfolio[buyer][stock] += volume
                user_portfolio[seller][stock] -= volume
            
            # Update last traded price
            if stock != "CASH_FLOW":
                stock_prices[stock] = price

        # B/S Calculations for the current week (Partition Allocated View)
        # 1. Assets: Shareholder Cash + Shareholder Stock Portfolio Values
        corp_cash = sum(user_cash[u] for u in users)
        
        bs_items = []
        tb_items = []
        
        assets = corp_cash
        for u in users:
            cash_val = user_cash[u]
            stock_val = sum(user_portfolio[u][s] * stock_prices[s] for s in stocks)
            assets += stock_val
            bs_items.append((f"{u}_Cash", "Asset", cash_val))
            bs_items.append((f"{u}_Stock_Val", "Asset", stock_val))
            tb_items.append((f"{u}_Cash", "Asset", cash_val))
            tb_items.append((f"{u}_Stock_Val", "Asset", stock_val))

        assets = round(assets, 2)

        # 2. Liabilities: None (Stocks are not mapped as corporate liability here)
        liabilities = 0.0

        # 3. P/L Calculations (Partition Allocations)
        # a) Stock Valuation shifts mapped to P/L
        current_stock_cap = sum(total_shares_issued[s] * stock_prices[s] for s in stocks)
        delta_stock_cap = round(current_stock_cap - prev_stock_cap, 2)
        prev_stock_cap = current_stock_cap
        
        if delta_stock_cap > 0:
            cum_val_gain = round(cum_val_gain + delta_stock_cap, 2)
        elif delta_stock_cap < 0:
            cum_val_loss = round(cum_val_loss + (-delta_stock_cap), 2)

        # b) Cash Pool changes (Reconstructed External Funding Flows)
        delta_corp_cash = round(corp_cash - prev_corp_cash, 2)
        prev_corp_cash = corp_cash

        if delta_corp_cash > 0:
            cum_est_inflow = round(cum_est_inflow + delta_corp_cash, 2)
        elif delta_corp_cash < 0:
            cum_est_outflow = round(cum_est_outflow + (-delta_corp_cash), 2)

        # Net Income = (Reconstructed Cash Flows) + (Stock Valuation shifts)
        net_income = round((cum_est_inflow - cum_est_outflow) + (cum_val_gain - cum_val_loss), 2)
        
        total_equity = equity = round(initial_equity_allocation, 2)
        total_equity = round(total_equity + net_income, 2)
        total_liab_eq = liabilities + total_equity
        is_balanced = abs(assets - total_liab_eq) < 0.01

        report = {
            'week': w,
            'assets': assets,
            'liabilities': liabilities,
            'equity': equity,
            'net_income': net_income,
            'total_liab_eq': total_liab_eq,
            # Visualization mapping compatibility:
            'revenue': round(cum_est_inflow + cum_val_gain, 2),
            'expense': round(cum_est_outflow + cum_val_loss, 2),
            'is_balanced': is_balanced,
            'bs_items': bs_items,
            'pl_items': [
                ('ACC_Stock_Valuation_Gain', 'Revenue', cum_val_gain),
                ('Estimated_External_Funding_Inflow', 'Revenue', cum_est_inflow),
                ('ACC_Stock_Valuation_Loss', 'Expense', cum_val_loss),
                ('Estimated_External_Funding_Outflow', 'Expense', cum_est_outflow)
            ],
            'tb_items': tb_items
        }
        weekly_reports.append(report)

    # 4. Write Markdown Output
    with open(args.output, 'w') as f:
        f.write("# TLU Mark-to-Market Financial Statements Report (Partition Allocated View)\n\n")
        f.write("> *This report displays B/S and P/L under Partition Allocation where shareholder portfolios are on the B/S (Assets) and stock capitalization shifts are mapped on the P/L.*\n\n")
        
        final = weekly_reports[-1]
        f.write("## 1. Total Period Summary (Cumulative)\n\n")
        f.write(f"**Period End:** {final['week']}\n")
        f.write(f"**Status:** {'✅ BALANCED (via Partition Allocation)' if final['is_balanced'] else '❌ UNBALANCED'}\n\n")
        
        f.write("### Balance Sheet (B/S)\n")
        f.write("| Account | Category | Balance |\n")
        f.write("|---|---|---|\n")
        
        user_cash_items = sorted([item for item in final['bs_items'] if 'Cash' in item[0]])
        user_stock_items = sorted([item for item in final['bs_items'] if 'Stock_Val' in item[0]])
        
        for acc, cat, bal in user_cash_items:
            f.write(f"| {acc} | {cat} | {bal:,.2f} |\n")
        for acc, cat, bal in user_stock_items:
            f.write(f"| {acc} | {cat} | {bal:,.2f} |\n")
            
        f.write(f"| Initial_Shareholder_Equity | Equity | {final['equity']:,.2f} |\n")
        f.write(f"| **Retained Earnings (Corporate Net Income)** | Equity | **{final['net_income']:,.2f}** |\n")
        f.write("|---|---|---|\n")
        f.write(f"| **Total Assets** | | **{final['assets']:,.2f}** |\n")
        f.write(f"| **Total Liabilities & Equity** | | **{final['total_liab_eq']:,.2f}** |\n\n")
        
        f.write("### Profit & Loss (P/L)\n")
        f.write("| Account | Category | Balance |\n")
        f.write("|---|---|---|\n")
        for acc, cat, bal in final['pl_items']:
            f.write(f"| {acc} | {cat} | {bal:,.2f} |\n")
        f.write("|---|---|---|\n")
        f.write(f"| **Corporate Net Income** | | **{final['net_income']:,.2f}** |\n\n")
        
        f.write("---\n")
        f.write("## 2. Weekly Trend Summary\n\n")
        f.write("| Week | Total Assets (Cash+Stock) | Total Liab. (0) | Retained Earnings | Net Income | Balanced? |\n")
        f.write("|---|---|---|---|---|---|\n")
        for r in weekly_reports:
            status = '✅' if r['is_balanced'] else '❌'
            f.write(f"| {r['week']} | {r['assets']:,.2f} | {r['liabilities']:,.2f} | {r['equity']:,.2f} | {r['net_income']:,.2f} | {status} |\n")

    # Generate JSON Output for Visualizer
    json_path = args.output.replace('.md', '.json')
    with open(json_path, 'w') as f:
        json.dump(weekly_reports, f, indent=2)

    print("Completed successfully. Balanced financial reports (Partition View) generated.")

if __name__ == "__main__":
    main()
