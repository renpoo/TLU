#!/usr/bin/env python3
# ==========================================
# 0_0_generate_dummy_journal.py
# TLU System: Utility & Simulation Layer
# Category: Dummy Data Generation & Signal Synthesis
# Version: Draft (SDL_4_1 Compliant)
# ==========================================

import sys
import csv
import argparse
import random
import datetime
import numpy as np

# --- 定数・ドメイン辞書 ---
# 空白を排除した厳密な文字列ラベル
ACCOUNTS = {
    "Hubs": ["Cash_HQ", "Accounts_Payable_Main", "Sales_Revenue_Global"],
    "Sparse": ["Marketing_Exp_Digital", "Travel_Exp_Domestic", "Petty_Cash", "Legal_Fees", "IT_Cloud_Infra"]
}
DEPARTMENTS = ["DPT_Sales", "DPT_Operations", "DPT_IT", "DPT_HR", "DPT_Marketing", "DPT_Admin"]

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="TLU Advanced JOURNAL Generator (SDL_4_1)")
    parser.add_argument("--mode", type=str, choices=["null", "real"], default="real",
                        help="null: 一様乱数(偽陽性テスト用), real: べき分布・因果・遅れを含む現実モデル")
    parser.add_argument("--months", type=int, default=24, help="生成する期間（月数）")
    parser.add_argument("--inject_anomalies", action="store_true", help="後半期間に意図的な異常を混入するか")
    parser.add_argument("--seed", type=int, default=42, help="再現性のための乱数シード")
    return parser

# ---------------------------------------------------------
# [純粋数学・信号生成モデル] Pure Signal Generators
# ---------------------------------------------------------

def generate_power_law_amount(alpha: float = 1.5, min_val: float = 10.0) -> float:
    """パレート分布(べき分布)に基づく金額生成: 少額多数、高額少数"""
    # np.random.pareto は 1/(x+1)^a の形なので、スケールを調整する
    return round((np.random.pareto(alpha) + 1) * min_val, 2)

def generate_pink_noise(length: int) -> np.ndarray:
    """1/fゆらぎ（Pink Noise）の簡易生成 (トレンド+短期揺らぎ用)"""
    # 簡略化のため、ホワイトノイズを積分しつつ減衰させるブラウン運動の変種として実装
    white = np.random.normal(0, 1, length)
    pink = np.zeros(length)
    for i in range(1, length):
        pink[i] = 0.9 * pink[i-1] + white[i] # 簡易的AR(1)過程
    return pink - np.min(pink) + 0.1 # 正の数にシフト

# ---------------------------------------------------------
# [ビジネスロジック・ジェネレータ] Journal Entry Creators
# ---------------------------------------------------------

def create_balanced_entry(entry_id: str, date_str: str, amount: float, src_acc: str, tgt_acc: str, memo: str, anomaly_leak: bool = False) -> list:
    """
    1つの取引（Entry_ID）につき、貸借バランスの取れた2行（またはバランスの崩れた異常行）を生成する。
    - 資金の流出元（Source） = 貸方（Credit）
    - 資金の流入先（Target） = 借方（Debit）
    """
    credit_amount = amount
    # 異常レシピ3: Conservation Residual (Leak) - バランスを崩す毒
    debit_amount = amount * 0.8 if anomaly_leak else amount

    entry = []
    # 行1: 貸方 (資金の流出元)
    entry.append([entry_id, date_str, src_acc, random.choice(DEPARTMENTS), "0.0", str(credit_amount), f"{memo}_CR"])
    # 行2: 借方 (資金の流入先)
    entry.append([entry_id, date_str, tgt_acc, random.choice(DEPARTMENTS), str(debit_amount), "0.0", f"{memo}_DR"])
    return entry

