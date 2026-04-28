#!/usr/bin/env python3
# ==========================================
# _0_0_generate_dummy_market.py
# TLU System: Utility & Simulation Layer
# Category: Dummy Data Generation (Event-Driven Market Model)
# ==========================================

import sys
import csv
import argparse
import random
import datetime
import numpy as np
from collections import defaultdict

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="TLU Market Transaction Generator")
    parser.add_argument("--months", type=int, default=12, help="Period to generate (in months)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--num-users", type=int, default=10, help="Number of users (N)")
    parser.add_argument("--num-stocks", type=int, default=5, help="Number of stocks (M)")
    parser.add_argument("--wash-trade-prob", type=float, default=0.0, help="Probability of a Wash Trade event per day")
    parser.add_argument("--pump-dump-prob", type=float, default=0.0, help="Probability of a Pump & Dump event per day")
    return parser

def generate_stream(args):
    start_date = datetime.datetime(2020, 1, 1, 9, 0, 0) # Start at 9:00 AM
    total_days = args.months * 30
    
    global_trans_count = 1
    
    writer = csv.writer(sys.stdout)
    writer.writerow(["Transaction_ID", "Timestamp", "Stock_ID", "Buyer_ID", "Seller_ID", "Price", "Volume", "Memo"])

    # Initialize Stocks
    stocks = [f"STK_{i:03d}" for i in range(1, args.num_stocks + 1)]
    stock_prices = {stock: random.uniform(100.0, 5000.0) for stock in stocks}
    
    # Initialize Users (Agents)
    users = [f"USR_{i:03d}" for i in range(1, args.num_users + 1)]
    
    # Stateful Ledger
    user_cash = {u: random.uniform(1_000_000, 10_000_000) for u in users}
    user_portfolio = {u: {s: 0 for s in stocks} for u in users}
    
    # Initial IPO Allocation (Give users some starting stocks)
    for u in users:
        for s in stocks:
            if random.random() > 0.5:
                user_portfolio[u][s] = random.randint(100, 5000)

    # Simple Random Walk params
    volatility = 0.02
    
    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        
        # Update base prices for the day (Geometric Brownian Motion step)
        for stock in stocks:
            change_percent = np.random.normal(0, volatility)
            stock_prices[stock] = max(1.0, stock_prices[stock] * (1 + change_percent))
            
        daily_transactions = []
        
        # 1. Generate Normal Baseline Trading (Random Noise)
        num_normal_trades = random.randint(10, 50)
        for _ in range(num_normal_trades):
            t_offset_seconds = random.randint(0, 6 * 3600) # Distribute within 6 hours
            trans_time = current_date + datetime.timedelta(seconds=t_offset_seconds)
            
            stock = random.choice(stocks)
            # Find a valid seller (must have stock)
            valid_sellers = [u for u in users if user_portfolio[u][stock] > 0]
            if not valid_sellers:
                continue
                
            seller = random.choice(valid_sellers)
            buyer = random.choice([u for u in users if u != seller])
            
            # Add some micro-volatility to the price
            price = stock_prices[stock] * (1 + np.random.normal(0, 0.005))
            price = round(price, 2)
            
            # Constraint: Buyer cash and Seller shares
            max_buyable = int(user_cash[buyer] // price)
            max_sellable = user_portfolio[seller][stock]
            
            if max_buyable <= 0 or max_sellable <= 0:
                continue
                
            requested_volume = random.randint(10, 500)
            volume = min(requested_volume, max_buyable, max_sellable)
            
            if volume > 0:
                # Update Ledgers
                user_cash[buyer] -= volume * price
                user_cash[seller] += volume * price
                user_portfolio[buyer][stock] += volume
                user_portfolio[seller][stock] -= volume
                
                daily_transactions.append([
                    f"M_{global_trans_count:06d}",
                    trans_time.isoformat(),
                    stock,
                    buyer,
                    seller,
                    f"{price:.2f}",
                    str(volume),
                    "Normal"
                ])
                global_trans_count += 1
            
        # 2. Anomaly: Wash Trading
        if args.wash_trade_prob > 0.0 and random.random() < args.wash_trade_prob:
            w_stock = random.choice(stocks)
            # Find two users who have some stock and cash
            valid_w_users = [u for u in users if user_portfolio[u][w_stock] > 0 and user_cash[u] > 10000]
            if len(valid_w_users) >= 2:
                w_user1, w_user2 = random.sample(valid_w_users, 2)
                w_price = stock_prices[w_stock]
                
                w_time = current_date + datetime.timedelta(seconds=random.randint(3600, 4 * 3600))
                num_washes = random.randint(5, 10)
                
                for i in range(num_washes):
                    w_time += datetime.timedelta(milliseconds=random.randint(100, 500))
                    
                    buyer = w_user1 if i % 2 == 0 else w_user2
                    seller = w_user2 if i % 2 == 0 else w_user1
                    
                    price = round(w_price * (1 + np.random.normal(0, 0.001)), 2)
                    max_buyable = int(user_cash[buyer] // price)
                    max_sellable = user_portfolio[seller][w_stock]
                    
                    if max_buyable <= 0 or max_sellable <= 0:
                        break # Loop broken due to lack of funds
                        
                    requested_volume = random.randint(1000, 5000)
                    volume = min(requested_volume, max_buyable, max_sellable)
                    
                    if volume > 0:
                        user_cash[buyer] -= volume * price
                        user_cash[seller] += volume * price
                        user_portfolio[buyer][w_stock] += volume
                        user_portfolio[seller][w_stock] -= volume
                        
                        daily_transactions.append([
                            f"M_{global_trans_count:06d}",
                            w_time.isoformat(),
                            w_stock,
                            buyer,
                            seller,
                            f"{price:.2f}",
                            str(volume),
                            "Wash_Trade"
                        ])
                        global_trans_count += 1

        # 3. Anomaly: Pump & Dump
        if args.pump_dump_prob > 0.0 and random.random() < args.pump_dump_prob:
            p_stock = random.choice(stocks)
            valid_instigators = [u for u in users if user_cash[u] > 500000] # Must have high cash to pump
            
            if valid_instigators:
                instigator = random.choice(valid_instigators)
                victims = [u for u in users if u != instigator]
                
                p_time = current_date + datetime.timedelta(hours=2)
                current_p_price = stock_prices[p_stock]
                
                # Phase 1: Pump
                for _ in range(5):
                    p_time += datetime.timedelta(minutes=random.randint(1, 5))
                    valid_sellers = [v for v in victims if user_portfolio[v][p_stock] > 0]
                    if not valid_sellers:
                        break
                        
                    seller = random.choice(valid_sellers)
                    current_p_price *= 1.05
                    price = round(current_p_price, 2)
                    
                    max_buyable = int(user_cash[instigator] // price)
                    max_sellable = user_portfolio[seller][p_stock]
                    
                    if max_buyable <= 0 or max_sellable <= 0:
                        break
                        
                    requested_volume = random.randint(500, 2000)
                    volume = min(requested_volume, max_buyable, max_sellable)
                    
                    if volume > 0:
                        user_cash[instigator] -= volume * price
                        user_cash[seller] += volume * price
                        user_portfolio[instigator][p_stock] += volume
                        user_portfolio[seller][p_stock] -= volume
                        
                        daily_transactions.append([
                            f"M_{global_trans_count:06d}",
                            p_time.isoformat(),
                            p_stock,
                            instigator,
                            seller,
                            f"{price:.2f}",
                            str(volume),
                            "Pump_Phase"
                        ])
                        global_trans_count += 1
                    
                # Phase 2: Dump
                p_time += datetime.timedelta(minutes=random.randint(10, 30))
                for _ in range(5):
                    p_time += datetime.timedelta(seconds=random.randint(10, 60))
                    valid_buyers = [v for v in victims if user_cash[v] > current_p_price]
                    if not valid_buyers or user_portfolio[instigator][p_stock] <= 0:
                        break
                        
                    buyer = random.choice(valid_buyers)
                    current_p_price *= 0.90
                    price = round(current_p_price, 2)
                    
                    max_buyable = int(user_cash[buyer] // price)
                    max_sellable = user_portfolio[instigator][p_stock]
                    
                    volume = min(random.randint(500, 2000), max_buyable, max_sellable)
                    
                    if volume > 0:
                        user_cash[buyer] -= volume * price
                        user_cash[instigator] += volume * price
                        user_portfolio[buyer][p_stock] += volume
                        user_portfolio[instigator][p_stock] -= volume
                        
                        daily_transactions.append([
                            f"M_{global_trans_count:06d}",
                            p_time.isoformat(),
                            p_stock,
                            buyer,
                            instigator,
                            f"{price:.2f}",
                            str(volume),
                            "Dump_Phase"
                        ])
                        global_trans_count += 1
                
                stock_prices[p_stock] = current_p_price

        # Sort daily transactions by time
        daily_transactions.sort(key=lambda x: x[1])
        
        # Output stream
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
