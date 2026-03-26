#!/bin/bash
# ==========================================
# vis_1_10_visualize_lag_matrix.sh
# TLU System: Lag Matrix Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.10: Lag Matrix ==="

run_tlu_visualization "Lag Matrix (Correlation)" "1_10_visualize_lag_matrix_correlation.py" "1_10_1__lag_matrix_correlation.png" "result.1_10_filter_lag_matrix.analysis.csv"
run_tlu_visualization "Lag Matrix (Optimal Lag)" "1_10_visualize_lag_matrix_lag.py" "1_10_2__lag_matrix_optimal_lag.png" "result.1_10_filter_lag_matrix.analysis.csv" --corr_thresh 0.5
