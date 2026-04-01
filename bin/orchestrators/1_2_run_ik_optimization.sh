#!/bin/bash
source "$(dirname "$0")/_tlu_env.sh"

run_tlu_pipeline "Inverse Kinematics (IK) Filter" \
    "Tgt" "Src" \
    "src.filters._1_2_filter_ik_optimization" "result.1_2_filter_ik.analysis.csv" \
    --target_labels="三条烏丸:100.0" --gamma=0.85 --max_k=5 --node_map="${TLU_NODE_MAP}"
