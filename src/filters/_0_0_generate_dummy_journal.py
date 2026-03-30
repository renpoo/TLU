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
    parser.add_argument("--months", type=int, default=12, help="生成する期間（月数）")
    parser.add_argument("--seed", type=int, default=42, help="乱数シード")
    parser.add_argument("--sales-leak", type=bool, default=False, help="売掛金が回収されない（1割の確率で）")
    parser.add_argument("--purchase-leak", type=bool, default=False, help="買掛金が支払われない（0.5割の確率で）")
    return parser

def create_entry(entry_id: str, date_str: str, amount: float, debit_acc: str, debit_dept: str, credit_acc: str, credit_dept: str, memo: str) -> list:
    """1つの複式簿記取引（2行）を生成する"""
    amount = round(amount, 2)
    entry = []
    # 貸方 (Credit: 資金の流出元)
    entry.append([entry_id, date_str, credit_acc, credit_dept, "0.0", str(amount), f"{memo}_CR"])
    # 借方 (Debit: 資金の流入先)
    entry.append([entry_id, date_str, debit_acc, debit_dept, str(amount), "0.0", f"{memo}_DR"])
    return entry

def generate_stream(args):
    start_date = datetime.date(2020, 1, 1)
    total_days = args.months * 30 
    
    global_entry_count = 1
    event_queue = defaultdict(list) # 未来のイベントをスケジュール
    
    writer = csv.writer(sys.stdout)
    writer.writerow(["Entry_ID", "Trans_Date", "Account_Name", "Dept_Name", "Debit", "Credit", "Memo"])

    # 季節変動波形（売上の波）
    seasonal_wave = (np.sin(np.linspace(0, 4 * np.pi, total_days)) + 1) / 2

    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        date_str = current_date.strftime("%Y-%m-%d")
        daily_entries = []

        # --------------------------------------------------
        # 1. イベントキューの消化（過去の因果・粘性の発現）
        # --------------------------------------------------
        if day in event_queue:
            for task in event_queue[day]:
                entries, global_entry_count = task(date_str, global_entry_count)
                daily_entries.extend(entries)
            del event_queue[day]

        # --------------------------------------------------
        # 2. 売上・回収サイクル (Cross-Dept: Sales -> Admin)
        # --------------------------------------------------
        base_sales = 2 + (seasonal_wave[day] * 3) + np.random.normal(0, 0.5)
        for _ in range(max(0, int(base_sales))):
            amount = np.random.lognormal(mean=np.log(800), sigma=0.4)
            amount = max(100.0, amount)

            # [売上発生]
            # 営業部(Sales)が売上を上げるが、債権(AR)を管理するのは本社(Admin)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, amount, 
                "Accounts_Receivable", "DPT_Admin", "Sales_Revenue", "DPT_Sales", "Sales_Record"
            ))
            global_entry_count += 1
            
            # [原価計上] (社内完結)
            cogs_amount = amount * random.uniform(0.4, 0.7)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, cogs_amount, 
                "COGS", "DPT_Ops", "Inventory", "DPT_Ops", "COGS_Record"
            ))
            global_entry_count += 1

            # [未来: 売掛金回収] 30〜90日後 (Admin内で完結)
            collection_day = day + random.randint(30, 90)
            def make_collection(amt):
                def task(d_str, e_count):
                    return create_entry(
                        f"E_{e_count:06d}", d_str, amt,
                        "Cash", "DPT_Admin", "Accounts_Receivable", "DPT_Admin", "AR_Collection"
                    ), e_count + 1
                return task

            if (args.sales_leak):
                # Sales Leakage 1: 売掛金が回収されない（1割の確率で）
                if random.random() < 0.1:
                    amount -= np.random.uniform(0, amount * 0.15)
            
            event_queue[collection_day].append(make_collection(amount))

        # --------------------------------------------------
        # 3. 購買・支払サイクル (Cross-Dept: Admin -> Ops)
        # --------------------------------------------------
        # Opsが在庫を補充するが、債務(AP)を負うのはAdmin
        if day % 7 == 0:
            purch_amount = np.random.normal(8000, 1000)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, purch_amount, 
                "Inventory", "DPT_Ops", "Accounts_Payable", "DPT_Admin", "Inventory_Purchase"
            ))
            global_entry_count += 1
            
            # [未来: 買掛金支払] 30〜90日後 (Admin内で完結)
            pay_day = day + random.randint(30, 90)
            def make_payment(amt):
                def task(d_str, e_count):
                    return create_entry(
                        f"E_{e_count:06d}", d_str, amt,
                        "Accounts_Payable", "DPT_Admin", "Cash", "DPT_Admin", "AP_Payment"
                    ), e_count + 1
                return task

            if (args.purchase_leak):
                # Purchase Leak 1: 買掛金が支払えない（0.5割の確率で）
                if random.random() < 0.05:
                    purch_amount -= np.random.uniform(0, purch_amount * 0.10)
            
            event_queue[pay_day].append(make_payment(purch_amount))

        # --------------------------------------------------
        # 4. 経費の精算 (Cross-Dept: Admin -> Sales/Ops)
        # --------------------------------------------------
        # 営業マンの交通費（Salesの経費だが、AdminのCashから出る）
        if random.random() < 0.4:
            travel_amt = random.uniform(30, 1200)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, travel_amt, 
                "Travel_Exp", "DPT_Sales", "Cash", "DPT_Admin", "Travel_Reimburse"
            ))
            global_entry_count += 1

        # --------------------------------------------------
        # 5. 月末サイクル（全社的な固定費）
        # --------------------------------------------------
        if current_date.day == 25:
            # 各部門の給与（経費は各部門につくが、支払いはすべてAdminのCash）
            # Ops部門の給与
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, 8000 + np.random.normal(0, 1000), 
                "Payroll_Exp", "DPT_Ops", "Cash", "DPT_Admin", "Payroll_Ops"
            ))
            global_entry_count += 1
            # Sales部門の給与
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, 6000 + np.random.normal(0, 1200), 
                "Payroll_Exp", "DPT_Sales", "Cash", "DPT_Admin", "Payroll_Sales"
            ))
            global_entry_count += 1
            # Admin部門自身の給与
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, 4000 + np.random.normal(0, 800), 
                "Payroll_Exp", "DPT_Admin", "Cash", "DPT_Admin", "Payroll_Admin"
            ))
            global_entry_count += 1
            
            # 本社家賃（Admin完結）
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, 5000 + np.random.normal(0, 1200),
                "Rent_Exp", "DPT_Admin", "Cash", "DPT_Admin", "Monthly_Rent"
            ))
            global_entry_count += 1

        # ストリーム出力
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
