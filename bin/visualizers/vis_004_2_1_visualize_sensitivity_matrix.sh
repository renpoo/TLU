#!/bin/bash
# ==========================================
# vis_004_2_1_visualize_sensitivity_matrix.sh
# TLU System: Sensitivity & Trade-off Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.13: Sensitivity & Trade-off ==="

# 1. Management Trade-off Matrix (Ripple vs Strain)
run_tlu_visualization "Sensitivity Trade-off Matrix" \
    "_004_2_1_visualize_sensitivity_matrix.py" \
    "004_2_1__sensitivity_matrix.png" \
    "result.004_2_1_filter_sensitivity.analysis.csv" \
    --top_k 3
