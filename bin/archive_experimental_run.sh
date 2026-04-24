#!/bin/bash
# ==========================================
# archive_experimental_run.sh
# TLU System: Experimental Run Archiver
# ==========================================
set -euo pipefail

# 1. Ensure we execute from the root directory
export TLU_PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${TLU_PROJECT_ROOT}"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
ARCHIVE_BASE="archives/run_${TIMESTAMP}"
ARCHIVE_DIR="${ARCHIVE_BASE}/workspace"

echo "=========================================="
echo "📦 Archiving Experimental Run: ${TIMESTAMP}"
echo "=========================================="

# 2. Create the archive directory structure structurally mapping defaults
mkdir -p "${ARCHIVE_DIR}"

# 3. Recursively copy all math and parameter components, EXCLUDING output_plots
if [ -d "workspace/config" ]; then
    cp -R "workspace/config" "${ARCHIVE_DIR}/config"
    echo "  -> Archived [config]"
fi

if [ -d "workspace/input_stream" ]; then
    cp -R "workspace/input_stream" "${ARCHIVE_DIR}/input_stream"
    echo "  -> Archived [input_stream]"
fi

if [ -d "workspace/ephemeral" ]; then
    cp -R "workspace/ephemeral" "${ARCHIVE_DIR}/ephemeral"
    echo "  -> Archived [ephemeral]"
fi

if [ -d "workspace/output_data" ]; then
    cp -R "workspace/output_data" "${ARCHIVE_DIR}/output_data"
    echo "  -> Archived [output_data]"
fi

echo "=========================================="
echo "✅ Archive mapping successfully populated at: ${ARCHIVE_BASE}"
echo "Note: The output_plots directory was intentionally excluded to preserve disk space."
echo "To regenerate visualizations for this archive later, run:"
echo "bash bin/batch_visualize_graphs.sh dark --target_env ${ARCHIVE_DIR}"
echo "=========================================="
