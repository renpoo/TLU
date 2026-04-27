#!/usr/bin/env python3
# ==========================================
# 002_1_3_visualize_manifold_dimensionality.py
# TLU System: Manifold Dimensionality Visualization
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import pandas as pd
import matplotlib.pyplot as plt

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Manifold Effective Dimensionality (Rank)")
    parser.set_defaults(filename="12_manifold_dimensionality.png")
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

    # We only need effective_rank per t_idx
    df_unique = df[['t_idx', 'effective_rank']].drop_duplicates()
    df_unique['effective_rank'] = df_unique['effective_rank'].astype(int)
    
    T_max = int(df['t_idx'].max()) + 1
    time_labels = load_time_labels(args.time_map, T_max)

    fig, ax = plt.subplots(figsize=(12, 7))
    
    if not df_unique.empty:
        ax.plot(df_unique['t_idx'], df_unique['effective_rank'], 
                linewidth=3, marker='o', color='#9b59b6', label='Effective Rank (SVD)')

        x_values = df_unique['t_idx'].values
        x_tick_labels = [time_labels.get(t, f"T_{int(t):02d}") for t in x_values]
        
        apply_smart_x_labels(ax, x_values, x_tick_labels, text_col)

    ax.set_title("Information Geometry: Manifold Effective Dimensionality (Rank)", fontsize=15, color=text_col)
    ax.set_xlabel("Timeline", fontsize=12, color=text_col)
    ax.set_ylabel("Effective Rank (Independent Pathways)", fontsize=12, color=text_col)
    
    ax.grid(True, linestyle=':', alpha=0.5, color=grid_col)
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)
    
    if not df_unique.empty:
        ax.legend(loc='upper right', facecolor=bg_col, edgecolor=edge_col, labelcolor=text_col)
    
    plt.subplots_adjust(bottom=0.15, left=0.08, right=0.95, top=0.92)
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
