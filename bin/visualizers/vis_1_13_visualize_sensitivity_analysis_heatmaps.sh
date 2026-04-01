#!/bin/bash
# ==========================================
# vis_1_13_visualize_sensitivity_analysis_heatmaps.sh
# TLU System: Sensitivity Analysis Series Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.13: Sensitivity Analysis Series Propagation ==="

run_tlu_visualization "Sensitivity Analysis Series Propagation Heatmap" \
    "1_13_visualize_sensitivity_analysis_series_heatmaps.py" \
    "1_13_2__sensitivity_analysis_series_heatmap.png" \
    "../ephemeral/_coo_stream.csv" \
    --gamma 0.8 --max_k 5

