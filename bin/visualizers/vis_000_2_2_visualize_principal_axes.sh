#!/bin/bash
# ==========================================
# vis_000_2_2_visualize_principal_axes.sh
# TLU System: Principal Axes Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 000_2_2: Principal Axes ==="

run_tlu_visualization "Principal Axes Ratio" "_000_2_2_visualize_principal_axes_ratio.py" "000_2_2__principal_axes_ratio.png" "result.000_2_2_filter_principal_axes.analysis.csv"
