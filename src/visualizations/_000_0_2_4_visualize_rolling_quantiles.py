#!/usr/bin/env python3
import sys, argparse
import pandas as pd
import matplotlib.pyplot as plt
from src.visualizations.visualizer_utils import get_base_parser, apply_theme, save_plot, apply_smart_x_labels
from src.visualizations.visualizer_data_utils import extract_rolling_quantiles

def main():
    parser = get_base_parser("Classical Stats: Rolling Quantile Bands")
    parser.add_argument("--target_node", type=str, default="US10Y")
    parser.add_argument("--window_size", type=int, default=12)
    args = parser.parse_args()
    theme_cfg = apply_theme(args.theme)

    try:
        df_dyn = pd.read_csv(sys.stdin)
    except Exception:
        sys.exit(1)

    available_nodes = df_dyn['node_label'].unique()
    if args.target_node not in available_nodes:
        args.target_node = available_nodes[0] if len(available_nodes) > 0 else "Unknown"

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor(theme_cfg['ui_canvas']['background'])
    ax.set_facecolor(theme_cfg['ui_canvas']['background'])
    for spine in ax.spines.values(): spine.set_color(theme_cfg['ui_canvas']['grid_line'])

    df_target = df_dyn[df_dyn['node_label'] == args.target_node]
    df_roll = extract_rolling_quantiles(df_target, window=args.window_size)
    
    if not df_roll.empty:
        t_vals = df_roll['t_idx'].values
        
        # Draw Whisker Bounds (Min/Max or 1.5 IQR)
        ax.fill_between(t_vals, df_roll['whisker_low'], df_roll['whisker_high'], 
                        color=theme_cfg['ui_canvas']['grid_line'], alpha=0.3, label=f'Whiskers (Rolling {args.window_size})')
        
        # Draw IQR Box (25th to 75th percentile)
        ax.fill_between(t_vals, df_roll['q25'], df_roll['q75'], 
                        color=theme_cfg['ui_canvas']['text_primary'], alpha=0.5, label='IQR (25th - 75th)')
        
        # Draw Median
        ax.plot(t_vals, df_roll['median'], color='tab:red', lw=2, label='Median')
        
        # Draw the actual scattered data points
        ax.scatter(t_vals, df_roll['velocity_v'], color=theme_cfg['kinematics']['colors']['velocity_v'], 
                   alpha=0.6, s=20, label='Actual Velocity')
            
        ax.set_ylabel('Velocity (Flux)', color=theme_cfg['ui_canvas']['text_primary'])
        ax.tick_params(colors=theme_cfg['ui_canvas']['grid_line'], labelcolor=theme_cfg['ui_canvas']['text_primary'])
        ax.legend(facecolor=theme_cfg['ui_canvas']['background'], edgecolor=theme_cfg['ui_canvas']['grid_line'], labelcolor=theme_cfg['ui_canvas']['text_primary'])
        
        # Smart X Labels matching the non-NaN t_vals exactly
        time_labels = df_dyn[['t_idx', 'time_label']].drop_duplicates()
        df_roll_labels = pd.merge(df_roll, time_labels, on='t_idx', how='left')
        apply_smart_x_labels(ax, t_vals, df_roll_labels['time_label'].values, theme_cfg['ui_canvas']['text_primary'], max_labels=15)

    plt.title(f"Classical Statistics: Continuous Rolling Box Plot ({args.target_node})", color=theme_cfg['ui_canvas']['text_primary'], fontweight='bold', pad=15)
    save_plot(fig, args.out_dir, args.filename or "000_0_2_4__rolling_quantiles.png")

if __name__ == "__main__": main()
