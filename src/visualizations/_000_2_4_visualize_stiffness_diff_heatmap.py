#!/usr/bin/env python3
# ==========================================
# _000_2_4_visualize_stiffness_diff_heatmap.py
# TLU System: Plot sequential heatmaps of stiffness temporal differences
# ==========================================

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.visualizations.visualizer_utils import get_base_parser, apply_theme, load_node_labels, save_plot

def setup_argparser():
    parser = get_base_parser("Stiffness Temporal Difference Heatmap Plotter")
    parser.set_defaults(filename="stiffness_diff.t.{t_idx:05d}.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    theme_cfg = apply_theme(args.theme) or {}
    ui_canvas = theme_cfg.get('ui_canvas', {})
    text_col = ui_canvas.get('text_primary', 'white')
    bg_col = ui_canvas.get('background', 'black')

    # Diverging colormap for positive/negative transitions
    cmap_name = 'coolwarm'

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    required = ['t_idx', 'src_idx', 'tgt_idx', 'stiffness_diff']
    for col in required:
        if col not in df.columns:
            print(f"Error: Missing column {col}", file=sys.stderr)
            sys.exit(1)

    max_t = int(df['t_idx'].max()) + 1
    N = int(max(df['src_idx'].max(), df['tgt_idx'].max())) + 1
    node_labels = load_node_labels(args.node_map, N)
    axis_labels = [node_labels.get(i, f"Node_{i:02d}") for i in range(N)]

    for t_idx in range(max_t):
        df_t = df[df['t_idx'] == t_idx]
        if df_t.empty:
            continue

        diff_matrix = np.zeros((N, N))
        for _, row in df_t.iterrows():
            diff_matrix[int(row['src_idx']), int(row['tgt_idx'])] = float(row['stiffness_diff'])

        # Symmetric scaling centered on zero
        max_abs = np.max(np.abs(diff_matrix))
        if max_abs == 0:
            max_abs = 1e-5
        vmin, vmax = -max_abs, max_abs

        fig, ax = plt.subplots(figsize=(12, 10))
        fig.patch.set_facecolor(bg_col)
        ax.set_facecolor(bg_col)

        sns.heatmap(diff_matrix, ax=ax, cmap=cmap_name, vmin=vmin, vmax=vmax,
                    xticklabels=axis_labels, yticklabels=axis_labels,
                    cbar_kws={'label': 'Stiffness Diff (K_t - K_t-1)'})

        ax.set_title(f"Stiffness Temporal Difference (t={t_idx})", color=text_col, fontsize=14, fontweight='bold')
        ax.set_xlabel("Target Node (Impact Received)", color=text_col, fontsize=12)
        ax.set_ylabel("Source Node (Shock Origin)", color=text_col, fontsize=12)

        ax.tick_params(colors=text_col)
        cbar = ax.collections[0].colorbar
        cbar.ax.yaxis.set_tick_params(color=text_col)
        plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color=text_col)

        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        plt.tight_layout()

        # Format output filename dynamically with step numbers
        base_name, ext = os.path.splitext(args.filename)
        out_filename = f"{base_name.replace('.png', '')}.t.{t_idx:05d}{ext}"
        save_plot(fig, args.out_dir, out_filename)
        plt.close(fig)

if __name__ == '__main__':
    main()
