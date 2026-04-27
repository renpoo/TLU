#!/usr/bin/env python3
# ==========================================
# 000_2_2_visualize_principal_axes_ratio.py
# TLU System: Principal Axes (PCA) Visualization
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Principal Axes Variance Ratio")
    parser.set_defaults(filename="04_principal_axes_ratio.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    bg_col = ui_canvas['legend_bg']
    edge_col = ui_canvas['legend_edge']
    grid_col = ui_canvas['grid_line']

    df = pd.read_csv(sys.stdin)
    if df.empty: sys.exit(0)

    # We only need the ratio per component per t_idx
    # The output has multiple rows per component (one for each node)
    # We can just drop duplicates based on t_idx and component_idx
    df_unique = df[['t_idx', 'component_idx', 'explained_variance_ratio']].drop_duplicates()
    df_unique['explained_variance_ratio'] = df_unique['explained_variance_ratio'].astype(float)
    
    # Load time dictionary
    T_max = int(df['t_idx'].max()) + 1
    time_labels = load_time_labels(args.time_map, T_max)

    pivot_data = df_unique.pivot(index='t_idx', columns='component_idx', values='explained_variance_ratio').fillna(0)

    fig, ax = plt.subplots(figsize=(12, 7))
    
    if not pivot_data.empty:
        # Plot as stacked bar chart to show cumulative ratio
        bottom = np.zeros(len(pivot_data))
        for col in pivot_data.columns:
            ax.bar(pivot_data.index, pivot_data[col], bottom=bottom, label=f"PC {int(col)+1}", alpha=0.8)
            bottom += pivot_data[col]

        # --- Time Label X-Axis Formatting ---
        x_values = pivot_data.index.values
        x_tick_labels = [time_labels.get(t, f"T_{int(t):02d}") for t in x_values]
        
        apply_smart_x_labels(ax, x_values, x_tick_labels, text_col)

    ax.set_title("Principal Components: Explained Variance Ratio (Dominant Modes)", fontsize=15, color=text_col)
    ax.set_xlabel("Timeline", fontsize=12, color=text_col)
    ax.set_ylabel("Explained Variance Ratio", fontsize=12, color=text_col)
    
    ax.grid(True, linestyle=':', alpha=0.5, color=grid_col)
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)
    
    if not pivot_data.empty:
        ax.legend(loc='upper right', facecolor=bg_col, edgecolor=edge_col, labelcolor=text_col)
    
    plt.subplots_adjust(bottom=0.15, left=0.08, right=0.95, top=0.92)
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
