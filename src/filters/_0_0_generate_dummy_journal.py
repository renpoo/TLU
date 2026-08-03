#!/usr/bin/env python3
# ==========================================
# _0_0_generate_dummy_journal.py
# TLU System: Utility & Simulation Layer
# Category: Dummy Data Generation (Event-Driven Causal Model)
# Version: 6.0.0 (Refactored with BaseGenerator Architecture)
# ==========================================

import sys
import csv
import argparse
import random
import datetime
import numpy as np
from collections import defaultdict

from src.filters.base_generator import BaseGenerator

def create_entry(entry_id: str, date_str: str, amount: float, debit_acc: str, debit_dept: str, credit_acc: str, credit_dept: str, memo: str, unbalanced_debit: float = None) -> list:
    """Generate one double-entry bookkeeping transaction (2 rows)."""
    amount = round(amount, 2)
    debit_amt = round(unbalanced_debit, 2) if unbalanced_debit is not None else amount
    entry = []
    # Credit (Source of funds outflow)
    entry.append([entry_id, date_str, credit_acc, credit_dept, "0.0", str(amount), f"{memo}_CR"])
    # Debit (Destination of funds inflow)
    entry.append([entry_id, date_str, debit_acc, debit_dept, str(debit_amt), "0.0", f"{memo}_DR"])
    return entry

