#!/usr/bin/env python3
# ==========================================
# _005_1_2_visualize_phase_drift_heatmap.py
# TLU System: Traversing Phase Shift Heatmap
# ==========================================
import sys
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Traversing Phase Shift Heatmap")
    parser.add_argument('--master_node', type=int, default=6, help="The reference node to calculate phase shift against (Master)")
    parser.add_argument('--is_pca', action='store_true', help="Set to true if visualizing PCA components instead of normal nodes")
    parser.set_defaults(filename="005_1_2_phase_drift_heatmap.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    
    # We use a diverging colormap for phase shift (negative = lead, positive = lag, or vice versa)
    cmap_name = theme_cfg['topology_and_correlation']['colormaps']['lag_matrix_map'] # e.g. RdBu_r

    df = pd.read_csv(sys.stdin)
    if df.empty: sys.exit(0)

    # Filter to only keep rows where src_idx == master_node
    master_df = df[df['src_idx'] == args.master_node].copy()
    
    if master_df.empty:
        sys.stderr.write(f"[WARN] No data found for master node {args.master_node}. Exiting.\n")
        sys.exit(0)

    # Pivot to get t_idx as columns, tgt_idx as rows, phase_shift as values
    pivot_df = master_df.pivot(index='tgt_idx', columns='t_idx', values='phase_shift').fillna(0)
    
    # Optional: We could weight or filter by coherence, but let's just plot phase shift for now.
    
    # Prepare labels
    N = int(max(df['src_idx'].max(), df['tgt_idx'].max())) + 1
    if args.is_pca:
        idx_to_label = {i: f"PC{i+1}" for i in range(N)}
        ylabel = "Principal Component (Target)"
        title_prefix = f"PCA Phase Drift Heatmap (Master: PC{args.master_node+1})"
    else:
        idx_to_label = load_node_labels(args.node_map, N)
        ylabel = "Node (Target)"
        title_prefix = f"Node Phase Drift Heatmap (Master: Node {args.master_node})"

    y_labels = [f"{i:02d}: {idx_to_label.get(i, f'N_{i}')}" for i in pivot_df.index]
    
    T = int(df['t_idx'].max()) + 1
    t_idx_to_label = load_time_labels(args.time_map, T)
    x_labels = [t_idx_to_label.get(int(t), str(int(t))) for t in pivot_df.columns]

    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Draw heatmap. 
    # Phase shift is in radians, roughly -pi to pi.
    import seaborn as sns
    sns.heatmap(pivot_df, ax=ax, cmap=cmap_name, robust=True, 
                vmin=-np.pi, vmax=np.pi,
                cbar_kws={'label': 'Phase Shift (Radians)'}, 
                xticklabels=x_labels, yticklabels=y_labels)

    ax.set_title(f"{title_prefix}\nViscosity / Rhythm Mutation Over Time", fontsize=15, color=text_col, pad=15)
    ax.set_ylabel(ylabel, color=text_col, fontsize=12)
    ax.set_xlabel("Time (t_idx)", color=text_col, fontsize=12)

    # Adjust axis tick marks
    # Show fewer x ticks if there are many
    n_ticks = len(x_labels)
    if n_ticks > 20:
        step = n_ticks // 20
        ax.set_xticks(np.arange(0, n_ticks, step) + 0.5)
        ax.set_xticklabels(x_labels[::step], rotation=90)
    else:
        ax.tick_params(axis='x', rotation=90)

    ax.tick_params(colors=text_col)
    
    plt.tight_layout()
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
