#!/bin/bash
# ==========================================
# 00_0_run_preprocess_journal.sh
# TLU System: Preprocessing Orchestrator (Phase 0)
# Action: Thin Adapter Pipeline for Accounting Journals
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# Default interval is month (or defined in sys_params)
INTERVAL=${1:-${TLU_AGGREGATION_INTERVAL:-month}}
COL_TIME=${2:-${TLU_COL_TRANS_DATE:-Trans_Date}}

# The dummy generator outputs raw journals here
INPUT_FILE="${TLU_PROJECT_ROOT}/${TARGET_ENV:-workspace}/input_stream/Dummy_Journal_Stream.csv"
# The output is the Hodgepodge COO stream ready for Phase 1
OUTPUT_FILE="${TLU_PROJECT_ROOT}/${TARGET_ENV:-workspace}/input_stream/Aggregated_Journal_Stream.csv"

echo "=================================================="
echo "TLU Phase 0: Preprocessing Journal Data (A1 | A2)"
echo "=================================================="
echo "Input: ${INPUT_FILE}"
echo "Output: ${OUTPUT_FILE}"
echo "Interval: ${INTERVAL}"
echo "Time Column: ${COL_TIME}"
echo "Running thin adapter pipeline..."

# Ensure output directory exists
mkdir -p "$(dirname "${OUTPUT_FILE}")"

# Unix Pipeline: Parse -> Aggregate
cat "${INPUT_FILE}" \
  | $TLU_PY src/filters/00_1_parse_journal.py --col_time "${COL_TIME}" \
  | $TLU_PY src/filters/00_2_aggregate_journal.py --interval "${INTERVAL}" \
  > "${OUTPUT_FILE}"

echo "Completed. Hodgepodge COO stream generated successfully."
echo "=================================================="
