#!/usr/bin/env python3
# ==========================================
# 1_12_visualize_network_topology.py
# TLU System: Network Topology (Flow & Structural Stress)
# Pattern B: Sequential Animation Frames with Fixed Layout & Robust Scaling (Repulsive Layout)
# ==========================================

import sys
import numpy as np
import pandas as pd
import japanize_matplotlib
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
import matplotlib.patches as mpatches

# 共通ユーティリティのインポート
from src.visualizations.visualizer_utils import get_base_parser, apply_theme, load_node_labels, load_time_labels, save_plot

def setup_argparser():
    parser = get_base_parser("Network Topology: Flow and Structural Stress (Sequential Generator)")
    parser.add_argument("--t_target", type=int, default=None, 
                        help="描画対象のタイムステップ (指定がない場合は全時刻を連番で生成)")
    parser.add_argument("--layout_seed", type=int, default=42, 
                        help="ネットワーク配置の乱数シード")
    parser.add_argument("--top_k", type=int, default=3, 
                        help="絶対純流入出（Net Flux）が大きい特異点ノードのハイライト数")
    parser.set_defaults(filename="27_network_topology.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    theme_cfg = apply_theme(args.theme) or {}
    ui_canvas = theme_cfg.get('ui_canvas', {})
    text_col = ui_canvas.get('text_primary', 'white')
    bg_col = ui_canvas.get('legend_bg', 'black')
    edge_col = ui_canvas.get('legend_edge', 'gray')

    # テーマからのカラー設定と直感化（マイナス＝赤、プラス＝青 へ反転）
    cmap_node = theme_cfg.get('thermodynamics', {}).get('colormaps', {}).get('displacement_delta_map', 'coolwarm')
    if not cmap_node.endswith('_r'):
        cmap_node = f"{cmap_node}_r"
        
    cmap_edge = theme_cfg.get('forensics', {}).get('colormaps', {}).get('z_score_shock_map', 'plasma')
    c_outlier_text = theme_cfg.get('forensics', {}).get('colors', {}).get('anomaly_outlier', 'salmon')

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading from standard input: {e}", file=sys.stderr); sys.exit(1)

    if df.empty:
        sys.exit(0)

    N = int(max(df['src_idx'].max(), df['tgt_idx'].max())) + 1
    T_max = int(df['t_idx'].max()) + 1
    idx_to_label = load_node_labels(args.node_map, N)
    time_labels = load_time_labels(args.time_map, T_max)

    # ==========================================================
    # 1. アニメーションのための固定レイアウト（Fixed Positioning）の計算
    # ==========================================================
    G_global = nx.DiGraph()
    G_global.add_nodes_from(range(N))
    for _, row in df.iterrows():
        G_global.add_edge(int(row['src_idx']), int(row['tgt_idx']))
        
    # [修正箇所] 斥力を強め（k=2.5）、スケールを広げて（scale=1.5）ノードを分散させる
    pos = nx.spring_layout(G_global, k=2.5, iterations=100, scale=1.5, seed=args.layout_seed)

    # ==========================================================
    # 2. ロバスト・スケーリング（95パーセンタイル）の事前計算
    # ==========================================================
    global_max_weight = np.percentile(df['weight'], 95) if len(df) > 0 else 1.0
    global_max_stress = np.percentile(df['stress'], 95) if len(df) > 0 else 1.0
    
    global_max_weight = max(global_max_weight, 1e-5)
    global_max_stress = max(global_max_stress, 1e-5)

    all_net_fluxes = []
    for t_val in df['t_idx'].unique():
        df_t_temp = df[df['t_idx'] == t_val]
        nf = np.zeros(N)
        for _, r in df_t_temp.iterrows():
            nf[int(r['tgt_idx'])] += r['weight']
            nf[int(r['src_idx'])] -= r['weight']
        all_net_fluxes.extend(np.abs(nf))
    
    global_vmax_node = np.percentile(all_net_fluxes, 95) if all_net_fluxes else 1.0
    global_vmax_node = max(global_vmax_node, 1e-5)

    t_targets = [args.t_target] if args.t_target is not None else sorted(df['t_idx'].unique())

    # ==========================================================
    # 3. 各タイムステップごとの連番描画ループ
    # ==========================================================
    for t in t_targets:
        t = int(t)
        df_t = df[df['t_idx'] == t]

        G = nx.DiGraph()
        G.add_nodes_from(range(N))

        net_flux = np.zeros(N)
        for _, row in df_t.iterrows():
            src, tgt, w, s = int(row['src_idx']), int(row['tgt_idx']), row['weight'], row['stress']
            G.add_edge(src, tgt, weight=w, stress=s)
            net_flux[tgt] += w
            net_flux[src] -= w

        top_k_indices = np.argsort(np.abs(net_flux))[-args.top_k:].tolist()

        fig = plt.figure(figsize=(16, 10))
        # ネットワークの描画領域（scale=1.5に合わせて少し調整）
        ax = fig.add_axes([0.15, 0.1, 0.60, 0.80])

        node_colors = [net_flux[i] for i in range(N)]
        node_sizes = [500 + 1500 * (min(abs(net_flux[i]), global_vmax_node) / global_vmax_node) for i in range(N)]

        nodes = nx.draw_networkx_nodes(
            G, pos, ax=ax,
            node_color=node_colors, cmap=cmap_node,
            node_size=node_sizes, vmin=-global_vmax_node, vmax=global_vmax_node,
            edgecolors=text_col, linewidths=1.5
        )

        for i in range(N):
            x, y = pos[i]
            if i in top_k_indices:
                ax.text(x, y + 0.1, f"{i:02d}", fontsize=14, fontweight='bold', color=c_outlier_text, ha='center')
            else:
                ax.text(x, y + 0.1, f"{i:02d}", fontsize=11, color=text_col, alpha=0.9, ha='center')

        edges = G.edges(data=True)
        if edges:
            edge_stresses = [d['stress'] for u, v, d in edges]
            edge_weights = [d['weight'] for u, v, d in edges]
            
            widths = [1.0 + 5.0 * (min(w, global_max_weight) / global_max_weight) for w in edge_weights]

            nx.draw_networkx_edges(
                G, pos, ax=ax, edgelist=edges,
                edge_color=edge_stresses, edge_cmap=plt.get_cmap(cmap_edge),
                width=widths, edge_vmin=0, edge_vmax=global_max_stress,
                arrowsize=40, connectionstyle='arc3,rad=0.1'
            )

        ax.axis('off')

        time_label_str = time_labels.get(t, f"t={t:02d}")
        ax.set_title(f"Network Topology & Stress Propagation\nTimeline: {time_label_str} (t_idx={t})", 
                     fontsize=16, color=text_col, fontweight='bold', pad=20)

        cax_edge = fig.add_axes([0.05, 0.2, 0.015, 0.3])
        sm_edge = ScalarMappable(cmap=cmap_edge, norm=Normalize(vmin=0, vmax=global_max_stress))
        cbar_edge = fig.colorbar(sm_edge, cax=cax_edge, extend='max')
        cbar_edge.set_label('Edge Stress (Z-Score)', color=text_col, fontsize=10)
        cbar_edge.ax.yaxis.set_tick_params(color=text_col)
        plt.setp(plt.getp(cbar_edge.ax.axes, 'yticklabels'), color=text_col)

        cax_node = fig.add_axes([0.05, 0.6, 0.015, 0.3])
        sm_node = ScalarMappable(cmap=cmap_node, norm=Normalize(vmin=-global_vmax_node, vmax=global_vmax_node))
        cbar_node = fig.colorbar(sm_node, cax=cax_node, extend='both')
        cbar_node.set_label('Net Flux (Inflow - Outflow)', color=text_col, fontsize=10)
        cbar_node.ax.yaxis.set_tick_params(color=text_col)
        plt.setp(plt.getp(cbar_node.ax.axes, 'yticklabels'), color=text_col)

        handles, labels = [], []
        display_count = min(N, args.max_legend)
        for i in range(display_count):
            handles.append(mpatches.Patch(color='none'))
            labels.append(f"{i:02d} : {idx_to_label.get(i, f'Node_{i}')}")
        if N > args.max_legend:
            handles.append(mpatches.Patch(color='none'))
            labels.append(f"... and {N - args.max_legend} more")

        leg = ax.legend(handles, labels, title="Node Map:\n" + "-"*30,
                        loc='center left', bbox_to_anchor=(1.05, 0.5), 
                        facecolor=bg_col, edgecolor=edge_col,
                        handlelength=0, handletextpad=0, prop={'family': 'monospace', 'size': 10})
        plt.setp(leg.get_title(), color=text_col, family='monospace')

        for text_obj in leg.get_texts():
            text_str = text_obj.get_text()
            if ":" in text_str:
                idx_str = text_str.split(":")[0].strip()
                if idx_str.isdigit() and int(idx_str) in top_k_indices:
                    text_obj.set_color(c_outlier_text)
                    text_obj.set_fontweight('bold')
                else:
                    text_obj.set_color(text_col)
            else:
                text_obj.set_color(text_col)

        out_name = args.filename
        if args.t_target is None:
            base, ext = out_name.rsplit('.', 1) if '.' in out_name else (out_name, 'png')
            out_name = f"{base}.t.{t:05d}.{ext}"

        save_plot(fig, args.out_dir, out_name)
        plt.close(fig)

if __name__ == "__main__":
    main()