def generate_stream(args, generator: BaseGenerator = None):
    start_date = datetime.date(2020, 1, 1)
    total_days = args.months * 30 
    
    global_entry_count = 1
    event_queue = defaultdict(list)
    
    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow(["Entry_ID", "Trans_Date", "Account_Name", "Dept_Name", "Debit", "Credit", "Memo"])

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

    if args.out_initial_state:
        if generator:
            generator.export_initial_state(args.out_initial_state, balances, prefix="ACC_")
        else:
            with open(args.out_initial_state, "w", encoding="utf-8") as f:
                state_writer = csv.writer(f, lineterminator='\n')
                state_writer.writerow(["node_label", "initial_X"])
                for acc, val in balances.items():
                    if val > 0:
                        state_writer.writerow([f"ACC_{acc}", f"{val:.2f}"])

    def attempt_entry(entry_id, date_str, amount, debit_acc, debit_dept, credit_acc, credit_dept, memo, unbalanced_debit=None):
        nonlocal balances
        amount = round(amount, 2)
        
        if credit_acc in ["Cash", "Accounts_Receivable", "Inventory"]:
            if balances[credit_acc] < amount:
                amount = balances[credit_acc]
        
        if amount <= 0.01:
            return [], 0.0
            
        balances[credit_acc] -= amount
        
        eff_debit_amt = unbalanced_debit if unbalanced_debit is not None else amount
        if debit_acc in balances:
            balances[debit_acc] += eff_debit_amt
            
        return create_entry(entry_id, date_str, amount, debit_acc, debit_dept, credit_acc, credit_dept, memo, unbalanced_debit), amount

    sales_prob = getattr(args, "sales_leak_prob", 0.0)
    purchase_prob = getattr(args, "purchase_leak_prob", 0.0)
    wash_prob = getattr(args, "wash_trade_prob", 0.0)
    unbalanced_prob = getattr(args, "unbalanced_mistake_prob", 0.0)

    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        date_str = current_date.strftime("%Y-%m-%d")
        daily_entries = []
        
        # 1. Process scheduled events
        if day in event_queue:
            for event in event_queue[day]:
                entries, _ = attempt_entry(
                    f"E_{global_entry_count:06d}", date_str, event['amount'],
                    event['debit_acc'], event['debit_dept'],
                    event['credit_acc'], event['credit_dept'], event['memo']
                )
                if entries:
                    daily_entries.extend(entries)
                    global_entry_count += 1
            del event_queue[day]
            
        # 2. Daily recurring operations
        # a. Purchase Inventory (CR Cash -> DR Inventory)
        if random.random() < 0.6:
            po_amt = random.uniform(5000, 20000)
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, po_amt,
                "Inventory", "DPT_Ops", "Cash", "DPT_Admin", "Purchase_Stock"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1

        # b. Credit Purchase (AP)
        if random.random() < 0.4:
            ap_amt = random.uniform(10000, 30000)
            entries, actual_ap = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, ap_amt,
                "Inventory", "DPT_Ops", "Accounts_Payable", "DPT_Admin", "Supplier_Invoice"
            )
            if entries:
                daily_entries.extend(entries)
                global_entry_count += 1
                if random.random() >= purchase_prob:
                    pay_day = day + random.randint(15, 45)
                    event_queue[pay_day].append({
                        'amount': actual_ap,
                        'debit_acc': 'Accounts_Payable', 'debit_dept': 'DPT_Admin',
                        'credit_acc': 'Cash', 'credit_dept': 'DPT_Admin',
                        'memo': 'Pay_Supplier'
                    })

        # c. Sales (AR)
        if random.random() < 0.7:
            sale_amt = random.uniform(15000, 50000)
            entries, actual_sale = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, sale_amt,
                "Accounts_Receivable", "DPT_Sales", "Sales_Revenue", "DPT_Sales", "Customer_Invoice"
            )
            if entries:
                daily_entries.extend(entries)
                global_entry_count += 1
                cogs_amt = actual_sale * random.uniform(0.5, 0.7)
                cogs_entries, _ = attempt_entry(
                    f"E_{global_entry_count:06d}", date_str, cogs_amt,
                    "COGS", "DPT_Ops", "Inventory", "DPT_Ops", "Recognize_COGS"
                )
                if cogs_entries: daily_entries.extend(cogs_entries); global_entry_count += 1

                if random.random() >= sales_prob:
                    collect_day = day + random.randint(15, 45)
                    event_queue[collect_day].append({
                        'amount': actual_sale,
                        'debit_acc': 'Cash', 'debit_dept': 'DPT_Admin',
                        'credit_acc': 'Accounts_Receivable', 'credit_dept': 'DPT_Sales',
                        'memo': 'Collect_AR'
                    })

        # d. Operating Expenses
        if random.random() < 0.3:
            exp_amt = random.uniform(1000, 5000)
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, exp_amt,
                "Travel_Exp", "DPT_Sales", "Cash", "DPT_Admin", "Travel_Expense"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1

        # e. Monthly Payroll & Rent
        if current_date.day == 25:
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, 50000.0,
                "Payroll_Exp", "DPT_Admin", "Cash", "DPT_Admin", "Staff_Payroll"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1
            
            entries2, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, 20000.0,
                "Rent_Exp", "DPT_Admin", "Cash", "DPT_Admin", "Office_Rent"
            )
            if entries2: daily_entries.extend(entries2); global_entry_count += 1

        # f. Unbalanced Mistake Anomaly
        if unbalanced_prob > 0.0 and random.random() < unbalanced_prob:
            mistake_amt = random.uniform(1000, 10000)
            unbalanced_amt = mistake_amt * random.choice([0.5, 1.5, 2.0])
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, mistake_amt,
                "COGS", "DPT_Ops", "Cash", "DPT_Admin", "Journal_Entry_Error", unbalanced_debit=unbalanced_amt
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1

        # g. Wash Trading Anomaly
        if wash_prob > 0.0 and random.random() < wash_prob:
            wash_amount = random.uniform(50000, 200000)
            entries, wash_exec = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, wash_amount,
                "Accounts_Receivable", "DPT_Admin", "Cash", "DPT_Admin", "Wash_Funding"
            )
            if entries:
                daily_entries.extend(entries)
                global_entry_count += 1
                entries2, _ = attempt_entry(
                    f"E_{global_entry_count:06d}", date_str, wash_exec,
                    "Accounts_Receivable", "DPT_Admin", "Sales_Revenue", "DPT_Sales", "Wash_Sale"
                )
                if entries2: daily_entries.extend(entries2); global_entry_count += 1
                entries3, _ = attempt_entry(
                    f"E_{global_entry_count:06d}", date_str, wash_exec,
                    "Cash", "DPT_Admin", "Accounts_Receivable", "DPT_Admin", "Wash_Collection"
                )
                if entries3: daily_entries.extend(entries3); global_entry_count += 1

        for row in daily_entries:
            writer.writerow(row)


class DummyJournalGenerator(BaseGenerator):
    cli_description = "TLU Event-Driven SME Hub-and-Spoke Journal Generator"

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--sales-leak-prob", type=float, default=0.0, help="Accounts receivable leak probability")
        parser.add_argument("--purchase-leak-prob", type=float, default=0.0, help="Accounts payable leak probability")
        parser.add_argument("--wash-trade-prob", type=float, default=0.0, help="Wash trading probability per day")
        parser.add_argument("--unbalanced-mistake-prob", type=float, default=0.0, help="Unbalanced debit != credit error probability")

    def generate(self, args: argparse.Namespace):
        generate_stream(args, self)

def main():
    gen = DummyJournalGenerator()
    gen.run()

if __name__ == "__main__":
    main()
