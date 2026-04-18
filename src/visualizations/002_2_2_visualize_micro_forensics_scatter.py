#!/usr/bin/env python3
# ==========================================
# 002_2_2_visualize_micro_forensics_scatter.py
# TLU System: Forensics Phase Space (Z-Score vs KL Drift)
# Strict Theme Mode (Fail-Fast)
# ==========================================
import sys
import pandas as pd
import matplotlib.pyplot as plt

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Forensics Phase Space: Z-Score vs KL Drift")
    parser.add_argument("--z_thresh", type=float, default=3.0, help="Warning line for Z-score")
    parser.add_argument("--kl_thresh", type=float, default=2.0, help="Warning line for KL drift")
    parser.set_defaults(filename="23_forensics_scatter_space.png")
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
    
    c_normal = ui_canvas['data_normal']
    c_alert = theme_cfg['forensics']['colors']['z_score_shock']

    df = pd.read_csv(sys.stdin)
    if df.empty: sys.exit(0)

    # [Fix] Synchronize with micro (node-level) column names
    max_anomalies = df.groupby('node_idx').agg({
        'node_univariate_z_score': 'max',
        'node_kl_drift': 'max'
    }).reset_index()

    N = int(max_anomalies['node_idx'].max()) + 1
    labels = load_node_labels(args.node_map, N)

    fig, ax = plt.subplots(figsize=(12, 8))
    
    colors = [c_normal if (row['node_univariate_z_score'] < args.z_thresh and row['node_kl_drift'] < args.kl_thresh) else c_alert 
              for _, row in max_anomalies.iterrows()]
              
    ax.scatter(max_anomalies['node_univariate_z_score'], max_anomalies['node_kl_drift'], 
               color=colors, s=120, alpha=0.7, edgecolors=text_col)

    ax.axvline(args.z_thresh, color=grid_col, linestyle='--', alpha=0.7, label=f'Z-Score Thresh ({args.z_thresh})')
    ax.axhline(args.kl_thresh, color=grid_col, linestyle='-.', alpha=0.7, label=f'KL Drift Thresh ({args.kl_thresh})')

    for _, row in max_anomalies.iterrows():
        if row['node_univariate_z_score'] >= args.z_thresh or row['node_kl_drift'] >= args.kl_thresh:
            idx = int(row['node_idx'])
            ax.text(row['node_univariate_z_score'], row['node_kl_drift'], f" {idx:02d}", 
                    color=c_alert, fontsize=11, fontweight='bold', va='bottom', ha='left')

    ax.set_title("Micro Forensics Space: Max Z-Score vs Max KL Drift (Bottleneck Identification)", fontsize=15, color=text_col)
    ax.set_xlabel("Max Node Z-Score (Univariate Activity Shock)", fontsize=12, color=text_col)
    ax.set_ylabel("Max Node KL Drift (Structural Pattern Mutation)", fontsize=12, color=text_col)
    ax.grid(True, linestyle=':', alpha=0.5, color=grid_col)
    ax.tick_params(colors=text_col)
    
    ax.legend(loc='upper right', facecolor=bg_col, edgecolor=edge_col, labelcolor=text_col)

    node_lines = [f"{i:02d}: {labels.get(i, '')}" for i in range(min(N, args.max_legend))]
    fig.text(0.78, 0.5, "Node Index Map:\n" + "-"*15 + "\n" + "\n".join(node_lines), 
             fontsize=9, color=text_col, verticalalignment='center', family='monospace', 
             bbox=dict(facecolor=bg_col, alpha=0.8, edgecolor=edge_col))
    plt.subplots_adjust(right=0.75)
    
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
