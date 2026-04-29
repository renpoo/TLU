#!/bin/bash
# ==========================================
# batch_meta_analysis.sh
# TLU System: Cross-Environment Meta-Analysis Orchestrator
# ==========================================
set -euo pipefail

# Parse command line arguments
ENVS=""
OUT_DIR="workspace/meta_analysis"
THEME="dark"

while [[ $# -gt 0 ]]; do
  case $1 in
    --envs)
      ENVS="$2"
      shift 2
      ;;
    --out)
      OUT_DIR="$2"
      shift 2
      ;;
    --theme)
      THEME="$2"
      shift 2
      ;;
    *)
      echo "Unknown parameter passed: $1"
      exit 1
      ;;
  esac
done

if [ -z "$ENVS" ]; then
    echo "Usage: bash bin/batch_meta_analysis.sh --envs \"path/to/envs/*\" [--out workspace/meta_analysis]"
    exit 1
fi

source "$(dirname "$0")/orchestrators/_tlu_env.sh"

echo "🚀 Starting TLU Cross-Environment Meta-Analysis..."
echo "📂 Target Environments: ${ENVS}"
echo "📂 Output Directory: ${OUT_DIR}"
echo "--------------------------------------------------"

# Resolve wildcards into a space-separated list
# We use eval to safely expand the wildcard string passed by the user
RESOLVED_ENVS=$(eval echo $ENVS)

# Ensure output directory exists locally so we don't get permission errors
mkdir -p "${OUT_DIR}"

${TLU_PY} src/visualizations/vis_meta_cross_environment.py \
    --envs ${RESOLVED_ENVS} \
    --out "${OUT_DIR}" \
    --theme "${THEME}"

echo "--------------------------------------------------"
echo "✅ Meta-Analysis completed. Check ${OUT_DIR} for results."
