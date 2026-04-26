#!/bin/bash
# ==========================================
# 005_1_1_run_resonant_frequency.sh
# TLU System: Autocorrelation & Resonant Frequency Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 2. Parameter retrieval and Fail-Fast verification
MAX_LAG="${TLU_OBSERVATION_WINDOW_MONTHS:?Environment variable TLU_OBSERVATION_WINDOW_MONTHS is not set.}"

# 3. Execute pipeline
# We don't actually need src/tgt column projection here as we sum it up inside, but run_tlu_pipeline expects it.
run_tlu_pipeline "Autocorrelation & Resonant Frequency Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._005_1_1_filter_resonant_frequency" "result.005_1_1_filter_resonant_frequency.analysis.csv" \
    --max_tau="${MAX_LAG}"
