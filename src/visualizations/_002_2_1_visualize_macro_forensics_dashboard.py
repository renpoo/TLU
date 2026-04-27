#!/usr/bin/env python3
# ==========================================
# 1_8_visualize_macro_forensics_dashboard.py
# TLU System: Macro Forensics Dashboard
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import pandas as pd
import matplotlib.pyplot as plt

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Macro Forensics Dashboard: System-wide Anomalies")
    parser.set_defaults(filename="21_macro_forensics_dashboard.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    # Eliminate fallbacks
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    grid_col = ui_canvas['grid_line']
    zero_col = ui_canvas['zero_line']
    
    colors = theme_cfg['forensics']['colors']
    c_residual = colors['benford_actual'] 
    c_drift = theme_cfg['thermodynamics']['colors']['temperature_T'] 
    c_zscore = colors['z_score_shock']

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr); sys.exit(1)
        
    if df.empty: sys.exit(0)

    T_max = int(df['t_idx'].max()) + 1
    time_labels = load_time_labels(args.time_map, T_max)
    
    x_values = df['t_idx'].values
    x_tick_labels = [time_labels.get(t, f"T_{int(t):02d}") for t in x_values]

    fig, axes = plt.subplots(3, 1, figsize=(16, 12), sharex=True)

    # --- 1. System Conservation Residual ---
    axes[0].plot(x_values, df['conservation_residual'], marker='s', color=c_residual, linewidth=2)
    axes[0].set_title("1. System Conservation Residual (Leakage Detection)", fontsize=15, color=text_col, loc='left', fontweight='bold')
    axes[0].set_ylabel("|Residual|", color=text_col, fontsize=12)
    axes[0].axhline(0, color=zero_col, linestyle='--', alpha=0.7)

    # --- 2. System Structural Drift ---
    axes[1].plot(x_values, df['kl_divergence_drift'], marker='^', color=c_drift, linewidth=2)
    axes[1].set_title("2. System Structural Drift (KL Divergence)", fontsize=15, color=text_col, loc='left', fontweight='bold')
    axes[1].set_ylabel("KL Divergence", color=text_col, fontsize=12)
    
    # --- 3. System Multivariate Shock ---
    axes[2].plot(x_values, df['mahalanobis_z_score'], marker='o', color=c_zscore, linewidth=2)
    axes[2].set_title("3. Statistical Anomaly (Mahalanobis Z-Score)", fontsize=15, color=text_col, loc='left', fontweight='bold')
    axes[2].set_ylabel("Z-Score (sigma)", color=text_col, fontsize=12)
    axes[2].set_xlabel("Timeline", color=text_col, fontsize=12)
    axes[2].axhline(args.thresh_z_score, color=grid_col, linestyle='--', alpha=0.8, label=f'Threshold ({args.thresh_z_score})')
    axes[2].legend(loc='upper right', facecolor=ui_canvas['legend_bg'], edgecolor=ui_canvas['legend_edge'], labelcolor=text_col)

    axes[2].set_xticks(x_values)
    axes[2].set_xticklabels(x_tick_labels, rotation=45, color=text_col, ha='right', fontsize=11)

    for ax in axes:
        ax.tick_params(axis='y', colors=text_col)
        ax.grid(True, linestyle=':', alpha=0.4, color=grid_col)
        for spine in ax.spines.values():
            spine.set_color(text_col)

    plt.subplots_adjust(bottom=0.15, left=0.08, right=0.95, top=0.95, hspace=0.25)
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
