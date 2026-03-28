#!/usr/bin/env python3
# ==========================================
# _0_0_generate_dummy_journal.py
# TLU System: Utility & Simulation Layer
# Category: Dummy Data Generation & Signal Synthesis
# Version: SME Model (Small to Medium Enterprise)
# ==========================================

import sys
import csv
import argparse
import random
import datetime
import numpy as np

# --- 定数・ドメイン辞書 ---
# 中小企業(SME)レヴェルに合わせたシンプルな名称
ACCOUNTS = {
    "Hubs": ["Cash", "Accounts_Payable", "Sales_Revenue"],
    "Sparse": ["Marketing_Exp", "Travel_Exp", "Petty_Cash", "Legal_Fees", "IT_Exp"]
}
DEPARTMENTS = ["DPT_Sales", "DPT_Operations", "DPT_Admin"]

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="TLU SME JOURNAL Generator (SDL_4_1)")
    parser.add_argument("--mode", type=str, choices=["null", "real"], default="real",
                        help="null: 一様乱数(偽陽性テスト用), real: べき分布・因果・遅れを含むSMEモデル")
    parser.add_argument("--months", type=int, default=24, help="生成する期間（月数）")
    parser.add_argument("--inject_anomalies", action="store_true", help="後半期間に意図的な異常を混入するか")
    parser.add_argument("--seed", type=int, default=42, help="再現性のための乱数シード")
    return parser

# ---------------------------------------------------------
# [純粋数学・信号生成モデル] Pure Signal Generators
# ---------------------------------------------------------

def generate_power_law_amount(alpha: float = 2.5, min_val: float = 10.0) -> float:
    """パレート分布(べき分布)に基づく金額生成
    ※ SMEモデル: alphaを高く(2.5~3.0)設定し、極端な巨額取引を抑制する
    """
    return round((np.random.pareto(alpha) + 1) * min_val, 2)

def generate_pink_noise(length: int) -> np.ndarray:
    """1/fゆらぎ（Pink Noise）の簡易生成 (トレンド+短期揺らぎ用)"""
    white = np.random.normal(0, 1, length)
    pink = np.zeros(length)
    for i in range(1, length):
        pink[i] = 0.85 * pink[i-1] + white[i] # SMEはやや自己相関(慣性)が低め
    return pink - np.min(pink) + 0.1 

# ---------------------------------------------------------
# [ビジネスロジック・ジェネレータ] Journal Entry Creators
# ---------------------------------------------------------

def create_balanced_entry(entry_id: str, date_str: str, amount: float, src_acc: str, tgt_acc: str, memo: str, anomaly_leak: bool = False) -> list:
    """
    1つの取引（Entry_ID）につき、貸借バランスの取れた2行（またはバランスの崩れた異常行）を生成する。
    """
    credit_amount = amount
    debit_amount = amount * 0.9 if anomaly_leak else amount # Leakの規模も10%程度に縮小

    entry = []
    # 行1: 貸方 (資金の流出元)
    entry.append([entry_id, date_str, src_acc, random.choice(DEPARTMENTS), "0.0", str(credit_amount), f"{memo}_CR"])
    # 行2: 借方 (資金の流入先)
    entry.append([entry_id, date_str, tgt_acc, random.choice(DEPARTMENTS), str(debit_amount), "0.0", f"{memo}_DR"])
    return entry

def generate_stream(args):
    """メインのストリーム生成オーケストレーション"""
    start_date = datetime.date(2024, 1, 1)
    total_days = args.months * 30 
    
    # SMEのマーケティング投資波形 (ベースを小さく)
    base_mkt_signal = generate_pink_noise(total_days) * 15
    lag_days = 45 # 効果が出るまでのタイムラグもSMEは短め(45日)に設定
    
    journalobal_entry_count = 1
    
    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        date_str = current_date.strftime("%Y-%m-%d")
        
        progress = day / total_days
        is_anomaly_period = args.inject_anomalies and progress > 0.6

        daily_entries = []

        if args.mode == "null":
            # Baseline (Null) Mode
            txns = np.random.poisson(3)
            for _ in range(txns):
                amount = round(random.uniform(10, 300), 2)
                src = random.choice(ACCOUNTS["Hubs"] + ACCOUNTS["Sparse"])
                tgt = random.choice(ACCOUNTS["Hubs"] + ACCOUNTS["Sparse"])
                daily_entries.extend(create_balanced_entry(
                    f"E_{journalobal_entry_count:06d}", date_str, amount, src, tgt, "Null_Txn"
                ))
                journalobal_entry_count += 1
                
        elif args.mode == "real":
            # Real Business Mode (SME Scale)
            
            # --- パターンA: 因果的遅れ (Marketing -> Sales) ---
            mkt_vol = int(base_mkt_signal[day])
            if mkt_vol > 0:
                amount = generate_power_law_amount(alpha=2.5, min_val=50.0)
                daily_entries.extend(create_balanced_entry(
                    f"E_{journalobal_entry_count:06d}", date_str, amount, "Cash", "Marketing_Exp", "Mkt_Invest"
                ))
                journalobal_entry_count += 1
                
            if day >= lag_days:
                lagged_sales_drive = int(base_mkt_signal[day - lag_days] * 1.2) 
                if lagged_sales_drive > 0:
                    amount = generate_power_law_amount(alpha=2.2, min_val=150.0)
                    daily_entries.extend(create_balanced_entry(
                        f"E_{journalobal_entry_count:06d}", date_str, amount, "Sales_Revenue", "Cash", "Lagged_Sales"
                    ))
                    journalobal_entry_count += 1

            # --- パターンB: 日常取引 (SMEは取引数が少なめ) ---
            txns = np.random.poisson(5) # 平均5件/日
            for _ in range(txns):
                amount = generate_power_law_amount(alpha=3.0, min_val=10.0)
                src = random.choice(ACCOUNTS["Hubs"])
                tgt = random.choice(ACCOUNTS["Sparse"])
                
                # --- 異常レシピ注入 ---
                is_leak = False
                if is_anomaly_period and random.random() < 0.03: # 異常発生確率も少し下げる
                    anomaly_type = random.choice(["z_spike", "drift", "leak"])
                    
                    if anomaly_type == "z_spike":
                        # SMEのスパイクは10倍程度
                        amount *= 10.0
                        memo = "ANOMALY_SPIKE"
                    elif anomaly_type == "drift":
                        tgt = random.choice(ACCOUNTS["Hubs"])
                        memo = "ANOMALY_DRIFT"
                    elif anomaly_type == "leak":
                        is_leak = True
                        memo = "ANOMALY_LEAK"
                else:
                    memo = "Daily_Ops"

                daily_entries.extend(create_balanced_entry(
                    f"E_{journalobal_entry_count:06d}", date_str, amount, src, tgt, memo, is_leak
                ))
                journalobal_entry_count += 1

        writer = csv.writer(sys.stdout)
        for row in daily_entries:
            writer.writerow(row)

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    random.seed(args.seed)
    np.random.seed(args.seed)

    writer = csv.writer(sys.stdout)
    writer.writerow(["Entry_ID", "Trans_Date", "Account_Name", "Dept_Name", "Debit", "Credit", "Memo"])

    generate_stream(args)

if __name__ == "__main__":
    main()
