#!/bin/bash
source "$(dirname "$0")/_tlu_env.sh"

# 2. パラメータの取得と Fail-Fast 検証
GAMMA="${TLU_DAMPING_FACTOR:?環境変数 TLU_DAMPING_FACTOR が設定されていません。}"

# 3. パイプラインの実行
run_tlu_pipeline "Inverse Kinematics (IK) Filter" \
    "Tgt" "Src" \
    "src.filters._003_1_2_filter_ik_optimization" "result.003_1_2_filter_ik.analysis.csv" \
    --target_labels="ACC_Sales_Revenue:100.0" --gamma="${GAMMA}" --max_k=5 --node_map="${TLU_NODE_MAP}"

# --target_labels="三条烏丸:100.0" --gamma=0.85 --max_k=5 --node_map="${TLU_NODE_MAP}"
