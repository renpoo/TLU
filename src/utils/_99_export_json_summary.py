#!/usr/bin/env python3
"""
==========================================
_99_export_json_summary.py
TLU System: Summary JSON Exporter for TLU Studio / TLU-App
==========================================
Combines processed CSV metrics (Thermodynamics, Topology, Jacobian, State)
into a unified JSON stream for instant WebGL / UI rendering in TLU-App.
"""

import os
import sys
import json
import argparse
import pandas as pd
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser(description="Export TLU analysis summary to JSON")
    parser.add_argument("--out_dir", type=str, default=None, help="Directory containing output CSV files")
    parser.add_argument("--node_map", type=str, default=None, help="Path to _node_map.csv")
    parser.add_argument("--time_map", type=str, default=None, help="Path to _time_map.csv")
    parser.add_argument("--output", type=str, default=None, help="Target JSON output file path")
    return parser.parse_args()

def load_mapping(filepath):
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

def safe_read_csv(filepath):
    if filepath and os.path.exists(filepath):
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            print(f"[WARN] Failed to read {filepath}: {e}", file=sys.stderr)
    return None

def main():
    args = parse_args()
    
    target_env = os.environ.get("TARGET_ENV", "workspace")
    out_dir = args.out_dir or os.path.join(target_env, "output_data")
    node_map_path = args.node_map or os.path.join(target_env, "ephemeral", "_node_map.csv")
    time_map_path = args.time_map or os.path.join(target_env, "ephemeral", "_time_map.csv")
    output_path = args.output or os.path.join(out_dir, "summary.json")
    
    node_map = load_mapping(node_map_path)
    time_map = load_mapping(time_map_path)
    
    summary = {
        "metadata": {
            "target_env": target_env,
            "node_count": len(node_map),
            "time_count": len(time_map),
            "node_labels": node_map,
            "time_labels": time_map
        },
        "thermodynamics": {},
        "topology": {},
        "jacobian": {}
    }
    
    # 1. Thermodynamics State
    df_thermo = safe_read_csv(os.path.join(out_dir, "result.000_1_1_filter_dynamics.analysis.csv"))
    if df_thermo is not None and not df_thermo.empty:
        summary["thermodynamics"]["dynamics"] = df_thermo.replace({np.nan: None}).to_dict(orient="records")

    df_macro_thermo = safe_read_csv(os.path.join(out_dir, "result.001_1_1_filter_macro_thermodynamics.analysis.csv"))
    if df_macro_thermo is not None and not df_macro_thermo.empty:
        summary["thermodynamics"]["macro"] = df_macro_thermo.replace({np.nan: None}).to_dict(orient="records")

    df_local_thermo = safe_read_csv(os.path.join(out_dir, "result.001_1_2_filter_local_thermodynamics.analysis.csv"))
    if df_local_thermo is not None and not df_local_thermo.empty:
        summary["thermodynamics"]["local"] = df_local_thermo.replace({np.nan: None}).to_dict(orient="records")
        
    # 2. Topology / Flow Metrics
    df_topo = safe_read_csv(os.path.join(out_dir, "result.002_1_2_filter_network_topology.analysis.csv"))
    if df_topo is not None and not df_topo.empty:
        summary["topology"] = {
            "records_count": len(df_topo),
            "records": df_topo.replace({np.nan: None}).to_dict(orient="records")
        }
        
    # 3. Jacobian Trajectory Metrics
    df_jac1 = safe_read_csv(os.path.join(out_dir, "result.003_1_3_jacobian_1st.analysis.csv"))
    if df_jac1 is not None and not df_jac1.empty:
        summary["jacobian"]["order_1st"] = df_jac1.replace({np.nan: None}).to_dict(orient="records")

    df_jac2 = safe_read_csv(os.path.join(out_dir, "result.003_1_3_jacobian_2nd.analysis.csv"))
    if df_jac2 is not None and not df_jac2.empty:
        summary["jacobian"]["order_2nd"] = df_jac2.replace({np.nan: None}).to_dict(orient="records")

    df_jac3 = safe_read_csv(os.path.join(out_dir, "result.003_1_3_jacobian_3rd.analysis.csv"))
    if df_jac3 is not None and not df_jac3.empty:
        summary["jacobian"]["order_3rd"] = df_jac3.replace({np.nan: None}).to_dict(orient="records")
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
        
    print(f"✅ Successfully exported TLU summary JSON to: {output_path}")

if __name__ == "__main__":
    main()
