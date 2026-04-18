#!/usr/bin/env python3
# ==========================================
# 1_6_visualize_local_thermo_scatter.py
# TLU System: Local Thermodynamics Portfolio (Scatter Plots)
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Local Thermodynamics Phase Space: Scale vs Volatility/Complexity")
    parser.add_argument("--mode", type=str, choices=['temperature', 'entropy', 'gradient'], required=True, 
                        help="Select metric for Y-axis (temperature=volatility, entropy=complexity, gradient=thermal-friction)")
    parser.add_argument("--top_k", type=int, default=3, help="Number of singular points to highlight")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    # Eliminate fallbacks and enforce strict key reference (Fail-Fast)
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    bg_col = ui_canvas['legend_bg']
    edge_col = ui_canvas['legend_edge']
    grid_col = ui_canvas['grid_line']
    
    # Strictly require universal plot color for normal data
    c_normal = ui_canvas['data_normal']

    forensics_colors = theme_cfg['forensics']['colors']
    c_outlier = forensics_colors['z_score_shock']
    c_outlier_text = forensics_colors['anomaly_outlier']

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading from standard input: {e}", file=sys.stderr); sys.exit(1)
        
    if df.empty: sys.exit(0)

    df_mean = df.groupby('node_idx').mean().reset_index()
    N = int(df_mean['node_idx'].max()) + 1
    idx_to_label = load_node_labels(args.node_map, N)

    fig, ax = plt.subplots(figsize=(14, 8))

    x_data = df_mean['local_internal_energy_u']
    x_label = 'Local Internal Energy ($u_i$) - Scale & Volume'
    
    if args.mode == 'temperature':
        y_data = np.log10(np.where(df_mean['local_temperature_t'] <= 0, 1e-6, df_mean['local_temperature_t']))
        y_label = 'Local Temperature (Log10 $t_i$) - Volatility'
        title = 'Local Thermo Portfolio: Scale vs Volatility (Risk Identification)'
        highlight_metric = 'local_temperature_t' 
    elif args.mode == 'entropy':
        y_data = df_mean['local_entropy_s']
        y_label = 'Local Entropy ($s_i$) - Complexity & Dispersion'
        title = 'Local Thermo Portfolio: Scale vs Complexity (Hub Identification)'
        highlight_metric = 'local_entropy_s' 
    else: # gradient
        y_data = df_mean['local_grad_t']
        y_label = 'Local Temperature Gradient ($\\nabla t_i$) - Friction & Force'
        title = 'Local Thermo Portfolio: Scale vs Thermal Gradient (Bottleneck Identification)'
        highlight_metric = 'local_grad_t'

    df_mean['plot_y'] = y_data
    top_k_df = df_mean.nlargest(args.top_k, highlight_metric)
    normals = df_mean.drop(top_k_df.index)
    top_k_indices = top_k_df['node_idx'].astype(int).tolist()

    # Plot normal nodes (Replace hardcoded 'tab:blue' with c_normal)
    ax.scatter(normals['local_internal_energy_u'], normals['plot_y'], 
               color=c_normal, s=120, alpha=0.6, edgecolors=text_col)
               
    # Plot singular points (heavy nodes)
    ax.scatter(top_k_df['local_internal_energy_u'], top_k_df['plot_y'], 
               color=c_outlier, s=300, alpha=0.9, edgecolors=text_col, marker='*')

    # Purify plot labels
    for _, row in top_k_df.iterrows():
        idx = int(row['node_idx'])
        ax.text(row['local_internal_energy_u'], row['plot_y'], f"  {idx:02d}", 
                color=c_outlier_text, fontsize=12, fontweight='bold', va='center', ha='left')
    for _, row in normals.iterrows():
        idx = int(row['node_idx'])
        ax.text(row['local_internal_energy_u'], row['plot_y'], f"  {idx:02d}", 
                color=text_col, fontsize=10, alpha=0.7, va='center', ha='left')

    # Custom legend (Highlight sync)
    handles, labels = [], []
    display_count = min(N, args.max_legend)
    for i in range(display_count):
        handles.append(mpatches.Patch(color='none'))
        labels.append(f"{i:02d} : {idx_to_label.get(i, f'Node_{i}')}")
    if N > args.max_legend:
        handles.append(mpatches.Patch(color='none'))
        labels.append(f"... and {N - args.max_legend} more nodes")

    leg = ax.legend(handles, labels, title="Node Map (Index -> Name):\n" + "-"*30,
                    loc='center left', bbox_to_anchor=(1.02, 0.5),
                    facecolor=bg_col, edgecolor=edge_col,
                    handlelength=0, handletextpad=0, prop={'family': 'monospace', 'size': 10})
    plt.setp(leg.get_title(), color=text_col, family='monospace')

    for text_obj in leg.get_texts():
        text_str = text_obj.get_text()
        if ":" in text_str:
            idx_str = text_str.split(":")[0].strip()
            if idx_str.isdigit() and int(idx_str) in top_k_indices:
                text_obj.set_color(c_outlier_text)
                text_obj.set_fontweight('bold')
            else:
                text_obj.set_color(text_col)
        else:
            text_obj.set_color(text_col)
             
    plt.subplots_adjust(right=0.77, left=0.1, top=0.9, bottom=0.1)

    ax.set_xlabel(x_label, fontsize=12, color=text_col, labelpad=10)
    ax.set_ylabel(y_label, fontsize=12, color=text_col, labelpad=10)
    ax.set_title(title, fontsize=15, color=text_col, fontweight='bold', pad=15)
    
    ax.margins(0.15)
    ax.grid(True, linestyle=':', alpha=0.4, color=grid_col)
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)

    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
