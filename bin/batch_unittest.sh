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
    "tests.unit.test_0_1_aggregate_stream"
    "tests.unit.test_0_2_skip_initial_stream"
    "tests.unit.test_base_aggregator"
    "tests.unit.test_base_filter"
    "tests.unit.test_base_generator"
    "tests.unit.test_base_visualizer"
    "tests.unit.test_cli_parser"
    "tests.unit.test_stream_processor"
    "tests.unit.test_index_registry"
    "tests.unit.test_core_accounting_taxonomy"
    "tests.unit.test_core_contracts"
    "tests.unit.test_core_control_theory"
    "tests.unit.test_core_dynamics"
    "tests.unit.test_core_echo_dynamics"
    "tests.unit.test_core_forensics"
    "tests.unit.test_core_information_geometry"
    "tests.unit.test_core_kinematics"
    "tests.unit.test_core_safe_linalg"
    "tests.unit.test_core_temporal_binning"
    "tests.unit.test_core_tensor_ops"
    "tests.unit.test_core_thermodynamics"
    "tests.unit.test_core_topology"
    "tests.unit.test_dummy_market_generator"
    "tests.unit.test_filter_linear_algebra"
    "tests.unit.test_filter_phase_shift"
    "tests.unit.test_003_1_3_filter_jacobian_trajectory"
    "tests.unit.test_utils"

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

# 2.5 Mechanical verification: Verify that ALL existing test_*.py files are listed in TEST_MODULES
echo "[VERIFYING] Test module list completeness..."
ALL_TEST_FILES=$(find tests/unit tests/integration -name "test_*.py" | sort)
MISSING_TESTS=0

for test_file in ${ALL_TEST_FILES}; do
    # Convert file path to module name (e.g. tests/unit/test_foo.py -> tests.unit.test_foo)
    mod_name=$(echo "${test_file}" | sed 's/\.py$//' | tr '/' '.')
    if [[ ! " ${TEST_MODULES[*]} " =~ " ${mod_name} " ]]; then
        echo -e "⚠️  [WARNING] Unexecuted test file detected: ${test_file} (${mod_name})"
        MISSING_TESTS=$((MISSING_TESTS + 1))
    fi
done

if [ ${MISSING_TESTS} -gt 0 ]; then
    echo "❌ ERROR: Found ${MISSING_TESTS} unexecuted test file(s). Please add them to TEST_MODULES in batch_unittest.sh."
    exit 1
fi
echo "✅ Test module completeness check PASSED (all $(echo "${ALL_TEST_FILES}" | wc -l | tr -d ' ') test files included)."

# 3. Sequential execution of tests
for module in "${TEST_MODULES[@]}"; do
    echo -e "\n[EXECUTING] ${module}"
    $TLU_PY -m "${module}"
done

echo ""
echo "=================================================="
echo "✅ All tests completed successfully."
echo "=================================================="
