#!/usr/bin/env python3
# ==========================================
# 1_13_visualize_sensitivity_analysis_series_heatmaps.py
# TLU System: Sensitivity Analysis -- Neumann Series -- Propagation (Echo Matrix Expansion)
# ==========================================
import sys
import numpy as np
import pandas as pd
import seaborn as sns
import japanize_matplotlib
import matplotlib.pyplot as plt
import os

from src.visualizations.visualizer_utils import get_base_parser, apply_theme, load_node_labels, save_plot

def setup_argparser():
    parser = get_base_parser("Sensitivity Analysis Series Propagation Heatmap")
    parser.add_argument("--gamma", type=float, default=0.85, help="減衰率 (Discount Factor)")
    parser.add_argument("--t_target", type=int, default=None, help="解析対象のタイムステップ (未指定なら全時刻t_idxを処理)")
    parser.add_argument("--epsilon", type=float, default=1e-5, help="零行列とみなす閾値")
    parser.set_defaults(filename="1_13_2__sensitivity_analysis_series_heatmap.png")
    return parser

def compute_transition_matrix(T_matrix):
    """ Tテンソルから推移確率行列Pを計算 """
    outflow = np.sum(T_matrix, axis=1)
    outflow_col = outflow[:, np.newaxis]
    P_matrix = np.zeros_like(T_matrix, dtype=float)
    return np.divide(T_matrix, outflow_col, out=P_matrix, where=outflow_col != 0)

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    theme_cfg = apply_theme(args.theme) or {}
    ui_canvas = theme_cfg.get('ui_canvas', {})
    text_col = ui_canvas.get('text_primary', 'white')
    bg_col = ui_canvas.get('background', 'black')
    
    cmap_name = theme_cfg.get('topology_and_correlation', {}).get('colormaps', {}).get('lag_matrix_map', 'viridis')

    df = pd.read_csv(sys.stdin)
    if df.empty: sys.exit(0)

    N = int(max(df['src_idx'].max(), df['tgt_idx'].max())) + 1
    labels = load_node_labels(args.node_map, N)
    axis_labels = [f"{i:02d}: {labels.get(i, f'N_{i}')}" for i in range(N)]

    # ターゲット時刻のリストを作成 (指定がなければ全時刻)
    if args.t_target is not None:
        target_t_list = [args.t_target]
    else:
        target_t_list = sorted(df['t_idx'].unique())

    # 実時間 (t) のループ
    for target_t in target_t_list:
        df_t = df[df['t_idx'] == target_t]
        
        # 遷移テンソル T の構築
        T_matrix = np.zeros((N, N))
        for _, row in df_t.iterrows():
            T_matrix[int(row['src_idx']), int(row['tgt_idx'])] += float(row['value'])

        # 推移確率行列 P の構築
        P_matrix = compute_transition_matrix(T_matrix)

        # 仮想波及時間 (k: ノイマン級数の各項) のループ
        k = 0
        current_P = np.eye(N) # k=0 は単位行列 I
        
        while True:
            M_k = (args.gamma ** k) * current_P
            
            # 零行列化（波及の完全消滅）を判定
            if k > 0 and np.sum(M_k) < args.epsilon:
                print(f"Propagation fully decayed at t={target_t}, k={k}. Stopping visualization for this time step.", file=sys.stderr)
                break
                
            # ★ 修正: k=0 (単位行列) は構造情報を持たないため描画をスキップする
            if k >= 0:
                fig, ax = plt.subplots(figsize=(12, 10))
                
                sns.heatmap(M_k, ax=ax, cmap=cmap_name, vmin=0.0, vmax=1.0,
                            xticklabels=axis_labels, yticklabels=axis_labels,
                            cbar_kws={'label': f'Impact Intensity (gamma={args.gamma})'})
                            
                ax.set_title(f"Sensitivity Analysis Series Propagation: Order k={k}\n(Time Step: {target_t})", 
                             fontsize=16, color=text_col, pad=20, fontweight='bold')
                ax.set_xlabel("Target Node (Impact Received)", color=text_col, fontsize=12)
                ax.set_ylabel("Source Node (Shock Origin)", color=text_col, fontsize=12)
                ax.tick_params(axis='x', rotation=45, colors=text_col)
                ax.tick_params(axis='y', rotation=0, colors=text_col)
                ax.set_facecolor(bg_col)
                
                plt.subplots_adjust(bottom=0.25, left=0.25, right=0.95, top=0.9)
                
                # ★ 修正: ファイル名を k 優先の連番に変更 (OSでのソートを劇的に改善)
                base_name, ext = os.path.splitext(args.filename)
                out_name = f"{base_name.replace('.png', '')}.k.{k:05d}.t.{target_t:05d}{ext}"
                
                save_plot(fig, args.out_dir, out_name)
                plt.close(fig)

            # 次のステップへ (P^(k+1) = P^k * P)
            current_P = np.dot(current_P, P_matrix)
            k += 1
            
            # 安全装置
            if k > 20:
                print(f"Reached maximum expansion order (k=20) at t={target_t}. Stopping.", file=sys.stderr)
                break

if __name__ == "__main__":
    main()
