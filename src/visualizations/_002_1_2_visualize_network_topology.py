#!/usr/bin/env python3
# ==========================================
# 002_1_2_visualize_network_topology.py
# TLU System: Network Topology (Flow & Structural Stress)
# Pattern B: Sequential Animation Frames with Fixed Layout & Robust Scaling (Repulsive Layout)
# ==========================================

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
import matplotlib.patches as mpatches

# Import common utilities
from src.visualizations.visualizer_utils import *

def setup_argparser():
    parser = get_base_parser("Network Topology: Flow and Structural Stress (Sequential Generator)")
    parser.add_argument("--t_target", type=int, default=None, 
                        help="Target time step for drawing (if omitted, sequential numbers are generated for all times)")
    parser.add_argument("--layout_seed", type=int, default=42, 
                        help="Random seed for network layout")
    parser.add_argument("--top_k", type=int, default=3, 
                        help="Number of singular node highlights with large absolute Net Flux")
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
    canvas_bg = ui_canvas.get('bg', '#121212')

    # Color setting and intuition from the theme (inverted: minus = red, plus = blue)
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
    # 1. Calculation of fixed layout (Fixed Positioning) for animation
    # ==========================================================
    G_global = nx.DiGraph()
    G_global.add_nodes_from(range(N))
    for _, row in df.iterrows():
        G_global.add_edge(int(row['src_idx']), int(row['tgt_idx']))
        
    # [Fix] Strengthen repulsive force (k=2.5) and widen scale (scale=1.5) to disperse nodes
    pos = nx.spring_layout(G_global, k=2.5, iterations=100, scale=1.5, seed=args.layout_seed)

    # ==========================================================
    # 2. Pre-calculation of robust scaling (95th percentile)
    # ==========================================================
    global_max_weight = np.percentile(df['weight'], 95) if len(df) > 0 else 1.0
    global_max_stress = np.percentile(df['stress'], 95) if len(df) > 0 else 1.0
    
    global_max_weight = max(global_max_weight, 1e-5)
    global_max_stress = max(global_max_stress, 1e-5)

    all_net_fluxes = []
    # all_gross_fluxes = []
    for t_val in df['t_idx'].unique():
        df_t_temp = df[df['t_idx'] == t_val]
        nf = np.zeros(N)
        # gf = np.zeros(N)
        for _, r in df_t_temp.iterrows():
            nf[int(r['tgt_idx'])] += r['weight']
            nf[int(r['src_idx'])] -= r['weight']
            # gf[int(r['tgt_idx'])] += r['weight']
            # gf[int(r['src_idx'])] += r['weight']
        all_net_fluxes.extend(np.abs(nf))
        # all_gross_fluxes.extend(gf)
    
    global_vmax_node = np.percentile(all_net_fluxes, 95) if all_net_fluxes else 1.0
    global_vmax_node = max(global_vmax_node, 1e-5)
    
    # global_vmax_gross = np.percentile(all_gross_fluxes, 95) if all_gross_fluxes else 1.0
    # global_vmax_gross = max(global_vmax_gross, 1e-5)

    t_targets = [args.t_target] if args.t_target is not None else sorted(df['t_idx'].unique())

    # ==========================================================
    # 3. Sequential drawing loop for each time step
    # ==========================================================
    for t in t_targets:
        t = int(t)
        df_t = df[df['t_idx'] == t]

        G = nx.DiGraph()
        G.add_nodes_from(range(N))

        net_flux = np.zeros(N)
        # gross_flux = np.zeros(N)
        for _, row in df_t.iterrows():
            src, tgt, w, s = int(row['src_idx']), int(row['tgt_idx']), row['weight'], row['stress']
            G.add_edge(src, tgt, weight=w, stress=s)
            net_flux[tgt] += w
            net_flux[src] -= w
            # gross_flux[tgt] += w
            # gross_flux[src] += w

        top_k_indices = np.argsort(np.abs(net_flux))[-args.top_k:].tolist()

        fig = plt.figure(figsize=(16, 10))
        # Network drawing area (adjusted slightly to match scale=1.5)
        ax = fig.add_axes([0.15, 0.1, 0.60, 0.80])

        # ノードカラーをRGBAにマッピング。質量ゼロの場合は背景色で塗りつぶす（空洞のリングにする）
        sm_node_temp = ScalarMappable(cmap=cmap_node, norm=Normalize(vmin=-global_vmax_node, vmax=global_vmax_node))
        # node_colors = [canvas_bg if gross_flux[i] == 0 else sm_node_temp.to_rgba(net_flux[i]) for i in range(N)]
        node_colors = [canvas_bg if abs(net_flux[i]) == 0 else sm_node_temp.to_rgba(net_flux[i]) for i in range(N)]
        
        # サイズは一律でベースサイズ(300)を持たせ、活動量に応じて拡張する
        # node_sizes = [300 if gross_flux[i] == 0 else 300 + 5000 * (min(gross_flux[i], global_vmax_gross) / global_vmax_gross) for i in range(N)]
        node_sizes = [300 if abs(net_flux[i]) == 0 else 300 + 5000 * (min(abs(net_flux[i]), global_vmax_node) / global_vmax_node) for i in range(N)]

        nodes = nx.draw_networkx_nodes(
            G, pos, ax=ax,
            node_color=node_colors,
            node_size=node_sizes,
            edgecolors=text_col, linewidths=1.5
        )

        for i in range(N):
            x, y = pos[i]
            label_name = idx_to_label.get(i, "")
            # if gross_flux[i] == 0:
            if abs(net_flux[i]) == 0:
                # 質量ゼロの幽霊ノードは、空間アンカーとして半透明で描画
                ax.text(x, y + 0.1, f"{i:02d}", fontsize=9, color=text_col, alpha=0.3, ha='center')
            elif label_name == "UNKNOWN_LEAK":
                ax.text(x, y + 0.1, f"{i:02d}", fontsize=14, fontweight='bold', color='gold', ha='center')
            elif i in top_k_indices:
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
                arrowsize=40, connectionstyle='arc3,rad=0.25'
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
                idx_str, label_str = text_str.split(":", 1)
                idx_str = idx_str.strip()
                label_str = label_str.strip()
                
                if idx_str.isdigit():
                    idx = int(idx_str)
                    # if label_str == "UNKNOWN_LEAK" and gross_flux[idx] > 0:
                    if label_str == "UNKNOWN_LEAK" and abs(net_flux[idx]) > 0:
                        text_obj.set_color('gold')
                        text_obj.set_fontweight('bold')
                    elif idx in top_k_indices:
                        text_obj.set_color(c_outlier_text)
                        text_obj.set_fontweight('bold')
                    else:
                        text_obj.set_color(text_col)
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
