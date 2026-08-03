#!/usr/bin/env python3
# ==========================================
# _001_1_1_visualize_thermodynamics_dashboard.py
# TLU System: Macro Thermodynamics Dashboard
# Version: 6.0.0 (Refactored with BaseVisualizer Architecture)
# ==========================================
import sys
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.visualizations.base_visualizer import BaseVisualizer
from src.visualizations.visualizer_utils import load_time_labels

class ThermodynamicsDashboardVisualizer(BaseVisualizer):
    cli_description = "Thermodynamics Dashboard (X=t, Y=S, Z=T)"
    default_filename = "1_5_1__thermodynamics_dashboard.png"

    def render_plot(self, df: pd.DataFrame, theme_cfg: dict, args: argparse.Namespace) -> plt.Figure:
        ui_canvas = theme_cfg['ui_canvas']
        text_col = ui_canvas['text_primary']
        legend_bg_col = ui_canvas['legend_bg']
        legend_edge_col = ui_canvas['legend_edge']
        grid_line_col = ui_canvas['grid_line']
        zero_line_col = ui_canvas['zero_line']

        colors = theme_cfg['thermodynamics']['colors']
        c_U = colors['gross_activity_U']
        c_F = colors['free_energy_F']
        c_T = colors['temperature_T']
        c_S = colors['entropy_S']

        t = df['t_idx']
        U = df['gross_activity_U']
        S = df['entropy_S']
        T_raw = df['temperature_T']

        T_max_idx = int(t.max()) + 1
        time_labels = load_time_labels(args.time_map, T_max_idx)
        
        T_corrected = np.maximum(T_raw, 0)
        TS = T_corrected * S
        F_corrected = U - TS

        fig, axes = plt.subplots(4, 1, figsize=(12, 12), sharex=True)
        
        # 1. Internal Energy (U)
        axes[0].plot(t, U, color=c_U, marker='s', markersize=5, linewidth=2, label='Internal Energy (U)')
        axes[0].axhline(0, color=zero_line_col, linestyle='--', linewidth=1)
        axes[0].set_title("1. Internal Energy (U) : Gross Activity Scale", loc='left', fontweight='bold', color=text_col)
        axes[0].set_ylabel("U (Amount)", color=text_col)
        leg0 = axes[0].legend(loc='best', facecolor=legend_bg_col, edgecolor=legend_edge_col)
        for text in leg0.get_texts(): text.set_color(text_col)
        axes[0].grid(True, linestyle=':', alpha=0.8, color=grid_line_col)

        # 2. Free Energy (F)
        axes[1].plot(t, F_corrected, color=c_F, marker='o', markersize=5, linewidth=2, label='Free Energy (F)')
        axes[1].axhline(0, color=zero_line_col, linestyle='--', linewidth=1)
        axes[1].set_title("2. Free Energy (F) : Net Available Power (Corrected)", loc='left', fontweight='bold', color=text_col)
        axes[1].set_ylabel("F (Amount)", color=text_col)
        leg1 = axes[1].legend(loc='best', facecolor=legend_bg_col, edgecolor=legend_edge_col)
        for text in leg1.get_texts(): text.set_color(text_col)
        axes[1].grid(True, linestyle=':', alpha=0.8, color=grid_line_col)

        # 3. Temperature (T)
        axes[2].plot(t, T_corrected, color=c_T, marker='^', markersize=5, linewidth=2, label='Temperature (T)')
        axes[2].axhline(0, color=zero_line_col, linestyle='--', linewidth=1)
        axes[2].set_title("3. Temperature (T) : Volatility / Friction Level (Corrected)", loc='left', fontweight='bold', color=text_col)
        axes[2].set_ylabel("T (Amount)", color=text_col)
        leg2 = axes[2].legend(loc='best', facecolor=legend_bg_col, edgecolor=legend_edge_col)
        for text in leg2.get_texts(): text.set_color(text_col)
        axes[2].grid(True, linestyle=':', alpha=0.8, color=grid_line_col)

        # 4. Entropy (S)
        axes[3].plot(t, S, color=c_S, marker='x', markersize=5, linewidth=2, label='Entropy (S)')
        axes[3].axhline(0, color=zero_line_col, linestyle='--', linewidth=1)
        axes[3].set_title("4. Entropy (S) : Structural Disorder & Information Dispersion", loc='left', fontweight='bold', color=text_col)
        axes[3].set_ylabel("S (Ratio)", color=text_col)
        leg3 = axes[3].legend(loc='best', facecolor=legend_bg_col, edgecolor=legend_edge_col)
        for text in leg3.get_texts(): text.set_color(text_col)
        axes[3].grid(True, linestyle=':', alpha=0.8, color=grid_line_col)

        bottom_ax = axes[3]
        ticks = df['t_idx'].values
        labels = [str(time_labels.get(t, t)) for t in ticks]
        bottom_ax.set_xticks(ticks)
        bottom_ax.set_xticklabels(labels, rotation=90, ha='center', color=text_col)
        bottom_ax.set_xlabel("Timeline", color=text_col, fontsize=12)

        for ax in axes:
            ax.margins(0.1)
            ax.tick_params(axis='y', colors=text_col)
            for spine in ax.spines.values():
                spine.set_color(text_col)

        return fig

def main():
    vis = ThermodynamicsDashboardVisualizer()
    vis.run()

if __name__ == "__main__":
    main()
