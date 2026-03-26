#!/usr/bin/env python3
# ==========================================
# 1_7_visualize_control_input_trajectory.py
# TLU System: Control Input Trajectory
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import pandas as pd
import matplotlib.pyplot as plt
from src.visualizations.visualizer_utils import get_base_parser, apply_theme, load_node_labels, save_plot

def setup_argparser():
    parser = get_base_parser("Optimal Control Input Trajectory (u)")
    parser.set_defaults(filename="19_control_input_trajectory.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    
    # フォールバックの排除
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    bg_col = ui_canvas['legend_bg']
    edge_col = ui_canvas['legend_edge']
    grid_col = ui_canvas['grid_line']

    df = pd.read_csv(sys.stdin)
    if df.empty: sys.exit(0)

    active_nodes = df.groupby('node_idx')['optimal_input_u'].sum()
    active_nodes = active_nodes[active_nodes != 0].index.tolist()
    
    df_active = df[df['node_idx'].isin(active_nodes)]
    pivot_u = df_active.pivot(index='t_idx', columns='node_idx', values='optimal_input_u').fillna(0)

    N = int(df['node_idx'].max()) + 1
    labels = load_node_labels(args.node_map, N)

    fig, ax = plt.subplots(figsize=(12, 7))
    if not pivot_u.empty:
        ax.stackplot(pivot_u.index, pivot_u.T, labels=[f"{col:02d}: {labels.get(col, '')}" for col in pivot_u.columns], alpha=0.8)

    ax.set_title("Optimal Control Input ($u$) Trajectory over Time", fontsize=15, color=text_col)
    ax.set_xlabel("Time Step ($t$)", fontsize=12, color=text_col)
    ax.set_ylabel("Control Input Magnitude ($u$)", fontsize=12, color=text_col)
    ax.grid(True, linestyle=':', alpha=0.5, color=grid_col)
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)
    
    if not pivot_u.empty:
        # ハードコードされた facecolor='black', edgecolor='gray' をテーマ変数に置換
        ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), 
                  facecolor=bg_col, edgecolor=edge_col, labelcolor=text_col)
    
    plt.tight_layout()
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
