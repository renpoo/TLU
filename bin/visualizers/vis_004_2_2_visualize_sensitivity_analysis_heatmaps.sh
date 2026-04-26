#!/bin/bash
# ==========================================
# vis_004_2_1_visualize_sensitivity_analysis_heatmaps.sh
# TLU System: Sensitivity Analysis Series Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.13: Sensitivity Analysis Series Propagation ==="

run_tlu_visualization "Sensitivity Time-Series Heatmaps" \
    "_004_2_1_visualize_sensitivity_analysis_series_heatmaps.py" \
    "004_2_1__sensitivity_series_heatmaps.png" \
    "result.004_2_1_filter_sensitivity.analysis.csv" \
    --gamma 0.85 --max_k 5
