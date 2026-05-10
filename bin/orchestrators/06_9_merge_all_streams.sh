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
OUTPUT_FILE="${TARGET_ENV:-workspace}/input_stream/Unified_COO_Stream.csv"

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

echo " -> Merging streams into a single unified COO pipeline..."

# We use Python to concatenate and sort the streams chronologically by t_idx.
# Since t_idx is ISO-8601 formatted (e.g. YYYY-MM, YYYY-Www), string sorting works perfectly.
# If the streams are not sorted, 000_1_1 will time-travel backward.
$TLU_PY -c "
import pandas as pd
import sys

streams = sys.argv[1:-1]
output_file = sys.argv[-1]

dfs = []
for f in streams:
    try:
        dfs.append(pd.read_csv(f))
    except Exception as e:
        print(f'Error reading {f}: {e}')

if dfs:
    combined = pd.concat(dfs, ignore_index=True)
    combined = combined.sort_values(['t_idx', 'src_idx', 'tgt_idx'])
    combined.to_csv(output_file, index=False)
" "${STREAMS_TO_MERGE[@]}" "${OUTPUT_FILE}"

echo "✅ Success! Output saved to: ${OUTPUT_FILE}"
echo "Ready for Phase Space generation (000_1_1_filter_dynamics_state.py) and subsequent TLU/WMU bifurcation."
