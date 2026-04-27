#!/usr/bin/env python3
# ==========================================
# 1_5_visualize_thermodynamics_dashboard.py
# TLU System: Macro Thermodynamics Dashboard
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import system common infrastructure
from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Thermodynamics Dashboard (X=t, Y=S, Z=T)")
    parser.set_defaults(filename="1_5_1__thermodynamics_dashboard.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    # Eliminate fallbacks and enforce strict key reference (Fail-Fast)
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    legend_bg_col = ui_canvas['legend_bg']
    legend_edge_col = ui_canvas['legend_edge']
    grid_line_col = ui_canvas['grid_line']
    zero_line_col = ui_canvas['zero_line']

    # Strict extraction of semantic colors
    colors = theme_cfg['thermodynamics']['colors']
    c_U = colors['gross_activity_U']
    c_F = colors['free_energy_F']
    c_T = colors['temperature_T']
    c_S = colors['entropy_S']

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading from standard input: {e}", file=sys.stderr); sys.exit(1)

    if df.empty:
        print("Warning: Received empty data stream.", file=sys.stderr); sys.exit(0)

    t = df['t_idx']
    U = df['gross_activity_U']
    S = df['entropy_S']
    T_raw = df['temperature_T']

    T_max_idx = int(t.max()) + 1
    time_labels = load_time_labels(args.time_map, T_max_idx)
    
    T_corrected = np.maximum(T_raw, 0)
    TS = T_corrected * S
    F_corrected = U - TS

    fig, axes = plt.subplots(4, 1, figsize=(12, 12), sharex=True)
    
    # --- 1st row: Internal Energy (U) ---
    axes[0].plot(t, U, color=c_U, marker='s', markersize=5, linewidth=2, label='Internal Energy (U)')
    axes[0].axhline(0, color=zero_line_col, linestyle='--', linewidth=1)
    axes[0].set_title("1. Internal Energy (U) : Gross Activity Scale", loc='left', fontweight='bold', color=text_col)
    axes[0].set_ylabel("U (Amount)", color=text_col)
    leg0 = axes[0].legend(loc='best', facecolor=legend_bg_col, edgecolor=legend_edge_col)
    for text in leg0.get_texts(): text.set_color(text_col)
    axes[0].grid(True, linestyle=':', alpha=0.8, color=grid_line_col)

    # --- 2nd row: Free Energy (F) ---
    axes[1].plot(t, F_corrected, color=c_F, marker='o', markersize=5, linewidth=2, label='Free Energy (F)')
    axes[1].axhline(0, color=zero_line_col, linestyle='--', linewidth=1)
    axes[1].set_title("2. Free Energy (F) : Net Available Power (Corrected)", loc='left', fontweight='bold', color=text_col)
    axes[1].set_ylabel("F (Amount)", color=text_col)
    leg1 = axes[1].legend(loc='best', facecolor=legend_bg_col, edgecolor=legend_edge_col)
    for text in leg1.get_texts(): text.set_color(text_col)
    axes[1].grid(True, linestyle=':', alpha=0.8, color=grid_line_col)

    # --- 3rd row: Temperature (T) ---
    axes[2].plot(t, T_corrected, color=c_T, marker='^', markersize=5, linewidth=2, label='Temperature (T)')
    axes[2].axhline(0, color=zero_line_col, linestyle='--', linewidth=1)
    axes[2].set_title("3. Temperature (T) : Volatility / Friction Level (Corrected)", loc='left', fontweight='bold', color=text_col)
    axes[2].set_ylabel("T (Amount)", color=text_col)
    leg2 = axes[2].legend(loc='best', facecolor=legend_bg_col, edgecolor=legend_edge_col)
    for text in leg2.get_texts(): text.set_color(text_col)
    axes[2].grid(True, linestyle=':', alpha=0.8, color=grid_line_col)

    # --- 4th row: Entropy (S) ---
    axes[3].plot(t, S, color=c_S, marker='x', markersize=5, linewidth=2, label='Entropy (S)')
    axes[3].axhline(0, color=zero_line_col, linestyle='--', linewidth=1)
    axes[3].set_title("4. Entropy (S) : Structural Disorder & Information Dispersion", loc='left', fontweight='bold', color=text_col)
    axes[3].set_ylabel("S (Ratio)", color=text_col)
    leg3 = axes[3].legend(loc='best', facecolor=legend_bg_col, edgecolor=legend_edge_col)
    for text in leg3.get_texts(): text.set_color(text_col)
    axes[3].grid(True, linestyle=':', alpha=0.8, color=grid_line_col)

    # Combine and format X-axis labels
    bottom_ax = axes[3]
    ticks = df['t_idx'].values
    labels = [str(time_labels.get(t, t)) for t in ticks]
    bottom_ax.set_xticks(ticks)
    bottom_ax.set_xticklabels(labels, rotation=90, ha='center', color=text_col)
    bottom_ax.set_xlabel("Timeline", color=text_col, fontsize=12)

    for ax in axes:
        ax.margins(0.1)
        ax.tick_params(axis='y', colors=text_col)
        for spine in ax.spines.values():
            spine.set_color(text_col)

    plt.tight_layout()
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
