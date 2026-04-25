#!/bin/bash
# ==========================================
# _tlu_env.sh
# TLU System: Environment Abstraction Layer
# ==========================================
set -euo pipefail

# --- Global CLI Argument Scanning ---
for arg in "$@"; do
    if [ "$arg" == "--interactive" ]; then
        export TLU_INTERACTIVE="true"
    fi
done

# --- 0. Project Root & Python Path Resolution ---
# Determine project root by backtracking from _tlu_env.sh absolute path (bin/orchestrators/)
export TLU_PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# Ensure execution from the project root regardless of where the script is called from
cd "${TLU_PROJECT_ROOT}"

# Export PYTHONPATH so Python can recognize 'src' folder as a module
export PYTHONPATH="${TLU_PROJECT_ROOT}:${PYTHONPATH:-}"

# --- 1. Docker Commands ---
# export TLU_PY="python3"
export TLU_PY="docker compose exec -T tlu-engine python3"

# export TLU_AWK="awk"
export TLU_AWK="docker compose exec -T tlu-engine awk"

# --- 2. Common Paths (Dynamic Validation) ---
export TLU_VIZ_DIR="src/visualizations"

if [ -n "${TARGET_ENV:-}" ]; then
    export TLU_OUT_DIR="${TARGET_ENV}/output_data"
    export TLU_TIME_MAP="${TARGET_ENV}/ephemeral/_time_map.csv"
    export TLU_NODE_MAP="${TARGET_ENV}/ephemeral/_node_map.csv"
    export TLU_SYS_PARAMS="${TARGET_ENV}/config/_sys_params.csv"
    export TLU_TMP_COO="${TARGET_ENV}/ephemeral/_coo_stream.csv"
    
    # In Target Mode, plots explicitly render inside the archive folder
    export TLU_PLOT_DIR="${TARGET_ENV}/output_plots"
else
    # Default Paths
    export TLU_OUT_DIR="workspace/output_data"
    export TLU_TIME_MAP="workspace/ephemeral/_time_map.csv"
    export TLU_NODE_MAP="workspace/ephemeral/_node_map.csv"
    export TLU_SYS_PARAMS="workspace/config/_sys_params.csv"
    export TLU_TMP_COO="workspace/ephemeral/_coo_stream.csv"
    export TLU_PLOT_DIR="workspace/output_plots"
fi

# Ensure tracking plot environments exist safely without crashing executions
mkdir -p "${TLU_PLOT_DIR}"

# ==========================================
# 2.5 Dynamic Hyperparameter Injection
# ==========================================
# Expand constants defined in CSV as system-wide environment variables ($TLU_*)
if [ -f "${TLU_SYS_PARAMS}" ]; then
    # echo "[INFO] Loading system parameters from ${TLU_SYS_PARAMS}..."
    while IFS=, read -r key value || [ -n "$key" ]; do
        # Skip empty lines and comments
        [[ -z "$key" || "$key" == \#* ]] && continue
        
        # Remove spaces and carriage returns to normalize
        clean_key=$(echo "$key" | xargs)
        clean_value=$(echo "$value" | tr -d '\r' | xargs)
        
        # Example: damping_factor -> TLU_DAMPING_FACTOR
        # macOS default Bash (v3.2) does not support ${var^^}, so use tr to uppercase.
        upper_key=$(echo "$clean_key" | tr '[:lower:]' '[:upper:]')
        export "TLU_${upper_key}=${clean_value}"
    done < "${TLU_SYS_PARAMS}"
else
    echo "[WARN] Parameter file ${TLU_SYS_PARAMS} not found. Subsequent runs may fail if variables are missing."
fi

# Dynamically construct the absolute path to the input CSV based on the active target environment
export TLU_INPUT_CSV="${TARGET_ENV:-workspace}/${TLU_INPUT_CSV:?Environment variable TLU_INPUT_CSV is missing. Please define input_csv in _sys_params.csv}"

# --- 3. Unified Pipeline Runner ---
# Usage: run_tlu_pipeline <description> <src_col> <tgt_col> <execution_module> <output_filename> [extra_args...]
run_tlu_pipeline() {
    local filter_desc="$1"
    local proj_src="$2"
    local proj_tgt="$3"
    local filter_module="$4"
    local out_filename="$5"
    shift 5
    local extra_args=("$@")

    echo "Running ${filter_desc}..."

    # Step 1: Projection (Anonymization of events and dictionary generation)
    # Ensure _node_map.csv is fully written before proceeding
    cat "${TLU_INPUT_CSV}" \
    | $TLU_PY -m src.filters._0_2_projector_to_coo \
        --col_time="${TLU_COL_TRANS_DATE:?}" --col_src="${proj_src}" --col_tgt="${proj_tgt}" --col_val="${TLU_COL_AMOUNT:?}" \
    > "${TLU_TMP_COO}"

    # Step 2: Filtering (Mathematical Analysis)
    # Safely execute by reading the completed latest _node_map.csv
    cat "${TLU_TMP_COO}" \
    | $TLU_PY -m "${filter_module}" "${extra_args[@]:-}" \
    > "${TLU_OUT_DIR}/${out_filename}"

    echo "${filter_desc} completed."
    echo ""
}

# --- 4. Unified Visualization Runner ---
# Usage: run_tlu_visualization <step/description> <script_name> <output_filename> <input_filename> [extra_args...]
run_tlu_visualization() {
    local step_desc="$1"
    local script="$2"
    local out_file="$3"
    local in_file="$4"
    shift 4
    local extra_args=("$@")

    if [ "${TLU_INTERACTIVE:-false}" == "true" ]; then
        extra_args+=("--interactive")
    fi

    # Get THEME from environment variables (fallback to dark if unset)
    local theme="${TLU_THEME:-dark}"
    
    # Remove extension from script name and convert to Python module path notation
    local module_path="src.visualizations.${script%.py}"

    echo "  -> Generating [${theme}]: ${step_desc}..."
    
    # Safely branch based on presence of extra arguments (completely prevents empty string args)
    # Unify all calls to -m (module execution) to guarantee path resolution from current directory
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
