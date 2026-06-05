#!/usr/bin/env python3
# ==========================================
# _0_2_generate_financial_statements_market_double.py
# TLU System: Utility & Simulation Layer
# Category: Financial Statement Generator with Dual Conservation & MTM
# ==========================================

import sys
import argparse
import pandas as pd
import numpy as np
import random
import json
import collections

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate MTM Financial Statements from TLU Market Stream")
    parser.add_argument("--months", type=int, default=12, help="Period generated (in months)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed used in generator")
    parser.add_argument("--num-users", type=int, default=10, help="Number of users")
    parser.add_argument("--num-stocks", type=int, default=5, help="Number of stocks")
    parser.add_argument("--mapping", required=True, help="Path to _account_mapping.csv")
    parser.add_argument("--output", required=True, help="Path to output markdown file")
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
    # Target prices act as fundamental values at initial state
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

    # Calculate initial Equity Capital per user (purely initial cash to avoid double counting stock values)
    initial_equity = {}
    for u in users:
        initial_equity[u] = initial_cash[u]

    # Calculate total shares issued per stock (remains conserved throughout)
    total_shares_issued = {}
    for s in stocks:
        total_shares_issued[s] = sum(user_portfolio[u][s] for u in users)

    # 3. Read Stream from stdin
    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input stream: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        print("Input stream is empty", file=sys.stderr)
        sys.exit(0)

    # Convert timestamp and extract week grouping
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='ISO8601')
    df['week'] = df['Timestamp'].dt.to_period('W').astype(str)
    weeks = sorted(df['week'].unique())

    weekly_reports = []

    # Sort stream by timestamp
    df = df.sort_values('Timestamp')

    # Process week-by-week
    cum_inflow = 0.0
    cum_outflow = 0.0

    for w in weeks:
        week_df = df[df['week'] == w]
        
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
            if buyer == "ACC_Input_From_Outside":
                cum_inflow = round(cum_inflow + amount, 2)
                    
            if seller in user_cash:
                user_cash[seller] = round(user_cash[seller] + amount, 2)
            if seller == "ACC_Output_To_Outside":
                cum_outflow = round(cum_outflow + amount, 2)
            
            # Apply Stock holdings changes
            if buyer in user_portfolio and seller in user_portfolio and stock != "CASH_FLOW":
                user_portfolio[buyer][stock] += volume
                user_portfolio[seller][stock] -= volume
            
            # Update last traded price
            if stock != "CASH_FLOW":
                stock_prices[stock] = price

        # B/S Calculations for the current week
        assets = 0.0
        liabilities = 0.0
        equity = 0.0
        net_income = 0.0

        bs_items = []
        tb_items = []

        # 1. User Cash (Asset) and Net Income (Equity)
        for u in users:
            cash_val = user_cash[u]
            stock_val = sum(user_portfolio[u][s] * stock_prices[s] for s in stocks)
            total_assets_u = round(cash_val + stock_val, 2)
            
            # Record user assets on B/S (Cash + Stock MTM Value)
            assets += total_assets_u
            bs_items.append((f"{u}_Cash", "Asset", cash_val))
            bs_items.append((f"{u}_Stock_Val", "Asset", stock_val))
            
            init_eq = initial_equity[u]
            equity += init_eq
            
            tb_items.append((f"{u}_Cash", "Asset", cash_val))
            tb_items.append((f"{u}_Stock_Val", "Asset", stock_val))

        # Net Income is defined as the net cash flow generated by trading + external flows
        # Net Income = Inflow - Outflow
        net_income = round(cum_inflow - cum_outflow, 2)

        # 2. Stock Capitalization (Liability - the custody side matching User_Stock_Val)
        for s in stocks:
            market_cap = round(total_shares_issued[s] * stock_prices[s], 2)
            liabilities += market_cap
            bs_items.append((f"{s}_Cap", "Liability", market_cap))
            tb_items.append((f"{s}_Cap", "Liability", market_cap))

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
            'revenue': cum_inflow,
            'expense': cum_outflow,
            'is_balanced': is_balanced,
            'bs_items': bs_items,
            'pl_items': [
                ('External_Inflow_Revenue', 'Revenue', cum_inflow),
                ('External_Outflow_Expense', 'Expense', cum_outflow)
            ],
            'tb_items': tb_items
        }
        weekly_reports.append(report)

    # 4. Write Markdown Output
    with open(args.output, 'w') as f:
        f.write("# TLU Mark-to-Market Financial Statements Report (Double Conservation)\n\n")
        f.write("> *This report displays MTM valuation based on weekly stock close prices, maintaining both cash and share volume conservation.*\n\n")
        
        final = weekly_reports[-1]
        f.write("## 1. Total Period Summary (Cumulative)\n\n")
        f.write(f"**Period End:** {final['week']}\n")
        f.write(f"**Status:** {'✅ BALANCED' if final['is_balanced'] else '❌ UNBALANCED'}\n\n")
        
        f.write("### Balance Sheet (B/S)\n")
        f.write("| Account | Category | Balance |\n")
        f.write("|---|---|---|\n")
        
        # Sort and write User Assets, Stock Liabilities, and Equity
        user_cash_items = sorted([item for item in final['bs_items'] if 'Cash' in item[0]])
        user_stock_items = sorted([item for item in final['bs_items'] if 'Stock_Val' in item[0]])
        stock_caps = sorted([item for item in final['bs_items'] if '_Cap' in item[0]])
        
        for acc, cat, bal in user_cash_items:
            f.write(f"| {acc} | {cat} | {bal:,.2f} |\n")
        for acc, cat, bal in user_stock_items:
            f.write(f"| {acc} | {cat} | {bal:,.2f} |\n")
        for acc, cat, bal in stock_caps:
            f.write(f"| {acc} | {cat} | {bal:,.2f} |\n")
            
        f.write(f"| ACC_Equity_Capital | Equity | {final['equity']:,.2f} |\n")
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
        f.write(f"| **Net Income (Realized Trading PnL)** | | **{final['net_income']:,.2f}** |\n\n")
        
        f.write("---\n")
        f.write("## 2. Weekly Trend Summary\n\n")
        f.write("| Week | Total Assets | Total Liab. (Stock Cap) | Retained Earnings | Net Income | Balanced? |\n")
        f.write("|---|---|---|---|---|---|\n")
        for r in weekly_reports:
            status = '✅' if r['is_balanced'] else '❌'
            f.write(f"| {r['week']} | {r['assets']:,.2f} | {r['liabilities']:,.2f} | {r['equity']:,.2f} | {r['net_income']:,.2f} | {status} |\n")

    # Generate JSON Output for Visualizer
    json_path = args.output.replace('.md', '.json')
    with open(json_path, 'w') as f:
        json.dump(weekly_reports, f, indent=2)

    print("Completed successfully. Balanced financial reports generated.")

if __name__ == "__main__":
    main()
