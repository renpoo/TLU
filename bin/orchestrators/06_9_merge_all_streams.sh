#!/bin/bash
# ==========================================
# 06_9_merge_all_streams.sh
# TLU System: Unified Stream Combiner for WMU
# ==========================================
# Description:
# Concatenates internal accounting streams and external market streams into a single
# universal COO pipeline, then converts it into a Time-Node signal matrix format
# required by the Wave Mechanics Unit (WMU).
# Designed for end-users (business practitioners) who shouldn't run raw cat commands.
# ==========================================
set -euo pipefail

# Ensure we run from project root
cd "$(dirname "$0")/../.."
source "bin/orchestrators/_tlu_env.sh"

JOURNAL_STREAM="${TARGET_ENV:-workspace}/input_stream/Aggregated_Journal_Stream.csv"
MARKET_STREAM="${TARGET_ENV:-workspace}/input_stream/Aggregated_Market_Stream.csv"
OUTPUT_FILE="${TARGET_ENV:-workspace}/input_stream/WMU_Time_Node_Stream.csv"

echo "=================================================="
echo "TLU Phase 06: Merging Global Streams (Internal + External)"
echo "=================================================="

# Check if streams exist
STREAMS_TO_MERGE=()

if [ -f "${JOURNAL_STREAM}" ]; then
    echo " -> Found Journal Stream: ${JOURNAL_STREAM}"
    STREAMS_TO_MERGE+=("${JOURNAL_STREAM}")
fi

if [ -f "${MARKET_STREAM}" ]; then
    echo " -> Found Market Stream: ${MARKET_STREAM}"
    STREAMS_TO_MERGE+=("${MARKET_STREAM}")
fi

if [ ${#STREAMS_TO_MERGE[@]} -eq 0 ]; then
    echo "[ERROR] No data streams found to merge. Please run 00_0_run_preprocess_journal.sh or 06_0_run_preprocess_market.sh first."
    exit 1
fi

echo " -> Merging streams and translating to Time-Node format..."

# We use awk to skip the CSV header for all files except the first one,
# then pipe the concatenated COO stream directly into the Time-Node translator.
awk 'FNR==1 && NR!=1{next;}{print}' "${STREAMS_TO_MERGE[@]}" \
  | $TLU_PY src/filters/06_4_coo_to_time_node_stream.py \
  > "${OUTPUT_FILE}"

echo "✅ Success! Output saved to: ${OUTPUT_FILE}"
echo "Ready for Wave Mechanics Unit (WMU) analysis."
