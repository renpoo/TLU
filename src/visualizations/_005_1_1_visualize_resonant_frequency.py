#!/usr/bin/env python3
# ==========================================
# _005_1_1_visualize_resonant_frequency.py
# TLU System: Resonant Frequency Visualization
# ==========================================
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Resonant Frequency & Spectral Power")
    parser.set_defaults(filename="005_1_1_resonant_frequency.png")
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
    
    # Use a colormap for power
    cmap_name = theme_cfg['thermodynamics']['colormaps']['volatility_T_map']

    df = pd.read_csv(sys.stdin)
    if df.empty: sys.exit(0)

    # Convert frequency to period (weeks in this case, since 1 step = 1 week)
    # Avoid division by zero
    df['period'] = np.where(df['dominant_frequency'] > 0, 1.0 / df['dominant_frequency'], 0)
    
    # Sort by node index for standard order
    df = df.sort_values('node_idx')

    N = int(df['node_idx'].max()) + 1
    labels = load_node_labels(args.node_map, N)
    
    node_names = [f"{int(row['node_idx']):02d}: {labels.get(int(row['node_idx']), '')}" for _, row in df.iterrows()]
    periods = df['period'].values
    powers = df['spectral_power'].values

    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Normalize powers for coloring
    norm = Normalize(vmin=0, vmax=max(powers))
    cmap = plt.get_cmap(cmap_name)
    colors = [cmap(norm(p)) for p in powers]
    
    # Create horizontal bar chart
    y_pos = np.arange(len(node_names))
    bars = ax.barh(y_pos, periods, color=colors, edgecolor=edge_col)
    
    # Invert y-axis so Node 0 is at the top
    ax.invert_yaxis()
    
    # Label the axes
    ax.set_yticks(y_pos)
    ax.set_yticklabels(node_names, fontsize=10, color=text_col)
    ax.set_xlabel('Resonant Period (Weeks)', fontsize=12, color=text_col)
    ax.set_title('Node Resonant Frequencies (Cycle Lengths) & Spectral Power', fontsize=15, color=text_col)
    
    # Add data labels
    for i, (bar, p) in enumerate(zip(bars, periods)):
        if p > 0:
            ax.text(p + 0.5, i, f'{p:.1f} wks', va='center', color=text_col, fontweight='bold')
    
    # Add a colorbar for Spectral Power
    sm = ScalarMappable(norm=norm, cmap=cmap)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, orientation='vertical', pad=0.02)
    cbar.set_label('Spectral Power (Energy)', color=text_col, fontsize=12)
    cbar.ax.yaxis.set_tick_params(color=text_col)
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color=text_col)
    
    ax.grid(True, axis='x', linestyle=':', alpha=0.5, color=grid_col)
    ax.tick_params(colors=text_col)
    
    plt.tight_layout()
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
