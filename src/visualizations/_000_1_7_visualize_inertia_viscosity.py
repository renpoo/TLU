#!/usr/bin/env python3
# ==========================================
# _000_1_7_visualize_inertia_viscosity.py
# TLU System: Dynamics Phase Space (Inertia vs Viscosity)
# Version: 6.0.0 (Refactored with BaseVisualizer Architecture)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.visualizations.base_visualizer import BaseVisualizer
from src.visualizations.visualizer_utils import load_node_labels, render_node_map_legend

class InertiaViscosityVisualizer(BaseVisualizer):
    cli_description = "Dynamics Phase Space: Inertia vs Viscosity Scatter Plot"
    default_filename = "1_3_7_inertia_viscosity_scatter.png"

    def add_arguments(self, parser: argparse.ArgumentParser):
        parser.add_argument("--top_k", type=int, default=3, help="Number of singular points to highlight")

    def render_plot(self, df: pd.DataFrame, theme_cfg: dict, args: argparse.Namespace) -> plt.Figure:
        ui_canvas = theme_cfg['ui_canvas']
        text_col = ui_canvas['text_primary']
        grid_line_col = ui_canvas['grid_line']
        c_normal = ui_canvas['data_normal']

        forensics_colors = theme_cfg['forensics']['colors']
        c_outlier = forensics_colors['z_score_shock']
        c_outlier_text = forensics_colors['anomaly_outlier']

        df_mean = df.groupby('node_idx').mean(numeric_only=True).reset_index()
        df_mean['log_C'] = np.log10(np.where(df_mean['viscosity_C'] <= 0, 1e-6, df_mean['viscosity_C']))

        N = int(df_mean['node_idx'].max()) + 1
        idx_to_label = load_node_labels(args.node_map, N)

        fig, ax = plt.subplots(figsize=(14, 8))
        
        top_k_df = df_mean.nlargest(args.top_k, 'inertia_M')
        normals = df_mean.drop(top_k_df.index)

        ax.scatter(normals['inertia_M'], normals['log_C'], 
                   color=c_normal, s=120, alpha=0.7, edgecolors=text_col, linewidths=1.0)
        
        ax.scatter(top_k_df['inertia_M'], top_k_df['log_C'], 
                   color=c_outlier, s=300, alpha=0.9, edgecolors=text_col, marker='*', linewidths=1.2)

        for _, row in top_k_df.iterrows():
            idx = int(row['node_idx'])
            ax.text(row['inertia_M'], row['log_C'], f"  {idx:02d}", 
                    color=c_outlier_text, fontsize=12, fontweight='bold', va='bottom', ha='left')
                    
        for _, row in normals.iterrows():
            idx = int(row['node_idx'])
            ax.text(row['inertia_M'], row['log_C'], f"  {idx:02d}", 
                    color=text_col, fontsize=10, alpha=0.9, va='bottom', ha='left')

        top_k_indices = top_k_df['node_idx'].astype(int).tolist()
        render_node_map_legend(ax, idx_to_label, highlight_indices=top_k_indices, max_legend=args.max_legend, theme_cfg=theme_cfg)
                     
        plt.subplots_adjust(right=0.77, left=0.1, top=0.9, bottom=0.1)

        ax.set_xlabel('Inertia (M) - Mass & Scale', fontsize=12, color=text_col, labelpad=10)
        ax.set_ylabel('Viscosity (Log10 C) - Friction & Resistance', fontsize=12, color=text_col, labelpad=10)
        ax.set_title('Dynamics Phase Space: Inertia vs Viscosity (Bottleneck Identification)', fontsize=15, color=text_col, fontweight='bold', pad=15)
        
        ax.margins(0.15)
        ax.grid(True, linestyle=':', alpha=0.6, color=grid_line_col)
        ax.tick_params(colors=text_col)
        for spine in ax.spines.values():
            spine.set_color(text_col)

        return fig

def main():
    vis = InertiaViscosityVisualizer()
    vis.run()

if __name__ == "__main__":
    main()
