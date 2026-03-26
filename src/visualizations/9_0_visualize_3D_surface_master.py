#!/usr/bin/env python3
# ==========================================
# 9_0_visualize_3D_surface_master.py
# TLU System: Universal 3D Surface Master Template (True Pattern C)
# ==========================================

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from src.visualizations.visualizer_utils import get_base_parser, apply_theme, load_node_labels, load_time_labels, save_plot

def setup_argparser():
    parser = get_base_parser("Universal 3D Surface Plotter")
    parser.add_argument("--target_col", type=str, required=True, help="Z軸（高さ）にプロットするカラム名")
    parser.add_argument("--color_col", type=str, default=None, help="表面の色にマッピングするカラム名（未指定時はtarget_col）")
    parser.add_argument("--z_label", type=str, default=None, help="Z軸の表示ラベル")
    parser.add_argument("--c_label", type=str, default=None, help="カラーバーの表示ラベル")
    parser.set_defaults(filename="3d_surface.png")
    return parser

def resolve_colormap(target_col: str, theme_cfg: dict) -> str:
    """ [Pure Logic] カラム名から最適なカラーマップを推論・解決する """
    cmap_name = 'viridis'
    for category, config in theme_cfg.items():
        if not isinstance(config, dict): continue
        colormaps = config.get('colormaps', {})
        for key, cmap in colormaps.items():
            if target_col in key or key in target_col:
                return cmap
                
    if 'velocity' in target_col or 'temperature' in target_col or 'flux' in target_col:
        cmap_name = 'magma'
    elif 'delta' in target_col or 'residual' in target_col:
        cmap_name = 'coolwarm'
    elif 'kl_drift' in target_col or 'curvature' in target_col:
        cmap_name = 'inferno'
    elif 'z_score' in target_col or 'stress' in target_col:
        cmap_name = 'plasma'

    return cmap_name

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

    # グラフ領域を画面いっぱいに贅沢に使用する（凡例は存在しないため）
    fig = plt.figure(figsize=(18, 14))
    ax = fig.add_axes([0.10, 0.20, 0.60, 0.60], projection='3d')

    T_mesh, N_mesh = np.meshgrid(np.arange(max_t), np.arange(max_n))
    norm = plt.Normalize(c_matrix.min(), c_matrix.max())
    
    surf = ax.plot_surface(
        T_mesh, N_mesh, z_matrix, 
        facecolors=cmap(norm(c_matrix)),
        shade=False, antialiased=True, alpha=0.9,
        linewidth=0.2, edgecolor=grid_col
    )

    z_axis_label = args.z_label if args.z_label else args.target_col
    c_axis_label = args.c_label if args.c_label else color_target

    # 軸タイトルのパディング（ラベル文字との衝突回避）
    x_tick_labels = [time_labels.get(i, f"T_{i:02d}") for i in range(max_t)]
    y_tick_labels = [node_labels.get(i, '')[:20] for i in range(max_n)]
    max_len_x = max(len(label) for label in x_tick_labels)
    max_len_y = max(len(label) for label in y_tick_labels)

    ax.set_xlabel('Timeline', labelpad=max_len_x / MAX_LEN_X * 50.0, color=text_col)
    ax.set_ylabel('Node (Dept/Account)', labelpad=max_len_y / MAX_LEN_Y * 50.0, color=text_col)
    ax.set_zlabel(z_axis_label, labelpad=25, color=text_col)

    title_str = f"Unified 3D Field Evolution: {args.target_col}"
    if args.color_col:
        title_str += f"\n(Height: {args.target_col} / Color: {args.color_col})"
    ax.set_title(title_str, fontsize=16, pad=2, color=text_col, fontweight='bold')

    # --- 真・パターンC: 直接ラベリングとパディングの調整 ---
    ax.set_xticks(np.arange(max_t))
    # x軸ラベル：45度回転し、パディングを広げてメッシュから離す
    ax.set_xticklabels(x_tick_labels, rotation=45, ha='right', va='center', fontsize=10, color=text_col)
    ax.tick_params(axis='x', pad=max_len_x / MAX_LEN_X * 15.0)

    ax.set_yticks(np.arange(max_n))
    # y軸ラベル：角度をつけ、さらにパディングを大きく取ってグラフ本体から離す
    ax.set_yticklabels(y_tick_labels, rotation=-15, ha='left', va='center', fontsize=10, color=text_col)
    ax.tick_params(axis='y', pad=max_len_y / MAX_LEN_Y * 5.0 )

    ax.tick_params(axis='z', colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)

    # 視認性の向上：時間推移を長く見せる直方体アスペクト比
    try:
        ax.set_box_aspect(aspect=(2.5, 1.5, 1.0))
    except AttributeError:
        pass

    ax.view_init(elev=30, azim=-55)
    
    # カラーバーの配置（グラフの左側にスリムに配置）
    cax = fig.add_axes([0.1, 0.3, 0.02, 0.4])
    mappable = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    mappable.set_array(c_matrix)
    cbar = fig.colorbar(mappable, cax=cax)
    cbar.set_label(c_axis_label, fontsize=10, color=text_col)
    cbar.ax.yaxis.set_tick_params(color=text_col)
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color=text_col)

    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
