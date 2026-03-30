#!/bin/bash
# ==========================================
# 0_0_run_dummy_generator.sh
# TLU System: Dummy Journal Generator Launcher
# Phase 0: The Source Stream
# ==========================================

# 1. 環境変数の読み込み（_tlu_env.sh の呼び出し）
source "$(dirname "$0")/_tlu_env.sh"

# 2. 出力先の定義
# 既存の環境変数 TLU_PROJECT_ROOT を利用し、後続パイプラインの入力となるディレクトリへ出力します。
OUTPUT_FILE="${TLU_PROJECT_ROOT}/workspace/input_stream/Dummy_Journal_Stream.csv"

echo "=================================================="
echo "TLU Phase 0: Dummy Journal Generator"
echo "=================================================="
echo "Mode: Real Business (Scale-free, Causal Lags, Pink Noise)"
echo "Anomalies: Enabled (Z-Spikes, Drifts, Leaks will be injected)"
echo "Output: ${OUTPUT_FILE}"
echo "Running..."

# 3. 生成スクリプトの実行
# ${TLU_PY} により、Dockerコンテナ内またはローカル環境で透過的に実行されます。
# ※ 00_generate_dummy_journal.py が src/filters/ ディレクトリに配置されていると仮定したモジュール指定です。
#    配置場所（src.generators など）に合わせて適宜変更してください。

${TLU_PY} -m src.filters._0_0_generate_dummy_journal \
    --months 36 \
    --seed 42 \
    --sales-leak true \
    --purchase-leak true \
    > "${OUTPUT_FILE}"

echo "Completed. Dummy stream has been successfully generated."
echo "=================================================="
