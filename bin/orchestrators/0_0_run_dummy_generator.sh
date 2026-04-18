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
OUTPUT_FILE="${TLU_PROJECT_ROOT}/workspace/input_stream/Dummy_Journal_Stream.csv"

echo "=================================================="
echo "TLU Phase 0: Dummy Journal Generator"
echo "=================================================="
echo "Mode: Real Business (Scale-free, Causal Lags, Pink Noise)"
echo "Anomalies: Enabled (Z-Spikes, Drifts, Leaks will be injected)"
echo "Output: ${OUTPUT_FILE}"
echo "Running..."

# 3. Parameter retrieval and Fail-Fast verification
MONTHS="${TLU_DUMMY_DURATION_MONTHS:?Environment variable TLU_DUMMY_DURATION_MONTHS is not set.}"
SEED="${TLU_DUMMY_RANDOM_SEED:?Environment variable TLU_DUMMY_RANDOM_SEED is not set.}"

# 4. Execute generator script
# Executes transparently in the Docker container or local environment via ${TLU_PY}.
# Note: Assumes _0_0_generate_dummy_journal.py is in src/filters/.
# Adjust module path if placed elsewhere (e.g. src.generators).

${TLU_PY} -m src.filters._0_0_generate_dummy_journal \
    --months "${MONTHS}" \
    --seed "${SEED}" \
    > "${OUTPUT_FILE}"
    # --sales-leak 0.01 \
    # --purchase-leak 0.005 \
    # > "${OUTPUT_FILE}"

echo "Completed. Dummy stream has been successfully generated."
echo "=================================================="
