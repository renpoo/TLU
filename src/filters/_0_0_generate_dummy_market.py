#!/usr/bin/env python3
# ==========================================
# _0_0_generate_dummy_market_z.py
# TLU System: Utility & Simulation Layer
# Category: Dummy Data Generation (Market Dual-Entry Ledger)
# ==========================================

import sys
import csv
import argparse
import random
import datetime
import numpy as np

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="TLU Open-Market Dual-Entry Transaction Generator")
    parser.add_argument("--months", type=int, default=12, help="Period to generate (in months)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--num-users", type=int, default=50, help="Number of users (N)")
    parser.add_argument("--num-stocks", type=int, default=3, help="Number of stocks (M)")
    parser.add_argument("--wash-trade-prob", type=float, default=0.0, help="Probability of a Wash Trade event per day")
    parser.add_argument("--panic-dump-prob", type=float, default=0.0, help="Probability of a Panic Dump event per day")
    parser.add_argument("--out-initial-state", type=str, default="", help="Path to write the initial state CSV")
    
    # External Flow parameters
    parser.add_argument("--external-flow-prob", type=float, default=0.2, help="Probability of external flow event per day")
    parser.add_argument("--external-flow-mean", type=float, default=20000000.0, help="Mean amount of cash flow (positive for inflow, negative for outflow)")
    parser.add_argument("--external-flow-std", type=float, default=40000000.0, help="Standard deviation of cash flow")
    return parser

