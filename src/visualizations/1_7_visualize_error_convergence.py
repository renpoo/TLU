#!/usr/bin/env python3
# ==========================================
# 1_7_visualize_error_convergence.py
# TLU System: State Error Convergence Tracking
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import pandas as pd
import matplotlib.pyplot as plt
from src.visualizations.visualizer_utils import get_base_parser, apply_theme, load_node_labels, save_plot

def setup_argparser():
    parser = get_base_parser("State Error Convergence Tracking (|x|)")
    parser.set_defaults(filename="20_control_error_convergence.png")
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
    zero_line_col = ui_canvas['zero_line']

    df = pd.read_csv(sys.stdin)
    if df.empty: sys.exit(0)

    target_nodes = df.groupby('node_idx')['state_error_x'].sum()
    target_nodes = target_nodes[target_nodes > 0].index.tolist()
    
    df_target = df[df['node_idx'].isin(target_nodes)]
    pivot_gap = df_target.pivot(index='t_idx', columns='node_idx', values='state_error_x').fillna(0)

    N = int(df['node_idx'].max()) + 1
    labels = load_node_labels(args.node_map, N)

    fig, ax = plt.subplots(figsize=(12, 7))
    for col in pivot_gap.columns:
        ax.plot(pivot_gap.index, pivot_gap[col], linewidth=3, marker='o', label=f"{col:02d}: {labels.get(col, '')}")

    # ゼロエラーラインのハードコード 'gray' を置換
    ax.axhline(0, color=zero_line_col, linestyle='--', linewidth=1.5, label='Zero Error State')
    
    ax.set_title("State Error Convergence Tracking ($|x| = |q - q_{target}|$)", fontsize=15, color=text_col)
    ax.set_xlabel("Time Step ($t$)", fontsize=12, color=text_col)
    ax.set_ylabel("Absolute State Error ($|x|$)", fontsize=12, color=text_col)
    ax.grid(True, linestyle=':', alpha=0.5, color=grid_col)
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)
    
    if not pivot_gap.empty:
        # 凡例のハードコード 'black', 'gray' を置換
        ax.legend(loc='upper right', facecolor=bg_col, edgecolor=edge_col, labelcolor=text_col)
    
    plt.tight_layout()
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
