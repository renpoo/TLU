#!/usr/bin/env python3
# ==========================================
# _000_1_7_1_visualize_viscosity_trend.py
# TLU System: Local Viscosity Temporal Evolution Heatmap
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Local Viscosity Temporal Evolution")
    parser.set_defaults(filename="000_1_7_1__viscosity_trend.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    
    # Inferno cmap is ideal for representing stagnation/viscous friction
    cmap = sns.color_palette("inferno", as_cmap=True)

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr); sys.exit(1)
        
    if df.empty: sys.exit(0)

    # Convert viscosity (viscosity_C) to log scale for better visual variance
    df['log_C'] = np.log10(np.where(df['viscosity_C'] <= 0, 1e-6, df['viscosity_C']))

    # Pivot: Rows = node_idx, Cols = t_idx
    df_unique = df.groupby(['node_idx', 't_idx']).first().reset_index()
    pivot_data = df_unique.pivot(index='node_idx', columns='t_idx', values='log_C').fillna(np.log10(1e-6))

    # Load node labels
    N = int(df['node_idx'].max()) + 1
    try:
        node_labels = load_node_labels(args.node_map, N)
    except FileNotFoundError:
        node_labels = {i: f"Node_{i}" for i in range(N)}

    # Load time dictionary
    T_max = int(df['t_idx'].max()) + 1
    time_labels = load_time_labels(args.time_map, T_max)

    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Prepare labels
    y_tick_labels = [node_labels.get(i, f"Node_{i}") for i in pivot_data.index]
    x_tick_labels = [time_labels.get(t, f"T_{int(t):02d}") for t in pivot_data.columns]

    sns.heatmap(pivot_data, cmap=cmap, ax=ax, cbar_kws={'label': 'Log10(Viscosity C)'})
    
    ax.set_title("Local Viscosity Temporal Evolution (Stagnation Heatmap)", fontsize=16, color=text_col)
    ax.set_xlabel("Timeline", fontsize=12, color=text_col)
    ax.set_ylabel("Accounts / Nodes (Stagnation Regions)", fontsize=12, color=text_col)
    
    # Apply standard UI theme to colorbar
    cbar = ax.collections[0].colorbar
    cbar.ax.yaxis.set_tick_params(color=text_col)
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color=text_col)
    cbar.set_label('Log10(Viscosity C)', color=text_col)
    
    # Formatting ticks
    ax.set_xticks(np.arange(len(x_tick_labels)) + 0.5)
    ax.set_xticklabels(x_tick_labels, rotation=90, ha='center', color=text_col)
    ax.set_yticks(np.arange(len(y_tick_labels)) + 0.5)
    ax.set_yticklabels(y_tick_labels, rotation=0, color=text_col)

    for spine in ax.spines.values():
        spine.set_color(text_col)

    plt.subplots_adjust(bottom=0.20, left=0.25, right=0.95, top=0.92)

    # Save logic respects base infrastructure
    save_plot(fig, args.out_dir, args.filename)
    plt.close()

if __name__ == "__main__":
    main()
