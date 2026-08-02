#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

echo "=== Packaging TLU Core Engine with PyInstaller ==="

mkdir -p "${PROJECT_ROOT}/scratch/pyinstaller_build"
cd "${PROJECT_ROOT}"

# Check if pyinstaller is available
if ! command -v pyinstaller &> /dev/null; then
    echo "[INFO] Installing pyinstaller..."
    python3 -m pip install --user pyinstaller || pip3 install pyinstaller
fi

# Run PyInstaller using python3 module or executable
python3 -m PyInstaller --onefile \
    --name "tlu-engine-aarch64-apple-darwin" \
    --distpath "${PROJECT_ROOT}/scratch/dist" \
    --workpath "${PROJECT_ROOT}/scratch/build" \
    --specpath "${PROJECT_ROOT}/scratch/spec" \
    src/utils/standalone_engine.py

# Target directory in TLU-App
TARGET_BIN_DIR="/Users/renpoo/Documents/GitHub/TLU-App/src-tauri/bin"
mkdir -p "${TARGET_BIN_DIR}"

cp "${PROJECT_ROOT}/scratch/dist/tlu-engine-aarch64-apple-darwin" "${TARGET_BIN_DIR}/"
chmod +x "${TARGET_BIN_DIR}/tlu-engine-aarch64-apple-darwin"

echo "✅ Frozen Sidecar binary successfully created at: ${TARGET_BIN_DIR}/tlu-engine-aarch64-apple-darwin"
