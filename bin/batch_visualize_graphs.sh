#!/bin/bash
# ==========================================
# batch_visualize_graphs.sh
# TLU System: Visualization Orchestrator
# ==========================================
set -euo pipefail

# 環境変数の読み込み
source "$(dirname "$0")/orchestrators/_tlu_env.sh"

# テーマを環境変数としてエクスポート（個別スクリプト群が参照する）
export TLU_THEME="${1:-dark}"

VIZ_ORCH_DIR="./bin/visualizers"

# 実行する可視化ランチャーの配列（実行順）
SCRIPTS=(
    "vis_1_1_visualize_forward_kinematics.sh"
    "vis_1_2_visualize_inverse_kinematics.sh"
    "vis_1_3_visualize_dynamics.sh"
    "vis_1_5_visualize_macro_thermodynamics.sh"
    "vis_1_6_visualize_local_thermo.sh"
    "vis_1_7_visualize_control_theory.sh"
    "vis_1_8_visualize_macro_forensics.sh"
    "vis_1_9_visualize_micro_forensics.sh"
    "vis_1_10_visualize_lag_matrix.sh"
    "vis_1_11_visualize_info_geometry.sh"
    "vis_1_12_visualize_topology.sh"
    "vis_1_13_visualize_sensitivity_matrix.sh"
    "vis_1_13_visualize_sensitivity_analysis_heatmaps.sh"
    "vis_1_14_visualize_structural_stiffness.sh"
)

echo "🚀 Starting TLU Visualization Pipeline (Theme: ${TLU_THEME})..."
echo "--------------------------------------------------"

for script in "${SCRIPTS[@]}"; do
    # スクリプトが存在する場合のみ実行
    if [ -f "${VIZ_ORCH_DIR}/${script}" ]; then
        bash "${VIZ_ORCH_DIR}/${script}"
    else
        echo "[WARN] Script not found: ${script}"
    fi
done

echo "--------------------------------------------------"
echo "✅ All visualizations completed successfully."
