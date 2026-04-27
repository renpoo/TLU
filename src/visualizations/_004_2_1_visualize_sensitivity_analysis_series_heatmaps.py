#!/usr/bin/env python3
# ==========================================
# 1_13_visualize_sensitivity_analysis_series_heatmaps.py
# TLU System: Sensitivity Analysis -- Neumann Series -- Propagation (Echo Matrix Expansion)
# ==========================================
import sys
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Sensitivity Analysis Series Propagation Heatmap")
    parser.add_argument("--gamma", type=float, default=0.85, help="Discount factor")
    parser.add_argument("--max_k", type=int, default=10, help="Max expansion order")
    parser.add_argument("--t_target", type=int, default=None, help="Time step to analyze (processes all time t_idx if omitted)")
    parser.add_argument("--epsilon", type=float, default=1e-5, help="Threshold to consider as zero matrix")
    parser.set_defaults(filename="1_13_2__sensitivity_analysis_series_heatmap.png")
    return parser

def compute_transition_matrix(T_matrix):
    """ Calculate transition probability matrix P from T tensor """
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

    # Create list of target times (all times if omitted)
    if args.t_target is not None:
        target_t_list = [args.t_target]
    else:
        target_t_list = sorted(df['t_idx'].unique())

    # Real time (t) loop
    for target_t in target_t_list:
        df_t = df[df['t_idx'] == target_t]
        
        # Construction of transition tensor T
        T_matrix = np.zeros((N, N))
        for _, row in df_t.iterrows():
            T_matrix[int(row['src_idx']), int(row['tgt_idx'])] += float(row['value'])

        # Construction of transition probability matrix P
        P_matrix = compute_transition_matrix(T_matrix)

        # Virtual propagation time (k: terms of Neumann series) loop
        k = 0
        current_P = np.eye(N) # k=0 is identity matrix I
        
        while True:
            M_k = (args.gamma ** k) * current_P
            
            # Determine zero matrix (complete extinction of propagation)
            if k > 0 and np.sum(M_k) < args.epsilon:
                print(f"Propagation fully decayed at t={target_t}, k={k}. Stopping visualization for this time step.", file=sys.stderr)
                break
                
            # ★ Fix: Skip drawing for k=0 (identity matrix) as it has no structural information
            if k >= 0:
                fig, ax = plt.subplots(figsize=(12, 10))
                
                sns.heatmap(M_k, ax=ax, cmap=cmap_name, vmin=0.0, vmax=1.0,
                            xticklabels=axis_labels, yticklabels=axis_labels,
                            cbar_kws={'label': f'Impact Intensity (gamma={args.gamma})'})
                            
                ax.set_title(f"Sensitivity Analysis Series Propagation: Order k={k}\n(Time Step: {target_t})", 
                             fontsize=16, color=text_col, pad=args.max_k, fontweight='bold')
                ax.set_xlabel("Target Node (Impact Received)", color=text_col, fontsize=12)
                ax.set_ylabel("Source Node (Shock Origin)", color=text_col, fontsize=12)
                ax.tick_params(axis='x', rotation=90, colors=text_col)
                ax.tick_params(axis='y', rotation=0, colors=text_col)
                ax.set_facecolor(bg_col)
                
                plt.subplots_adjust(bottom=0.25, left=0.25, right=0.95, top=0.9)
                
                # ★ Fix: Change filename to k-priority sequential numbers (dramatically improves OS sorting)
                base_name, ext = os.path.splitext(args.filename)
                out_name = f"{base_name.replace('.png', '')}.k.{k:05d}.t.{target_t:05d}{ext}"
                
                save_plot(fig, args.out_dir, out_name)
                plt.close(fig)

            # Move to next step (P^(k+1) = P^k * P)
            current_P = np.dot(current_P, P_matrix)
            k += 1
            
            # Safety catch
            if k > args.max_k:
                print(f"Reached maximum expansion order (k={args.max_k}) at t={target_t}. Stopping.", file=sys.stderr)
                break

if __name__ == "__main__":
    main()
