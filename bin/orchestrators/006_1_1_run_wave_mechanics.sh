#!/bin/bash
# ==========================================
# 006_1_1_run_wave_mechanics.sh
# TLU System: Wave Mechanics (Phase Space) Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

echo "Running Wave Mechanics (Phase Space) Filter"

# We bypass run_tlu_pipeline because we need to read from the hydrated dynamics output
# rather than the raw COO stream.
DYNAMICS_FILE="${TLU_OUT_DIR}/result.000_1_1_filter_dynamics.analysis.csv"
OUTPUT_FILE="${TLU_OUT_DIR}/result.006_1_1_filter_wave_mechanics.analysis.csv"

if [ ! -f "${DYNAMICS_FILE}" ]; then
    echo "[ERROR] ${DYNAMICS_FILE} not found. Must run 000_1_1_run_dynamics_state.sh first."
    exit 1
fi

cat "${DYNAMICS_FILE}" \
| $TLU_PY -m src.filters._006_1_1_filter_wave_mechanics --out_plot="006_wmu_phase_matrix" \
> "${OUTPUT_FILE}"

echo "Wave Mechanics Filter completed."
echo ""
