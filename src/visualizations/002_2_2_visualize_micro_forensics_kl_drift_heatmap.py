#!/usr/bin/env python3
# ==========================================
# 002_2_2_visualize_micro_forensics_kl_drift_heatmap.py
# TLU System: Micro Forensics KL Drift Heatmap
# Strict Theme Mode (Fail-Fast) & External Plotting Logic
# ==========================================

import sys
import pandas as pd
import matplotlib.pyplot as plt

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Micro Forensics Heatmap (Generates KL Drift figures)")
    parser.add_argument("--top_k", type=int, default=5, help="Number of critical outliers to highlight")
    parser.set_defaults(filename="1_9_1__micro_KL_drift_heatmap.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    # Eliminate fallbacks and enforce fail-fast
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    colors = theme_cfg['forensics']['colors']
    cmap_kl = theme_cfg['forensics']['colormaps']['kl_drift_map']
    c_outlier_text = colors['anomaly_outlier']

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr); sys.exit(1)
        
    if df.empty: sys.exit(0)

    N = int(df['node_idx'].max()) + 1
    T_max = int(df['t_idx'].max()) + 1
    idx_to_label = load_node_labels(args.node_map, N)
    time_labels = load_time_labels(args.time_map, T_max)

    pivot_kl = df.pivot(index='node_idx', columns='t_idx', values='node_kl_drift').fillna(0)

    x_tick_labels = [time_labels.get(c, f"T_{int(c):02d}") for c in pivot_kl.columns]
    y_tick_labels = [f"{i:02d}: {idx_to_label.get(i, f'N_{i}')}" for i in range(N)]
    top_k_idx = df.groupby('node_idx')['node_kl_drift'].mean().nlargest(args.top_k).index.tolist()

    base_filename = args.filename.replace('.png', '').replace('_forensics', '')

    fig_kl, ax_kl = plt.subplots(figsize=(16, 7))
    
    # Delegate to common library drawing logic
    draw_single_heatmap(
        ax_kl, pivot_kl, cmap_kl, 'KL Divergence', 
        "Micro Forensics A: Structural Pattern Mutation (Node KL Drift)",
        x_tick_labels, y_tick_labels, top_k_idx, text_col, c_outlier_text
    )
    
    plt.subplots_adjust(left=0.25, right=0.98, top=0.92, bottom=0.22)
    
    kl_filename = f"{base_filename}.png"
    save_plot(fig_kl, args.out_dir, kl_filename)
    plt.close(fig_kl)

if __name__ == "__main__":
    main()
