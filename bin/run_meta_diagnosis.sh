#!/bin/bash
# ==========================================
# run_meta_diagnosis.sh
# TLU System: Automated Meta-Diagnosis Engine
# ==========================================
set -euo pipefail

# Allow passing TARGET_ENV as an argument, otherwise fallback to the environment variable
export TARGET_ENV="${1:-${TARGET_ENV:-workspace}}"

# Source environment
source "$(dirname "$0")/orchestrators/_tlu_env.sh"

echo "--------------------------------------------------"
echo "[EXECUTING] _99_meta_diagnosis.py"
echo "Running Automated Meta-Diagnosis Engine for: ${TARGET_ENV}..."

# Execute the diagnostic engine inside the container
${TLU_PY} src/filters/_99_meta_diagnosis.py

echo "--------------------------------------------------"
