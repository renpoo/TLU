#!/usr/bin/env python3
# ==========================================
# 000_2_1_visualize_structural_stiffness.py
# TLU System: Structural Stiffness Heatmap Visualizer
# Version: 8.0.0 (Symmetrical Logarithmic Normalization Applied)
# ==========================================
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import SymLogNorm
from tqdm import tqdm

from src.visualizations.visualizer_utils import *

def validate_theme_keys(theme_dict):
    """テーマファイルに転用可能な発散色カラーマップが存在するか厳格にチェックする"""
    try:
        _ = theme_dict['forensics']['colormaps']['z_score_heatmap']
    except KeyError as e:
        raise KeyError(f"[FAIL-FAST] Required fallback theme key is missing: {e}")

def setup_argparser():
    parser = get_base_parser("Structural Stiffness Heatmap (SymLog Scale)")
    parser.set_defaults(filename="1_14_1__structural_stiffness_symlog.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)
        
    if df.empty:
        print("[WARN] Received empty data stream.", file=sys.stderr)
        sys.exit(0)

    N = int(df['src_idx'].max() + 1)
    T_max = int(df['t_idx'].max()) + 1 if 't_idx' in df.columns else 1
    
    node_labels = load_node_labels(args.node_map, N)
    time_labels = load_time_labels(args.time_map, T_max)

    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    
    validate_theme_keys(theme_cfg) 

    # 正負の符号を維持した発散色（RdBu_r等）を適用
    cmap_stiffness = theme_cfg['forensics']['colormaps']['z_score_heatmap']
    vmax_p = theme_cfg.get("theme_robust_percentile", 95) 

    t_indices = sorted(df['t_idx'].unique())
    
    axis_labels = [f"{i:02d}: {node_labels.get(i, f'N_{i}')}" for i in range(N)]
    base_name, ext = os.path.splitext(args.filename)
    
    symlog_norm = SymLogNorm(
        linthresh=1e-1,
        vmin=-1e-3,
        vmax=1e-3, 
        base=10
    )

    K_matrix_list = []

    for t_idx in tqdm(t_indices, desc="Rendering SymLog Stiffness Heatmaps"):
        df_slice = df[df['t_idx'] == t_idx]
        
        K_matrix = np.zeros((N, N))
        for _, row in df_slice.iterrows():
            K_matrix[int(row['src_idx']), int(row['tgt_idx'])] = row['stiffness_k']

        # ロバスト・スケーリングの算出
        vmax_robust = np.percentile(np.abs(K_matrix), vmax_p)
        if vmax_robust == 0:
             vmax_robust = 1e-6 

        # --- SymLogNorm (対称対数正規化) の設定 ---
        # ゼロ付近で log(0) となり計算が破綻するのを防ぐための線形領域 (linthresh) を設定。
        # 最大オーダーの 1/10000 程度を境界とし、それ以上は対数スケールで描画する。
        linthresh = max(vmax_robust * 1e-4, 1e-15)
        
        symlog_norm = SymLogNorm(
            linthresh=min(linthresh, symlog_norm.linthresh), 
            vmin=-max(vmax_robust, symlog_norm.vmax), 
            vmax=max(vmax_robust, symlog_norm.vmax), 
            base=10
        )

        K_matrix_list.append(K_matrix)

    for t_idx in tqdm(t_indices, desc="Rendering SymLog Stiffness Heatmaps"):
        current_time_label = time_labels.get(t_idx, f"t={t_idx}")
        title = f"Structural Stiffness (Precision Matrix) [SymLog Scale]\nTimeline: {current_time_label}"
        
        fig, ax = plt.subplots(figsize=(14, 12))
        
        # draw_matrix_heatmap への委譲をやめ、SymLogNormを適用して直接描画する
        sns.heatmap(
            pd.DataFrame(K_matrix_list[t_idx]), 
            ax=ax, 
            cmap=cmap_stiffness, 
            norm=symlog_norm,  # 対称対数スケールを適用
            xticklabels=axis_labels, 
            yticklabels=axis_labels,
            cbar_kws={'label': "Stiffness / Precision (SymLog10 Scale)", 'extend': 'both'}
        )
        
        # 標準的なフォーマットの適用
        ax.set_title(title, fontsize=16, color=text_col, pad=20, fontweight='bold')
        ax.set_xlabel("Target Node (Effect)", color=text_col, fontsize=12)
        ax.set_ylabel("Source Node (Cause)", color=text_col, fontsize=12)
        ax.tick_params(axis='x', rotation=45, colors=text_col)
        ax.tick_params(axis='y', rotation=0, colors=text_col)
        
        plt.tight_layout()
        
        out_name = f"{base_name.replace('.png', '')}.t.{t_idx:05d}{ext}"
        save_plot(fig, args.out_dir, out_name)
        plt.close(fig)

if __name__ == "__main__":
    main()
