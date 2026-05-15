#!/usr/bin/env python3
import sys, os, argparse
import pandas as pd
import matplotlib.pyplot as plt
from src.visualizations.visualizer_utils import get_base_parser, apply_theme, save_plot, apply_smart_x_labels
from src.visualizations.visualizer_data_utils import extract_stacked_bar_data

def main():
    parser = get_base_parser("Classical Stats: Stacked Bar")
    args = parser.parse_args()
    theme_cfg = apply_theme(args.theme)

    try:
        df_dyn = pd.read_csv(sys.stdin)
    except Exception as e:
        sys.exit(1)

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(theme_cfg['ui_canvas']['background'])
    ax.set_facecolor(theme_cfg['ui_canvas']['background'])
    for spine in ax.spines.values(): spine.set_color(theme_cfg['ui_canvas']['grid_line'])

    df_stacked = extract_stacked_bar_data(df_dyn)
    if not df_stacked.empty:
        pivot_stacked = df_stacked.pivot(index='t_idx', columns='node_label', values='normalized_share').fillna(0)
        if len(pivot_stacked.columns) > 10:
            top_cols = pivot_stacked.sum().nlargest(9).index.tolist()
            pivot_stacked['Others'] = pivot_stacked.drop(columns=top_cols).sum(axis=1)
            pivot_stacked = pivot_stacked[top_cols + ['Others']]
            
        pivot_stacked.plot(kind='area', ax=ax, stacked=True, alpha=0.8, colormap='tab20', legend=False)
        ax.set_ylim(0, 1)
        ax.set_ylabel("Normalized Share (Velocity)", color=theme_cfg['ui_canvas']['text_primary'])
        ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), facecolor=theme_cfg['ui_canvas']['background'], labelcolor=theme_cfg['ui_canvas']['text_primary'])
        
        time_labels = df_dyn[['t_idx', 'time_label']].drop_duplicates().sort_values('t_idx')
        apply_smart_x_labels(ax, pivot_stacked.index.values, time_labels['time_label'].values, theme_cfg['ui_canvas']['text_primary'], max_labels=15)

    plt.title("Classical Statistics: Normalized System Structure (100% Stacked Bar)", color=theme_cfg['ui_canvas']['text_primary'], fontweight='bold', pad=15)
    save_plot(fig, args.out_dir, args.filename or "000_0_2_1__stacked_bar.png")

if __name__ == "__main__": main()
