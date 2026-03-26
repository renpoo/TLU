#!/bin/bash
# ==========================================
# vis_1_13_visualize_sensitivity.sh
# TLU System: Sensitivity & Trade-off Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.13: Sensitivity & Trade-off ==="

# 1. 経営のトレードオフ・マトリクス (Ripple vs Strain)
run_tlu_visualization "Sensitivity Trade-off Matrix" \
    "1_13_visualize_sensitivity_matrix.py" \
    "1_13_1__sensitivity_matrix.png" \
    "result.1_13_filter_sensitivity.analysis.csv" \
    --top_k 3
