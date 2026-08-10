#!/bin/bash
# ==========================================
# batch_unittest.sh
# TLU System: Unit and Integration Test Runner
# ==========================================
set -euo pipefail

echo "=================================================="
echo "TLU System: Unit & Integration Test Runner"
echo "=================================================="

# 1. Load environment variables
source "$(dirname "$0")/orchestrators/_tlu_env.sh"

# 2. Define test modules
TEST_MODULES=(
    # --- Unit Tests ---
    "tests.unit.test_00_1_parse_journal"
    "tests.unit.test_00_2_aggregate_journal"
    "tests.unit.test_0_0_generate_dummy_journal"
    "tests.unit.test_0_0_generate_dummy_market"
    "tests.unit.test_cli_parser"
    "tests.unit.test_stream_processor"
    "tests.unit.test_index_registry"
    "tests.unit.test_core_safe_linalg"
    "tests.unit.test_core_tensor_ops"
    "tests.unit.test_core_kinematics"
    "tests.unit.test_core_dynamics"
    "tests.unit.test_core_information_geometry"
    "tests.unit.test_core_thermodynamics"
    "tests.unit.test_core_forensics"
    "tests.unit.test_core_control_theory"
    "tests.unit.test_core_topology"
    "tests.unit.test_filter_linear_algebra"
    "tests.unit.test_filter_phase_shift"
    "tests.unit.test_003_1_3_filter_jacobian_trajectory"

    
    # --- Integration Tests ---
    "tests.integration.test_000_1_1_filter_dynamics_state"
    "tests.integration.test_000_2_1_filter_structural_stiffness"
    "tests.integration.test_001_1_1_filter_macro_thermodynamics"
    "tests.integration.test_001_1_2_filter_local_thermodynamics"
    "tests.integration.test_001_2_1_filter_lag_matrix"
    "tests.integration.test_002_1_1_filter_info_curvature"
    "tests.integration.test_002_1_2_filter_network_topology"
    "tests.integration.test_002_2_1_filter_macro_forensics"
    "tests.integration.test_002_2_2_filter_micro_forensics"
    "tests.integration.test_003_1_1_filter_fk_simulation"
    "tests.integration.test_003_1_2_filter_ik_optimization"
    "tests.integration.test_004_1_1_filter_control_theory"
    "tests.integration.test_004_2_1_filter_sensitivity"
    "tests.integration.test_005_1_1_filter_resonant_frequency"
    "tests.integration.test_005_1_2_filter_phase_shift_coherence"
    "tests.integration.test_005_2_1_filter_fractal_noise"
)

# 3. Sequential execution of tests
for module in "${TEST_MODULES[@]}"; do
    echo -e "\n[EXECUTING] ${module}"
    $TLU_PY -m "${module}"
done

# 4. Record test execution to regression history ledger (tlu_dev_history/journal.jsonl)
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "unknown")
CURRENT_COMMIT=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
TOTAL_COUNT=${#TEST_MODULES[@]}

LEDGER_DIR="$(dirname "$0")/../tlu_dev_history"
LEDGER_FILE="${LEDGER_DIR}/journal.jsonl"

if [ -d "${LEDGER_DIR}" ]; then
    echo "{\"timestamp\": \"${TIMESTAMP}\", \"record_type\": \"run_record\", \"tool\": \"batch_unittest\", \"branch\": \"${CURRENT_BRANCH}\", \"commit_hash\": \"${CURRENT_COMMIT}\", \"counts\": {\"total\": ${TOTAL_COUNT}, \"passed\": ${TOTAL_COUNT}, \"failed\": 0}, \"status\": \"PASSED\"}" >> "${LEDGER_FILE}"
    echo "📜 Recorded test run to ${LEDGER_FILE}"
fi

echo ""
echo "=================================================="
echo "✅ All tests completed successfully."
echo "=================================================="
