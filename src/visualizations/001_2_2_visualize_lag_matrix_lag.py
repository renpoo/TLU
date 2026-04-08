#!/usr/bin/env python3
# ==========================================
# 001_2_2_visualize_lag_matrix_lag.py
# TLU System: Optimal Time-Lag Matrix
# Strict Theme Mode (Fail-Fast) & External Plotting Logic
# ==========================================

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 共通ユーティリティから draw_matrix_heatmap をインポート
from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Lag Matrix: Optimal Time-Lag")
    parser.add_argument("--corr_thresh", type=float, default=0.5, help="ラグを表示する相関係数の閾値")
    parser.set_defaults(filename="1_10_lag_matrix_optimal_lag.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    bg_col = ui_canvas['background']
    cmap_name = theme_cfg['topology_and_correlation']['colormaps']['lag_matrix_map']

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr); sys.exit(1)

    if df.empty: sys.exit(0)

    N = int(max(df['src_idx'].max(), df['tgt_idx'].max())) + 1
    idx_to_label = load_node_labels(args.node_map, N)

    pivot_corr = df.pivot(index='src_idx', columns='tgt_idx', values='max_correlation').fillna(0)
    pivot_lag = df.pivot(index='src_idx', columns='tgt_idx', values='optimal_lag').fillna(0)

    mask = np.abs(pivot_corr) < args.corr_thresh
    axis_labels = [f"{i:02d}: {idx_to_label.get(i, f'N_{i}')}" for i in range(N)]

    fig, ax = plt.subplots(figsize=(14, 12))
    
    # 共通描画ロジックへ委譲
    title = f"Node-to-Node Optimal Time-Lag Matrix (Masked |ρ| < {args.corr_thresh})"
    draw_matrix_heatmap(
        ax, pivot_lag, cmap_name, 'Optimal Lag (Time Steps)', title, 
        axis_labels, text_col, bg_col=bg_col, mask=mask
    )

    plt.subplots_adjust(bottom=0.2, left=0.2, right=0.95, top=0.9)
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
