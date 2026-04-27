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
    """Strictly check if there is a divergent colormap that can be diverted to the theme file"""
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

    # Apply divergent color (e.g., RdBu_r) keeping positive/negative signs
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

        # Calculate robust scaling
        vmax_robust = np.percentile(np.abs(K_matrix), vmax_p)
        if vmax_robust == 0:
             vmax_robust = 1e-6 

        # --- SymLogNorm (Symmetric Logarithmic Normalization) Settings ---
        # Set a linear region (linthresh) to prevent calculation breakdown due to log(0) near zero.
        # Set the boundary around 1/10000 of the maximum order, and draw logarithmically beyond that.
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
        
        # Stop delegating to draw_matrix_heatmap and draw directly applying SymLogNorm
        sns.heatmap(
            pd.DataFrame(K_matrix_list[t_idx]), 
            ax=ax, 
            cmap=cmap_stiffness, 
            norm=symlog_norm,  # Apply symmetric logarithmic scale
            xticklabels=axis_labels, 
            yticklabels=axis_labels,
            cbar_kws={'label': "Stiffness / Precision (SymLog10 Scale)", 'extend': 'both'}
        )
        
        # Apply standard formatting
        ax.set_title(title, fontsize=16, color=text_col, pad=20, fontweight='bold')
        ax.set_xlabel("Target Node (Effect)", color=text_col, fontsize=12)
        ax.set_ylabel("Source Node (Cause)", color=text_col, fontsize=12)
        ax.tick_params(axis='x', rotation=90, colors=text_col)
        ax.tick_params(axis='y', rotation=0, colors=text_col)
        
        plt.tight_layout()
        
        out_name = f"{base_name.replace('.png', '')}.t.{t_idx:05d}{ext}"
        save_plot(fig, args.out_dir, out_name)
        plt.close(fig)

if __name__ == "__main__":
    main()
