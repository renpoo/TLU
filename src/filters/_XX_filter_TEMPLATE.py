#!/usr/bin/env python3
# ==========================================
# _XX_filter_TEMPLATE.py
# TLU System: [Domain Name] I/O Pipeline Filter
# ==========================================
import sys
import csv
import argparse
import numpy as np

# 1. 共通基盤のインポート (I/O層の再利用)
from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices

# 2. 数理コアモジュールのインポート (ここに旧版の core_*.py を指定)
# import src.core.core_your_domain as cyd

def run_your_domain_analysis(t_idx: int, T_slice: np.ndarray, extra_param: float) -> list[list]:
    """
    [Pure Orchestration Function]
    時間スライス(T_slice)を受け取り、純粋数学層(core_*.py)を呼び出して解析を行い、
    CSVに出力するためのレコード（行のリスト）を返す。
    
    ※この関数内には、旧版の数理ロジックやコア関数呼び出しをそのまま移植してください。
    """
    N = T_slice.shape[0]
    records = []
    
    # === ここに真の数理解析（旧版コードの呼び出し）を実装 ===
    # 例: P = compute_transition_matrix(T_slice)
    #     results = cyd.your_math_function(P, extra_param)
    
    # === 結果をレコードとしてフォーマット ===
    # 例: for i in range(N):
    #         records.append([t_idx, i, results[i]])
    
    return records

def main():
    # 1. 共通パーサーのセットアップ
    parser = get_base_parser("TLU [Domain Name] Filter")
    
    # 2. このフィルター特有の引数があれば追加
    parser.add_argument("--extra_param", type=float, default=1.0, help="Custom parameter for this filter")
    
    # 3. パイプラインの初期化（標準入力、ノード数Nの取得、引数パース）
    # ※ sys_params や node_map の読み込みは setup_pipeline が安全に行います
    args, reader, N, sys_params = setup_pipeline(parser)
    if N <= 0:
        return

    # 4. 出力用のライターとヘッダーの準備
    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow(["t_idx", "node_idx", "metric_value"]) # カラム名は適切に変更してください

    # 5. ストリーム処理ループ（時間スライスごとの処理）
    # ※ yield_time_slices が、巨大なCSVから t_idx ごとの (N x N) 行列を安全に切り出します
    for t_idx, T_slice in yield_time_slices(reader, N):
        
        # オーケストレーション関数を呼び出し、結果を受け取る
        records = run_your_domain_analysis(t_idx, T_slice, args.extra_param)
        
        # 結果を標準出力へストリーミング
        for rec in records:
            writer.writerow(rec)

if __name__ == "__main__":
    main()
