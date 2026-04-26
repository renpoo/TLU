#!/usr/bin/env python3
# ==========================================
# _0_0_generate_dummy_journal.py
# TLU System: Utility & Simulation Layer
# Category: Dummy Data Generation (Event-Driven Causal Model)
# Version: 5.0 (Hub-and-Spoke / Centralized Treasury Model)
# ==========================================

import sys
import csv
import argparse
import random
import datetime
import numpy as np
from collections import defaultdict

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="TLU Event-Driven SME Hub-and-Spoke Journal Generator")
    parser.add_argument("--months", type=int, default=12, help="Period to generate (in months)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--sales-leak-prob", type=float, default=0.0, help="Accounts receivable not collected (with probability args.sales_leak_prob)")
    parser.add_argument("--purchase-leak-prob", type=float, default=0.0, help="Accounts payable not paid (with probability args.purchase_leak_prob)")
    parser.add_argument("--wash-trade-prob", type=float, default=0.0, help="Probability of triggering a Wash Trading (Round-tripping) cycle per day")
    return parser

def create_entry(entry_id: str, date_str: str, amount: float, debit_acc: str, debit_dept: str, credit_acc: str, credit_dept: str, memo: str) -> list:
    """Generate one double-entry bookkeeping transaction (2 rows)"""
    amount = round(amount, 2)
    entry = []
    # Credit (Source of funds outflow)
    entry.append([entry_id, date_str, credit_acc, credit_dept, "0.0", str(amount), f"{memo}_CR"])
    # Debit (Destination of funds inflow)
    entry.append([entry_id, date_str, debit_acc, debit_dept, str(amount), "0.0", f"{memo}_DR"])
    return entry

