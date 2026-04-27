#!/bin/bash
# ==========================================
# 0_0_run_dummy_generator.sh
# TLU System: Dummy Journal Generator Launcher
# Phase 0: The Source Stream
# ==========================================

# 1. Load environment variables (_tlu_env.sh)
source "$(dirname "$0")/_tlu_env.sh"

# 2. Define output destination
# Output to the directory that becomes the input for subsequent pipelines using TLU_PROJECT_ROOT.
ENV_DIR="${TARGET_ENV:-workspace}"
OUTPUT_FILE="${TLU_PROJECT_ROOT}/${ENV_DIR}/input_stream/Dummy_Journal_Stream.csv"

echo "=================================================="
echo "TLU Phase 0: Dummy Journal Generator"
echo "=================================================="
echo "Mode: Real Business (Scale-free, Causal Lags, Pink Noise)"
echo "Anomalies: Enabled (Z-Spikes, Drifts, Leaks will be injected)"
echo "Output: ${OUTPUT_FILE}"
echo "Running..."

# 3. Parameter retrieval (Decoupled from _sys_params.csv)
# Set via environment variables in generate_all_samples.sh, with safe defaults.
MONTHS="${DUMMY_DURATION_MONTHS:-12}"
SEED="${DUMMY_RANDOM_SEED:-42}"

# 4. Execute generator script
# Executes transparently in the Docker container or local environment via ${TLU_PY}.
# Note: Assumes _0_0_generate_dummy_journal.py is in src/filters/.
# Adjust module path if placed elsewhere (e.g. src.generators).

${TLU_PY} -m src.filters._0_0_generate_dummy_journal \
    --months "${MONTHS}" \
    --seed "${SEED}" \
    --sales-leak-prob "${DUMMY_SALES_LEAK_PROB:-0.0}" \
    --purchase-leak-prob "${DUMMY_PURCHASE_LEAK_PROB:-0.0}" \
    --wash-trade-prob "${DUMMY_WASH_TRADE_PROB:-0.0}" \
    --unbalanced-mistake-prob "${DUMMY_UNBALANCED_PROB:-0.0}" \
    > "${OUTPUT_FILE}"
    # > "${OUTPUT_FILE}"

echo "Completed. Dummy stream has been successfully generated."
echo "=================================================="
