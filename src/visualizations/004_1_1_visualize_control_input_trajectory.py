#!/usr/bin/env python3
# ==========================================
# 1_7_visualize_control_input_trajectory.py
# TLU System: Control Input Trajectory
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import pandas as pd
import matplotlib.pyplot as plt

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Optimal Control Input Trajectory (u)")
    parser.set_defaults(filename="1_7_1__control_input_trajectory.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    
    # Apply theme variables
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    bg_col = ui_canvas['legend_bg']
    edge_col = ui_canvas['legend_edge']
    grid_col = ui_canvas['grid_line']

    # Read stream from standard input
    df = pd.read_csv(sys.stdin)
    if df.empty: sys.exit(0)

    # Type safety
    df['optimal_input_u'] = df['optimal_input_u'].astype(float)

    # Load dictionary (Time & Node)
    N = int(df['node_idx'].max()) + 1
    T_max = int(df['t_idx'].max()) + 1
    labels = load_node_labels(args.node_map, N)
    time_labels = load_time_labels(args.time_map, T_max)

    # Extract active nodes (determined by the sum of absolute values)
    active_nodes_series = df.groupby('node_idx')['optimal_input_u'].apply(lambda x: x.abs().sum())
    active_nodes = active_nodes_series[active_nodes_series > 0].index.tolist()
    
    df_active = df[df['node_idx'].isin(active_nodes)]
    pivot_u = df_active.pivot(index='t_idx', columns='node_idx', values='optimal_input_u').fillna(0)

    fig, ax = plt.subplots(figsize=(12, 7))
    
    if not pivot_u.empty:
        # Draw plot
        for col in pivot_u.columns:
            label_str = f"{col:02d}: {labels.get(col, '')}"
            ax.plot(pivot_u.index, pivot_u[col], marker='o', linewidth=2, label=label_str)
            
        # Neutral line
        ax.axhline(0, color=grid_col, linewidth=1.5, linestyle='--')
        
        # --- Time Label X-Axis Formatting ---
        x_values = pivot_u.index.values
        x_tick_labels = [time_labels.get(t, f"T_{int(t):02d}") for t in x_values]
        
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_tick_labels, rotation=45, color=text_col, ha='right', fontsize=11)

    ax.set_title("Optimal Control Input ($u$) Trajectory over Time", fontsize=15, color=text_col)
    ax.set_xlabel("Timeline", fontsize=12, color=text_col)
    ax.set_ylabel("Control Input Magnitude ($u$)", fontsize=12, color=text_col)
    
    ax.grid(True, linestyle=':', alpha=0.5, color=grid_col)
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)
    
    if not pivot_u.empty:
        ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), 
                  facecolor=bg_col, edgecolor=edge_col, labelcolor=text_col)
    
    # Margin adjustment (Ensure a little bottom so X-axis labels do not get cut off when rotated)
    plt.subplots_adjust(bottom=0.15, left=0.08, right=0.85, top=0.92)
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