def generate_stream(args):
    start_date = datetime.date(2020, 1, 1)
    total_days = args.months * 30 
    
    global_entry_count = 1
    event_queue = defaultdict(list) # Schedule future events
    
    writer = csv.writer(sys.stdout)
    writer.writerow(["Entry_ID", "Trans_Date", "Account_Name", "Dept_Name", "Debit", "Credit", "Memo"])

    # Seasonal fluctuation wave (sales wave)
    seasonal_wave = (np.sin(np.linspace(0, 4 * np.pi, total_days)) + 1) / 2

    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        date_str = current_date.strftime("%Y-%m-%d")
        daily_entries = []

        # --------------------------------------------------
        # 1. Process event queue (manifestation of past causality and viscosity)
        # --------------------------------------------------
        if day in event_queue:
            for task in event_queue[day]:
                entries, global_entry_count = task(date_str, global_entry_count)
                daily_entries.extend(entries)
            del event_queue[day]

        # --------------------------------------------------
        # 2. Sales and collection cycle (Cross-Dept: Sales -> Admin)
        # --------------------------------------------------
        base_sales = 2 + (seasonal_wave[day] * 3) + np.random.normal(0, 0.5)
        for _ in range(max(0, int(base_sales))):
            amount = np.random.lognormal(mean=np.log(800), sigma=0.4)
            amount = max(100.0, amount)

            # [Sales generated]
            # Sales department generates sales, but accounts receivable (AR) are managed by Admin
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, amount, 
                "Accounts_Receivable", "DPT_Admin", "Sales_Revenue", "DPT_Sales", "Sales_Record"
            ))
            global_entry_count += 1
            
            # [Cost of goods sold recorded] (internal)
            cogs_amount = amount * random.uniform(0.4, 0.7)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, cogs_amount, 
                "COGS", "DPT_Ops", "Inventory", "DPT_Ops", "COGS_Record"
            ))
            global_entry_count += 1

            # [Future: AR collection] 30-90 days later (completed within Admin)
            collection_day = day + random.randint(30, 90)
            def make_collection(amt):
                def task(d_str, e_count):
                    return create_entry(
                        f"E_{e_count:06d}", d_str, amt,
                        "Cash", "DPT_Admin", "Accounts_Receivable", "DPT_Admin", "AR_Collection"
                    ), e_count + 1
                return task

            if (args.sales_leak_prob > 0.00):
                # Sales Leakage 1: AR not collected (with probability args.sales_leak_prob)
                if random.random() < args.sales_leak_prob:
                    amount -= np.random.uniform(0, amount * 0.10)
            
            event_queue[collection_day].append(make_collection(amount))

        # --------------------------------------------------
        # 3. Purchase and payment cycle (Cross-Dept: Admin -> Ops)
        # --------------------------------------------------
        # Ops replenishes inventory, but accounts payable (AP) are held by Admin
        if day % 7 == 0:
            purch_amount = np.random.normal(8000, 1000)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, purch_amount, 
                "Inventory", "DPT_Ops", "Accounts_Payable", "DPT_Admin", "Inventory_Purchase"
            ))
            global_entry_count += 1
            
            # [Future: AP payment] 30-90 days later (completed within Admin)
            pay_day = day + random.randint(30, 90)
            def make_payment(amt):
                def task(d_str, e_count):
                    return create_entry(
                        f"E_{e_count:06d}", d_str, amt,
                        "Accounts_Payable", "DPT_Admin", "Cash", "DPT_Admin", "AP_Payment"
                    ), e_count + 1
                return task

            if (args.purchase_leak_prob > 0.00):
                # Purchase Leak 1: AP cannot be paid (with probability args.purchase_leak_prob)
                if random.random() < args.purchase_leak_prob:
                    purch_amount -= np.random.uniform(0, purch_amount * 0.05)
            
            event_queue[pay_day].append(make_payment(purch_amount))

        # --------------------------------------------------
        # 4. Expense reimbursement (Cross-Dept: Admin -> Sales/Ops)
        # --------------------------------------------------
        # Salesperson travel expenses (Sales expense, paid from Admin Cash)
        if random.random() < 0.4:
            travel_amt = random.uniform(30, 1200)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, travel_amt, 
                "Travel_Exp", "DPT_Sales", "Cash", "DPT_Admin", "Travel_Reimburse"
            ))
            global_entry_count += 1

        # --------------------------------------------------
        # 5. Month-end cycle (company-wide fixed costs)
        # --------------------------------------------------
        if current_date.day == 25:
            # Department salaries (expense per dept, paid from Admin Cash)
            # Ops department salary
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, 8000 + np.random.normal(0, 1000), 
                "Payroll_Exp", "DPT_Ops", "Cash", "DPT_Admin", "Payroll_Ops"
            ))
            global_entry_count += 1
            # Sales department salary
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, 6000 + np.random.normal(0, 1200), 
                "Payroll_Exp", "DPT_Sales", "Cash", "DPT_Admin", "Payroll_Sales"
            ))
            global_entry_count += 1
            # Admin department salary
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, 4000 + np.random.normal(0, 800), 
                "Payroll_Exp", "DPT_Admin", "Cash", "DPT_Admin", "Payroll_Admin"
            ))
            global_entry_count += 1
            
            # Office rent (completed within Admin)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, 5000 + np.random.normal(0, 1200),
                "Rent_Exp", "DPT_Admin", "Cash", "DPT_Admin", "Monthly_Rent"
            ))
            global_entry_count += 1
        # --------------------------------------------------
        # 6. Anomaly Injection: Wash Trading (Round-tripping)
        # --------------------------------------------------
        if args.wash_trade_prob > 0.0 and random.random() < args.wash_trade_prob:
            wash_amount = np.random.normal(15000, 3000)
            wash_amount = max(5000.0, wash_amount)
            
            # Step 1: Fund the shell company (CR Cash -> DR Accounts_Receivable)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, wash_amount,
                "Accounts_Receivable", "DPT_Admin", "Cash", "DPT_Admin", "Wash_Funding"
            ))
            global_entry_count += 1
            
            # Step 2: Fake Sale to the shell company (CR Sales_Revenue -> DR Accounts_Receivable)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, wash_amount,
                "Accounts_Receivable", "DPT_Admin", "Sales_Revenue", "DPT_Sales", "Wash_Sale"
            ))
            global_entry_count += 1
            
            # Step 3: Shell company pays using the funded cash (CR Accounts_Receivable -> DR Cash)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, wash_amount,
                "Cash", "DPT_Admin", "Accounts_Receivable", "DPT_Admin", "Wash_Collection"
            ))
            global_entry_count += 1

        # Stream output
        for row in daily_entries:
            writer.writerow(row)

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    generate_stream(args)

if __name__ == "__main__":
    main()
