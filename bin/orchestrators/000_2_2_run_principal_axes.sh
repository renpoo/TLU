#!/bin/bash
# ==========================================
# 000_2_2_run_principal_axes.sh
# TLU System: Principal Axes (PCA) Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

HISTORY_WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?Environment variable TLU_OBSERVATION_WINDOW_MONTHS is not set.}"

run_tlu_pipeline "Principal Axes Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._000_2_2_filter_principal_axes" "result.000_2_2_filter_principal_axes.analysis.csv" \
    --history_window="${HISTORY_WINDOW}" \
    --top_k=3 \
    --node_map="${TLU_NODE_MAP}"
