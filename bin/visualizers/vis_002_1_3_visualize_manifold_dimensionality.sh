#!/bin/bash
# ==========================================
# vis_002_1_3_visualize_manifold_dimensionality.sh
# TLU System: Manifold Dimensionality Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 002_1_3: Manifold Dimensionality ==="

run_tlu_visualization "Manifold Dimensionality" "_002_1_3_visualize_manifold_dimensionality.py" "002_1_3__manifold_dimensionality.png" "result.002_1_3_filter_manifold_dimensionality.analysis.csv"
