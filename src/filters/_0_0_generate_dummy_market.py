#!/usr/bin/env python3
# ==========================================
# _0_0_generate_dummy_market.py
# TLU System: Utility & Simulation Layer
# Category: Dummy Data Generation (Market Dual-Entry Ledger)
# Version: 6.0.0 (Refactored with BaseGenerator Architecture)
# ==========================================

import sys
import csv
import argparse
import random
import datetime
import numpy as np

from src.filters.base_generator import BaseGenerator

def generate_stream(args, generator: BaseGenerator = None):
    start_date = datetime.datetime(2020, 1, 1, 9, 0, 0)
    total_days = args.months * 30
    global_trans_count = 1
    
    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow([
        "Transaction_ID", "Timestamp", "Debit_Account", "Credit_Account", 
        "Asset_Type", "Amount", "Price", "Memo"
    ])

    stocks = [f"STK_{i:03d}" for i in range(1, args.num_stocks + 1)]
    target_prices = {stock: random.uniform(1000.0, 5000.0) for stock in stocks}
    stock_prices = target_prices.copy()
    
    users = [f"USR_{i:03d}" for i in range(1, args.num_users + 1)]
    user_cash = {}
    initial_user_cash = {}
    user_portfolio = {u: {s: 0 for s in stocks} for u in users}
    user_profiles = {}
    
    num_inst = max(2, int(args.num_users * 0.10))
    num_hft = max(2, int(args.num_users * 0.10))
    
    inst_users = users[:num_inst]
    hft_users = users[num_inst:num_inst+num_hft]
    retail_users = users[num_inst+num_hft:]
    
    for u in inst_users:
        user_profiles[u] = 'INST'
        cash = random.uniform(10000000.0, 50000000.0)
        user_cash[u] = cash
        initial_user_cash[u] = cash
        for s in stocks:
            user_portfolio[u][s] = random.randint(1000, 10000)
            
    for u in hft_users:
        user_profiles[u] = 'HFT'
        cash = random.uniform(5000000.0, 20000000.0)
        user_cash[u] = cash
        initial_user_cash[u] = cash
        for s in stocks:
            user_portfolio[u][s] = random.randint(500, 5000)
            
    for u in retail_users:
        user_profiles[u] = 'RETAIL'
        cash = random.uniform(100000.0, 1000000.0)
        user_cash[u] = cash
        initial_user_cash[u] = cash
        for s in stocks:
            if random.random() > 0.3:
                user_portfolio[u][s] = random.randint(100, 1000)

    if args.out_initial_state:
        balances = {}
        for u in users:
            balances[f"{u}_Cash"] = user_cash[u]
            user_stock_val = sum(user_portfolio[u][s] * stock_prices[s] for s in stocks)
            balances[f"{u}_Stock"] = user_stock_val
        for s in stocks:
            total_issued_val = sum(user_portfolio[u][s] * stock_prices[s] for u in users)
            balances[f"{s}_Issuer"] = total_issued_val
            
        if generator:
            generator.export_initial_state(args.out_initial_state, balances, prefix="")
        else:
            with open(args.out_initial_state, "w", encoding="utf-8") as f:
                state_writer = csv.writer(f, lineterminator='\n')
                state_writer.writerow(["node_label", "initial_X"])
                for label, val in balances.items():
                    if val > 0:
                        state_writer.writerow([label, f"{val:.2f}"])

    volatility = 0.015
    
    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        daily_transactions = []
        
        if random.random() < args.external_flow_prob:
            raw_flow = np.random.normal(args.external_flow_mean, args.external_flow_std)
            flow_amt = round(raw_flow, 2)
            
            if flow_amt != 0.0:
                recip = random.choice(users)
                if flow_amt > 0:
                    user_cash[recip] = round(user_cash[recip] + flow_amt, 2)
                    tx_id = f"M_{global_trans_count:06d}"
                    daily_transactions.append([
                        tx_id, current_date.isoformat(), f"{recip}_Cash", "ACC_Input_From_Outside_Cash",
                        "CASH", f"{flow_amt:.2f}", "1.00", "External_Cash_Inflow"
                    ])
                    global_trans_count += 1
                else:
                    out_amt = min(user_cash[recip], abs(flow_amt))
                    if out_amt > 0:
                        user_cash[recip] = round(user_cash[recip] - out_amt, 2)
                        tx_id = f"M_{global_trans_count:06d}"
                        daily_transactions.append([
                            tx_id, current_date.isoformat(), "ACC_Output_To_Outside_Cash", f"{recip}_Cash",
                            "CASH", f"{out_amt:.2f}", "1.00", "External_Cash_Outflow"
                        ])
                        global_trans_count += 1

        for stock in stocks:
            shock = np.random.normal(0, volatility)
            stock_prices[stock] = max(1.0, stock_prices[stock] * (1.0 + shock))
            
            num_trades = random.randint(5, 20)
            for _ in range(num_trades):
                minute_offset = random.randint(0, 360)
                tx_time = current_date + datetime.timedelta(minutes=minute_offset)
                
                buyer, seller = random.sample(users, 2)
                
                trade_price = round(stock_prices[stock] * random.uniform(0.995, 1.005), 2)
                trade_qty = random.randint(10, 500)
                
                trade_qty = min(trade_qty, user_portfolio[seller][stock])
                
                total_cost = round(trade_qty * trade_price, 2)
                if user_cash[buyer] < total_cost:
                    if trade_price > 0:
                        trade_qty = int(user_cash[buyer] // trade_price)
                        total_cost = round(trade_qty * trade_price, 2)
                    else:
                        trade_qty = 0

                if trade_qty > 0 and total_cost > 0:
                    user_cash[buyer] = round(user_cash[buyer] - total_cost, 2)
                    user_cash[seller] = round(user_cash[seller] + total_cost, 2)
                    user_portfolio[buyer][stock] += trade_qty
                    user_portfolio[seller][stock] -= trade_qty
                    
                    tx_id = f"M_{global_trans_count:06d}"
                    daily_transactions.append([
                        tx_id, tx_time.isoformat(), f"{buyer}_Stock", f"{seller}_Stock",
                        stock, str(trade_qty), f"{trade_price:.2f}", "Normal_Trade"
                    ])
                    daily_transactions.append([
                        tx_id, tx_time.isoformat(), f"{seller}_Cash", f"{buyer}_Cash",
                        "CASH", f"{total_cost:.2f}", "1.00", "Normal_Trade"
                    ])
                    global_trans_count += 1

        if args.wash_trade_prob > 0.0 and random.random() < args.wash_trade_prob:
            w_user1, w_user2 = random.sample(users, 2)
            w_stock = random.choice(stocks)
            w_price = round(stock_prices[w_stock], 2)
            w_qty = random.randint(1000, 5000)
            w_amount = round(w_qty * w_price, 2)
            
            w_time = current_date + datetime.timedelta(hours=2)
            tx_id = f"M_{global_trans_count:06d}"
            
            user_cash[w_user1] = round(user_cash[w_user1] - w_amount, 2)
            user_cash[w_user2] = round(user_cash[w_user2] + w_amount, 2)
            user_portfolio[w_user1][w_stock] += w_qty
            user_portfolio[w_user2][w_stock] -= w_qty
            
            daily_transactions.append([
                tx_id, w_time.isoformat(), f"{w_user1}_Stock", f"{w_user2}_Stock",
                w_stock, str(w_qty), f"{w_price:.2f}", "Wash_Trade_Leg1"
            ])
            daily_transactions.append([
                tx_id, w_time.isoformat(), f"{w_user2}_Cash", f"{w_user1}_Cash",
                "CASH", f"{w_amount:.2f}", "1.00", "Wash_Trade_Leg1"
            ])
            global_trans_count += 1
            
            w_time2 = w_time + datetime.timedelta(minutes=5)
            tx_id2 = f"M_{global_trans_count:06d}"
            
            user_cash[w_user2] = round(user_cash[w_user2] - w_amount, 2)
            user_cash[w_user1] = round(user_cash[w_user1] + w_amount, 2)
            user_portfolio[w_user2][w_stock] += w_qty
            user_portfolio[w_user1][w_stock] -= w_qty
            
            daily_transactions.append([
                tx_id2, w_time2.isoformat(), f"{w_user2}_Stock", f"{w_user1}_Stock",
                w_stock, str(w_qty), f"{w_price:.2f}", "Wash_Trade_Leg2"
            ])
            daily_transactions.append([
                tx_id2, w_time2.isoformat(), f"{w_user1}_Cash", f"{w_user2}_Cash",
                "CASH", f"{w_amount:.2f}", "1.00", "Wash_Trade_Leg2"
            ])
            global_trans_count += 1

        if args.panic_dump_prob > 0.0 and random.random() < args.panic_dump_prob:
            p_stock = random.choice(stocks)
            stock_prices[p_stock] *= 0.70
            p_price = round(stock_prices[p_stock], 2)
            
            p_time = current_date + datetime.timedelta(hours=4)
            
            for retail in retail_users:
                r_qty = user_portfolio[retail][p_stock]
                if r_qty > 0:
                    r_mm = random.choice(inst_users + hft_users)
                    r_actual = int(r_qty * random.uniform(0.5, 1.0))
                    if r_actual > 0:
                        r_amount = round(r_actual * r_price, 2)
                        user_cash[r_mm] = round(user_cash[r_mm] - r_amount, 2)
                        user_cash[retail] = round(user_cash[retail] + r_amount, 2)
                        user_portfolio[r_mm][p_stock] += r_actual
                        user_portfolio[retail][p_stock] -= r_actual
                        
                        tx_id = f"M_{global_trans_count:06d}"
                        daily_transactions.append([
                            tx_id, p_time.isoformat(), f"{r_mm}_Stock", f"{retail}_Stock",
                            p_stock, str(r_actual), f"{r_price:.2f}", "Panic_Dump_Retail"
                        ])
                        daily_transactions.append([
                            tx_id, p_time.isoformat(), f"{retail}_Cash", f"{r_mm}_Cash",
                            "CASH", f"{r_amount:.2f}", "1.00", "Panic_Dump_Retail"
                        ])
                        global_trans_count += 1

        daily_transactions.sort(key=lambda x: (x[1], x[0]))
        for row in daily_transactions:
            writer.writerow(row)


class DummyMarketGenerator(BaseGenerator):
    cli_description = "TLU Open-Market Dual-Entry Transaction Generator"

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--num-users", type=int, default=50, help="Number of users (N)")
        parser.add_argument("--num-stocks", type=int, default=3, help="Number of stocks (M)")
        parser.add_argument("--wash-trade-prob", type=float, default=0.0, help="Probability of a Wash Trade event per day")
        parser.add_argument("--panic-dump-prob", type=float, default=0.0, help="Probability of a Panic Dump event per day")
        parser.add_argument("--external-flow-prob", type=float, default=0.2, help="Probability of external flow event per day")
        parser.add_argument("--external-flow-mean", type=float, default=20000000.0, help="Mean amount of cash flow")
        parser.add_argument("--external-flow-std", type=float, default=40000000.0, help="Standard deviation of cash flow")

    def generate(self, args: argparse.Namespace):
        generate_stream(args, self)

def main():
    gen = DummyMarketGenerator()
    gen.run()

if __name__ == "__main__":
    main()
