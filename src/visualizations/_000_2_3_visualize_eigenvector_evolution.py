#!/usr/bin/env python3
# ==========================================
# _000_2_3_visualize_eigenvector_evolution.py
# TLU System: Eigenvector Evolution Heatmap (PC1)
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Eigenvector Evolution Heatmap")
    parser.add_argument("--component", type=int, default=0, help="Component index to plot (0=PC1, 1=PC2, ...)")
    parser.set_defaults(filename="000_2_3__eigenvector_evolution_heatmap.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    grid_col = ui_canvas['grid_line']
    
    # We will use the physics theme gradient, but a diverging or absolute magnitude map is good
    # Here we'll use a hot/magma style for magnitude of influence
    import seaborn as sns
    cmap = sns.color_palette("magma", as_cmap=True)

    df = pd.read_csv(sys.stdin)
    if df.empty: sys.exit(0)

    # Filter for the specified principal component
    df_pc = df[df['component_idx'] == args.component].copy()
    
    if df_pc.empty: sys.exit(0)
    
    # Extract absolute vector value to see magnitude of influence
    df_pc['magnitude'] = df_pc['vector_value'].astype(float).abs()

    # Pivot: Rows = node_idx, Cols = t_idx
    pivot_data = df_pc.pivot(index='node_idx', columns='t_idx', values='magnitude').fillna(0)

    # Load node labels
    N = int(df_pc['node_idx'].max()) + 1
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

    # Dynamic suffix for title (1st, 2nd, 3rd, 4th, etc.)
    if args.component == 0:
        pc_label = "1st"
    elif args.component == 1:
        pc_label = "2nd"
    elif args.component == 2:
        pc_label = "3rd"
    else:
        pc_label = f"{args.component + 1}th"

    sns.heatmap(pivot_data, cmap=cmap, ax=ax, cbar_kws={'label': f'Magnitude (Absolute {pc_label} PC Value)'})
    
    ax.set_title(f"Temporal Evolution of {pc_label} Principal Component (Regime Shift Radar)", fontsize=16, color=text_col)
    ax.set_xlabel("Timeline", fontsize=12, color=text_col)
    ax.set_ylabel("Accounts (Nodes)", fontsize=12, color=text_col)
    
    # Apply standard UI theme to colorbar
    cbar = ax.collections[0].colorbar
    cbar.ax.yaxis.set_tick_params(color=text_col)
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color=text_col)
    cbar.set_label(f'Magnitude (Absolute {pc_label} PC Value)', color=text_col)
    
    # Formatting ticks
    ax.set_xticks(np.arange(len(x_tick_labels)) + 0.5)
    ax.set_xticklabels(x_tick_labels, rotation=90, ha='center', color=text_col)
    ax.set_yticks(np.arange(len(y_tick_labels)) + 0.5)
    ax.set_yticklabels(y_tick_labels, rotation=0, color=text_col)

    for spine in ax.spines.values():
        spine.set_color(text_col)

    plt.subplots_adjust(bottom=0.20, left=0.25, right=0.95, top=0.92)
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
