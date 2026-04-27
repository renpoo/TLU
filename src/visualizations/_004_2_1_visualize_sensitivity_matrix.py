#!/usr/bin/env python3
# ==========================================
# 1_13_visualize_sensitivity_matrix.py
# TLU System: Sensitivity Trade-off Matrix
# Strict Theme Mode (Fail-Fast)
# ==========================================
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Sensitivity Trade-off Matrix: Ripple vs Strain")
    parser.add_argument("--top_k", type=int, default=3, help="Number of singular points to highlight")
    parser.set_defaults(filename="1_80_1__sensitivity_matrix.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    
    # Strict theme reference
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    bg_col = ui_canvas['legend_bg']
    edge_col = ui_canvas['legend_edge']
    grid_col = ui_canvas['grid_line']
    c_normal = ui_canvas['data_normal']
    
    # Borrow warning colors from the forensics domain (to paint high-risk nodes)
    c_danger = theme_cfg['forensics']['colors']['z_score_shock']

    df = pd.read_csv(sys.stdin)
    if df.empty: sys.exit(0)

    # Extract data of the latest time
    max_t = df['t_idx'].max()
    df_latest = df[df['t_idx'] == max_t].copy()

    N = int(df_latest['node_idx'].max()) + 1
    idx_to_label = load_node_labels(args.node_map, N)

    fig, ax = plt.subplots(figsize=(14, 9))

    # X: Ripple effect (FK), Y: Strain (IK)
    x_data = df_latest['fk_total_ripple']
    y_data = df_latest['ik_strain_energy']
    
    # Divide into 4 quadrants by the median
    x_med = np.median(x_data)
    y_med = np.median(y_data)

    # Highlight conditions: Small ripple but large strain (top left), or extremely large ripple (bottom right)
    top_nodes = df_latest.nlargest(args.top_k, 'ik_strain_energy')['node_idx'].tolist() + \
                df_latest.nlargest(args.top_k, 'fk_total_ripple')['node_idx'].tolist()
    top_nodes = list(set(top_nodes))

    for _, row in df_latest.iterrows():
        idx = int(row['node_idx'])
        is_top = idx in top_nodes
        color = c_danger if is_top else c_normal
        size = 300 if is_top else 100
        alpha = 0.9 if is_top else 0.5
        marker = '*' if is_top else 'o'
        
        ax.scatter(row['fk_total_ripple'], row['ik_strain_energy'], 
                   color=color, s=size, alpha=alpha, edgecolors=text_col, marker=marker)
        
        if is_top:
            ax.text(row['fk_total_ripple'], row['ik_strain_energy'], f"  {idx:02d}", 
                    color=c_danger, fontsize=12, fontweight='bold', va='center', ha='left')
        else:
            ax.text(row['fk_total_ripple'], row['ik_strain_energy'], f"  {idx:02d}", 
                    color=text_col, fontsize=9, alpha=0.6, va='center', ha='left')

    # Boundaries of quadrants
    ax.axvline(x_med, color=grid_col, linestyle='--', alpha=0.5)
    ax.axhline(y_med, color=grid_col, linestyle='-.', alpha=0.5)

    ax.set_title("Management Trade-off Matrix: Impact (FK) vs Cost (IK)", fontsize=16, color=text_col, fontweight='bold', pad=15)
    ax.set_xlabel("Total Ripple Effect [FK] (Leverage & ROI)", fontsize=12, color=text_col, labelpad=10)
    ax.set_ylabel("Strain Energy [IK] (Friction & Cost)", fontsize=12, color=text_col, labelpad=10)
    
    # quadrant annotations
    ax.text(x_med * 0.1, y_med * 1.5, "Bad Idea\n(High Cost, Low ROI)", color=text_col, alpha=0.5, fontsize=10, ha='left')
    ax.text(x_med * 1.5, y_med * 0.1, "Quick Win\n(Low Cost, High ROI)", color=text_col, alpha=0.5, fontsize=10, ha='left')

    ax.grid(True, linestyle=':', alpha=0.4, color=grid_col)
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)

    # Legend
    handles, legend_labels = [], []
    display_count = min(N, args.max_legend)
    for i in range(display_count):
        handles.append(mpatches.Patch(color='none'))
        legend_labels.append(f"{i:02d} : {idx_to_label.get(i, f'Node_{i}')}")
    if N > args.max_legend:
        handles.append(mpatches.Patch(color='none'))
        legend_labels.append(f"... and {N - args.max_legend} more nodes")

    leg = ax.legend(handles, legend_labels, title="Node Map (Index -> Name):\n" + "-"*30,
                    loc='center left', bbox_to_anchor=(1.02, 0.5),
                    facecolor=bg_col, edgecolor=edge_col,
                    handlelength=0, handletextpad=0, prop={'family': 'monospace', 'size': 10})
    plt.setp(leg.get_title(), color=text_col, family='monospace')

    for text_obj in leg.get_texts():
        text_str = text_obj.get_text()
        if ":" in text_str:
            idx_str = text_str.split(":")[0].strip()
            if idx_str.isdigit() and int(idx_str) in top_nodes:
                text_obj.set_color(c_danger)
                text_obj.set_fontweight('bold')
            else:
                text_obj.set_color(text_col)
        else:
            text_obj.set_color(text_col)
    plt.subplots_adjust(right=0.75)
    
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
