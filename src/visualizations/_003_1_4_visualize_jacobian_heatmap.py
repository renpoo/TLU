#!/usr/bin/env python3
# ==========================================
# _003_1_4_visualize_jacobian_heatmap.py
# TLU System: Multi-Order Jacobian Trajectory Heatmap Visualizer
# ==========================================
import sys
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Multi-Order Jacobian Heatmap Plotter")
    parser.add_argument("--order", type=int, default=1, help="Jacobian Order (1, 2, or 3)")
    parser.add_argument("--t_target", type=int, default=None, help="Target timestep to plot. Plots all sequentially if omitted.")
    parser.set_defaults(filename="jacobian_order_{order}.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    theme_cfg = apply_theme(args.theme) or {}
    ui_canvas = theme_cfg.get('ui_canvas', {})
    text_col = ui_canvas.get('text_primary', 'white')
    bg_col = ui_canvas.get('background', 'black')
    
    cmap_name = theme_cfg.get('topology_and_correlation', {}).get('colormaps', {}).get('jacobian_map', 'plasma')

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading CSV: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    # 1. Determine dimensions N
    N = int(max(df['src_idx'].max(), df['dst_idx'].max())) + 1
    labels = load_node_labels(args.node_map, N)
    axis_labels = [f"{i:02d}: {labels.get(i, f'N_{i}')}" for i in range(N)]

    # 2. Get target timesteps list
    if args.t_target is not None:
        target_t_list = [args.t_target]
    else:
        target_t_list = sorted(df['t_idx'].unique())

    T_max = max(target_t_list) if target_t_list else 0
    time_labels = load_time_labels(args.time_map, T_max + 1)

import concurrent.futures

def render_frame(t, df_t, N, axis_labels, time_labels, cmap_name, text_col, bg_col, order, filename, out_dir):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    J_matrix = np.zeros((N, N))
    for _, row in df_t.iterrows():
        J_matrix[int(row['src_idx']), int(row['dst_idx'])] = float(row['jacobian_value'])

    fig, ax = plt.subplots(figsize=(12, 10))
    
    sns.heatmap(J_matrix, ax=ax, cmap=cmap_name, vmin=0.0, vmax=1.0,
                xticklabels=axis_labels, yticklabels=axis_labels,
                cbar_kws={'label': f'Sensitivity Value'})

    time_label_str = time_labels.get(t, f"t={t:02d}")
    order_str = {1: "1st (Direct)", 2: "2nd (1-hop)", 3: "3rd (2-hop)"}.get(order, f"{order}th")
    
    ax.set_title(f"Jacobian Sensitivity Matrix: {order_str} Order\nTimeline: {time_label_str} (t_idx={t})", 
                 fontsize=16, color=text_col, pad=20, fontweight='bold')
    ax.set_xlabel("Target Node (Impact Received)", color=text_col, fontsize=12)
    ax.set_ylabel("Source Node (Shock Origin)", color=text_col, fontsize=12)
    ax.tick_params(axis='x', rotation=90, colors=text_col)
    ax.tick_params(axis='y', rotation=0, colors=text_col)
    ax.set_facecolor(bg_col)
    
    plt.subplots_adjust(bottom=0.25, left=0.25, right=0.95, top=0.9)

    base_name, ext = os.path.splitext(filename)
    formatted_base = base_name.format(order=order)
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
    
    cmap_name = theme_cfg.get('topology_and_correlation', {}).get('colormaps', {}).get('jacobian_map', 'plasma')

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading CSV: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        sys.exit(0)

    # 1. Determine dimensions N
    N = int(max(df['src_idx'].max(), df['dst_idx'].max())) + 1
    labels = load_node_labels(args.node_map, N)
    axis_labels = [f"{i:02d}: {labels.get(i, f'N_{i}')}" for i in range(N)]

    # 2. Get target timesteps list
    if args.t_target is not None:
        target_t_list = [args.t_target]
    else:
        target_t_list = sorted(df['t_idx'].unique())

    T_max = max(target_t_list) if target_t_list else 0
    time_labels = load_time_labels(args.time_map, T_max + 1)

    # 3. Generate heatmap for each target step using ProcessPoolExecutor
    if len(target_t_list) <= 1:
        for t in target_t_list:
            df_t = df[df['t_idx'] == t]
            render_frame(t, df_t, N, axis_labels, time_labels, cmap_name, text_col, bg_col, args.order, args.filename, args.out_dir)
    else:
        max_workers = min(len(target_t_list), os.cpu_count() or 4)
        tasks = []
        with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
            for t in target_t_list:
                df_t = df[df['t_idx'] == t]
                tasks.append(
                    executor.submit(render_frame, t, df_t, N, axis_labels, time_labels, cmap_name, text_col, bg_col, args.order, args.filename, args.out_dir)
                )
            for future in concurrent.futures.as_completed(tasks):
                future.result()

if __name__ == "__main__":
    main()
