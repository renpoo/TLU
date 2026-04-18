#!/bin/bash
# ==========================================
# 002_2_1_run_forensics.sh
# TLU System: Forensics & Anomaly Detection Orchestrator
# ==========================================
# 1. 共通環境の読み込み（ここで _sys_params.csv の内容が環境変数として展開される）
source "$(dirname "$0")/_tlu_env.sh"

# 2. パラメータの取得と Fail-Fast 検証
# 設定値がCSV(環境変数)に存在しない場合、明確なエラーメッセージを出力して即座に処理を停止する
BASELINE_WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?環境変数 TLU_OBSERVATION_WINDOW_MONTHS が設定されていません。_sys_params.csv を確認してください。}"
Z_SCORE_THRESH="${TLU_ANOMALY_Z_SCORE_THRESHOLD:?環境変数 TLU_ANOMALY_Z_SCORE_THRESHOLD が設定されていません。}"

# 注意: LEAK_TOLERANCE と KL_DRIFT_THRESH は初期の _sys_params.csv には存在しませんでした。
# CSVに追加されることを前提に、取得を強制します。
LEAK_TOLERANCE="${TLU_LEAK_TOLERANCE:?環境変数 TLU_LEAK_TOLERANCE が設定されていません。_sys_params.csv に leak_tolerance を追加してください。}"
KL_DRIFT_THRESH="${TLU_KL_DRIFT_THRESH:?環境変数 TLU_KL_DRIFT_THRESH が設定されていません。_sys_params.csv に kl_drift_thresh を追加してください。}"

# 3. Pythonコアへの注入 (Dependency Injection)
run_tlu_pipeline "Forensics Filter" \
    "Src" "Tgt" \
    "src.filters._002_2_1_filter_macro_forensics" "result.002_2_1_filter_macro_forensics.analysis.csv" \
    --baseline_window="${BASELINE_WINDOW}" \
    --leak_tolerance="${LEAK_TOLERANCE}" \
    --kl_drift_thresh="${KL_DRIFT_THRESH}" \
    --z_score_thresh="${Z_SCORE_THRESH}" \
    --node_map="${TLU_NODE_MAP}"
