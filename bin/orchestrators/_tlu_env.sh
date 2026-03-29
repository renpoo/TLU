#!/bin/bash
# ==========================================
# _tlu_env.sh
# TLU System: Environment Abstraction Layer
# ==========================================
set -euo pipefail

# --- 0. Project Root & Python Path Resolution ---
# _tlu_env.sh の絶対位置 (bin/orchestrators/) から逆算してプロジェクトルートを特定
export TLU_PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# どこからスクリプトが呼ばれても、必ずプロジェクトルートに移動して実行する
cd "${TLU_PROJECT_ROOT}"

# Pythonが 'src' フォルダをモジュールとして認識できるように PYTHONPATH をエクスポート
export PYTHONPATH="${TLU_PROJECT_ROOT}:${PYTHONPATH:-}"

# --- 1. Docker Commands ---
export TLU_PY="python3"
# export TLU_PY="docker compose exec -T tlu-engine python3"
export TLU_AWK="awk"
# export TLU_AWK="docker compose exec -T tlu-engine awk"

# --- 2. Common Paths ---
export TLU_INPUT_CSV="workspace/input_stream/Dummy_Journal_Stream_Amount.Monthly.csv"
# export TLU_INPUT_CSV="workspace/input_stream/General-Ledger-Amount.Src.Tgt.Monthly.csv"
export TLU_OUT_DIR="workspace/output_data"
export TLU_TIME_MAP="workspace/ephemeral/_time_map.csv"
export TLU_NODE_MAP="workspace/ephemeral/_node_map.csv"
export TLU_DOMAIN_TAGS="workspace/config/_domain_tags.csv"
export TLU_SYS_PARAMS="workspace/config/_sys_params.csv"
export TLU_TMP_COO="workspace/ephemeral/_coo_stream.csv"
export TLU_PLOT_DIR="workspace/output_plots"
export TLU_VIZ_DIR="src/visualizations"

# --- 3. Unified Pipeline Runner ---
# 使い方: run_tlu_pipeline <説明> <始点カラム> <終点カラム> <実行モジュール> <出力ファイル名> [追加引数...]
run_tlu_pipeline() {
    local filter_desc="$1"
    local proj_src="$2"
    local proj_tgt="$3"
    local filter_module="$4"
    local out_filename="$5"
    shift 5
    local extra_args=("$@")

    echo "Running ${filter_desc}..."

    # Step 1: プロジェクション（事象の無名化と辞書の生成）
    # ※ ここで確実に _node_map.csv が最後まで書き切られるのを待つ
    cat "${TLU_INPUT_CSV}" \
    | $TLU_PY -m src.filters._0_2_projector_to_coo \
        --col_time="Trans_Date" --col_src="${proj_src}" --col_tgt="${proj_tgt}" --col_val="Amount" \
    > "${TLU_TMP_COO}"

    # Step 2: フィルタリング（数理解析）
    # ※ 完成した最新の _node_map.csv を読み込んで安全に実行される
    cat "${TLU_TMP_COO}" \
    | $TLU_PY -m "${filter_module}" "${extra_args[@]:-}" \
    > "${TLU_OUT_DIR}/${out_filename}"

    echo "${filter_desc} completed."
    echo ""
}

# --- 4. Unified Visualization Runner ---
# 使い方: run_tlu_visualization <ステップ/説明> <スクリプト名> <出力ファイル名> <入力ファイル名> [追加引数...]
run_tlu_visualization() {
    local step_desc="$1"
    local script="$2"
    local out_file="$3"
    local in_file="$4"
    shift 4
    local extra_args=("$@")

    # THEMEは環境変数から取得（未設定ならdark）
    local theme="${TLU_THEME:-dark}"
    
    # スクリプト名から拡張子を取り除き、Pythonのモジュールパス記法に変換
    local module_path="src.visualizations.${script%.py}"

    echo "  -> Generating [${theme}]: ${step_desc}..."
    
    # 追加引数の有無で安全に分岐させる（空文字引数の混入を完全に防止）
    # 呼び出しをすべて -m (モジュール実行) に統一し、カレントディレクトリからのパス解決を保証する
    if [ ${#extra_args[@]} -gt 0 ]; then
        $TLU_PY -m "${module_path}" \
            --theme "${theme}" \
            --out_dir "${TLU_PLOT_DIR}" \
            --filename "${out_file}" \
            --node_map "${TLU_NODE_MAP}" \
            --time_map "${TLU_TIME_MAP}" \
            "${extra_args[@]}" \
            < "${TLU_OUT_DIR}/${in_file}"
    else
        $TLU_PY -m "${module_path}" \
            --theme "${theme}" \
            --out_dir "${TLU_PLOT_DIR}" \
            --filename "${out_file}" \
            --node_map "${TLU_NODE_MAP}" \
            --time_map "${TLU_TIME_MAP}" \
            < "${TLU_OUT_DIR}/${in_file}"
    fi
}
