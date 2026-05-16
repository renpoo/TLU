#!/bin/bash
# ==========================================
# vis_000_0_2_visualize_basic_statistics.sh
# TLU System: Classical Statistics Baseline (Modular Visuals)
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 0.5: Classical Statistics Baseline ==="

run_tlu_visualization "Classical Stats: 1. Stacked Bar" "_000_0_2_1_visualize_stacked_bar.py" "000_0_2_1__stacked_bar.png" "result.000_1_1_filter_dynamics.analysis.csv"

NODE_MAP_FILE="${TLU_NODE_MAP}"
if [ -f "$NODE_MAP_FILE" ]; then
    # Extract node labels and format them exactly as the semantic hydrator does: '00_NodeName'
    # Use $1 (node_idx) and $2 (node_label) from the CSV.
    $TLU_AWK -F',' 'NR>1 {printf "%02d_%s\n", $1, $2}' "$NODE_MAP_FILE" | while read -r TARGET_NODE; do
        if [ -z "$TARGET_NODE" ]; then continue; fi
        
        # Semantic Window Size: 1/3 of the observation cycle (e.g., Quarterly for Monthly data)
        # Bounded to a minimum of 4 to ensure Kurtosis can be calculated.
        WINDOW_SIZE=$(( TLU_OBSERVATION_WINDOW_STEPS / 3 ))
        if [ "$WINDOW_SIZE" -lt 4 ]; then WINDOW_SIZE=4; fi

        run_tlu_visualization "Classical Stats: 2. Scatter Drift (${TARGET_NODE})" "_000_0_2_2_visualize_scatter_drift.py" "000_0_2_2__scatter_drift_${TARGET_NODE}.png" "result.000_1_1_filter_dynamics.analysis.csv" \
            --target_node "${TARGET_NODE}"

        run_tlu_visualization "Classical Stats: 3. Histogram KDE (${TARGET_NODE})" "_000_0_2_3_visualize_histogram_kde.py" "000_0_2_3__histogram_kde_${TARGET_NODE}.png" "result.000_1_1_filter_dynamics.analysis.csv" \
            --target_node "${TARGET_NODE}"

        run_tlu_visualization "Classical Stats: 4. Rolling Quantile Bands (${TARGET_NODE})" "_000_0_2_4_visualize_rolling_quantiles.py" "000_0_2_4__rolling_quantiles_${TARGET_NODE}.png" "result.000_1_1_filter_dynamics.analysis.csv" \
            --target_node "${TARGET_NODE}" \
            --window_size "${WINDOW_SIZE}"

        run_tlu_visualization "Classical Stats: 5. Kurtosis vs Phase (${TARGET_NODE})" "_000_0_2_5_visualize_kurtosis_vs_phase.py" "000_0_2_5__kurtosis_vs_phase_${TARGET_NODE}.png" "result.000_1_1_filter_dynamics.analysis.csv" \
            --phase_csv "${TLU_OUT_DIR}/result.005_1_2_filter_phase_shift_coherence.analysis.csv" \
            --target_node "${TARGET_NODE}" \
            --window_size "${WINDOW_SIZE}"
    done
else
    echo "[WARN] Node map not found at $NODE_MAP_FILE. Cannot generate per-node classical stats."
fi
