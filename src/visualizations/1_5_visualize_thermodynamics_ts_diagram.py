#!/usr/bin/env python3
# ==========================================
# 1_5_visualize_thermodynamics_ts_diagram.py
# TLU System: Macro Thermodynamics
# Safe Margin with Highlight-Synced Legend & Fail-Fast Theme Mode
# ==========================================

import sys
import pandas as pd
import japanize_matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches

from src.visualizations.visualizer_utils import get_base_parser, apply_theme, save_plot, load_time_labels

def setup_argparser():
    parser = get_base_parser("3D Extended T-S Diagram: Timeline View (X=t, Y=S, Z=T)")
    parser.add_argument("--elev", type=float, default=25.0, help="仰角 (Elevation)")
    parser.add_argument("--azim", type=float, default=-15.0, help="方位角 (Azimuth)")
    parser.add_argument("--top_k", type=int, default=3, help="温度(T)が最も高い特異点の数")
    parser.set_defaults(filename="15_thermodynamics_ts_diagram.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    # フォールバックを駆逐し、厳格なキー参照（Fail-Fast）を強制
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    legend_bg = ui_canvas['legend_bg']
    legend_edge = ui_canvas['legend_edge']
    text_col = ui_canvas['text_primary']
    grid_col = ui_canvas['grid_line']
    shadow_col = ui_canvas['zero_line']
    trajectory_col = ui_canvas['trajectory_line']

    cmap_name = theme_cfg['thermodynamics']['colormaps']['volatility_T_map']
    c_outlier_text = theme_cfg['forensics']['colors']['anomaly_outlier']
    c_outlier_marker = theme_cfg['forensics']['colors']['z_score_shock']

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading from standard input: {e}", file=sys.stderr); sys.exit(1)

    if df.empty:
        print("Warning: Received empty data stream.", file=sys.stderr); sys.exit(0)

    t = df['t_idx'].values
    S = df['entropy_S'].values
    T = df['temperature_T'].values

    T_max_idx = int(t.max()) + 1
    # 辞書のロード
    time_labels = load_time_labels(args.time_map, T_max_idx)

    top_k_indices = df.nlargest(args.top_k, 'temperature_T')['t_idx'].astype(int).tolist()

    fig = plt.figure(figsize=(18, 12))
    ax = fig.add_axes([0.10, 0.30, 0.40, 0.50], projection='3d')
    ax.view_init(elev=args.elev, azim=args.azim)

    # 軌跡（線）の描画
    ax.plot(t, S, T, color=trajectory_col, linestyle=':', alpha=0.5, linewidth=2, zorder=1)

    # プロット（点）の描画
    scatter = ax.scatter(t, S, T, c=T, cmap=cmap_name, s=120, 
                         edgecolor=text_col, linewidth=0.8, alpha=0.9, zorder=2)

    # --- 修正箇所: プロット注釈のカレンダー表記（time_map）解決 ---
    for i in range(len(df)):
        t_val = int(t[i])
        offset = (T.max() - T.min()) * 0.02
        
        # 辞書からカレンダー表記を取得
        time_str = time_labels.get(t_val, f"t={t_val:02d}")
        
        if t_val in top_k_indices:
            ax.scatter(t[i], S[i], T[i], color=c_outlier_marker, s=300, marker='*', edgecolor=text_col, zorder=3)
            # 異常値のハイライト表記
            ax.text(t[i], S[i], T[i] + offset, f" {time_str}", fontsize=11, fontweight='bold', color=c_outlier_text, ha='center')
        else:
            # 通常値の表記
            ax.text(t[i], S[i], T[i] + offset, f" {time_str}", fontsize=9, alpha=0.8, color=text_col, ha='center')

    # 底面への影（射影）の描画
    z_min = T.min() - (T.max() - T.min()) * 0.1 if T.max() > T.min() else T.min() - 1
    ax.set_zlim(z_min, T.max())
    ax.plot(t, S, zs=z_min, zdir='z', color=shadow_col, linestyle='--', alpha=0.5, zorder=0)
    ax.scatter(t, S, zs=z_min, zdir='z', c=T, cmap=cmap_name, s=40, alpha=0.3, zorder=0)

    ax.set_xlabel('Timeline (t_idx)', fontsize=12, labelpad=10, color=text_col)
    ax.set_ylabel('System Entropy (S) - Disorder', fontsize=12, labelpad=10, color=text_col)
    ax.set_zlabel('System Temperature (T) - Volatility', fontsize=12, labelpad=10, color=text_col)
    ax.set_title('3D Macro Thermodynamic Evolution: Timeline View', fontsize=16, pad=10, color=text_col, fontweight='bold')
    
    ax.tick_params(axis='x', pad=5, colors=text_col)
    ax.tick_params(axis='y', pad=5, colors=text_col)
    ax.tick_params(axis='z', pad=5, colors=text_col)

    cax = fig.add_axes([0.05, 0.35, 0.015, 0.45])
    cbar = fig.colorbar(scatter, cax=cax)
    cbar.set_label('Temperature (T) - Heat / Volatility', color=text_col, fontsize=10)
    cbar.ax.yaxis.set_tick_params(color=text_col)
    plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color=text_col)

    # --- 凡例はSource 27の元の通り（解決済み）を維持 ---
    handles, labels = [], []
    for i in range(T_max_idx):
        handles.append(mpatches.Patch(color='none'))
        labels.append(f"t={i:02d} : {time_labels.get(i, f'Time_{i:02d}')}")

    leg = ax.legend(handles, labels, title="Time Map:\n" + "-"*20,
                    loc='center left', bbox_to_anchor=(1.2, 0.5), 
                    facecolor=legend_bg, edgecolor=legend_edge,
                    handlelength=0, handletextpad=0, prop={'family': 'monospace', 'size': 10})
    plt.setp(leg.get_title(), color=text_col, family='monospace')

    for text_obj in leg.get_texts():
        text_str = text_obj.get_text()
        if ":" in text_str:
            t_str = text_str.split(":")[0].replace('t=', '').strip()
            if t_str.isdigit() and int(t_str) in top_k_indices:
                text_obj.set_color(c_outlier_text)
                text_obj.set_fontweight('bold')
            else:
                text_obj.set_color(text_col)

    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
