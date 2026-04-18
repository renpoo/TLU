#!/bin/bash
# ==========================================
# batch_visualize_graphs.sh
# TLU System: Visualization Orchestrator
# ==========================================
set -euo pipefail

# Load environment variables
source "$(dirname "$0")/orchestrators/_tlu_env.sh"

# Export theme as an environment variable (referenced by individual visualization scripts)
export TLU_THEME="${1:-dark}"

VIZ_ORCH_DIR="./bin/visualizers"

# Array of visualization launchers to execute (in sequential order)
SCRIPTS=(
    "vis_000_1_1_visualize_dynamics_state.sh"
    "vis_000_2_1_visualize_structural_stiffness.sh"
    "vis_001_1_1_visualize_macro_thermodynamics.sh"
    "vis_001_2_1_visualize_local_thermodynamics.sh"
    "vis_001_2_2_visualize_lag_matrix.sh"
    "vis_002_1_1_visualize_info_geometry.sh"
    "vis_002_1_2_visualize_network_topology.sh"
    "vis_002_2_1_visualize_macro_forensics.sh"
    "vis_002_2_2_visualize_micro_forensics.sh"
    "vis_003_1_1_visualize_fk_simulation.sh"
    "vis_003_1_2_visualize_ik_optimization.sh"
    "vis_004_1_1_visualize_control_theory.sh"
    "vis_004_2_1_visualize_sensitivity_matrix.sh"
    "vis_004_2_2_visualize_sensitivity_analysis_heatmaps.sh"
)

echo "🚀 Starting TLU Visualization Pipeline (Theme: ${TLU_THEME})..."
echo "--------------------------------------------------"

rm -rf workspace/output_plots/*

for script in "${SCRIPTS[@]}"; do
    # Execute only if the script exists
    if [ -f "${VIZ_ORCH_DIR}/${script}" ]; then
        bash "${VIZ_ORCH_DIR}/${script}"
    else
        echo "[WARN] Script not found: ${script}"
    fi
done

echo "--------------------------------------------------"
echo "✅ All visualizations completed successfully."