def generate_stream(args):
    """メインのストリーム生成オーケストレーション"""
    start_date = datetime.date(2024, 1, 1)
    total_days = args.months * 30 # 簡易計算
    
    # 1. 事前シグナル生成 (Causal Time Lag の準備)
    # 例: マーケティング費用の波形を生成し、3ヶ月(90日)遅れで売上に転写する
    base_mkt_signal = generate_pink_noise(total_days) * 50
    lag_days = 90
    
    journalobal_entry_count = 1
    
    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        date_str = current_date.strftime("%Y-%m-%d")
        
        # 進行度 (0.0 ~ 1.0)
        progress = day / total_days
        # 後半 (progress > 0.6) かつフラグONなら異常モード発動
        is_anomaly_period = args.inject_anomalies and progress > 0.6

        daily_entries = []

        if args.mode == "null":
            # Baseline (Null) Mode: ホワイトノイズと一様分布
            txns = np.random.poisson(5)
            for _ in range(txns):
                amount = round(random.uniform(10, 1000), 2)
                src = random.choice(ACCOUNTS["Hubs"] + ACCOUNTS["Sparse"])
                tgt = random.choice(ACCOUNTS["Hubs"] + ACCOUNTS["Sparse"])
                daily_entries.extend(create_balanced_entry(
                    f"E_{journalobal_entry_count:06d}", date_str, amount, src, tgt, "Null_Txn"
                ))
                journalobal_entry_count += 1
                
        elif args.mode == "real":
            # Real Business Mode
            
            # --- パターンA: 因果的遅れ (Marketing -> Sales) ---
            mkt_vol = int(base_mkt_signal[day])
            if mkt_vol > 0:
                amount = generate_power_law_amount(alpha=1.5, min_val=100.0)
                daily_entries.extend(create_balanced_entry(
                    f"E_{journalobal_entry_count:06d}", date_str, amount, "Cash_HQ", "Marketing_Exp_Digital", "Mkt_Invest"
                ))
                journalobal_entry_count += 1
                
            # 90日前のマーケティング投資が今日の売上をドライブする（相互相関テスト用）
            if day >= lag_days:
                lagged_sales_drive = int(base_mkt_signal[day - lag_days] * 1.5) # 効果を増幅
                if lagged_sales_drive > 0:
                    amount = generate_power_law_amount(alpha=1.2, min_val=500.0)
                    daily_entries.extend(create_balanced_entry(
                        f"E_{journalobal_entry_count:06d}", date_str, amount, "Sales_Revenue_Global", "Cash_HQ", "Lagged_Sales"
                    ))
                    journalobal_entry_count += 1

            # --- パターンB: スケールフリーな日常取引 (少額多数) ---
            txns = np.random.poisson(10)
            for _ in range(txns):
                amount = generate_power_law_amount(alpha=2.0, min_val=10.0)
                # Hub -> Sparse への資金移動が主
                src = random.choice(ACCOUNTS["Hubs"])
                tgt = random.choice(ACCOUNTS["Sparse"])
                
                # --- 異常レシピ注入 ---
                is_leak = False
                if is_anomaly_period and random.random() < 0.05:
                    anomaly_type = random.choice(["z_spike", "drift", "leak"])
                    
                    if anomaly_type == "z_spike":
                        # 異常レシピ1: Z-score Spike (3シグマ超)
                        amount *= 50.0
                        memo = "ANOMALY_SPIKE"
                    elif anomaly_type == "drift":
                        # 異常レシピ2: KL Divergence (構造的ドリフト)
                        # Hub同士など、通常あり得ない経路への大量資金移動
                        tgt = random.choice(ACCOUNTS["Hubs"])
                        memo = "ANOMALY_DRIFT"
                    elif anomaly_type == "leak":
                        # 異常レシピ3: Conservation Residual (貸借不一致の漏電)
                        is_leak = True
                        memo = "ANOMALY_LEAK"
                else:
                    memo = "Daily_Ops"

                daily_entries.extend(create_balanced_entry(
                    f"E_{journalobal_entry_count:06d}", date_str, amount, src, tgt, memo, is_leak
                ))
                journalobal_entry_count += 1

        # 標準出力へストリーム (I/O)
        writer = csv.writer(sys.stdout)
        for row in daily_entries:
            writer.writerow(row)

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    # 乱数シードの固定 (TDDの決定論的振る舞いのため)
    random.seed(args.seed)
    np.random.seed(args.seed)

    # ヘッダー出力
    writer = csv.writer(sys.stdout)
    writer.writerow(["Entry_ID", "Trans_Date", "Account_Name", "Dept_Name", "Debit", "Credit", "Memo"])

    # ストリーム生成開始
    generate_stream(args)

if __name__ == "__main__":
    main()
