#!/bin/bash
# ==========================================
# batch_processing.sh
# TLU System: Batch Processing Orchestrator
# ==========================================
set -euo pipefail

ORCH_DIR="./bin/orchestrators"

# 実行するスクリプトの配列（実行順）
SCRIPTS=(
    # "1_1_run_fk_simulation.sh"
    # "1_2_run_ik_optimization.sh"
    "1_3_run_dynamics_state.sh"
    "1_4_run_time_lag.sh"
    "1_5_run_thermodynamics_macro.sh"
    "1_6_run_local_thermo.sh"
    "1_7_run_control_theory.sh"
    "1_8_run_macro_forensics.sh"
    "1_9_run_micro_forensics.sh"
    "1_10_run_lag_matrix.sh"
    "1_11_run_info_curvature.sh"
    "1_12_run_network_topology.sh"
    "1_13_run_sensitivity.sh"
    "1_14_run_structural_stiffness.sh"
)

echo "Starting batch processing..."

for script in "${SCRIPTS[@]}"; do
    echo -e "\nRunning ${script}..."
    bash "${ORCH_DIR}/${script}"
done

echo -e "\nBatch processing completed successfully."
