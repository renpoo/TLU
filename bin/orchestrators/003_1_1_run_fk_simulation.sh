#!/bin/bash
source "$(dirname "$0")/_tlu_env.sh"

# 2. Parameter retrieval and Fail-Fast verification
GAMMA="${TLU_DAMPING_FACTOR:?Environment variable TLU_DAMPING_FACTOR is not set.}"

# 3. Execute pipeline
run_tlu_pipeline "Forward Kinematics (FK) Filter" \
    "Src" "Tgt" \
    "src.filters._003_1_1_filter_fk_simulation" "result.003_1_1_filter_fk.analysis.csv" \
    --fk_input_mode="static" --static_dq_labels="ACC_Sales_Revenue:100" --gamma="${GAMMA}" --max_k=5 --node_map="${TLU_NODE_MAP}"


# --fk_input_mode="actual" --gamma=0.85 --max_k=6 --node_map="${TLU_NODE_MAP}"

# --fk_input_mode="static" --static_dq_labels="ACC_Sales_Revenue:100" --gamma=0.85 --max_k=5 --node_map="${TLU_NODE_MAP}"

# --fk_input_mode="static" --static_dq_labels="三条烏丸:100" --gamma=0.85 --max_k=5 --node_map="${TLU_NODE_MAP}"
