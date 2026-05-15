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
    parser.add_argument("--unbalanced-mistake-prob", type=float, default=0.0, help="Probability of a journaling mistake where Debit != Credit")
    parser.add_argument("--out-initial-state", type=str, default="", help="Path to write the initial state (Day 0) CSV")
    return parser

def create_entry(entry_id: str, date_str: str, amount: float, debit_acc: str, debit_dept: str, credit_acc: str, credit_dept: str, memo: str, unbalanced_debit: float = None) -> list:
    """Generate one double-entry bookkeeping transaction (2 rows). (Legacy formatting only)"""
    amount = round(amount, 2)
    debit_amt = round(unbalanced_debit, 2) if unbalanced_debit is not None else amount
    entry = []
    # Credit (Source of funds outflow)
    entry.append([entry_id, date_str, credit_acc, credit_dept, "0.0", str(amount), f"{memo}_CR"])
    # Debit (Destination of funds inflow)
    entry.append([entry_id, date_str, debit_acc, debit_dept, str(debit_amt), "0.0", f"{memo}_DR"])
    return entry

def generate_stream(args):
    start_date = datetime.date(2020, 1, 1)
    total_days = args.months * 30 
    
    global_entry_count = 1
    event_queue = defaultdict(list) # Schedule future events
    
    writer = csv.writer(sys.stdout)
    writer.writerow(["Entry_ID", "Trans_Date", "Account_Name", "Dept_Name", "Debit", "Credit", "Memo"])

    # Inject Initial Capital to prevent negative Cash/Inventory in the stream
    init_date = "2020-01-01"
    init_entries = []
    
    # Define some basic initial state (balances) for Day 0 if requested
    if args.out_initial_state:
        with open(args.out_initial_state, "w", encoding="utf-8") as f:
            state_writer = csv.writer(f, lineterminator='\n')
            state_writer.writerow(["node_label", "initial_X"])
            # Assuming DPT_Admin, DPT_Sales, DPT_Ops are part of node names in the stream.
            # In TLU, typically nodes are formulated as "Account_Name_Dept_Name" or similar via the mapping.
            # We'll just write some dummy global values for the accounts themselves.
            # Usually the mapping creates nodes like "Account_Name". We will just use the Account_Name.
            # Provide a mathematically balanced opening accounting state
            balances = {
                "Cash": 500000.00,
                "Inventory": 500000.00,
                "Equity_Capital": 1000000.00,
                # Set others to 0 so they don't break mass limits but don't add false opening balances
                "Accounts_Receivable": 0.0,
                "Accounts_Payable": 0.0,
                "Sales_Revenue": 0.0,
                "COGS": 0.0,
                "Travel_Exp": 0.0,
                "Payroll_Exp": 0.0,
                "Rent_Exp": 0.0
            }
            for acc, val in balances.items():
                if val > 0:
                    state_writer.writerow([f"ACC_{acc}", f"{val:.2f}"])
    else:
        balances = {
            "Cash": 500000.00,
            "Inventory": 500000.00,
            "Equity_Capital": 1000000.00,
            "Accounts_Receivable": 0.0,
            "Accounts_Payable": 0.0,
            "Sales_Revenue": 0.0,
            "COGS": 0.0,
            "Travel_Exp": 0.0,
            "Payroll_Exp": 0.0,
            "Rent_Exp": 0.0
        }

    def attempt_entry(entry_id, date_str, amount, debit_acc, debit_dept, credit_acc, credit_dept, memo, unbalanced_debit=None):
        nonlocal balances
        amount = round(amount, 2)
        
        # Enforce mass conservation ONLY on internal physical assets.
        # External sources (Revenue, Payables/Suppliers) have infinite capacity.
        if credit_acc in ["Cash", "Accounts_Receivable", "Inventory"]:
            if balances[credit_acc] < amount:
                amount = balances[credit_acc] # Limit transaction to available mass
        
        if amount <= 0:
            return [], 0.0

        debit_amt = round(unbalanced_debit, 2) if unbalanced_debit is not None else amount
        balances[credit_acc] -= amount
        balances[debit_acc] += debit_amt

        entry = create_entry(entry_id, date_str, amount, debit_acc, debit_dept, credit_acc, credit_dept, memo, unbalanced_debit)
        return entry, amount

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
            entries, exec_amt = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, amount, 
                "Accounts_Receivable", "DPT_Admin", "Sales_Revenue", "DPT_Sales", "Sales_Record"
            )
            if entries:
                daily_entries.extend(entries)
                global_entry_count += 1
            
            # [Cost of goods sold recorded] (internal)
            cogs_amount = exec_amt * random.uniform(0.4, 0.7)
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, cogs_amount, 
                "COGS", "DPT_Ops", "Inventory", "DPT_Ops", "COGS_Record"
            )
            if entries:
                daily_entries.extend(entries)
                global_entry_count += 1

            # [Future: Accounts_Receivable collection] 30-90 days later (completed within Admin)
            collection_day = day + random.randint(30, 90)
            
            # Sales Leakage / Embezzlement
            # Cash is stolen during collection. The accounts receivable is credited (reduced), 
            # but the cash is never debited (never arrives). This violates mass conservation.
            stolen_from_sales = 0.0
            if args.sales_leak_prob > 0.0 and random.random() < args.sales_leak_prob:
                stolen_from_sales = amount * random.uniform(0.1, 0.5)
                amount -= stolen_from_sales
                
                # Unbalanced entry: Credit Accounts_Receivable, but Debit=0.0 (Money disappears into the void)
                entries, stolen_amt = attempt_entry(
                    f"E_{global_entry_count:06d}", date_str, stolen_from_sales,
                    "Cash", "DPT_Admin", "Accounts_Receivable", "DPT_Admin", "Embezzlement_Leak",
                    unbalanced_debit=0.0
                )
                if entries:
                    daily_entries.extend(entries)
                    global_entry_count += 1
                amount -= stolen_amt

            def make_collection(amt):
                def task(d_str, e_count):
                    unbalanced_debit = None
                    if args.unbalanced_mistake_prob > 0.0 and random.random() < args.unbalanced_mistake_prob:
                        unbalanced_debit = amt * random.uniform(0.0, 0.9) # Mistake leak

                    entries, _ = attempt_entry(
                        f"E_{e_count:06d}", d_str, amt,
                        "Cash", "DPT_Admin", "Accounts_Receivable", "DPT_Admin", "AR_Collection",
                        unbalanced_debit=unbalanced_debit
                    )
                    if entries:
                        return entries, e_count + 1
                    return [], e_count
                return task

            if amount > 0:
                event_queue[collection_day].append(make_collection(amount))

        # --------------------------------------------------
        # 3. Purchase and payment cycle (Cross-Dept: Admin -> Ops)
        # --------------------------------------------------
        # Ops replenishes inventory, but accounts payable (AP) are held by Admin
        if day % 7 == 0:
            purch_amount = np.random.normal(12000, 1500)
            entries, exec_purch = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, purch_amount, 
                "Inventory", "DPT_Ops", "Accounts_Payable", "DPT_Admin", "Inventory_Purchase"
            )
            if entries:
                daily_entries.extend(entries)
                global_entry_count += 1
            purch_amount = exec_purch
            
            # [Future: AP payment] 30-90 days later (completed within Admin)
            pay_day = day + random.randint(30, 90)
            
            # Purchase Leakage / Embezzlement
            # Cash is withdrawn for payment, but the Accounts Payable is not cleared (money stolen).
            stolen_from_purchases = 0.0
            if args.purchase_leak_prob > 0.0 and random.random() < args.purchase_leak_prob:
                stolen_from_purchases = purch_amount * random.uniform(0.1, 0.5)
                purch_amount -= stolen_from_purchases
                
                # Unbalanced entry: Credit Cash (money leaves), but Debit=0.0 (AP is not reduced)
                entries, stolen_amt = attempt_entry(
                    f"E_{global_entry_count:06d}", date_str, stolen_from_purchases,
                    "Accounts_Payable", "DPT_Admin", "Cash", "DPT_Admin", "Embezzlement_Leak",
                    unbalanced_debit=0.0
                )
                if entries:
                    daily_entries.extend(entries)
                    global_entry_count += 1
                purch_amount -= stolen_amt

            def make_payment(amt):
                def task(d_str, e_count):
                    entries, _ = attempt_entry(
                        f"E_{e_count:06d}", d_str, amt,
                        "Accounts_Payable", "DPT_Admin", "Cash", "DPT_Admin", "AP_Payment"
                    )
                    if entries:
                        return entries, e_count + 1
                    return [], e_count
                return task

            if purch_amount > 0:
                event_queue[pay_day].append(make_payment(purch_amount))

        # --------------------------------------------------
        # 4. Expense reimbursement (Cross-Dept: Admin -> Sales/Ops)
        # --------------------------------------------------
        # Salesperson travel expenses (Sales expense, paid from Admin Cash)
        if random.random() < 0.4:
            travel_amt = random.uniform(30, 1200)
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, travel_amt, 
                "Travel_Exp", "DPT_Sales", "Cash", "DPT_Admin", "Travel_Reimburse"
            )
            if entries:
                daily_entries.extend(entries)
                global_entry_count += 1

        # --------------------------------------------------
        # 5. Month-end cycle (company-wide fixed costs)
        # --------------------------------------------------
        if current_date.day == 25:
            # Department salaries (expense per dept, paid from Admin Cash)
            # Ops department salary
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, 8000 + np.random.normal(0, 1000), 
                "Payroll_Exp", "DPT_Ops", "Cash", "DPT_Admin", "Payroll_Ops"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1
            # Sales department salary
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, 6000 + np.random.normal(0, 1200), 
                "Payroll_Exp", "DPT_Sales", "Cash", "DPT_Admin", "Payroll_Sales"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1
            # Admin department salary
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, 4000 + np.random.normal(0, 800), 
                "Payroll_Exp", "DPT_Admin", "Cash", "DPT_Admin", "Payroll_Admin"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1
            
            # Office rent (completed within Admin)
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, 5000 + np.random.normal(0, 1200),
                "Rent_Exp", "DPT_Admin", "Cash", "DPT_Admin", "Monthly_Rent"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1
        # --------------------------------------------------
        # 6. Anomaly Injection: Wash Trading (Round-tripping / Kiting)
        # --------------------------------------------------
        if args.wash_trade_prob > 0.0 and random.random() < args.wash_trade_prob:
            # Massive volume to strongly trigger the topological spectral radius
            wash_amount = np.random.normal(50000, 5000)
            wash_amount = max(20000.0, wash_amount)
            
            # Step 1: Fund the shell company secretly (CR Cash -> DR Accounts_Receivable)
            entries, wash_exec = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, wash_amount,
                "Accounts_Receivable", "DPT_Admin", "Cash", "DPT_Admin", "Wash_Funding"
            )
            if entries:
                daily_entries.extend(entries)
                global_entry_count += 1
                
                # Step 2: Fake Sale to the shell company (CR Sales_Revenue -> DR Accounts_Receivable)
                entries2, _ = attempt_entry(
                    f"E_{global_entry_count:06d}", date_str, wash_exec,
                    "Accounts_Receivable", "DPT_Admin", "Sales_Revenue", "DPT_Sales", "Wash_Sale"
                )
                if entries2: daily_entries.extend(entries2); global_entry_count += 1
                
                # Step 3: Shell company pays using the exact funded cash (CR Accounts_Receivable -> DR Cash)
                entries3, _ = attempt_entry(
                    f"E_{global_entry_count:06d}", date_str, wash_exec,
                    "Cash", "DPT_Admin", "Accounts_Receivable", "DPT_Admin", "Wash_Collection"
                )
                if entries3: daily_entries.extend(entries3); global_entry_count += 1

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
