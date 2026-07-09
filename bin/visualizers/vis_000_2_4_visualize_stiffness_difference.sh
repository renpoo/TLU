#!/bin/bash
# ==========================================
# vis_000_2_4_visualize_stiffness_difference.sh
# TLU System: Run sequential plotting of stiffness temporal differences
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Stiffness Temporal Differences ==="

run_tlu_visualization "Stiffness Diff Heatmaps" "_000_2_4_visualize_stiffness_diff_heatmap.py" "000_2_4__stiffness_diff.png" "result.000_2_4_stiffness_diff.analysis.csv"
