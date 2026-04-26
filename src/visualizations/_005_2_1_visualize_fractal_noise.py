#!/usr/bin/env python3
# ==========================================
# _005_2_1_visualize_fractal_noise.py
# TLU System: Fractal Dimensionality & 1/f Noise Visualizer
# ==========================================
import sys
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Fractal Noise Bar Chart")
    parser.set_defaults(filename="005_2_1_fractal_noise_spectrum.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    
    df = pd.read_csv(sys.stdin)
    if df.empty:
        sys.exit(0)

    # Load node labels
    N = int(df['node_idx'].max()) + 1
    idx_to_label = load_node_labels(args.node_map, N)
    
    df['node_label'] = df['node_idx'].map(lambda i: f"{i:02d}: {idx_to_label.get(i, f'N_{i}')}")
    
    # Sort by beta for better visualization
    df = df.sort_values(by='spectral_exponent_beta', ascending=True)

    fig, ax = plt.subplots(figsize=(12, 8))
    
    colors = []
    for cls in df['noise_classification']:
        if cls == 'Pink Noise':
            colors.append('#ff1493') # Deep pink
        elif cls == 'White Noise':
            colors.append('#00bfff') # Deep sky blue
        elif cls == 'Brown Noise':
            colors.append('#8b4513') # Saddle brown
        else:
            colors.append('#888888')

    bars = ax.barh(df['node_label'], df['spectral_exponent_beta'], color=colors, edgecolor='none')
    
    # Draw classification boundaries
    ax.axvline(x=0.5, color='#aaaaaa', linestyle='--', alpha=0.7, zorder=0)
    ax.axvline(x=1.5, color='#aaaaaa', linestyle='--', alpha=0.7, zorder=0)
    
    # Annotate zones
    ymin, ymax = ax.get_ylim()
    ax.text(0.25, ymax, 'White Noise\n(< 0.5)', color='#00bfff', ha='center', va='bottom', fontsize=10, weight='bold')
    ax.text(1.0, ymax, 'Pink Noise\n(0.5 - 1.5)', color='#ff1493', ha='center', va='bottom', fontsize=10, weight='bold')
    ax.text(1.75, ymax, 'Brown Noise\n(> 1.5)', color='#8b4513', ha='center', va='bottom', fontsize=10, weight='bold')

    ax.set_title("System Memory & Complexity (1/f Noise Spectrum)", fontsize=16, color=text_col, pad=20)
    ax.set_xlabel(r"Spectral Exponent $\beta$", fontsize=12, color=text_col)
    ax.set_ylabel("Node", fontsize=12, color=text_col)
    
    ax.tick_params(colors=text_col)
    
    # Value labels
    for bar in bars:
        width = bar.get_width()
        x_pos = width + 0.05 if width >= 0 else width - 0.05
        ha = 'left' if width >= 0 else 'right'
        ax.text(x_pos, bar.get_y() + bar.get_height()/2, f"{width:.2f}", 
                va='center', ha=ha, color=text_col, fontsize=10)

    # Adjust x limits to give space for labels
    xmin, xmax = ax.get_xlim()
    ax.set_xlim(min(xmin, -0.5), max(xmax, 2.5))
    
    plt.tight_layout()
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
