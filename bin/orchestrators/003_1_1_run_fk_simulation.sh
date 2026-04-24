#!/bin/bash
source "$(dirname "$0")/_tlu_env.sh"

# 2. Parameter retrieval and Fail-Fast verification
GAMMA="${TLU_DAMPING_FACTOR:?Environment variable TLU_DAMPING_FACTOR is not set.}"
MAX_K="${TLU_KINEMATICS_MAX_K:?Environment variable TLU_KINEMATICS_MAX_K is not set.}"
FK_MODE="${TLU_FK_INPUT_MODE:?Environment variable TLU_FK_INPUT_MODE is not set.}"
# Allow static_dq_labels to be empty if mode is actual, but pull from environment
STATIC_LABELS="${TLU_FK_STATIC_DQ_LABELS:-}"

# 3. Execute pipeline
run_tlu_pipeline "Forward Kinematics (FK) Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._003_1_1_filter_fk_simulation" "result.003_1_1_filter_fk.analysis.csv" \
    --fk_input_mode="${FK_MODE}" \
    --static_dq_labels="${STATIC_LABELS}" \
    --gamma="${GAMMA}" \
    --max_k="${MAX_K}" \
    --node_map="${TLU_NODE_MAP}"


# --fk_input_mode="actual" --gamma=0.85 --max_k=6 --node_map="${TLU_NODE_MAP}"

# --fk_input_mode="static" --static_dq_labels="ACC_Sales_Revenue:100" --gamma=0.85 --max_k=5 --node_map="${TLU_NODE_MAP}"

# --fk_input_mode="static" --static_dq_labels="三条烏丸:100" --gamma=0.85 --max_k=5 --node_map="${TLU_NODE_MAP}"
