#!/usr/bin/env python3
# ==========================================
# 004_1_2_visualize_system_stability.py
# TLU System: System Stability (Spectral Radius) Visualization
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import pandas as pd
import matplotlib.pyplot as plt

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("System Stability (Spectral Radius)")
    parser.set_defaults(filename="19_system_stability_radius.png")
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

    df = pd.read_csv(sys.stdin)
    if df.empty: sys.exit(0)

    df['spectral_radius'] = df['spectral_radius'].astype(float)
    
    T_max = int(df['t_idx'].max()) + 1
    time_labels = load_time_labels(args.time_map, T_max)

    fig, ax = plt.subplots(figsize=(12, 7))
    
    if not df.empty:
        # Plot spectral radius
        ax.plot(df['t_idx'], df['spectral_radius'], 
                linewidth=3, marker='o', color='#e74c3c', label='Spectral Radius ($|\\lambda_{max}|$ )')

        x_values = df['t_idx'].values
        x_tick_labels = [time_labels.get(t, f"T_{int(t):02d}") for t in x_values]
        
        ax.set_xticks(x_values)
        ax.set_xticklabels(x_tick_labels, rotation=45, color=text_col, ha='right', fontsize=11)

    # Stability Threshold line
    ax.axhline(args.thresh_spectral_radius, color='#e67e22', linestyle='--', linewidth=2, label=f'Stability Threshold ({args.thresh_spectral_radius})')

    ax.set_title("Control Theory: System Stability (Poles / Spectral Radius)", fontsize=15, color=text_col)
    ax.set_xlabel("Timeline", fontsize=12, color=text_col)
    ax.set_ylabel("Spectral Radius ($|\\lambda_{max}|$)", fontsize=12, color=text_col)
    
    ax.grid(True, linestyle=':', alpha=0.5, color=grid_col)
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)
    
    if not df.empty:
        ax.legend(loc='upper left', facecolor=bg_col, edgecolor=edge_col, labelcolor=text_col)
    
    plt.subplots_adjust(bottom=0.15, left=0.08, right=0.95, top=0.92)
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
