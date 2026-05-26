#!/usr/bin/env python3
# ==========================================
# 9_1_visualize_3D_ribbon_master.py
# TLU System: Universal 3D Ribbon Master Template
# ==========================================

import sys
import pandas as pd
import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection

from src.visualizations.visualizer_utils import get_base_parser, apply_theme, load_node_labels, load_time_labels, save_plot

def setup_argparser():
    parser = get_base_parser("Universal 3D Ribbon Plotter")
    parser.add_argument("--target_col", type=str, required=True, help="Column name to plot on Z-axis (height)")
    parser.add_argument("--color_col", type=str, default=None, help="Column name to map to surface color (target_col if unspecified)")
    parser.add_argument("--z_label", type=str, default=None, help="Z-axis display label")
    parser.add_argument("--c_label", type=str, default=None, help="Colorbar display label")
    parser.set_defaults(filename="3d_ribbon.png")
    return parser

def resolve_colormap(target_col: str, theme_cfg: dict) -> str:
    """ [Pure Logic] Infer and resolve optimal colormap from column name """
    cmap_name = 'viridis'
    for category, config in theme_cfg.items():
        if not isinstance(config, dict): continue
        colormaps = config.get('colormaps', {})
        for key, cmap in colormaps.items():
            if target_col in key or key in target_col:
                return cmap
                
    if 'velocity' in target_col or 'temperature' in target_col or 'flux' in target_col or target_col == 'z_score_v':
        cmap_name = 'magma'
    elif 'delta' in target_col or 'residual' in target_col:
        cmap_name = 'coolwarm'
    elif 'kl_drift' in target_col or 'curvature' in target_col:
        cmap_name = 'inferno'
    elif target_col == 'z_score_X':
        cmap_name = 'viridis'
    elif 'z_score' in target_col or 'stress' in target_col:
        cmap_name = 'plasma'

    return cmap_name

