#!/usr/bin/env python3
# ==========================================
# 1_3_visualize_phase_portrait.py
# TLU System: 3D Phase Space (Chromatic Trajectories)
# Pattern C & B Hybrid: Strict Theme Mode (Fail-Fast)
# ==========================================
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import colorsys

# 共通可視化基盤のインポート
from src.visualizations.visualizer_utils import get_base_parser, apply_theme, load_node_labels, save_plot

def setup_argparser():
    parser = get_base_parser("3D Phase Space: Chromatic Node Trajectories (q, v, a)")
    parser.add_argument("--elev", type=float, default=25.0, help="仰角 (Elevation)")
    parser.add_argument("--azim", type=float, default=-65.0, help="方位角 (Azimuth)")
    parser.set_defaults(filename="18_phase_portrait_3d.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    # フォールバックを駆逐し、厳格なキー参照（Fail-Fast）を強制
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    bg_col = ui_canvas['legend_bg']
    edge_col = ui_canvas['legend_edge']

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr); sys.exit(1)
        
    if df.empty: sys.exit(0)

    # カラム名の同期
    col_q = 'net_flux_q'
    col_v = 'velocity_v'
    col_a = 'acceleration_a'

    max_t = df['t_idx'].max()
    N = int(df['node_idx'].max()) + 1
    node_labels = load_node_labels(args.node_map, N)

    fig = plt.figure(figsize=(16, 16))
    
    # 【修正】3Dプロットエリアを左に寄せ、幅を広げる。
    # 旧: [0.12, 0.18, 0.55, 0.65] (左マージン12%, 幅55%)
    # 新: [0.05, 0.18, 0.60, 0.65] (左マージン5%, 幅60%)
    # これにより、プロットが左に寄り、右マージンが広がります。
    ax = fig.add_axes([0.05, 0.20, 0.60, 0.65], projection='3d')
    ax.view_init(elev=args.elev, azim=args.azim)

    # 軌跡の色（色相）割り当て。
    # HLS空間でのグラデーション計算（時間軸の進行による明度変化）が必要なため、
    # Hue（色相）の等分生成という数理的アプローチは維持します。
    hues = np.linspace(0, 1, N, endpoint=False)
    legend_elements = []

    for n in range(N):
        node_df = df[df['node_idx'] == n].sort_values('t_idx')
        if len(node_df) < 2: continue

        q = node_df[col_q].values
        v = node_df[col_v].values
        a = node_df[col_a].values
        t_vals = node_df['t_idx'].values
        hue = hues[n]

        # 軌跡の描画
        for i in range(len(t_vals) - 1):
            progress = t_vals[i] / (max_t - 1) if max_t > 1 else 1.0
            lightness = 0.2 + 0.6 * progress
            rgb = colorsys.hls_to_rgb(hue, lightness, 0.9)
            ax.plot(q[i:i+2], v[i:i+2], a[i:i+2], color=rgb, linewidth=2.0)
        
        # 最終到達点のプロット
        final_rgb = colorsys.hls_to_rgb(hue, 0.8, 0.9)
        ax.scatter(q[-1], v[-1], a[-1], color=final_rgb, s=50, edgecolors=text_col, alpha=1.0)
        
        # 凡例用のライン要素
        legend_rgb = colorsys.hls_to_rgb(hue, 0.6, 0.9)
        label = node_labels.get(n, f"N_{n:02d}")[:18] 
        if len(legend_elements) < args.max_legend:
            legend_elements.append(plt.Line2D([0], [0], color=legend_rgb, lw=3, label=f"{n:02d}: {label}"))

    if N > args.max_legend:
        legend_elements.append(plt.Line2D([0], [0], color='none', label=f"... and {N - args.max_legend} more"))

    ax.set_xlabel('Net Flux (q)', labelpad=15, color=text_col)
    ax.set_ylabel('Velocity (v)', labelpad=25, color=text_col)
    ax.set_zlabel('Acceleration (a)', labelpad=20, color=text_col)
    ax.set_title('Dynamics Phase Portrait (q -> v -> a Trajectories)', fontsize=16, pad=20, color=text_col, fontweight='bold')
    
    ax.tick_params(axis='x', pad=8, colors=text_col)
    ax.tick_params(axis='y', pad=8, colors=text_col)
    ax.tick_params(axis='z', pad=8, colors=text_col)

    try:
        ax.set_box_aspect(aspect=(1.0, 1.0, 1.0))
    except AttributeError:
        pass

    ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    
    for spine in ax.spines.values():
        spine.set_color(text_col)

    if legend_elements:
        # 【修正】凡例タイトルの区切り線を短くする（ハイフン30個 -> 20個）。
        # これにより、凡例の幅が狭くなり、重なりが解消されます。
        leg = ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1.05, 0.5), 
                        title="Node Map (Index -> Name):\n" + "-"*24,
                        facecolor=bg_col, edgecolor=edge_col, 
                        prop={'family': 'monospace', 'size': 8})
        plt.setp(leg.get_title(), color=text_col, family='monospace')
        for text_obj in leg.get_texts():
            text_obj.set_color(text_col)
                  
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
