#!/bin/bash
# ==========================================
# batch_unittest.sh
# TLU System: Unit and Integration Test Runner
# ==========================================
set -euo pipefail

echo "Running unit tests..."

# 環境変数の読み込み
source "$(dirname "$0")/orchestrators/_tlu_env.sh"

# テスト対象モジュールのリスト
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
    
    # --- Integration Tests ---
    "tests.integration.test_1_1_filter_fk_simulation"
    "tests.integration.test_1_2_filter_ik_optimization"
    "tests.integration.test_1_3_filter_dynamics_state"
    "tests.integration.test_1_4_filter_time_lag"
    "tests.integration.test_1_5_filter_thermodynamics_macro"
    "tests.integration.test_1_6_filter_local_thermo"
    "tests.integration.test_1_7_filter_control_theory"
    "tests.integration.test_1_8_filter_macro_forensics"
    "tests.integration.test_1_9_filter_micro_forensics"
    "tests.integration.test_1_10_filter_lag_matrix"
    "tests.integration.test_1_11_filter_info_curvature"
    "tests.integration.test_1_12_filter_network_topology"
    "tests.integration.test_1_13_filter_sensitivity"
    "tests.integration.test_1_14_filter_structural_stiffness"
)

for module in "${TEST_MODULES[@]}"; do
    echo -e "\nExecuting: ${module}"
    $TLU_PY -m "${module}"
done

echo -e "\n✅ All tests completed successfully."
