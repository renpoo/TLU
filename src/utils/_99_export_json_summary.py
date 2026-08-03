#!/usr/bin/env python3
# ==========================================
# _99_export_json_summary.py
# TLU System: Summary JSON Exporter for TLU Studio / TLU-App
# Version: 6.0.0 (Refactored with Dynamic Metric Registry)
# ==========================================
"""!
@file _99_export_json_summary.py
@brief Combines processed CSV metrics into a unified JSON stream for WebGL / UI rendering.
"""

import os
import sys
import json
import argparse
import pandas as pd
import numpy as np
from typing import Dict, Any, List, Tuple

def parse_args():
    parser = argparse.ArgumentParser(description="Export TLU analysis summary to JSON")
    parser.add_argument("--out_dir", type=str, default=None, help="Directory containing output CSV files")
    parser.add_argument("--node_map", type=str, default=None, help="Path to _node_map.csv")
    parser.add_argument("--time_map", type=str, default=None, help="Path to _time_map.csv")
    parser.add_argument("--output", type=str, default=None, help="Target JSON output file path")
    return parser.parse_args()

def load_mapping(filepath: str) -> Dict[int, str]:
    if not filepath or not os.path.exists(filepath):
        return {}
    try:
        df = pd.read_csv(filepath)
        if 'node_idx' in df.columns and 'node_label' in df.columns:
            return dict(zip(df['node_idx'].astype(int), df['node_label']))
        elif 't_idx' in df.columns and 'time_label' in df.columns:
            return dict(zip(df['t_idx'].astype(int), df['time_label']))
        elif 'idx' in df.columns and 'label' in df.columns:
            return dict(zip(df['idx'].astype(int), df['label']))
        elif 'idx' in df.columns and 'time_label' in df.columns:
            return dict(zip(df['idx'].astype(int), df['time_label']))
    except Exception as e:
        print(f"[WARN] Failed to load map {filepath}: {e}", file=sys.stderr)
    return {}

def safe_read_csv(filepath: str) -> Optional[pd.DataFrame]:
    if filepath and os.path.exists(filepath):
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            print(f"[WARN] Failed to read {filepath}: {e}", file=sys.stderr)
    return None

METRIC_REGISTRY: List[Tuple[str, str, str]] = [
    ("000_1_1", "thermodynamics", "dynamics"),
    ("000_2_1", "thermodynamics", "stiffness"),
    ("000_2_2", "thermodynamics", "principal_axes"),
    ("000_2_4", "thermodynamics", "stiffness_diff"),
    ("001_1_1", "thermodynamics", "macro"),
    ("001_1_2", "thermodynamics", "local"),
    ("001_2_1", "thermodynamics", "lag_matrix"),
    ("002_1_1", "forensics", "info_curvature"),
    ("002_1_2", "topology", "records"),
    ("002_1_3", "topology", "manifold_dimensionality"),
    ("002_2_1", "forensics", "macro"),
    ("002_2_2", "forensics", "records"),
    ("003_1_1", "kinematics", "fk"),
    ("003_1_2", "kinematics", "ik"),
    ("jacobian_1st", "jacobian", "order_1st"),
    ("jacobian_2nd", "jacobian", "order_2nd"),
    ("jacobian_3rd", "jacobian", "order_3rd"),
    ("004_1_1", "control", "lqr_trajectory"),
    ("004_1_2", "control", "stability"),
    ("004_2_1", "control", "sensitivity"),
    ("005_1_1", "wave_fractal", "resonant_frequency"),
    ("005_1_2", "wave_fractal", "phase_shift_coherence"),
    ("005_2_1", "wave_fractal", "fractal_noise"),
]

def export_summary_json(out_dir: str, node_map_path: str = None, time_map_path: str = None) -> Dict[str, Any]:
    target_env = os.environ.get("TARGET_ENV", "workspace")
    if node_map_path is None:
        node_map_path = os.path.join(target_env, "ephemeral", "_node_map.csv")
    if time_map_path is None:
        time_map_path = os.path.join(target_env, "ephemeral", "_time_map.csv")

    node_map = load_mapping(node_map_path)
    time_map = load_mapping(time_map_path)
    
    config_dir = os.path.join(target_env, "config")
    account_config = []
    sys_params = []

    df_acc_map = safe_read_csv(os.path.join(config_dir, "_account_mapping.csv"))
    if df_acc_map is None or df_acc_map.empty:
        df_acc_map = safe_read_csv(os.path.join(config_dir, "account_mapping.csv"))
    if df_acc_map is None or df_acc_map.empty:
        df_acc_map = safe_read_csv(os.path.join(config_dir, "node_config.csv"))

    if df_acc_map is not None and not df_acc_map.empty:
        account_config = df_acc_map.replace({np.nan: None}).to_dict(orient="records")

    df_params = safe_read_csv(os.path.join(config_dir, "_sys_params.csv"))
    if df_params is not None and not df_params.empty:
        sys_params = df_params.replace({np.nan: None}).to_dict(orient="records")

    summary = {
        "metadata": {
            "target_env": target_env,
            "node_count": len(node_map),
            "time_count": len(time_map),
            "node_labels": node_map,
            "time_labels": time_map,
            "account_config": account_config,
            "sys_params": sys_params
        },
        "input_config": {
            "account_mapping": account_config,
            "sys_params": sys_params
        },
        "thermodynamics": {},
        "topology": {},
        "jacobian": {},
        "kinematics": {},
        "forensics": {},
        "control": {},
        "wave_fractal": {}
    }

    if not os.path.exists(out_dir):
        return summary

    files_in_dir = os.listdir(out_dir)

    for pattern, cat, key in METRIC_REGISTRY:
        matched_file = next((f for f in files_in_dir if pattern in f and f.endswith('.csv')), None)
        if matched_file:
            df = safe_read_csv(os.path.join(out_dir, matched_file))
            if df is not None and not df.empty:
                records = df.replace({np.nan: None}).to_dict(orient="records")
                if cat == "topology" and key == "records":
                    summary["topology"] = {
                        "records_count": len(df),
                        "records": records
                    }
                else:
                    if cat not in summary:
                        summary[cat] = {}
                    summary[cat][key] = records

    return summary

def main():
    args = parse_args()
    target_env = os.environ.get("TARGET_ENV", "workspace")
    out_dir = args.out_dir or os.path.join(target_env, "output_data")
    node_map_path = args.node_map or os.path.join(target_env, "ephemeral", "_node_map.csv")
    time_map_path = args.time_map or os.path.join(target_env, "ephemeral", "_time_map.csv")
    output_path = args.output or os.path.join(out_dir, "summary.json")

    summary = export_summary_json(out_dir, node_map_path, time_map_path)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"[OK] Summary JSON successfully exported to: {output_path}")

if __name__ == "__main__":
    main()
