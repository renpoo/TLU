#!/usr/bin/env python3
# ==========================================
# 002_1_2_visualize_info_stress_scatter.py
# TLU System: Structural Stress Matrix (Density vs Curvature)
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Structural Stress Matrix: Density vs Curvature")
    parser.add_argument("--top_k", type=int, default=3, help="ハイライトする危険特異点の数")
    parser.set_defaults(filename="26_info_stress_scatter.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    # フォールバック排除
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    bg_col = ui_canvas['legend_bg']
    edge_col = ui_canvas['legend_edge']
    grid_col = ui_canvas['grid_line']
    
    c_normal = ui_canvas['data_normal']
    
    # 以前の Forensics からの Context Bleed を解消。
    # 意図的なFail-fastのため、情報幾何学ドメイン用のキーを要求する。
    info_colors = theme_cfg['information_geometry']['colors']
    c_danger = info_colors['stress_outlier']
    c_danger_text = info_colors['stress_outlier_text']

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading from standard input: {e}", file=sys.stderr); sys.exit(1)
        
    if df.empty: sys.exit(0)

    df_mean = df.groupby('node_idx').mean().reset_index()
    N = int(df_mean['node_idx'].max()) + 1
    idx_to_label = load_node_labels(args.node_map, N)

    fig, ax = plt.subplots(figsize=(14, 8))

    df_mean['stress_score'] = df_mean['density'] * df_mean['curvature']
    top_k_df = df_mean.nlargest(args.top_k, 'stress_score')
    normals = df_mean.drop(top_k_df.index)
    top_k_indices = top_k_df['node_idx'].astype(int).tolist()

    ax.scatter(normals['density'], normals['curvature'], 
               color=c_normal, s=120, alpha=0.6, edgecolors=text_col)
    ax.scatter(top_k_df['density'], top_k_df['curvature'], 
               color=c_danger, s=300, alpha=0.9, edgecolors=text_col, marker='*')

    for _, row in top_k_df.iterrows():
        idx = int(row['node_idx'])
        ax.text(row['density'], row['curvature'], f"  {idx:02d}", 
                color=c_danger_text, fontsize=12, fontweight='bold', va='center', ha='left')
    for _, row in normals.iterrows():
        idx = int(row['node_idx'])
        ax.text(row['density'], row['curvature'], f"  {idx:02d}", 
                color=text_col, fontsize=10, alpha=0.7, va='center', ha='left')

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
                text_obj.set_color(c_danger_text)
                text_obj.set_fontweight('bold')
            else:
                text_obj.set_color(text_col)
        else:
            text_obj.set_color(text_col)

    plt.subplots_adjust(right=0.77, left=0.1, top=0.9, bottom=0.1)

    ax.set_title("Structural Stress Matrix: Information Density vs Curvature", fontsize=15, color=text_col, fontweight='bold', pad=15)
    ax.set_xlabel("Metric Density (Average Transaction Volume)", fontsize=12, color=text_col, labelpad=10)
    ax.set_ylabel("Information Curvature (Average Structural Distortion)", fontsize=12, color=text_col, labelpad=10)
    
    ax.margins(0.15)
    ax.grid(True, linestyle=':', alpha=0.4, color=grid_col)
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)

    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
