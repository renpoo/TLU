#!/bin/bash
# ==========================================
# batch_processing.sh
# TLU System: Batch Processing Orchestrator
# ==========================================
set -euo pipefail

# Parse command line arguments first so they are available when sourcing the environment
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
    --account_mapping)
      export TLU_ACCOUNT_MAPPING="$2"
      shift 2
      ;;
    *)
      if [[ "$1" == --* ]]; then
          echo "[ERROR] Unrecognized flag: $1"
          echo "Usage: $0 [--target_env <dir>] [--sys_params <file>] [--account_mapping <file>] [target_env_dir]"
          exit 1
      elif [ -d "$1" ]; then
          export TARGET_ENV="$1"
      else
          echo "[WARN] Ignoring unrecognized argument: $1"
      fi
      shift
      ;;
  esac
done

# 1. Load common environment (Initialize paths and hyperparameters)
# Assumes batch_processing.sh is executed from the project root
source "./bin/orchestrators/_tlu_env.sh"

ORCH_DIR="./bin/orchestrators"

# Array of scripts to execute (in sequential order)
SCRIPTS=(
    "000_0_1_run_financial_statements.sh"
    "000_0_1_run_financial_statements_periodic.sh"
    "0_0_run_auto_calibrate.sh"
    "000_1_1_run_dynamics_state.sh"
    "000_2_1_run_structural_stiffness.sh"
    "000_2_4_run_stiffness_difference.sh"
    "000_2_2_run_principal_axes.sh"
    "001_1_1_run_macro_thermodynamics.sh"
    "001_1_2_run_local_thermodynamics.sh"
    "001_2_1_run_lag_matrix.sh"
    "002_1_1_run_info_curvature.sh"
    "002_1_2_run_network_topology.sh"
    "002_1_3_run_manifold_dimensionality.sh"
    "002_2_1_run_macro_forensics.sh"
    "002_2_2_run_micro_forensics.sh"
    "003_1_1_run_fk_simulation.sh"
    "003_1_2_run_ik_optimization.sh"
    "003_1_3_run_jacobian_trajectory.sh"
    "004_1_1_run_control_theory.sh"
    "004_1_2_run_system_stability.sh"
    "004_2_1_run_sensitivity.sh"
    "005_1_1_run_resonant_frequency.sh"
    "005_1_2_run_phase_shift.sh"
    "005_2_1_run_fractal_noise.sh"
)

echo "Starting TLU batch processing..."

# 2. Output directory cleanup (using commonly defined paths)
if [ -d "${TLU_OUT_DIR}" ]; then
    echo "Cleaning up output directory: ${TLU_OUT_DIR}"
    rm -rf "${TLU_OUT_DIR}"/*
else
    mkdir -p "${TLU_OUT_DIR}"
fi

# 3. Sequential execution of each analysis process
ELAPSED_TIMES=()
total_start=$(date +%s)
PASSED_COUNT=0
FAILED_COUNT=0
FAILED_SCRIPTS=()

for script in "${SCRIPTS[@]}"; do
    echo -e "\n[EXECUTING] ${script}"
    start_time=$(date +%s)
    set +e
    bash "${ORCH_DIR}/${script}"
    res=$?
    set -e
    end_time=$(date +%s)
    elapsed=$((end_time - start_time))
    ELAPSED_TIMES+=($elapsed)

    if [ $res -eq 0 ]; then
        PASSED_COUNT=$((PASSED_COUNT + 1))
    else
        FAILED_COUNT=$((FAILED_COUNT + 1))
        FAILED_SCRIPTS+=("${script}")
        echo "❌ [FAILED] Script ${script} exited with code ${res}"
    fi
done

find . -name "* 2.md" -delete
find . -name "* 2.csv" -delete
find . -name "* 2.json" -delete

echo -e "\n[EXECUTING] Meta-Diagnosis Engine"
start_time=$(date +%s)
bash "bin/run_meta_diagnosis.sh"
end_time=$(date +%s)
diag_elapsed=$((end_time - start_time))

total_end=$(date +%s)
# Step 6: Export unified JSON summary for TLU Studio / TLU-App
echo ">>> Exporting Unified JSON Summary for TLU Studio..."
$TLU_PY -m src.utils._99_export_json_summary

total_elapsed=$((total_end - total_start))

# 4. Record execution to regression history ledger (tlu_dev_history/journal.jsonl)
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")
CURRENT_COMMIT=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
TOTAL_COUNT=${#SCRIPTS[@]}

if [ ${FAILED_COUNT} -eq 0 ]; then
    OVERALL_STATUS="PASSED"
else
    OVERALL_STATUS="FAILED"
fi

LEDGER_DIR="$(dirname "$0")/../tlu_dev_history"
LEDGER_FILE="${LEDGER_DIR}/journal.jsonl"

if [ -d "${LEDGER_DIR}" ]; then
    echo "{\"timestamp\": \"${TIMESTAMP}\", \"record_type\": \"run_record\", \"tool\": \"batch_processing\", \"target_env\": \"${TARGET_ENV:-default}\", \"branch\": \"${CURRENT_BRANCH}\", \"commit_hash\": \"${CURRENT_COMMIT}\", \"counts\": {\"total\": ${TOTAL_COUNT}, \"passed\": ${PASSED_COUNT}, \"failed\": ${FAILED_COUNT}}, \"status\": \"${OVERALL_STATUS}\"}" >> "${LEDGER_FILE}"
    echo "📜 Recorded batch processing run to ${LEDGER_FILE}"
fi

echo -e "\n=================================================="
echo "      TLU Batch Processing Execution Summary      "
echo "=================================================="
for i in "${!SCRIPTS[@]}"; do
    printf "%-50s : %d sec\n" "${SCRIPTS[$i]}" "${ELAPSED_TIMES[$i]}"
done
printf "%-50s : %d sec\n" "run_meta_diagnosis.sh" "$diag_elapsed"
echo "--------------------------------------------------"
echo "Total Calculation Time: $total_elapsed sec"
echo "Status: ${OVERALL_STATUS} (${PASSED_COUNT}/${TOTAL_COUNT} passed)"
echo "=================================================="

if [ ${FAILED_COUNT} -eq 0 ]; then
    echo -e "\nBatch processing completed successfully."
    exit 0
else
    echo -e "\n❌ Batch processing completed with ${FAILED_COUNT} failure(s)."
    exit 1
fi
