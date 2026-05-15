#!/usr/bin/env python3
import sys, argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.visualizations.visualizer_utils import get_base_parser, apply_theme, save_plot
from src.visualizations.visualizer_data_utils import extract_histogram_data

def main():
    parser = get_base_parser("Classical Stats: Histogram KDE")
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

    target_vel = df_dyn[df_dyn['node_label'] == args.target_node]['velocity_v']
    clean_data, outliers = extract_histogram_data(target_vel, z_thresh=3.0)
    
    if not clean_data.empty:
        sns.histplot(clean_data, kde=True, ax=ax, color=theme_cfg['kinematics']['colors']['velocity_v'], stat='density', alpha=0.5, edgecolor=theme_cfg['ui_canvas']['background'])
        if not outliers.empty:
            ax.scatter(outliers, np.zeros_like(outliers), color='red', marker='x', s=100, linewidth=2, label='Z > 3.0 Outlier (Fat Tail)')
            ax.legend(facecolor=theme_cfg['ui_canvas']['background'], edgecolor=theme_cfg['ui_canvas']['grid_line'], labelcolor=theme_cfg['ui_canvas']['text_primary'])
        
        ax.set_xlabel('Velocity (Flux)', color=theme_cfg['ui_canvas']['text_primary'])
        ax.set_ylabel('Probability Density', color=theme_cfg['ui_canvas']['text_primary'])
        ax.tick_params(colors=theme_cfg['ui_canvas']['grid_line'], labelcolor=theme_cfg['ui_canvas']['text_primary'])

    plt.title(f"Classical Statistics: Distribution & Fat Tails ({args.target_node})", color=theme_cfg['ui_canvas']['text_primary'], fontweight='bold', pad=15)
    save_plot(fig, args.out_dir, args.filename or "000_0_2_3__histogram_kde.png")

if __name__ == "__main__": main()
