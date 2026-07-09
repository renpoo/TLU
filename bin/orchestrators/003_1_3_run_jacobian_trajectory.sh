#!/bin/bash
source "$(dirname "$0")/_tlu_env.sh"

# 2. Parameter retrieval and Fail-Fast verification
GAMMA="${TLU_DAMPING_FACTOR:?Environment variable TLU_DAMPING_FACTOR is not set.}"
MAX_K="${TLU_KINEMATICS_MAX_K:?Environment variable TLU_KINEMATICS_MAX_K is not set.}"

# 3. Execute pipeline for 1st, 2nd, and 3rd order Jacobian trajectories
run_tlu_pipeline "Jacobian Trajectory Filter (1st-Order)" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._003_1_3_filter_jacobian_trajectory" "result.003_1_3_jacobian_1st.analysis.csv" \
    --target_labels="" \
    --gamma="${GAMMA}" \
    --max_k="${MAX_K}" \
    --order=1 \
    --node_map="${TLU_NODE_MAP}"

run_tlu_pipeline "Jacobian Trajectory Filter (2nd-Order)" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._003_1_3_filter_jacobian_trajectory" "result.003_1_3_jacobian_2nd.analysis.csv" \
    --target_labels="" \
    --gamma="${GAMMA}" \
    --max_k="${MAX_K}" \
    --order=2 \
    --node_map="${TLU_NODE_MAP}"

run_tlu_pipeline "Jacobian Trajectory Filter (3rd-Order)" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._003_1_3_filter_jacobian_trajectory" "result.003_1_3_jacobian_3rd.analysis.csv" \
    --target_labels="" \
    --gamma="${GAMMA}" \
    --max_k="${MAX_K}" \
    --order=3 \
    --node_map="${TLU_NODE_MAP}"

