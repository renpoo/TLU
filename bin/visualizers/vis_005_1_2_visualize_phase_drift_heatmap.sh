#!/bin/bash
# ==========================================
# vis_005_1_2_visualize_phase_drift_heatmap.sh
# TLU System: Phase Drift Heatmap Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"
export TLU_THEME="${TLU_THEME:-dark}"

echo "  -> Generating [${TLU_THEME}]: Traversing Phase Shift Heatmap..."

DATA_PATH="${TLU_OUT_DIR}/result.005_1_2_filter_phase_shift_coherence.analysis.csv"

if [ ! -f "$DATA_PATH" ]; then
    echo "[WARN] Data file not found: $DATA_PATH"
    exit 0
fi

# The heatmap script takes a single master node (e.g. Node 6) to compute pairwise phase shifts.
cat "$DATA_PATH" | ${TLU_PY} -m src.visualizations._005_1_2_visualize_phase_drift_heatmap \
    --master_node 6 \
    --out_dir "${TLU_PLOT_DIR}" \
    --filename "005_1_2__phase_drift_heatmap.png" \
    --theme "${TLU_THEME}" \
    --node_map "${TLU_NODE_MAP}" \
    --time_map "${TLU_TIME_MAP}"

echo "✅ Saved: ${TLU_PLOT_DIR}/005_1_2__phase_drift_heatmap.png"