def polygon_under_graph(x, y, z_base):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (x, y) line graph down to z_base.
    """
    return [(x[0], z_base), *zip(x, y), (x[-1], z_base)]

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    
    theme_cfg = apply_theme(args.theme) or {}
    ui_canvas = theme_cfg.get('ui_canvas', {})
    text_col = ui_canvas.get('text_primary', 'white')
    grid_col = ui_canvas.get('grid_line', 'gray')
    
    color_target = args.color_col if args.color_col else args.target_col
    cmap_name = resolve_colormap(color_target, theme_cfg)
    cmap = plt.get_cmap(cmap_name)

    MAX_LEN_X = 10
    MAX_LEN_Y = 20

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr); sys.exit(1)
        
    if df.empty: sys.exit(0)

    max_t = int(df['t_idx'].max()) + 1
    max_n = int(df['node_idx'].max()) + 1
    node_labels = load_node_labels(args.node_map, max_n)
    time_labels = load_time_labels(args.time_map, max_t)
    
    z_matrix = df.pivot(index='node_idx', columns='t_idx', values=args.target_col).reindex(index=range(max_n), columns=range(max_t)).fillna(0).values
    c_matrix = df.pivot(index='node_idx', columns='t_idx', values=color_target).reindex(index=range(max_n), columns=range(max_t)).fillna(0).values

    # Luxuriously use the graph area to fill the screen (since there is no legend)
    fig = plt.figure(figsize=(18, 14))
    ax = fig.add_axes([0.15, 0.10, 0.80, 0.80], projection='3d')
    ax.set_proj_type('ortho')

    # ---------------------------------------------------------
    # TLU Ribbon Layer (Vertical Gradient via plot_surface)
    # Mitigates spatial interpolation artifacts while preserving Z-axis color gradients.
    # ---------------------------------------------------------
    z_base = min(0.0, z_matrix.min())
    
    # Normalize colormap proportional to the absolute Z-axis height
    if not args.color_col or args.color_col == args.target_col:
        norm = plt.Normalize(z_base, z_matrix.max())
    else:
        norm = plt.Normalize(min(0.0, c_matrix.min()), c_matrix.max())

    # Vertical resolution for smooth color gradients on the ribbon walls
    z_res = 10
    xs = np.arange(max_t)
    X_ribbon = np.tile(xs, (z_res, 1))

    for i in range(max_n):
        ys = z_matrix[i, :]
        cs = c_matrix[i, :]
        
        # Draw the top edge outline for visual clarity
        ax.plot(xs, ys, zs=i, zdir='y', color=grid_col, linewidth=0.8, alpha=0.8)
        
        # Construct the vertical wall surface for this ribbon
        Y_ribbon = np.full_like(X_ribbon, i, dtype=float)
        ratios = np.linspace(0, 1, z_res)[:, np.newaxis]
        Z_ribbon = z_base + ratios * (ys - z_base)
        
        # Color matrix for the surface faces
        if not args.color_col or args.color_col == args.target_col:
            C_ribbon = Z_ribbon
        else:
            C_ribbon = ratios * cs
            
        # Apply the user's max() logic across the time interval (X-axis) to avoid color smoothing
        C_max_time = np.maximum(C_ribbon[:, :-1], C_ribbon[:, 1:])
        
        # Smooth gradient only along the vertical (Z-axis) by averaging face corners vertically
        face_C = (C_max_time[:-1, :] + C_max_time[1:, :]) / 2.0
        colors = cmap(norm(face_C))
        
        # Draw the ribbon (antialiased=False removes rendering smoothing between edges)
        ax.plot_surface(X_ribbon, Y_ribbon, Z_ribbon, facecolors=colors, shade=False, antialiased=False, alpha=0.85)
    
    ax.set_xlim(0, max_t - 1)
    ax.set_ylim(0, max_n - 1)
    
    # Ensure Z limits encompass all data and base
    z_max = z_matrix.max()
    z_range = z_max - z_base
    if z_range == 0: z_range = 1
    ax.set_zlim(z_base, z_max + z_range * 0.05)
    
    # Adjust viewing angle for better visibility of peaks
    ax.view_init(elev=35, azim=-55)

    z_axis_label = args.z_label if args.z_label else args.target_col
    c_axis_label = args.c_label if args.c_label else color_target

    # Padding for axis titles (collision avoidance with label characters)
    x_tick_labels = [time_labels.get(i, f"T_{i:02d}") for i in range(max_t)]
    y_tick_labels = [node_labels.get(i, '')[:20] for i in range(max_n)]
    max_len_x = max(len(label) for label in x_tick_labels)
    max_len_y = max(len(label) for label in y_tick_labels)

    ax.set_xlabel('Timeline', labelpad=max_len_x / MAX_LEN_X * 50.0, color=text_col)
    ax.set_ylabel('Node (Dept/Account)', labelpad=max_len_y / MAX_LEN_Y * 50.0, color=text_col)
    ax.set_zlabel(z_axis_label, labelpad=25, color=text_col)

    title_str = f"Unified 3D Ribbon Evolution: {args.target_col}"
    if args.color_col:
        title_str += f"\n(Height: {args.target_col} / Color: {args.color_col})"
    ax.set_title(title_str, fontsize=16, pad=2, color=text_col, fontweight='bold')

    # --- Direct labeling and padding adjustment ---
    ax.set_xticks(np.arange(max_t))
    ax.set_xticklabels(x_tick_labels, rotation=45, ha='right', va='center', fontsize=10, color=text_col)
    ax.tick_params(axis='x', pad=max_len_x / MAX_LEN_X * 15.0)

    ax.set_yticks(np.arange(max_n))
    ax.set_yticklabels(y_tick_labels, rotation=-15, ha='left', va='center', fontsize=10, color=text_col)
    ax.tick_params(axis='y', pad=max_len_y / MAX_LEN_Y * 5.0 )

    ax.tick_params(axis='z', colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)

    # Improve depth perception and visibility
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    try:
        ax.set_box_aspect(aspect=(2.5, 1.5, 1.0))
    except AttributeError:
        pass

    # Layout of colorbar
    cax = fig.add_axes([0.05, 0.3, 0.02, 0.4])
    mappable = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    mappable.set_array(c_matrix)
    cbar = fig.colorbar(mappable, cax=cax)
    cbar.set_label(c_axis_label, fontsize=10, color=text_col)
    cbar.ax.yaxis.set_tick_params(color=text_col)
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color=text_col)

    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
