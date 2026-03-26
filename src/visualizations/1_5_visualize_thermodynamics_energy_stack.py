#!/usr/bin/env python3
# ==========================================
# 1_5_visualize_thermodynamics_energy_stack.py
# TLU System: Presentation Layer (Thermodynamic Energy Stack)
# Strict Theme Mode (Fail-Fast)
# ==========================================

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.visualizations.visualizer_utils import get_base_parser, apply_theme, save_plot

def setup_argparser():
    parser = get_base_parser("Energy Stack: U, -TS, and F (Dimensionally Corrected)")
    parser.set_defaults(filename="14_energy_stack.png")
    return parser

def main():
    parser = setup_argparser()
    args = parser.parse_args()

    # フォールバックを駆逐し、厳格なキー参照（Fail-Fast）を強制
    theme_cfg = apply_theme(args.theme)
    ui_canvas = theme_cfg['ui_canvas']
    text_col = ui_canvas['text_primary']
    legend_bg = ui_canvas['legend_bg']
    legend_edge = ui_canvas['legend_edge']
    grid_col = ui_canvas['grid_line']
    zero_col = ui_canvas['zero_line']
    
    colors = theme_cfg['thermodynamics']['colors']
    c_U = colors['gross_activity_U']
    c_TS = colors['friction_loss_TS']
    c_F = colors['free_energy_F']

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"Error reading from standard input: {e}", file=sys.stderr); sys.exit(1)

    if df.empty:
        print("Warning: Received empty data stream.", file=sys.stderr); sys.exit(0)

    t = df['t_idx']
    U = df['gross_activity_U']
    S = df['entropy_S']
    T_raw = df['temperature_T']
    
    T_corrected = np.sqrt(np.maximum(T_raw, 0)) 
    TS = T_corrected * S
    F_corrected = U - TS

    fig, ax = plt.subplots(figsize=(12, 7))
    
    ax.fill_between(t, 0, U, color=c_U, alpha=0.5, label='Gross Activity (U)')
    ax.fill_between(t, 0, -TS, color=c_TS, alpha=0.5, label='Friction / Loss (-TS)')
    ax.plot(t, F_corrected, color=c_F, linewidth=3, marker='o', markersize=6, 
            label='Free Energy (F = U - TS)')
    
    ax.axhline(0, color=zero_col, linestyle='--', linewidth=1.5)

    ax.set_xlabel('Time Step (t_idx)', fontsize=12, color=text_col)
    ax.set_ylabel('Energy / Activity Scale', fontsize=12, color=text_col)
    ax.set_title('Thermodynamic Energy Stack: Efficiency & Friction Loss over Time', fontsize=15, pad=15, color=text_col, fontweight='bold')
    
    leg = ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), 
                    facecolor=legend_bg, edgecolor=legend_edge)
    for text in leg.get_texts(): text.set_color(text_col)
    
    ax.grid(True, linestyle=':', alpha=0.5, color=grid_col)
    ax.tick_params(colors=text_col)
    for spine in ax.spines.values():
        spine.set_color(text_col)
    ax.margins(0.05)
    
    plt.tight_layout()
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
