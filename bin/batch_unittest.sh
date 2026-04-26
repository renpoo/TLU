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
    "tests.unit.test_cli_parser"
    "tests.unit.test_stream_processor"
    "tests.unit.test_index_registry"
    "tests.unit.test_core_safe_linalg"
    "tests.unit.test_core_echo_dynamics"
    "tests.unit.test_core_tensor_ops"
    "tests.unit.test_core_kinematics"
    "tests.unit.test_core_dynamics"
    "tests.unit.test_core_information_geometry"
    "tests.unit.test_core_thermodynamics"
    "tests.unit.test_core_forensics"
    "tests.unit.test_core_control_theory"
    "tests.unit.test_core_topology"
    "tests.unit.test_filter_linear_algebra"
    
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
)

# 3. Sequential execution of tests
for module in "${TEST_MODULES[@]}"; do
    echo -e "\n[EXECUTING] ${module}"
    $TLU_PY -m "${module}"
done

echo ""
echo "=================================================="
echo "✅ All tests completed successfully."
echo "=================================================="
