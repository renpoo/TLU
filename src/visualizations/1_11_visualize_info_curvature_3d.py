#!/usr/bin/env python3
# ==========================================
# 1_11_visualize_info_curvature_3d.py
# TLU System: Information Geometry (3D Curvature Field)
# Strict Theme Mode (Fail-Fast) & Context Bleed Fixed
# ==========================================

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Information Curvature: 3D Manifold Distortion Field")
    parser.set_defaults(filename="25_info_curvature_3d.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    
    # フォールバック排除
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    
    # セマンティック・カラーマップの厳格取得 (Context Bleed 解消)
    cmap_name = theme_cfg['information_geometry']['colormaps']['density_map']
    cmap = plt.get_cmap(cmap_name)

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading from standard input: {e}", file=sys.stderr); sys.exit(1)
        
    if df.empty: sys.exit(0)

    max_t = int(df['t_idx'].max()) + 1
    max_n = int(df['node_idx'].max()) + 1
    node_labels = load_node_labels(args.node_map, max_n)
    time_labels = load_time_labels(args.time_map, max_t)
    
    curvature_matrix = np.zeros((max_n, max_t))
    density_matrix = np.zeros((max_n, max_t))
    
    for _, row in df.iterrows():
        t, n = int(row['t_idx']), int(row['node_idx'])
        curvature_matrix[n, t] = row['curvature']
        density_matrix[n, t] = row['density']

    fig = plt.figure(figsize=(18, 10))
    ax = fig.add_axes([0.05, 0.1, 0.65, 0.8], projection='3d')

    T_mesh, N_mesh = np.meshgrid(np.arange(max_t), np.arange(max_n))

    norm = plt.Normalize(density_matrix.min(), density_matrix.max())
    
    surf = ax.plot_surface(
        T_mesh, N_mesh, curvature_matrix, 
        facecolors=cmap(norm(density_matrix)),
        shade=False, antialiased=True, alpha=0.8
    )

    ax.set_xlabel('Time Step (t_idx)', labelpad=12, color=text_col)
    ax.set_ylabel('Node Index', labelpad=12, color=text_col)
    ax.set_zlabel('Information Curvature (Distortion)', labelpad=12, color=text_col)
    ax.set_title("Information Geometry: 3D Manifold Distortion Field\n(Height: Curvature / Color: Density)", fontsize=15, pad=30, x=0.5, color=text_col)

    ax.set_xticks(np.arange(0, max_t, max(1, max_t//10)))
    ax.set_yticks(np.arange(0, max_n, max(1, max_n//10)))
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)

    node_elements = []
    num_node_leg = min(max_n, args.max_legend)
    for i in range(num_node_leg):
        label = node_labels.get(i, f"N_{i:02d}")
        node_elements.append(plt.Line2D([0], [0], color='none', label=f"{i:02d}: {label}"))
    
    if max_n > args.max_legend:
        node_elements.append(plt.Line2D([0], [0], color='none', label=f"... and {max_n - args.max_legend} more"))
        
    fig.legend(handles=node_elements, loc='upper right', bbox_to_anchor=(0.95, 0.88), 
               fontsize=9, title="[ Node Map ]", frameon=False, ncol=1, labelcolor=text_col, title_fontproperties={'weight':'bold'})

    ax.view_init(elev=35, azim=-50)
    
    cax = fig.add_axes([0.1, 0.15, 0.015, 0.3])
    mappable = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    mappable.set_array(density_matrix)
    cbar = fig.colorbar(mappable, cax=cax)
    cbar.set_label('Metric Density (Transaction Volume)', fontsize=10, color=text_col)
    cbar.ax.yaxis.set_tick_params(color=text_col)
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color=text_col)

    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
