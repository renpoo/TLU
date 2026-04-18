#!/usr/bin/env python3
# ==========================================
# 000_1_7_visualize_inertia_viscosity.py
# TLU System: Dynamics Phase Space (Inertia vs Viscosity)
# Pattern B: Clean Scatter with Strict Theme Mode (Fail-Fast)
# ==========================================
import sys
import numpy as np
import pandas as pd
import japanize_matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Import common visualization infrastructure
from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Dynamics Phase Space: Inertia vs Viscosity Scatter Plot")
    parser.add_argument("--top_k", type=int, default=3, help="Number of singular points to highlight")
    parser.set_defaults(filename="1_3_7_inertia_viscosity_scatter.png") 
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    # Eliminate fallbacks and enforce strict key reference (Fail-Fast)
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    legend_bg_col = ui_canvas['legend_bg']
    legend_edge_col = ui_canvas['legend_edge']
    grid_line_col = ui_canvas['grid_line']
    
    # [Additional Requirement] Universal plot color for normal data (enforce addition to JSON side)
    c_normal = ui_canvas['data_normal']

    forensics_colors = theme_cfg['forensics']['colors']
    c_outlier = forensics_colors['z_score_shock']
    c_outlier_text = forensics_colors['anomaly_outlier']

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr); sys.exit(1)
        
    if df.empty: sys.exit(0)

    # Take the time average
    df_mean = df.groupby('node_idx').mean().reset_index()

    # Convert viscosity (C) to logarithmic scale
    df_mean['log_C'] = np.log10(np.where(df_mean['viscosity_C'] <= 0, 1e-6, df_mean['viscosity_C']))

    N = int(df_mean['node_idx'].max()) + 1
    idx_to_label = load_node_labels(args.node_map, N)

    # Set a landscape canvas to secure the legend area
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Highlight top mass M as singular points
    top_k_df = df_mean.nlargest(args.top_k, 'inertia_M')
    normals = df_mean.drop(top_k_df.index)

    # Plot normal nodes (purge hardcoded 'tab:blue')
    ax.scatter(normals['inertia_M'], normals['log_C'], 
               color=c_normal, s=120, alpha=0.7, edgecolors=text_col, linewidths=1.0)
    
    # Plot singular points (heavy nodes) (star-shaped)
    ax.scatter(top_k_df['inertia_M'], top_k_df['log_C'], 
               color=c_outlier, s=300, alpha=0.9, edgecolors=text_col, marker='*', linewidths=1.2)

    # Purify plot labels
    for _, row in top_k_df.iterrows():
        idx = int(row['node_idx'])
        ax.text(row['inertia_M'], row['log_C'], f"  {idx:02d}", 
                color=c_outlier_text, fontsize=12, fontweight='bold', va='bottom', ha='left')
                
    for _, row in normals.iterrows():
        idx = int(row['node_idx'])
        ax.text(row['inertia_M'], row['log_C'], f"  {idx:02d}", 
                color=text_col, fontsize=10, alpha=0.9, va='bottom', ha='left')

    # External legend (Node Map) highlight-supported version
    top_k_indices = top_k_df['node_idx'].astype(int).tolist()
    
    handles = []
    labels = []
    display_count = min(N, args.max_legend)
    
    for i in range(display_count):
        label_str = idx_to_label.get(i, f"Node_{i}")
        handles.append(mpatches.Patch(color='none'))
        labels.append(f"{i:02d} : {label_str}")
        
    if N > args.max_legend:
        handles.append(mpatches.Patch(color='none'))
        labels.append(f"... and {N - args.max_legend} more nodes")

    leg = ax.legend(handles, labels, 
                    title="Node Map (Index -> Name):\n" + "-"*28,
                    loc='center left', bbox_to_anchor=(1.02, 0.5),
                    facecolor=legend_bg_col, edgecolor=legend_edge_col,
                    handlelength=0, handletextpad=0, 
                    prop={'family': 'monospace', 'size': 10})
                    
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

    ax.set_xlabel('Inertia (M) - Mass & Scale', fontsize=12, color=text_col, labelpad=10)
    ax.set_ylabel('Viscosity (Log10 C) - Friction & Resistance', fontsize=12, color=text_col, labelpad=10)
    ax.set_title('Dynamics Phase Space: Inertia vs Viscosity (Bottleneck Identification)', fontsize=15, color=text_col, fontweight='bold', pad=15)
    
    ax.margins(0.15)
    ax.grid(True, linestyle=':', alpha=0.6, color=grid_line_col)
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)

    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
