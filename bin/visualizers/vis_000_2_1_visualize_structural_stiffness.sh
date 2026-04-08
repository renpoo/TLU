#!/bin/bash
# ==========================================
# vis_000_2_1_visualize_structural_stiffness.sh
# TLU System: Structural Stiffness Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.14: Structural Stiffness Matrix ==="

run_tlu_visualization "Structural Stiffness Heatmap" \
    "000_2_1_visualize_structural_stiffness.py" \
    "000_2_1__structural_stiffness.png" \
    "result.000_2_1_filter_structural_stiffness.analysis.csv"