def generate_stream(args):
    start_date = datetime.datetime(2020, 1, 1, 9, 0, 0)
    total_days = args.months * 30
    global_trans_count = 1
    
    writer = csv.writer(sys.stdout)
    # Header represents a dual-entry general journal (仕訳帳)
    writer.writerow([
        "Transaction_ID", "Timestamp", "Debit_Account", "Credit_Account", 
        "Asset_Type", "Amount", "Price", "Memo"
    ])

    stocks = [f"STK_{i:03d}" for i in range(1, args.num_stocks + 1)]
    # Target prices act as the fundamental value
    target_prices = {stock: random.uniform(1000.0, 5000.0) for stock in stocks}
    stock_prices = target_prices.copy()
    
    users = [f"USR_{i:03d}" for i in range(1, args.num_users + 1)]
    user_cash = {}
    initial_user_cash = {}
    user_portfolio = {u: {s: 0 for s in stocks} for u in users}
    user_profiles = {}
    
    # 1. Profile Assignment & Initial Mass Definition
    num_inst = max(2, int(args.num_users * 0.10))
    num_hft = max(2, int(args.num_users * 0.10))
    
    inst_users = users[:num_inst]
    hft_users = users[num_inst:num_inst+num_hft]
    retail_users = users[num_inst+num_hft:]

    for u in inst_users:
        user_profiles[u] = "Institutional"
        user_cash[u] = round(random.uniform(100_000_000, 500_000_000), 2)
        initial_user_cash[u] = user_cash[u]
        for s in stocks:
            user_portfolio[u][s] = random.randint(50000, 200000)

    for u in hft_users:
        user_profiles[u] = "HFT"
        user_cash[u] = round(random.uniform(50_000_000, 100_000_000), 2)
        initial_user_cash[u] = user_cash[u]
        for s in stocks:
            user_portfolio[u][s] = random.randint(1000, 5000)

    for u in retail_users:
        user_profiles[u] = "Retail"
        user_cash[u] = round(random.uniform(500_000, 2_000_000), 2)
        initial_user_cash[u] = user_cash[u]
        for s in stocks:
            if random.random() > 0.3:
                user_portfolio[u][s] = random.randint(100, 1000)

    # Export Initial State
    if args.out_initial_state:
        with open(args.out_initial_state, "w", encoding="utf-8") as f:
            state_writer = csv.writer(f, lineterminator='\n')
            state_writer.writerow(["node_label", "initial_X"])
            
            # Users' accounts (Cash & Stock)
            for u in users:
                state_writer.writerow([f"{u}_Cash", f"{user_cash[u]:.2f}"])
                user_stock_val = sum(user_portfolio[u][s] * stock_prices[s] for s in stocks)
                state_writer.writerow([f"{u}_Stock", f"{user_stock_val:.2f}"])
                
            # Stocks' issuing company liabilities
            for s in stocks:
                total_issued_val = sum(user_portfolio[u][s] * stock_prices[s] for u in users)
                # Liabilities are represented as positive to match Debit/Credit balance in accounting report
                # Our report generator adds this to Liabilities.
                # To balance Assets = Liab + Equity, we map USR_*_Cash and USR_*_Stock to Asset,
                # and STK_*_Issuer to Liability, and ACC_Input_From_Outside_Cash to Equity.
                # Since Cash and Stock are Dr (+), and Issuer is Cr (+):
                # Total Assets (Dr) = USR_Cash + USR_Stock.
                # Total Liab (Cr) = STK_Issuer.
                # The remaining difference goes to Equity (Cr).
                state_writer.writerow([f"{s}_Issuer", f"{total_issued_val:.2f}"])

    # 2. Daily Simulation
    volatility = 0.015
    
    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        daily_transactions = []
        
        # --- A. External Stochastic Flow Event (Cash Injection/Withdrawal) ---
        if random.random() < args.external_flow_prob:
            raw_flow = np.random.normal(args.external_flow_mean, args.external_flow_std)
            flow_amt = round(raw_flow, 2)
            
            target_users = retail_users + inst_users
            num_targets = min(len(target_users), random.randint(3, 8))
            selected_users = random.sample(target_users, k=num_targets)
            
            if flow_amt > 0:
                part_amt = round(flow_amt / num_targets, 2)
                for u in selected_users:
                    user_cash[u] = round(user_cash[u] + part_amt, 2)
                    t_offset = random.randint(0, 1800)
                    trans_time = current_date + datetime.timedelta(seconds=t_offset)
                    
                    tx_id = f"EX_IN_{global_trans_count:06d}"
                    # Cash Inflow: Debit User Cash, Credit External Source
                    daily_transactions.append([
                        tx_id, trans_time.isoformat(), f"{u}_Cash", "ACC_Input_From_Outside_Cash",
                        "CASH", f"{part_amt:.2f}", "1.00", "External_Inflow"
                    ])
                    global_trans_count += 1
            elif flow_amt < 0:
                abs_flow = abs(flow_amt)
                part_amt = round(abs_flow / num_targets, 2)
                for u in selected_users:
                    actual_part = min(part_amt, user_cash[u])
                    if actual_part > 0:
                        user_cash[u] = round(user_cash[u] - actual_part, 2)
                        t_offset = random.randint(0, 1800)
                        trans_time = current_date + datetime.timedelta(seconds=t_offset)
                        
                        tx_id = f"EX_OUT_{global_trans_count:06d}"
                        # Cash Outflow: Debit External Sink, Credit User Cash
                        daily_transactions.append([
                            tx_id, trans_time.isoformat(), "ACC_Output_To_Outside_Cash", f"{u}_Cash",
                            "CASH", f"{actual_part:.2f}", "1.00", "External_Outflow"
                        ])
                        global_trans_count += 1

        # Drift stock prices
        for stock in stocks:
            change_percent = np.random.normal(0, volatility)
            target_prices[stock] = max(1.0, target_prices[stock] * (1 + change_percent))
            
        # Normal Trading
        active_users = inst_users + retail_users
        random.shuffle(active_users)
        
        for u in active_users:
            profile = user_profiles[u]
            trade_prob = 0.03 if profile == "Institutional" else 0.18
            
            if random.random() < trade_prob:
                stock = random.choice(stocks)
                market_maker = random.choice(hft_users)
                
                inventory_ratio = user_portfolio[market_maker][stock] / 3000.0
                price_adjustment = 1.0 + (1.0 - inventory_ratio) * 0.015 
                
                raw_price = target_prices[stock] * price_adjustment * (1 + np.random.normal(0, 0.003))
                price = round(max(1.0, raw_price), 2)
                
                requested_volume = random.randint(5000, 20000) if profile == "Institutional" else random.randint(10, 350)
                
                cash_ratio = user_cash[u] / initial_user_cash[u]
                buy_prob = 0.5
                if cash_ratio > 1.2:
                    buy_prob = min(0.85, 0.5 + (cash_ratio - 1.0) * 0.15)
                elif cash_ratio < 0.8:
                    buy_prob = max(0.15, 0.5 - (1.0 - cash_ratio) * 0.25)
                
                is_buy = random.random() < buy_prob
                if is_buy:
                    buyer, seller = u, market_maker
                else:
                    buyer, seller = market_maker, u
                    
                max_buyable = int(user_cash[buyer] // price)
                max_sellable = user_portfolio[seller][stock]
                volume = min(requested_volume, max_buyable, max_sellable)
                
                if volume > 0:
                    amount = round(volume * price, 2)
                    
                    user_cash[buyer] = round(user_cash[buyer] - amount, 2)
                    user_cash[seller] = round(user_cash[seller] + amount, 2)
                    user_portfolio[buyer][stock] += volume
                    user_portfolio[seller][stock] -= volume
                    stock_prices[stock] = price
                    
                    demand_push = 0.0002 if is_buy else -0.0002
                    target_prices[stock] = max(1.0, target_prices[stock] * (1 + demand_push * volume))
                    
                    t_offset = random.randint(1800, 6 * 3600)
                    trans_time = current_date + datetime.timedelta(seconds=t_offset)
                    
                    tx_id = f"M_{global_trans_count:06d}"
                    # 1. Stock Entry: Debit Buyer_Stock, Credit Seller_Stock
                    daily_transactions.append([
                        tx_id, trans_time.isoformat(), f"{buyer}_Stock", f"{seller}_Stock",
                        stock, str(volume), f"{price:.2f}", "Normal"
                    ])
                    # 2. Cash Entry: Debit Seller_Cash, Credit Buyer_Cash
                    daily_transactions.append([
                        tx_id, trans_time.isoformat(), f"{seller}_Cash", f"{buyer}_Cash",
                        "CASH", f"{amount:.2f}", "1.00", "Normal"
                    ])
                    global_trans_count += 1
                    
        # HFT Inventory Balancing
        for hft in hft_users:
            for stock in stocks:
                inv = user_portfolio[hft][stock]
                if inv > 10000 or inv < 1000:
                    target_hft = random.choice([h for h in hft_users if h != hft])
                    price = round(target_prices[stock], 2)
                    
                    if inv > 10000:
                        buyer, seller = target_hft, hft
                        vol = random.randint(1000, 3000)
                    else:
                        buyer, seller = hft, target_hft
                        vol = random.randint(1000, 3000)
                        
                    max_buyable = int(user_cash[buyer] // price)
                    max_sellable = user_portfolio[seller][stock]
                    actual_vol = min(vol, max_buyable, max_sellable)
                    
                    if actual_vol > 0:
                        amount = round(actual_vol * price, 2)
                        user_cash[buyer] = round(user_cash[buyer] - amount, 2)
                        user_cash[seller] = round(user_cash[seller] + amount, 2)
                        user_portfolio[buyer][stock] += actual_vol
                        user_portfolio[seller][stock] -= actual_vol
                        
                        trans_time = current_date + datetime.timedelta(hours=6, minutes=random.randint(0, 59))
                        tx_id = f"M_{global_trans_count:06d}"
                        # 1. Stock Entry
                        daily_transactions.append([
                            tx_id, trans_time.isoformat(), f"{buyer}_Stock", f"{seller}_Stock",
                            stock, str(actual_vol), f"{price:.2f}", "MM_Balance"
                        ])
                        # 2. Cash Entry
                        daily_transactions.append([
                            tx_id, trans_time.isoformat(), f"{seller}_Cash", f"{buyer}_Cash",
                            "CASH", f"{amount:.2f}", "1.00", "MM_Balance"
                        ])
                        global_trans_count += 1

        # Wash Trade Anomaly
        if args.wash_trade_prob > 0.0 and random.random() < args.wash_trade_prob:
            w_stock = random.choice(stocks)
            w_user1, w_user2 = random.sample(hft_users, 2)
            w_price = round(target_prices[w_stock], 2)
            w_time = current_date + datetime.timedelta(hours=3)
            
            for i in range(20):
                w_time += datetime.timedelta(milliseconds=50)
                buyer = w_user1 if i % 2 == 0 else w_user2
                seller = w_user2 if i % 2 == 0 else w_user1
                volume = 5000
                
                max_buyable = int(user_cash[buyer] // w_price)
                max_sellable = user_portfolio[seller][w_stock]
                actual_vol = min(volume, max_buyable, max_sellable)
                
                if actual_vol > 0:
                    amount = round(actual_vol * w_price, 2)
                    user_cash[buyer] = round(user_cash[buyer] - amount, 2)
                    user_cash[seller] = round(user_cash[seller] + amount, 2)
                    user_portfolio[buyer][w_stock] += actual_vol
                    user_portfolio[seller][w_stock] -= actual_vol
                    
                    tx_id = f"M_{global_trans_count:06d}"
                    # 1. Stock Entry
                    daily_transactions.append([
                        tx_id, w_time.isoformat(), f"{buyer}_Stock", f"{seller}_Stock",
                        w_stock, str(actual_vol), f"{w_price:.2f}", "Wash_Trade"
                    ])
                    # 2. Cash Entry
                    daily_transactions.append([
                        tx_id, w_time.isoformat(), f"{seller}_Cash", f"{buyer}_Cash",
                        "CASH", f"{amount:.2f}", "1.00", "Wash_Trade"
                    ])
                    global_trans_count += 1

        # Panic Dump Anomaly
        if args.panic_dump_prob > 0.0 and random.random() < args.panic_dump_prob:
            p_stock = random.choice(stocks)
            whale = random.choice(inst_users)
            
            dump_vol = int(user_portfolio[whale][p_stock] * 0.8) 
            mm = random.choice(hft_users)
            price = round(stock_prices[p_stock] * 0.8, 2)
            
            max_buyable = int(user_cash[mm] // price)
            actual_dump = min(dump_vol, max_buyable)
            
            if actual_dump > 0:
                p_time = current_date + datetime.timedelta(hours=4)
                amount = round(actual_dump * price, 2)
                
                user_cash[mm] = round(user_cash[mm] - amount, 2)
                user_cash[whale] = round(user_cash[whale] + amount, 2)
                user_portfolio[mm][p_stock] += actual_dump
                user_portfolio[whale][p_stock] -= actual_dump
                
                tx_id = f"M_{global_trans_count:06d}"
                # 1. Stock Entry
                daily_transactions.append([
                    tx_id, p_time.isoformat(), f"{mm}_Stock", f"{whale}_Stock",
                    p_stock, str(actual_dump), f"{price:.2f}", "Panic_Dump_Whale"
                ])
                # 2. Cash Entry
                daily_transactions.append([
                    tx_id, p_time.isoformat(), f"{whale}_Cash", f"{mm}_Cash",
                    "CASH", f"{amount:.2f}", "1.00", "Panic_Dump_Whale"
                ])
                global_trans_count += 1
                
                target_prices[p_stock] *= 0.8
                
                for retail in retail_users:
                    if random.random() > 0.2 and user_portfolio[retail][p_stock] > 0:
                        p_time += datetime.timedelta(seconds=random.randint(1, 10))
                        r_dump_vol = user_portfolio[retail][p_stock]
                        r_mm = random.choice(hft_users)
                        r_price = round(price * random.uniform(0.8, 0.95), 2)
                        
                        max_r_buyable = int(user_cash[r_mm] // r_price)
                        r_actual = min(r_dump_vol, max_r_buyable)
                        
                        if r_actual > 0:
                            r_amount = round(r_actual * r_price, 2)
                            user_cash[r_mm] = round(user_cash[r_mm] - r_amount, 2)
                            user_cash[retail] = round(user_cash[retail] + r_amount, 2)
                            user_portfolio[r_mm][p_stock] += r_actual
                            user_portfolio[retail][p_stock] -= r_actual
                            
                            tx_id = f"M_{global_trans_count:06d}"
                            # 1. Stock Entry
                            daily_transactions.append([
                                tx_id, p_time.isoformat(), f"{r_mm}_Stock", f"{retail}_Stock",
                                p_stock, str(r_actual), f"{r_price:.2f}", "Panic_Dump_Retail"
                            ])
                            # 2. Cash Entry
                            daily_transactions.append([
                                tx_id, p_time.isoformat(), f"{retail}_Cash", f"{r_mm}_Cash",
                                "CASH", f"{r_amount:.2f}", "1.00", "Panic_Dump_Retail"
                            ])
                            global_trans_count += 1

        # Output daily transactions sorted by time.
        # Since we have two rows per transaction, we sort by timestamp, then by Transaction_ID.
        daily_transactions.sort(key=lambda x: (x[1], x[0]))
        for row in daily_transactions:
            writer.writerow(row)

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    generate_stream(args)

if __name__ == "__main__":
    main()
