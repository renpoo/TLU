#!/usr/bin/env python3
# src/filters/cli_parser.py
import argparse
import csv
import sys
from typing import Dict

def load_sys_params(filepath: str) -> Dict[str, float]:
    """!
    @brief Load system context parameters into a mapped dictionary.
    @details Recursively aggregates configuration baseline bounds eliminating missing variable bugs.

    @param filepath Absolute or relative configurations structure path.

    @return Extracted parameter dictionary instance.

    @pre
        - Struct is generally expected to exist (although logic allows default fallbacks).
    @post
        - Bypasses header rows safely while coercing implicit type definitions to float bounds.
    @invariant
        - Degrades gracefully emitting explicit [WARN] traces returning cleanly initialized dictionaries natively.
    """
    params = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            first_row = next(reader, None)
            if first_row and len(first_row) >= 2:
                key = first_row[0].strip()
                val = first_row[1].strip()
                try:
                    params[key] = float(val)
                except ValueError:
                    params[key] = val
            
            for row in reader:
                if len(row) >= 2:
                    key = row[0].strip()
                    val = row[1].strip()
                    try:
                        params[key] = float(val)
                    except ValueError:
                        params[key] = val
    except FileNotFoundError:
        print(f"[WARN] {filepath} not found. Using defaults.", file=sys.stderr)
        
    # Inject dynamically tuned parameters if auto-calibration was run
    import os, json
    env_dir = os.environ.get("TARGET_ENV", "workspace")
    tuned_params_path = os.path.join(env_dir, "ephemeral", "_tuned_params.json")
    if os.path.exists(tuned_params_path):
        try:
            with open(tuned_params_path, 'r') as f:
                tuned = json.load(f)
                for k, v in tuned.items():
                    params[k] = v
        except Exception:
            pass
            
    return params

def get_base_parser(description: str) -> argparse.ArgumentParser:
    """!
    @brief Generate a base parser commonly configured across all sequential filters.
    @details Asserts expected boundaries preventing missing explicit arguments structurally.

    @param description Meta string characterizing the execution target domain.

    @return Core ArgumentParser populated identically with namespace foundations.

    @pre
        - Standard execution depends implicitly on `--time_map` and `--node_map`.
    @post
        - Defines configuration variables targeting standard workspace ephemeral data outputs.
    """
    import os
    env_dir = os.environ.get("TARGET_ENV", "workspace")
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--time_map", type=str, default=f"{env_dir}/ephemeral/_time_map.csv")
    parser.add_argument("--node_map", type=str, default=f"{env_dir}/ephemeral/_node_map.csv")
    parser.add_argument("--sys_params", type=str, default=f"{env_dir}/config/_sys_params.csv")
    
    # Load thresholds from sys_params and inject them as parser arguments
    sys_params_path = os.environ.get("TLU_SYS_PARAMS", f"{env_dir}/config/_sys_params.csv")
    sys_params = load_sys_params(sys_params_path)
    parser.add_argument("--thresh_z_score", type=float, default=sys_params.get("thresh_z_score", 3.0))
    parser.add_argument("--thresh_spectral_radius", type=float, default=sys_params.get("thresh_spectral_radius", 0.95))
    parser.add_argument("--thresh_fractal_lower", type=float, default=sys_params.get("thresh_fractal_lower", 0.5))
    parser.add_argument("--thresh_fractal_upper", type=float, default=sys_params.get("thresh_fractal_upper", 1.5))
    parser.add_argument("--thresh_manifold_svd", type=float, default=sys_params.get("thresh_manifold_svd", 1e-10))
    parser.add_argument("--target_phase_frequency", type=float, default=sys_params.get("target_phase_frequency", 0.25))

    return parser

def parse_projector_args(args_list: list[str]) -> dict:
    """!
    @brief Parse CLI arguments explicitly overriding extraction projection limits.
    @details Generates mapped representations natively executing early stream phase parameters.

    @param args_list The system argv parameter list mapping source targets.

    @return Parsed parameter mapping configurations targeting dynamic variables.

    @pre
        - Target list dynamically configured.
    @post
        - Implicitly coerces strictly integer representations scaling strings naturally.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--col_time", type=str, default="")
    parser.add_argument("--col_src", type=str, default="")
    parser.add_argument("--col_tgt", type=str, default="")
    parser.add_argument("--col_val", type=str, default="")
    parser.add_argument("--col_multiplier", type=str, default="", help="Optional column to multiply col_val by (e.g. Price for Volume)")
    parser.add_argument("--interval", type=str, default="day")
    parser.add_argument("--time_format", type=str, default="%Y/%m/%d")

    parsed, _ = parser.parse_known_args(args_list)
    result = vars(parsed)
    
    import os
    env_dir = os.environ.get("TARGET_ENV", "workspace")
    # Gracefully merge loaded system parameter baselines resolving omitted stream aliases
    sys_params_path = os.environ.get("TLU_SYS_PARAMS", f"{env_dir}/config/_sys_params.csv")
    sys_params = load_sys_params(sys_params_path)
    
    col_mapping = ["col_time", "col_src", "col_tgt", "col_val"]
    
    # 1. Provide defaults safely natively enforcing `_sys_params.csv` mapping over empty parsing outputs
    for col in col_mapping:
        if not result.get(col):
            # Try specific map key inside sys params (e.g. col_trans_date natively mapped on workspace logic)
            if col == "col_time": result[col] = sys_params.get("col_trans_date", "Trans_Date")
            elif col == "col_src": result[col] = sys_params.get("col_src", "Src")
            elif col == "col_tgt": result[col] = sys_params.get("col_tgt", "Tgt")
            elif col == "col_val": result[col] = sys_params.get("col_amount", "Amount")

    for col in col_mapping:
        val = result.get(col, "")
        if isinstance(val, str) and val.isdigit():
            result[col] = int(val)
            
    return result
