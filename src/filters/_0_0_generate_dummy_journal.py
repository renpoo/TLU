#!/usr/bin/env python3
# ==========================================
# _0_0_generate_dummy_journal.py
# TLU System: Utility & Simulation Layer
# Category: Dummy Data Generation (Event-Driven Causal Model)
# Version: 3.0 (Strict SME Business Cycle & Topology)
# ==========================================

import sys
import csv
import argparse
import random
import datetime
import numpy as np
from collections import defaultdict

# --- 厳格なドメイン定義 (SME Chart of Accounts) ---
# 部門ごとに発生しうる勘定科目を縛る（構造的剛性: Stiffness の源泉）
DEPT_ACCOUNTS = {
    "DPT_Sales": ["Sales_Revenue", "Travel_Exp", "Entertainment_Exp"],
    "DPT_Ops": ["COGS", "Inventory", "Outsourcing_Exp", "Freight_Exp"],
    "DPT_Admin": ["Cash", "Accounts_Receivable", "Accounts_Payable", "Payroll_Exp", "Rent_Exp", "IT_Exp"]
}

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="TLU Event-Driven SME Journal Generator")
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
    
    # イベントキュー: { day_index: [ task_function, ... ] }
    # 未来の取引（売掛金の回収など）をスケジュールする
    event_queue = defaultdict(list)
    
    writer = csv.writer(sys.stdout)
    writer.writerow(["Entry_ID", "Trans_Date", "Account_Name", "Dept_Name", "Debit", "Credit", "Memo"])

    # --- 季節変動（サイン波）のベース ---
    # 売上は年間を通じて波がある（例：夏と冬にピーク）
    seasonal_wave = (np.sin(np.linspace(0, 4 * np.pi, total_days)) + 1) / 2 # 0.0 ~ 1.0

    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        date_str = current_date.strftime("%Y-%m-%d")
        daily_entries = []

        # --------------------------------------------------
        # 1. 予約されたイベント（過去の因果）の実行
        # --------------------------------------------------
        if day in event_queue:
            for task in event_queue[day]:
                entries, global_entry_count = task(date_str, global_entry_count)
                daily_entries.extend(entries)
            del event_queue[day]

        # --------------------------------------------------
        # 2. 売上サイクルの発生（日々の波）
        # --------------------------------------------------
        # 季節変動 + ノイズで本日の売上件数を決定
        base_sales_txns = 2 + (seasonal_wave[day] * 4) + np.random.normal(0, 1)
        sales_txns = max(0, int(base_sales_txns))
        
        for _ in range(sales_txns):
            # SMEの売上単価（対数正規分布でリアルに）
            amount = np.random.lognormal(mean=np.log(2000), sigma=0.8)
            amount = max(100.0, amount)

            # (A) 売上発生: 売掛金(Admin) / 売上高(Sales)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, amount, 
                "Accounts_Receivable", "DPT_Admin", "Sales_Revenue", "DPT_Sales", "Sales_Record"
            ))
            global_entry_count += 1
            
            # (B) 売上原価の計上（売上の約60%）: COGS(Ops) / 在庫(Ops)
            cogs_amount = amount * random.uniform(0.55, 0.65)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, cogs_amount, 
                "COGS", "DPT_Ops", "Inventory", "DPT_Ops", "COGS_Record"
            ))
            global_entry_count += 1

            # (C) 未来への因果: 30〜45日後に現金回収イベントを仕込む (これが粘性を生む)
            collection_delay = random.randint(30, 45)
            collection_day = day + collection_delay
            
            # 遅延評価のためのクロージャ
            def make_collection_task(amt):
                def collection_task(d_str, e_count):
                    ent = create_entry(
                        f"E_{e_count:06d}", d_str, amt,
                        "Cash", "DPT_Admin", "Accounts_Receivable", "DPT_Admin", "AR_Collection"
                    )
                    return ent, e_count + 1
                return collection_task
            
            event_queue[collection_day].append(make_collection_task(amount))

        # --------------------------------------------------
        # 3. 日常経費の発生
        # --------------------------------------------------
        if random.random() < 0.3: # 30%の確率で交通費発生
            amt = random.uniform(30, 150)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, amt, 
                "Travel_Exp", "DPT_Sales", "Cash", "DPT_Admin", "Travel_Reimburse"
            ))
            global_entry_count += 1

        # --------------------------------------------------
        # 4. 月末サイクルの発生（給与、家賃）
        # --------------------------------------------------
        # 毎月25日を給与日とする
        if current_date.day == 25:
            # 給与は一定額ベースに微小な残業代ノイズ
            payroll_amt = 15000 + np.random.normal(0, 500)
            daily_entries.extend(create_entry(
                f"E_{global_entry_count:06d}", date_str, payroll_amt, 
                "Payroll_Exp", "DPT_Admin", "Cash", "DPT_Admin", "Monthly_Payroll"
            ))
            global_entry_count += 1
            
            # 家賃（固定費）
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
