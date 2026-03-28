#!/usr/bin/env python3
# ==========================================
# _0_0_generate_dummy_journal.py
# TLU System: Utility & Simulation Layer
# Category: Dummy Data Generation (Event-Driven Causal Model)
# Version: 4.0 (Complex Network & Stable Hub SME Model)
# ==========================================

import sys
import csv
import argparse
import random
import datetime
import numpy as np
from collections import defaultdict

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="TLU Event-Driven SME Complex Journal Generator")
    parser.add_argument("--months", type=int, default=24, help="生成する期間（月数）")
    parser.add_argument("--seed", type=int, default=42, help="乱数シード")
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
    start_date = datetime.date(2024, 1, 1)
    total_days = args.months * 30 
    
    global_entry_count = 1
    event_queue = defaultdict(list) # 未来のイベントをスケジュール
    
    writer = csv.writer(sys.stdout)
    writer.writerow(["Entry_ID", "Trans_Date", "Account_Name", "Dept_Name", "Debit", "Credit", "Memo"])

    # 季節変動波形
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
        # 2. 売上・回収サイクル (Revenue Cycle)
        # --------------------------------------------------
        base_sales = 2 + (seasonal_wave[day] * 3) + np.random.normal(0, 0.5)
        for _ in range(max(0, int(base_sales))):
            # Adminのスパイクを抑えるため、対数正規分布の分散(sigma)を小さく(0.4)設定
            amount = np.random.lognormal(mean=np.log(1500), sigma=0.4)
            amount = max(100.0, amount)

            # [売上発生] AR(Admin) / Sales(Sales)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, amount, 
                "Accounts_Receivable", "DPT_Admin", "Sales_Revenue", "DPT_Sales", "Sales_Record"
            ))
            global_entry_count += 1
            
            # [原価計上] COGS(Ops) / Inventory(Ops)
            cogs_amount = amount * random.uniform(0.5, 0.6)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, cogs_amount, 
                "COGS", "DPT_Ops", "Inventory", "DPT_Ops", "COGS_Record"
            ))
            global_entry_count += 1

            # [未来: 売掛金回収] 30〜45日後 Cash(Admin) / AR(Admin)
            collection_day = day + random.randint(30, 45)
            def make_collection(amt):
                def task(d_str, e_count):
                    return create_entry(
                        f"E_{e_count:06d}", d_str, amt,
                        "Cash", "DPT_Admin", "Accounts_Receivable", "DPT_Admin", "AR_Collection"
                    ), e_count + 1
                return task
            event_queue[collection_day].append(make_collection(amount))

        # --------------------------------------------------
        # 3. 購買・支払サイクル (Purchasing Cycle) - 孤島を繋ぐ架け橋
        # --------------------------------------------------
        # 在庫が減った分を定期的に補充する（週に1回程度）
        if day % 7 == 0:
            purch_amount = np.random.normal(8000, 1000) # 変動は小さく
            # [仕入発生] Inventory(Ops) / AP(Admin)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, purch_amount, 
                "Inventory", "DPT_Ops", "Accounts_Payable", "DPT_Admin", "Inventory_Purchase"
            ))
            global_entry_count += 1
            
            # [未来: 買掛金支払] 30日後 AP(Admin) / Cash(Admin)
            pay_day = day + 30
            def make_payment(amt):
                def task(d_str, e_count):
                    return create_entry(
                        f"E_{e_count:06d}", d_str, amt,
                        "Accounts_Payable", "DPT_Admin", "Cash", "DPT_Admin", "AP_Payment"
                    ), e_count + 1
                return task
            event_queue[pay_day].append(make_payment(purch_amount))

        # --------------------------------------------------
        # 4. 経費・バイパス回路 (Prepaid & Depreciation)
        # --------------------------------------------------
        # 月初に大きな前払費用を払い、各部門へ配賦する（クロスエッジの形成）
        if current_date.day == 1:
            # サーバー代年間一括払い等: Prepaid_Exp(Admin) / Cash(Admin)
            prepaid_amt = 12000
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, prepaid_amt, 
                "Prepaid_Exp", "DPT_Admin", "Cash", "DPT_Admin", "Prepaid_IT_Annual"
            ))
            global_entry_count += 1
            
            # 毎月の償却・配賦 (1/12ずつ)
            amort_amt = prepaid_amt / 12
            # Sales部への配賦: IT_Exp(Sales) / Prepaid_Exp(Admin)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, amort_amt * 0.4, 
                "IT_Exp", "DPT_Sales", "Prepaid_Exp", "DPT_Admin", "IT_Amortization"
            ))
            global_entry_count += 1
            # Ops部への配賦: IT_Exp(Ops) / Prepaid_Exp(Admin)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, amort_amt * 0.6, 
                "IT_Exp", "DPT_Ops", "Prepaid_Exp", "DPT_Admin", "IT_Amortization"
            ))
            global_entry_count += 1

        # --------------------------------------------------
        # 5. 月末サイクル（Adminの固定費・変動極小化）
        # --------------------------------------------------
        if current_date.day == 25:
            # 給与（極めて安定した固定費）
            payroll_amt = 12000 + np.random.normal(0, 100)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, payroll_amt, 
                "Payroll_Exp", "DPT_Admin", "Cash", "DPT_Admin", "Monthly_Payroll"
            ))
            global_entry_count += 1
            
            # 家賃（完全な固定費）
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, 3000, 
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
