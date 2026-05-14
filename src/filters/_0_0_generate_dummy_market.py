#!/usr/bin/env python3
# ==========================================
# _0_0_generate_dummy_market.py
# TLU System: Utility & Simulation Layer
# Category: Dummy Data Generation (Market Topologies & Physical Mass Conservation)
# ==========================================

import sys
import csv
import argparse
import random
import datetime
import numpy as np

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="TLU Market Transaction Generator")
    parser.add_argument("--months", type=int, default=12, help="Period to generate (in months)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--num-users", type=int, default=50, help="Number of users (N)")
    parser.add_argument("--num-stocks", type=int, default=3, help="Number of stocks (M)")
    parser.add_argument("--wash-trade-prob", type=float, default=0.0, help="Probability of a Wash Trade event per day")
    parser.add_argument("--panic-dump-prob", type=float, default=0.0, help="Probability of a Panic Dump event per day")
    parser.add_argument("--out-initial-state", type=str, default="", help="Path to write the initial state CSV")
    return parser

def generate_stream(args):
    start_date = datetime.datetime(2020, 1, 1, 9, 0, 0)
    total_days = args.months * 30
    global_trans_count = 1
    
    writer = csv.writer(sys.stdout)
    writer.writerow(["Transaction_ID", "Timestamp", "Stock_ID", "Buyer_ID", "Seller_ID", "Price", "Volume", "Transaction_Amount", "Memo"])

    stocks = [f"STK_{i:03d}" for i in range(1, args.num_stocks + 1)]
    # Target prices act as the fundamental value
    target_prices = {stock: random.uniform(1000.0, 5000.0) for stock in stocks}
    stock_prices = target_prices.copy()
    
    users = [f"USR_{i:03d}" for i in range(1, args.num_users + 1)]
    user_cash = {}
    user_portfolio = {u: {s: 0 for s in stocks} for u in users}
    user_profiles = {}
    
    # 1. Profile Assignment & Initial Mass Definition (Integration from past history)
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
        # HFT has huge liquidity buffer (Cash) and a small buffer of stock to act as Market Maker
        user_cash[u] = round(random.uniform(50_000_000, 100_000_000), 2)
        for s in stocks:
            user_portfolio[u][s] = random.randint(1000, 5000)

    for u in retail_users:
        user_profiles[u] = "Retail"
        user_cash[u] = round(random.uniform(500_000, 2_000_000), 2)
        for s in stocks:
            if random.random() > 0.3:
                user_portfolio[u][s] = random.randint(100, 1000)

    # Export Initial State (Boundary Condition at t_0)
    if args.out_initial_state:
        with open(args.out_initial_state, "w", encoding="utf-8") as f:
            state_writer = csv.writer(f, lineterminator='\n')
            state_writer.writerow(["node_label", "initial_X"])
            for u in users:
                initial_stock_value = sum(user_portfolio[u][s] * stock_prices[s] for s in stocks)
                total_initial_mass = round(user_cash[u] + initial_stock_value, 2)
                state_writer.writerow([u, f"{total_initial_mass:.2f}"])

    # 2. Daily Simulation
    volatility = 0.01
    
    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        daily_transactions = []
        
        # Fundamental value drifts slightly
        for stock in stocks:
            change_percent = np.random.normal(0, volatility)
            target_prices[stock] = max(1.0, target_prices[stock] * (1 + change_percent))
            # Base price gravitates toward target price but is affected by HFT inventory in real-time
            
        # Normal Trading (HFT as Market Maker Hub)
        # Randomize user order to prevent bias
        active_users = inst_users + retail_users
        random.shuffle(active_users)
        
        for u in active_users:
            profile = user_profiles[u]
            trade_prob = 0.02 if profile == "Institutional" else 0.15
            
            if random.random() < trade_prob:
                stock = random.choice(stocks)
                market_maker = random.choice(hft_users)
                
                # Market maker adjusts price based on their inventory of this stock
                # If inventory is low (< 1000), price goes up (they don't want to sell)
                # If inventory is high (> 5000), price goes down (they want to sell)
                inventory_ratio = user_portfolio[market_maker][stock] / 3000.0
                price_adjustment = 1.0 + (1.0 - inventory_ratio) * 0.01 
                
                raw_price = target_prices[stock] * price_adjustment * (1 + np.random.normal(0, 0.002))
                price = round(max(1.0, raw_price), 2) # Strictly rounded to 2 decimals
                
                requested_volume = random.randint(5000, 20000) if profile == "Institutional" else random.randint(10, 300)
                
                is_buy = random.random() > 0.5
                if is_buy:
                    # User Buys from Market Maker (HFT)
                    buyer, seller = u, market_maker
                else:
                    # User Sells to Market Maker (HFT)
                    buyer, seller = market_maker, u
                    
                # STRICT PHYSICAL MASS CONSTRAINTS
                max_buyable = int(user_cash[buyer] // price)
                max_sellable = user_portfolio[seller][stock]
                volume = min(requested_volume, max_buyable, max_sellable)
                
                if volume > 0:
                    amount = round(volume * price, 2)
                    
                    user_cash[buyer] = round(user_cash[buyer] - amount, 2)
                    user_cash[seller] = round(user_cash[seller] + amount, 2)
                    user_portfolio[buyer][stock] += volume
                    user_portfolio[seller][stock] -= volume
                    
                    # Update stock public price
                    stock_prices[stock] = price
                    
                    t_offset = random.randint(0, 6 * 3600)
                    trans_time = current_date + datetime.timedelta(seconds=t_offset)
                    
                    daily_transactions.append([
                        f"M_{global_trans_count:06d}", trans_time.isoformat(), stock, buyer, seller,
                        f"{price:.2f}", str(volume), f"{amount:.2f}", "Normal"
                    ])
                    global_trans_count += 1
                    
        # HFT Inventory Balancing (End of Day, HFTs trade with each other to neutralize extreme inventory)
        for hft in hft_users:
            for stock in stocks:
                inv = user_portfolio[hft][stock]
                if inv > 10000 or inv < 1000: # Needs rebalancing
                    target_hft = random.choice([h for h in hft_users if h != hft])
                    # They trade at the fundamental target price
                    price = round(target_prices[stock], 2)
                    
                    if inv > 10000: # Sell excess to target
                        buyer, seller = target_hft, hft
                        vol = random.randint(1000, 3000)
                    else: # Buy deficit from target
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
                        daily_transactions.append([
                            f"M_{global_trans_count:06d}", trans_time.isoformat(), stock, buyer, seller,
                            f"{price:.2f}", str(actual_vol), f"{amount:.2f}", "MM_Balance"
                        ])
                        global_trans_count += 1

        # 3. Anomaly: Wash Trade (High-frequency infinite loop between 2 HFTs)
        if args.wash_trade_prob > 0.0 and random.random() < args.wash_trade_prob:
            w_stock = random.choice(stocks)
            w_user1, w_user2 = random.sample(hft_users, 2)
            w_price = round(target_prices[w_stock], 2)
            w_time = current_date + datetime.timedelta(hours=3)
            
            for i in range(20): # Extreme high frequency loop
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
                    
                    daily_transactions.append([
                        f"M_{global_trans_count:06d}", w_time.isoformat(), w_stock, buyer, seller,
                        f"{w_price:.2f}", str(actual_vol), f"{amount:.2f}", "Wash_Trade"
                    ])
                    global_trans_count += 1

        # 4. Anomaly: Panic Dump (Whale dumps, triggering retail sell-off)
        if args.panic_dump_prob > 0.0 and random.random() < args.panic_dump_prob:
            p_stock = random.choice(stocks)
            whale = random.choice(inst_users)
            
            dump_vol = int(user_portfolio[whale][p_stock] * 0.8) 
            mm = random.choice(hft_users)
            price = round(stock_prices[p_stock] * 0.8, 2) # 20% instant drop
            
            # Constraints
            max_buyable = int(user_cash[mm] // price)
            actual_dump = min(dump_vol, max_buyable)
            
            if actual_dump > 0:
                p_time = current_date + datetime.timedelta(hours=4)
                amount = round(actual_dump * price, 2)
                
                user_cash[mm] = round(user_cash[mm] - amount, 2)
                user_cash[whale] = round(user_cash[whale] + amount, 2)
                user_portfolio[mm][p_stock] += actual_dump
                user_portfolio[whale][p_stock] -= actual_dump
                
                daily_transactions.append([
                    f"M_{global_trans_count:06d}", p_time.isoformat(), p_stock, mm, whale,
                    f"{price:.2f}", str(actual_dump), f"{amount:.2f}", "Panic_Dump_Whale"
                ])
                global_trans_count += 1
                
                target_prices[p_stock] *= 0.8 # Market fundamental crashes
                
                # Retail panics
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
                            
                            daily_transactions.append([
                                f"M_{global_trans_count:06d}", p_time.isoformat(), p_stock, r_mm, retail,
                                f"{r_price:.2f}", str(r_actual), f"{r_amount:.2f}", "Panic_Dump_Retail"
                            ])
                            global_trans_count += 1

        # Output daily transactions sorted by time
        daily_transactions.sort(key=lambda x: x[1])
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
