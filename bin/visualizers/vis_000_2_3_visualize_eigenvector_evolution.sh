#!/bin/bash
# ==========================================
# vis_000_2_3_visualize_eigenvector_evolution.sh
# TLU System: Eigenvector Evolution Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 000_2_3: Eigenvector Evolution ==="

run_tlu_visualization "Eigenvector Evolution" "_000_2_3_visualize_eigenvector_evolution.py" "000_2_3__eigenvector_evolution.png" "result.000_2_2_filter_principal_axes.analysis.csv"
