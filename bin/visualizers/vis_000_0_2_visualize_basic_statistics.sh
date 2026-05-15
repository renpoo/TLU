#!/bin/bash
# ==========================================
# vis_000_0_2_visualize_basic_statistics.sh
# TLU System: Classical Statistics Baseline (Modular Visuals)
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 0.5: Classical Statistics Baseline ==="

run_tlu_visualization "Classical Stats: 1. Stacked Bar" "_000_0_2_1_visualize_stacked_bar.py" "000_0_2_1__stacked_bar.png" "result.000_1_1_filter_dynamics.analysis.csv"

run_tlu_visualization "Classical Stats: 2. Scatter Drift" "_000_0_2_2_visualize_scatter_drift.py" "000_0_2_2__scatter_drift.png" "result.000_1_1_filter_dynamics.analysis.csv" \
    --target_node "US10Y"

run_tlu_visualization "Classical Stats: 3. Histogram KDE" "_000_0_2_3_visualize_histogram_kde.py" "000_0_2_3__histogram_kde.png" "result.000_1_1_filter_dynamics.analysis.csv" \
    --target_node "US10Y"

run_tlu_visualization "Classical Stats: 4. Rolling Quantile Bands" "_000_0_2_4_visualize_rolling_quantiles.py" "000_0_2_4__rolling_quantiles.png" "result.000_1_1_filter_dynamics.analysis.csv" \
    --target_node "US10Y" \
    --window_size 12

run_tlu_visualization "Classical Stats: 5. Kurtosis vs Phase" "_000_0_2_5_visualize_kurtosis_vs_phase.py" "000_0_2_5__kurtosis_vs_phase.png" "result.000_1_1_filter_dynamics.analysis.csv" \
    --phase_csv "${TLU_OUT_DIR}/result.005_1_2_filter_phase_shift_coherence.analysis.csv" \
    --target_node "US10Y" \
    --window_size 12
