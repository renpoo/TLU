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
    
    # Initialize Users
    users = [f"USR_{i:03d}" for i in range(1, args.num_users + 1)]

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
        # Random number of trades per day: 10 to 50
        num_normal_trades = random.randint(10, 50)
        for _ in range(num_normal_trades):
            t_offset_seconds = random.randint(0, 6 * 3600) # Distribute within 6 hours
            trans_time = current_date + datetime.timedelta(seconds=t_offset_seconds)
            
            stock = random.choice(stocks)
            buyer, seller = random.sample(users, 2)
            
            # Add some micro-volatility to the price
            price = stock_prices[stock] * (1 + np.random.normal(0, 0.005))
            price = round(price, 2)
            volume = random.randint(100, 2000)
            
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
            # Select 1 stock and 2 specific users to ping-pong
            w_stock = random.choice(stocks)
            w_user1, w_user2 = random.sample(users, 2)
            w_price = stock_prices[w_stock]
            
            w_time = current_date + datetime.timedelta(seconds=random.randint(3600, 4 * 3600))
            
            # Generate 5-10 rapid back-and-forth trades
            num_washes = random.randint(5, 10)
            for i in range(num_washes):
                w_time += datetime.timedelta(milliseconds=random.randint(100, 500)) # Millisecond latency
                
                buyer = w_user1 if i % 2 == 0 else w_user2
                seller = w_user2 if i % 2 == 0 else w_user1
                volume = random.randint(5000, 10000) # High volume
                price = round(w_price * (1 + np.random.normal(0, 0.001)), 2) # Very tight price range
                
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
            instigator = random.choice(users)
            victims = [u for u in users if u != instigator]
            
            p_time = current_date + datetime.timedelta(hours=2)
            
            # Phase 1: Pump (Instigator buys massive amounts, driving price up)
            current_p_price = stock_prices[p_stock]
            for _ in range(5):
                p_time += datetime.timedelta(minutes=random.randint(1, 5))
                seller = random.choice(victims)
                volume = random.randint(3000, 8000)
                current_p_price *= 1.05 # 5% increase per trade
                
                daily_transactions.append([
                    f"M_{global_trans_count:06d}",
                    p_time.isoformat(),
                    p_stock,
                    instigator, # Instigator is buying
                    seller,
                    f"{current_p_price:.2f}",
                    str(volume),
                    "Pump_Phase"
                ])
                global_trans_count += 1
                
            # Phase 2: Dump (Instigator sells everything to victims at peak)
            p_time += datetime.timedelta(minutes=random.randint(10, 30))
            for _ in range(5):
                p_time += datetime.timedelta(seconds=random.randint(10, 60))
                buyer = random.choice(victims)
                volume = random.randint(3000, 8000)
                current_p_price *= 0.90 # Price crashes as they dump
                
                daily_transactions.append([
                    f"M_{global_trans_count:06d}",
                    p_time.isoformat(),
                    p_stock,
                    buyer,
                    instigator, # Instigator is selling
                    f"{current_p_price:.2f}",
                    str(volume),
                    "Dump_Phase"
                ])
                global_trans_count += 1
            
            # Update base price to reflect the crash
            stock_prices[p_stock] = current_p_price

        # Sort daily transactions by time just in case anomalies were out of order
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
