#!/bin/bash
# ==========================================
# 002_2_1_run_forensics.sh
# TLU System: Forensics & Anomaly Detection Orchestrator
# ==========================================
# 1. Load common environment (_sys_params.csv is expanded into environment variables here)
source "$(dirname "$0")/_tlu_env.sh"

# 2. Parameter retrieval and Fail-Fast verification
# If a setting is missing in the CSV (envvars), output a clear error and halt immediately.
BASELINE_WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?Environment variable TLU_OBSERVATION_WINDOW_MONTHS is not set. Please check _sys_params.csv.}"
Z_SCORE_THRESH="${TLU_ANOMALY_Z_SCORE_THRESHOLD:?Environment variable TLU_ANOMALY_Z_SCORE_THRESHOLD is not set.}"

# Note: LEAK_TOLERANCE and KL_DRIFT_THRESH were not in the initial _sys_params.csv.
# Assumes they are added to the CSV, forcing retrieval.
LEAK_TOLERANCE="${TLU_LEAK_TOLERANCE:?Environment variable TLU_LEAK_TOLERANCE is not set. Please add leak_tolerance to _sys_params.csv.}"
KL_DRIFT_THRESH="${TLU_KL_DRIFT_THRESH:?Environment variable TLU_KL_DRIFT_THRESH is not set. Please add kl_drift_thresh to _sys_params.csv.}"

# 3. Injection into Python core (Dependency Injection)
run_tlu_pipeline "Forensics Filter" \
    "Src" "Tgt" \
    "src.filters._002_2_1_filter_macro_forensics" "result.002_2_1_filter_macro_forensics.analysis.csv" \
    --baseline_window="${BASELINE_WINDOW}" \
    --leak_tolerance="${LEAK_TOLERANCE}" \
    --kl_drift_thresh="${KL_DRIFT_THRESH}" \
    --z_score_thresh="${Z_SCORE_THRESH}" \
    --node_map="${TLU_NODE_MAP}"
