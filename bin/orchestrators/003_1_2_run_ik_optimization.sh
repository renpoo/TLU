#!/bin/bash
source "$(dirname "$0")/_tlu_env.sh"

# 2. Parameter retrieval and Fail-Fast verification
GAMMA="${TLU_DAMPING_FACTOR:?Environment variable TLU_DAMPING_FACTOR is not set.}"
MAX_K="${TLU_KINEMATICS_MAX_K:?Environment variable TLU_KINEMATICS_MAX_K is not set.}"
TARGETS="${TLU_IK_TARGET_LABELS:?Environment variable TLU_IK_TARGET_LABELS is not set.}"

# 3. Execute pipeline
run_tlu_pipeline "Inverse Kinematics (IK) Filter" \
    "Tgt" "Src" \
    "src.filters._003_1_2_filter_ik_optimization" "result.003_1_2_filter_ik.analysis.csv" \
    --target_labels="${TARGETS}" \
    --gamma="${GAMMA}" \
    --max_k="${MAX_K}" \
    --node_map="${TLU_NODE_MAP}"

# --target_labels="三条烏丸:100.0" --gamma=0.85 --max_k=5 --node_map="${TLU_NODE_MAP}"
