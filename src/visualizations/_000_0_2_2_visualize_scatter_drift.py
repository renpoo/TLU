#!/usr/bin/env python3
import sys, argparse
import pandas as pd
import matplotlib.pyplot as plt
from src.visualizations.visualizer_utils import get_base_parser, apply_theme, save_plot

def main():
    parser = get_base_parser("Classical Stats: Scatter Drift")
    parser.add_argument("--target_node", type=str, default="US10Y")
    args = parser.parse_args()
    theme_cfg = apply_theme(args.theme)

    try:
        df_dyn = pd.read_csv(sys.stdin)
    except Exception:
        sys.exit(1)

    available_nodes = df_dyn['node_label'].unique()
    if args.target_node not in available_nodes:
        args.target_node = available_nodes[0] if len(available_nodes) > 0 else "Unknown"

    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor(theme_cfg['ui_canvas']['background'])
    ax.set_facecolor(theme_cfg['ui_canvas']['background'])
    for spine in ax.spines.values(): spine.set_color(theme_cfg['ui_canvas']['grid_line'])

    other_node = available_nodes[1] if len(available_nodes) > 1 else available_nodes[0]
    df_target = df_dyn[df_dyn['node_label'] == args.target_node].set_index('t_idx')['velocity_v']
    df_other = df_dyn[df_dyn['node_label'] == other_node].set_index('t_idx')['velocity_v']
    
    df_scat = pd.DataFrame({'Target': df_target, 'Other': df_other}).dropna()
    if not df_scat.empty:
        sc = ax.scatter(df_scat['Other'], df_scat['Target'], c=df_scat.index, cmap='viridis', alpha=0.8, s=50, edgecolors='white', linewidth=0.5)
        ax.set_xlabel(f"Velocity: {other_node}", color=theme_cfg['ui_canvas']['text_primary'])
        ax.set_ylabel(f"Velocity: {args.target_node}", color=theme_cfg['ui_canvas']['text_primary'])
        ax.tick_params(colors=theme_cfg['ui_canvas']['grid_line'], labelcolor=theme_cfg['ui_canvas']['text_primary'])
        cbar = fig.colorbar(sc, ax=ax)
        cbar.set_label('Time Progression (t_idx)', color=theme_cfg['ui_canvas']['text_primary'])
        cbar.ax.yaxis.set_tick_params(color=theme_cfg['ui_canvas']['text_primary'], labelcolor=theme_cfg['ui_canvas']['text_primary'])

    plt.title(f"Classical Statistics: Phase Drift Scatter ({args.target_node} vs {other_node})", color=theme_cfg['ui_canvas']['text_primary'], fontweight='bold', pad=15)
    save_plot(fig, args.out_dir, args.filename or "000_0_2_2__scatter_drift.png")

if __name__ == "__main__": main()
