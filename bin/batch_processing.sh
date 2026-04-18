#!/bin/bash
# ==========================================
# batch_processing.sh
# TLU System: Batch Processing Orchestrator
# ==========================================
set -euo pipefail

# 1. 共通環境の読み込み（パスとハイパーパラメータの初期化）
# batch_processing.sh がプロジェクトルートにあると仮定
source "./bin/orchestrators/_tlu_env.sh"

ORCH_DIR="./bin/orchestrators"

# 実行するスクリプトの配列（実行順）
SCRIPTS=(
    "000_1_1_run_dynamics_state.sh"
    "000_2_1_run_structural_stiffness.sh"
    "001_1_1_run_macro_thermodynamics.sh"
    "001_1_2_run_local_thermodynamics.sh"
    "001_2_1_run_lag_matrix.sh"
    "002_1_1_run_info_curvature.sh"
    "002_1_2_run_network_topology.sh"
    "002_2_1_run_macro_forensics.sh"
    "002_2_2_run_micro_forensics.sh"
    "003_1_1_run_fk_simulation.sh"
    "003_1_2_run_ik_optimization.sh"
    "004_1_1_run_control_theory.sh"
    "004_2_1_run_sensitivity.sh"
)

echo "Starting TLU batch processing..."

# 2. 出力ディレクトリのクリーンアップ（共通定義パスを使用）
if [ -d "${TLU_OUT_DIR}" ]; then
    echo "Cleaning up output directory: ${TLU_OUT_DIR}"
    rm -rf "${TLU_OUT_DIR}"/*
else
    mkdir -p "${TLU_OUT_DIR}"
fi

# 3. 各解析プロセスの逐次実行
for script in "${SCRIPTS[@]}"; do
    echo -e "\n[EXECUTING] ${script}"
    bash "${ORCH_DIR}/${script}"
done

echo -e "\nBatch processing completed successfully."
