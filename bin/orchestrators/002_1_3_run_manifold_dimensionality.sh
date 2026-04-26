#!/bin/bash
# ==========================================
# 002_1_3_run_manifold_dimensionality.sh
# TLU System: Manifold Dimensionality Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

run_tlu_pipeline "Manifold Dimensionality Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._002_1_3_filter_manifold_dimensionality" "result.002_1_3_filter_manifold_dimensionality.analysis.csv" \
    --top_k=5 \
    --node_map="${TLU_NODE_MAP}"
