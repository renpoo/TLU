#!/usr/bin/env python3
# ==========================================
# _002_1_3_visualize_network_topology_heatmap.py
# TLU System: Network Topology Sequential Matrix Heatmap (Flux Weight & Edge Stress)
# ==========================================
import sys
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import concurrent.futures

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Network Topology Matrix Heatmap Plotter")
    parser.add_argument("--metric", type=str, choices=['weight', 'stress'], default='weight', 
                        help="Topology metric to plot ('weight' for Transaction Flux, 'stress' for Edge Stress Z-Score)")
    parser.add_argument("--t_target", type=int, default=None, 
                        help="Target timestep to plot. Plots all sequentially if omitted.")
    parser.set_defaults(filename="27_topology_{metric}_heatmap.png")
    return parser

def render_frame(t, df_t, N, axis_labels, time_labels, cmap_name, metric, vmin, vmax, text_col, bg_col, filename, out_dir):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    matrix_vals = np.zeros((N, N))
    for _, row in df_t.iterrows():
        src = int(row['src_idx'])
        dst = int(row['tgt_idx'])
        val = float(row[metric])
        if src < N and dst < N:
            matrix_vals[src, dst] = val

    fig, ax = plt.subplots(figsize=(12, 10))
    
    cbar_title = "Transaction Flux Amount" if metric == 'weight' else "Edge Stress (Z-Score)"
    
    sns.heatmap(matrix_vals, ax=ax, cmap=cmap_name, vmin=vmin, vmax=vmax,
                xticklabels=axis_labels, yticklabels=axis_labels,
                cbar_kws={'label': cbar_title})

    time_label_str = time_labels.get(t, f"t={t:02d}")
    title_metric_str = "Transaction Flux Matrix (T_ij)" if metric == 'weight' else "Edge Stress Matrix (Z-Score)"
    
    ax.set_title(f"Network Topology Heatmap: {title_metric_str}\nTimeline: {time_label_str} (t_idx={t})", 
                 fontsize=16, color=text_col, pad=20, fontweight='bold')
    ax.set_xlabel("Target Node (Impact Received - Receive)", color=text_col, fontsize=12)
    ax.set_ylabel("Source Node (Shock Origin - Send)", color=text_col, fontsize=12)
    ax.tick_params(axis='x', rotation=90, colors=text_col)
    ax.tick_params(axis='y', rotation=0, colors=text_col)
    ax.set_facecolor(bg_col)
    
    plt.subplots_adjust(bottom=0.25, left=0.25, right=0.95, top=0.9)

    base_name, ext = os.path.splitext(filename)
    formatted_base = base_name.format(metric=metric)
    out_name = f"{formatted_base}.t.{t:05d}{ext}"

    save_plot(fig, out_dir, out_name)
    plt.close(fig)

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    theme_cfg = apply_theme(args.theme) or {}
    ui_canvas = theme_cfg.get('ui_canvas', {})
    text_col = ui_canvas.get('text_primary', 'white')
    bg_col = ui_canvas.get('background', 'black')
    
    if args.metric == 'stress':
        cmap_name = theme_cfg.get('forensics', {}).get('colormaps', {}).get('z_score_shock_map', 'plasma')
    else:
        cmap_name = theme_cfg.get('topology_and_correlation', {}).get('colormaps', {}).get('lag_matrix_map', 'viridis')

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading CSV: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    # 1. Determine dimensions N
    N = int(max(df['src_idx'].max(), df['tgt_idx'].max())) + 1
    labels = load_node_labels(args.node_map, N)
    axis_labels = [f"{i:02d}: {labels.get(i, f'N_{i}')}" for i in range(N)]

    # 2. Global domain limits (vmin / vmax)
    if args.metric == 'stress':
        vmin = 0.0
        vmax = float(np.percentile(df['stress'], 98)) if len(df) > 0 else 3.0
    else:
        vmin = 0.0
        vmax = float(np.percentile(df['weight'], 98)) if len(df) > 0 else 1.0

    # 3. Get target timesteps list
    if args.t_target is not None:
        target_t_list = [args.t_target]
    else:
        target_t_list = sorted(df['t_idx'].unique())

    T_max = max(target_t_list) if target_t_list else 0
    time_labels = load_time_labels(args.time_map, T_max + 1)

    # 4. Generate sequential frames in parallel
    if len(target_t_list) <= 1:
        for t in target_t_list:
            df_t = df[df['t_idx'] == t]
            render_frame(t, df_t, N, axis_labels, time_labels, cmap_name, args.metric, vmin, vmax, text_col, bg_col, args.filename, args.out_dir)
    else:
        max_workers = min(len(target_t_list), os.cpu_count() or 4)
        tasks = []
        with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
            for t in target_t_list:
                df_t = df[df['t_idx'] == t]
                tasks.append(
                    executor.submit(render_frame, t, df_t, N, axis_labels, time_labels, cmap_name, args.metric, vmin, vmax, text_col, bg_col, args.filename, args.out_dir)
                )
            for future in concurrent.futures.as_completed(tasks):
                future.result()

if __name__ == "__main__":
    main()
