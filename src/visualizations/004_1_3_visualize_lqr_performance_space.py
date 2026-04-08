#!/usr/bin/env python3
# ==========================================
# 1_7_visualize_lqr_performance_space.py
# TLU System: LQR Performance Space
# Pattern B: Clean Scatter with Highlight-Synced Legend (Fail-Fast)
# ==========================================

import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("LQR Performance Space: Control Effort vs Final Error")
    parser.add_argument("--top_k", type=int, default=3, help="制御誤差の大きい最悪のノードをハイライト")
    parser.set_defaults(filename="21_control_lqr_performance_space.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    # フォールバックを駆逐し、厳格なキー参照を強制
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    bg_col = ui_canvas['legend_bg']
    edge_col = ui_canvas['legend_edge']
    grid_col = ui_canvas['grid_line']
    c_normal = ui_canvas['data_normal']

    c_outlier = theme_cfg['forensics']['colors']['z_score_shock']
    c_outlier_text = theme_cfg['forensics']['colors']['anomaly_outlier']

    df = pd.read_csv(sys.stdin)
    if df.empty: sys.exit(0)

    # コスト計算と最終誤差の結合
    df['abs_u'] = df['optimal_input_u'].abs()
    cost_df = df.groupby('node_idx')['abs_u'].sum().reset_index()
    max_t = df['t_idx'].max()
    gap_df = df[df['t_idx'] == max_t][['node_idx', 'state_error_x']]
    
    merged = pd.merge(cost_df, gap_df, on='node_idx')
    merged = merged[(merged['abs_u'] > 0) | (merged['state_error_x'] > 0)]

    N = int(df['node_idx'].max()) + 1
    idx_to_label = load_node_labels(args.node_map, N)

    fig, ax = plt.subplots(figsize=(14, 8))

    # 最悪の誤差を持つトップKをハイライト
    top_k_df = merged.nlargest(args.top_k, 'state_error_x')
    normals = merged.drop(top_k_df.index)
    top_k_indices = top_k_df['node_idx'].astype(int).tolist()

    # プロット描画 (ハードコード 'tab:purple' を c_normal へ置換)
    ax.scatter(normals['abs_u'], normals['state_error_x'], 
               color=c_normal, s=120, alpha=0.6, edgecolors=text_col)
    ax.scatter(top_k_df['abs_u'], top_k_df['state_error_x'], 
               color=c_outlier, s=300, alpha=0.9, edgecolors=text_col, marker='*')

    # プロットラベルの純化
    for _, row in top_k_df.iterrows():
        idx = int(row['node_idx'])
        ax.text(row['abs_u'], row['state_error_x'], f"  {idx:02d}", 
                color=c_outlier_text, fontsize=12, fontweight='bold', va='center', ha='left')
    for _, row in normals.iterrows():
        idx = int(row['node_idx'])
        ax.text(row['abs_u'], row['state_error_x'], f"  {idx:02d}", 
                color=text_col, fontsize=10, alpha=0.7, va='center', ha='left')

    # カスタム凡例（ハイライト同期）
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

    ax.set_title("LQR Performance Space: Control Effort vs Final Error", fontsize=15, color=text_col, fontweight='bold', pad=15)
    ax.set_xlabel("Cumulative Control Effort (sum |u|)", fontsize=12, color=text_col, labelpad=10)
    ax.set_ylabel("Final Absolute State Error at t_max", fontsize=12, color=text_col, labelpad=10)
    
    ax.margins(0.15)
    ax.grid(True, linestyle=':', alpha=0.4, color=grid_col)
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)

    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
