#!/usr/bin/env python3
# ==========================================
# _00_0_2_visualize_basic_statistics.py
# TLU System: Classical Statistics vs TLU Wave Mechanics Visualization
# ==========================================

import sys
import os
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
from src.visualizations.visualizer_utils import get_base_parser, apply_theme, save_plot, apply_smart_x_labels

def main():
    parser = get_base_parser("Visualize Classical Statistics Baseline vs TLU Phase Shift (SDL_007)")
    # dynamics_csv is provided via stdin by the bash orchestrator
    parser.add_argument("--phase_csv", type=str, required=True, help="Input phase shift CSV")
    parser.add_argument("--target_node", type=str, default="US10Y", help="Node to visualize (defaults to US10Y or first node)")
    parser.add_argument("--window_size", type=int, default=12, help="Rolling window size for classical stats")
    args = parser.parse_args()

    theme_cfg = apply_theme(args.theme)
    bg_col = theme_cfg['ui_canvas']['background']
    text_col = theme_cfg['ui_canvas']['text_primary']
    color_kurtosis = theme_cfg['forensics']['colors']['z_score_shock']
    color_phase = theme_cfg['kinematics']['colors']['velocity_v']

    try:
        df_dyn = pd.read_csv(sys.stdin)
        df_phase = pd.read_csv(args.phase_csv)
    except Exception as e:
        print(f"❌ Input read error: {e}", file=sys.stderr)
        sys.exit(1)

    # 1. Rolling Kurtosis from Dynamics
    available_nodes = df_dyn['node_label'].unique()
    if len(available_nodes) == 0:
        print("❌ No nodes found in dynamics CSV", file=sys.stderr)
        sys.exit(1)
        
    if args.target_node not in available_nodes:
        if "US10Y" in available_nodes:
            args.target_node = "US10Y"
        else:
            args.target_node = available_nodes[0]

    df_node = df_dyn[df_dyn['node_label'] == args.target_node].sort_values('t_idx').copy()
    
    # Calculate rolling kurtosis (drop NaN if window not full)
    df_node['rolling_kurtosis'] = df_node['velocity_v'].rolling(window=args.window_size).apply(lambda x: kurtosis(x, nan_policy='omit'))

    # 2. Phase Shift (where Target Node is involved)
    df_ps = df_phase[(df_phase['tgt_idx'] == args.target_node)].sort_values('t_idx').copy()
    if df_ps.empty:
        df_ps = df_phase[(df_phase['src_idx'] == args.target_node)].sort_values('t_idx').copy()

    if df_ps.empty:
        print(f"⚠️ Phase shift data not found for {args.target_node}. Creating zero baseline.", file=sys.stderr)
        df_ps = pd.DataFrame({'t_idx': df_node['t_idx'], 'phase_shift': 0.0})

    # Merge aligned by time index
    df_merged = pd.merge(df_node, df_ps[['t_idx', 'phase_shift']], on='t_idx', how='inner')
    df_merged = df_merged.dropna(subset=['rolling_kurtosis'])

    # === Plotting ===
    fig, ax1 = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor(bg_col)
    ax1.set_facecolor(bg_col)
    
    # Customize spines
    for spine in ax1.spines.values():
        spine.set_color(theme_cfg['ui_canvas']['grid_line'])

    # Axis 1: TLU Phase Shift (Draw First / Bottom Layer)
    ax1.set_xlabel('Timeline', color=text_col, fontsize=12)
    ax1.set_ylabel('Phase Shift (TLU Wave Mechanics)', color=color_phase, fontsize=12, fontweight='bold')
    line1 = ax1.plot(df_merged['t_idx'], df_merged['phase_shift'], color=color_phase, lw=2.0, alpha=0.9, label='Phase Shift (TLU)')
    ax1.tick_params(axis='y', labelcolor=color_phase, colors=theme_cfg['ui_canvas']['grid_line'])
    ax1.axhline(0.0, color=theme_cfg['ui_canvas']['zero_line'], linestyle=':', alpha=0.5)

    # Axis 2: Classical Kurtosis (Draw Second / Top Layer)
    ax2 = ax1.twinx()
    for spine in ax2.spines.values():
        spine.set_color(theme_cfg['ui_canvas']['grid_line'])
        
    ax2.set_ylabel('Rolling Kurtosis (Classical)', color=color_kurtosis, fontsize=12, fontweight='bold')
    line2 = ax2.plot(df_merged['t_idx'], df_merged['rolling_kurtosis'], color=color_kurtosis, lw=2.5, label=f'Kurtosis ({args.window_size} periods)')
    ax2.tick_params(axis='y', labelcolor=color_kurtosis, colors=theme_cfg['ui_canvas']['grid_line'])
    
    # Highlight Fat Tail threshold (Kurtosis > 3 is leptokurtic)
    ax2.fill_between(df_merged['t_idx'], df_merged['rolling_kurtosis'], 3.0, where=(df_merged['rolling_kurtosis'] > 3.0), color=color_kurtosis, alpha=0.3, interpolate=True)
    ax2.axhline(3.0, color=color_kurtosis, linestyle='--', alpha=0.5, label='Normal Dist Threshold (K=3)')

    apply_smart_x_labels(ax1, df_merged['t_idx'].values, df_merged['time_label'].values, text_col, max_labels=20)

    # Legends
    lines = line1 + line2 + [plt.Line2D([0], [0], color=color_kurtosis, linestyle='--', alpha=0.5)]
    labels = [l.get_label() for l in line1 + line2] + ['Fat Tail Threshold (K=3)']
    
    legend = ax1.legend(lines, labels, loc='upper left', facecolor=theme_cfg['ui_canvas']['legend_bg'], edgecolor=theme_cfg['ui_canvas']['legend_edge'])
    for text in legend.get_texts():
        text.set_color(text_col)

    plt.title(f"Classical Statistics vs TLU Wave Mechanics: {args.target_node}", color=text_col, fontsize=16, fontweight='bold', pad=20)
    
    save_plot(fig, args.out_dir, args.filename or "000_0_2__basic_statistics.png")

if __name__ == "__main__":
    main()
