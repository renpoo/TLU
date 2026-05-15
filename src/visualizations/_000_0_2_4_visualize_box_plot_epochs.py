#!/usr/bin/env python3
import sys, argparse
import pandas as pd
import matplotlib.pyplot as plt
from src.visualizations.visualizer_utils import get_base_parser, apply_theme, save_plot
from src.visualizations.visualizer_data_utils import extract_box_plot_epochs

def main():
    parser = get_base_parser("Classical Stats: Box Plot Epochs")
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

    df_target_full = df_dyn[df_dyn['node_label'] == args.target_node]
    epochs_dict = extract_box_plot_epochs(df_target_full, n_epochs=3)
    
    if epochs_dict:
        epoch_data = [epochs_dict[k].dropna().values for k in epochs_dict.keys()]
        bp = ax.boxplot(epoch_data, patch_artist=True, tick_labels=list(epochs_dict.keys()))
        for box in bp['boxes']:
            box.set(facecolor=theme_cfg['ui_canvas']['graph_bg'], alpha=0.6, color=theme_cfg['ui_canvas']['grid_line'])
        for whisker in bp['whiskers']:
            whisker.set(color=theme_cfg['ui_canvas']['text_primary'], linewidth=1.5)
        for cap in bp['caps']:
            cap.set(color=theme_cfg['ui_canvas']['text_primary'], linewidth=1.5)
        for median in bp['medians']:
            median.set(color='tab:red', linewidth=2)
        for flier in bp['fliers']:
            flier.set(marker='o', color='red', alpha=0.5)
            
        ax.set_ylabel('Velocity Spread', color=theme_cfg['ui_canvas']['text_primary'])
        ax.tick_params(colors=theme_cfg['ui_canvas']['grid_line'], labelcolor=theme_cfg['ui_canvas']['text_primary'])

    plt.title(f"Classical Statistics: Regime Evolution Box Plot ({args.target_node})", color=theme_cfg['ui_canvas']['text_primary'], fontweight='bold', pad=15)
    save_plot(fig, args.out_dir, args.filename or "000_0_2_4__box_plot_epochs.png")

if __name__ == "__main__": main()
