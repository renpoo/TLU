#!/usr/bin/env python3
# ==========================================
# 001_2_2_visualize_lag_matrix_correlation.py
# TLU System: Cross-Correlation Matrix
# Strict Theme Mode (Fail-Fast) & External Plotting Logic
# ==========================================

import sys
import pandas as pd
import matplotlib.pyplot as plt

# Import draw_matrix_heatmap from common utilities
from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Lag Matrix: Cross-Correlation")
    parser.set_defaults(filename="1_10_lag_matrix_correlation.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    cmap_name = theme_cfg['topology_and_correlation']['colormaps']['lag_matrix_map']

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr); sys.exit(1)

    if df.empty: sys.exit(0)

    N = int(max(df['src_idx'].max(), df['tgt_idx'].max())) + 1
    idx_to_label = load_node_labels(args.node_map, N)

    pivot_corr = df.pivot(index='src_idx', columns='tgt_idx', values='max_correlation').fillna(0)
    axis_labels = [f"{i:02d}: {idx_to_label.get(i, f'N_{i}')}" for i in range(N)]

    fig, ax = plt.subplots(figsize=(14, 12))
    
    # Delegate to common drawing logic
    title = "Node-to-Node Cross-Correlation Matrix (Impact Strength)"
    draw_matrix_heatmap(
        ax, pivot_corr, cmap_name, 'Max Correlation Coefficient', title, 
        axis_labels, text_col, vmin=-1.0, vmax=1.0
    )

    plt.subplots_adjust(bottom=0.2, left=0.2, right=0.95, top=0.9)
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
