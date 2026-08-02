#!/bin/bash
# ==========================================
# batch_visualize_graphs.sh
# TLU System: Visualization Orchestrator
# ==========================================
set -euo pipefail

# Parse command line arguments first so they are available when sourcing the environment
export TLU_THEME="dark"
if [ -z "${TARGET_ENV:-}" ]; then
    unset TARGET_ENV
fi

while [[ $# -gt 0 ]]; do
  case $1 in
    --target_env)
      export TARGET_ENV="$2"
      shift 2
      ;;
    --sys_params)
      export TLU_SYS_PARAMS="$2"
      shift 2
      ;;
    --interactive)
      export TLU_INTERACTIVE="true"
      shift
      ;;
    *)
      if [[ "$1" == --* ]]; then
          echo "[ERROR] Unrecognized flag: $1"
          echo "Usage: $0 [--target_env <dir>] [--sys_params <file>] [--interactive] [target_env_dir | theme]"
          exit 1
      elif [ -d "$1" ]; then
          export TARGET_ENV="$1"
      else
          # Assume Theme fallback backward compatibility
          export TLU_THEME="$1"
      fi
      shift
      ;;
  esac
done

# Load environment variables AFTER parsing TARGET_ENV
source "$(dirname "$0")/orchestrators/_tlu_env.sh"

VIZ_ORCH_DIR="./bin/visualizers"

# Primary Dashboards / Macro Indicators (Check Engine Lights)
PRIMARY_SCRIPTS=(
    "vis_000_0_1_visualize_financial_statements.sh"
    "vis_000_0_1_visualize_financial_statements_periodic.sh"
    "vis_000_2_2_visualize_principal_axes.sh"
    "vis_001_1_1_visualize_macro_thermodynamics.sh"
    "vis_002_2_1_visualize_macro_forensics.sh"
    "vis_004_1_2_visualize_system_stability.sh"
)

# Support / Ancillary Diagnostics (Deep Dives)
SUPPORT_SCRIPTS=(
    "vis_000_1_1_visualize_dynamics_state.sh"
    "vis_000_1_7_visualize_inertia_viscosity.sh"
    "vis_000_1_7_1_visualize_viscosity_trend.sh"
    "vis_000_2_1_visualize_structural_stiffness.sh"
    "vis_000_2_4_visualize_stiffness_difference.sh"
    "vis_000_2_3_visualize_eigenvector_evolution.sh"
    "vis_001_2_1_visualize_local_thermodynamics.sh"
    "vis_001_2_2_visualize_lag_matrix.sh"
    "vis_002_1_1_visualize_info_geometry.sh"
    "vis_002_1_2_visualize_network_topology.sh"
    "vis_002_1_2_1_visualize_network_topology_heatmap.sh"
    "vis_002_1_3_visualize_manifold_dimensionality.sh"
    "vis_002_2_2_visualize_micro_forensics.sh"
    "vis_003_1_1_visualize_fk_simulation.sh"
    "vis_003_1_2_visualize_ik_optimization.sh"
    "vis_003_1_3_visualize_jacobian_trajectory.sh"

    "vis_004_1_1_visualize_control_theory.sh"
    "vis_004_2_1_visualize_sensitivity_matrix.sh"
    "vis_004_2_2_visualize_sensitivity_analysis_heatmaps.sh"
    "vis_005_1_1_visualize_resonant_frequency.sh"
    "vis_005_1_2_visualize_phase_drift_heatmap.sh"
    "vis_005_2_1_visualize_fractal_noise.sh"
)

echo "🚀 Starting TLU Visualization Pipeline (Theme: ${TLU_THEME})..."
if [ -n "${TARGET_ENV:-}" ]; then
    echo "📂 Target Environment: ${TARGET_ENV}"
fi
echo "--------------------------------------------------"

# Clean the effectively mapped output plots directory to prevent lingering geometric artifacts
echo "🧹 Cleaning previous outputs in: ${TLU_PLOT_DIR}"
# rm -rf "${TLU_PLOT_DIR}"/*
rm -rf "${TLU_PLOT_DIR}"

# We need to preserve the original PLOT_DIR base
BASE_PLOT_DIR="${TLU_PLOT_DIR}"

echo ">>> Generating Primary Macro-Dashboards..."
mkdir -p "${BASE_PLOT_DIR}"
export TLU_PLOT_DIR="${BASE_PLOT_DIR}"

# Detect CPU core count for parallel execution (Approach A)
NPROC=$(sysctl -n hw.ncpu 2>/dev/null || nproc 2>/dev/null || echo 4)

echo ">>> Generating Primary Macro-Dashboards in Parallel (Jobs: ${NPROC})..."
mkdir -p "${BASE_PLOT_DIR}"
export TLU_PLOT_DIR="${BASE_PLOT_DIR}"

total_viz_start=$(date +%s)

export VIZ_ORCH_DIR
run_script() {
    local script="$1"
    if [ -f "${VIZ_ORCH_DIR}/${script}" ]; then
        bash "${VIZ_ORCH_DIR}/${script}"
    fi
}
export -f run_script

printf "%s\n" "${PRIMARY_SCRIPTS[@]}" | xargs -P "${NPROC}" -I {} bash -c 'run_script "$@"' _ {}

echo ">>> Generating Support Diagnostics in Parallel (Jobs: ${NPROC})..."
mkdir -p "${BASE_PLOT_DIR}/support"
export TLU_PLOT_DIR="${BASE_PLOT_DIR}/support"

printf "%s\n" "${SUPPORT_SCRIPTS[@]}" | xargs -P "${NPROC}" -I {} bash -c 'run_script "$@"' _ {}

find . -name "* 2.png" -delete

# Restore the original plot dir just in case
export TLU_PLOT_DIR="${BASE_PLOT_DIR}"

echo -e "\n=================================================="
echo "      TLU Visualization Execution Summary         "
echo "=================================================="
total_viz_end=$(date +%s)
total_viz_elapsed=$((total_viz_end - total_viz_start))
echo "Total Parallel Visualization Time: $total_viz_elapsed sec"
echo "=================================================="

echo "--------------------------------------------------"
echo "✅ All visualizations completed successfully."
