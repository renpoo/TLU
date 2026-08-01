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

def export_summary_json(out_dir, node_map_path=None, time_map_path=None):
    target_env = os.environ.get("TARGET_ENV", "workspace")
    if node_map_path is None:
        node_map_path = os.path.join(target_env, "ephemeral", "_node_map.csv")
    if time_map_path is None:
        time_map_path = os.path.join(target_env, "ephemeral", "_time_map.csv")

    node_map = load_mapping(node_map_path)
    time_map = load_mapping(time_map_path)
    
    # Load account attributes and system parameters from config directory if available
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
            "target_env": os.environ.get("TARGET_ENV", "workspace"),
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
    
    # 1. Dynamics & Stiffness (4 CSVs)
    df_dynamics = safe_read_csv(os.path.join(out_dir, "result.000_1_1_filter_dynamics.analysis.csv"))
    if df_dynamics is not None and not df_dynamics.empty:
        summary["thermodynamics"]["dynamics"] = df_dynamics.replace({np.nan: None}).to_dict(orient="records")

    df_stiffness = safe_read_csv(os.path.join(out_dir, "result.000_2_1_filter_structural_stiffness.analysis.csv"))
    if df_stiffness is not None and not df_stiffness.empty:
        summary["thermodynamics"]["stiffness"] = df_stiffness.replace({np.nan: None}).to_dict(orient="records")

    df_principal = safe_read_csv(os.path.join(out_dir, "result.000_2_2_filter_principal_axes.analysis.csv"))
    if df_principal is not None and not df_principal.empty:
        summary["thermodynamics"]["principal_axes"] = df_principal.replace({np.nan: None}).to_dict(orient="records")

    df_stiff_diff = safe_read_csv(os.path.join(out_dir, "result.000_2_4_stiffness_diff.analysis.csv"))
    if df_stiff_diff is not None and not df_stiff_diff.empty:
        summary["thermodynamics"]["stiffness_diff"] = df_stiff_diff.replace({np.nan: None}).to_dict(orient="records")

    # 2. Thermodynamics & Lag (3 CSVs)
    df_macro_thermo = safe_read_csv(os.path.join(out_dir, "result.001_1_1_filter_macro_thermodynamics.analysis.csv"))
    if df_macro_thermo is not None and not df_macro_thermo.empty:
        summary["thermodynamics"]["macro"] = df_macro_thermo.replace({np.nan: None}).to_dict(orient="records")

    df_local_thermo = safe_read_csv(os.path.join(out_dir, "result.001_1_2_filter_local_thermodynamics.analysis.csv"))
    if df_local_thermo is not None and not df_local_thermo.empty:
        summary["thermodynamics"]["local"] = df_local_thermo.replace({np.nan: None}).to_dict(orient="records")

    df_lag = safe_read_csv(os.path.join(out_dir, "result.001_2_1_filter_lag_matrix.analysis.csv"))
    if df_lag is not None and not df_lag.empty:
        summary["thermodynamics"]["lag_matrix"] = df_lag.replace({np.nan: None}).to_dict(orient="records")

    # 3. Information Geometry & Topology & Forensics (5 CSVs)
    df_info_curv = safe_read_csv(os.path.join(out_dir, "result.002_1_1_filter_info_curvature.analysis.csv"))
    if df_info_curv is not None and not df_info_curv.empty:
        summary["forensics"]["info_curvature"] = df_info_curv.replace({np.nan: None}).to_dict(orient="records")

    df_topo = safe_read_csv(os.path.join(out_dir, "result.002_1_2_filter_network_topology.analysis.csv"))
    if df_topo is not None and not df_topo.empty:
        summary["topology"] = {
            "records_count": len(df_topo),
            "records": df_topo.replace({np.nan: None}).to_dict(orient="records")
        }

    df_manifold = safe_read_csv(os.path.join(out_dir, "result.002_1_3_filter_manifold_dimensionality.analysis.csv"))
    if df_manifold is not None and not df_manifold.empty:
        summary["topology"]["manifold_dimensionality"] = df_manifold.replace({np.nan: None}).to_dict(orient="records")

    df_macro_forensics = safe_read_csv(os.path.join(out_dir, "result.002_2_1_filter_macro_forensics.analysis.csv"))
    if df_macro_forensics is not None and not df_macro_forensics.empty:
        summary["forensics"]["macro"] = df_macro_forensics.replace({np.nan: None}).to_dict(orient="records")

    df_micro_forensics = safe_read_csv(os.path.join(out_dir, "result.002_2_2_filter_micro_forensics.analysis.csv"))
    if df_micro_forensics is not None and not df_micro_forensics.empty:
        summary["forensics"]["records"] = df_micro_forensics.replace({np.nan: None}).to_dict(orient="records")

    # 4. Kinematics & Jacobian (5 CSVs)
    df_fk = safe_read_csv(os.path.join(out_dir, "result.003_1_1_filter_fk.analysis.csv"))
    if df_fk is not None and not df_fk.empty:
        summary["kinematics"]["fk"] = df_fk.replace({np.nan: None}).to_dict(orient="records")

    df_ik = safe_read_csv(os.path.join(out_dir, "result.003_1_2_filter_ik.analysis.csv"))
    if df_ik is not None and not df_ik.empty:
        summary["kinematics"]["ik"] = df_ik.replace({np.nan: None}).to_dict(orient="records")

    df_jac1 = safe_read_csv(os.path.join(out_dir, "result.003_1_3_jacobian_1st.analysis.csv"))
    if df_jac1 is not None and not df_jac1.empty:
        summary["jacobian"]["order_1st"] = df_jac1.replace({np.nan: None}).to_dict(orient="records")

    df_jac2 = safe_read_csv(os.path.join(out_dir, "result.003_1_3_jacobian_2nd.analysis.csv"))
    if df_jac2 is not None and not df_jac2.empty:
        summary["jacobian"]["order_2nd"] = df_jac2.replace({np.nan: None}).to_dict(orient="records")

    df_jac3 = safe_read_csv(os.path.join(out_dir, "result.003_1_3_jacobian_3rd.analysis.csv"))
    if df_jac3 is not None and not df_jac3.empty:
        summary["jacobian"]["order_3rd"] = df_jac3.replace({np.nan: None}).to_dict(orient="records")

    # 5. Control Theory & Stability (3 CSVs)
    df_ctrl = safe_read_csv(os.path.join(out_dir, "result.004_1_1_filter_control_theory.analysis.csv"))
    if df_ctrl is not None and not df_ctrl.empty:
        summary["control"]["lqr_trajectory"] = df_ctrl.replace({np.nan: None}).to_dict(orient="records")

    df_stability = safe_read_csv(os.path.join(out_dir, "result.004_1_2_filter_system_stability.analysis.csv"))
    if df_stability is not None and not df_stability.empty:
        summary["control"]["stability"] = df_stability.replace({np.nan: None}).to_dict(orient="records")

    df_sens = safe_read_csv(os.path.join(out_dir, "result.004_2_1_filter_sensitivity.analysis.csv"))
    if df_sens is not None and not df_sens.empty:
        summary["control"]["sensitivity"] = df_sens.replace({np.nan: None}).to_dict(orient="records")

    # 6. Wave, Frequency & Fractal (3 CSVs)
    df_res_freq = safe_read_csv(os.path.join(out_dir, "result.005_1_1_filter_resonant_frequency.analysis.csv"))
    if df_res_freq is not None and not df_res_freq.empty:
        summary["wave_fractal"]["resonant_frequency"] = df_res_freq.replace({np.nan: None}).to_dict(orient="records")

    df_phase_shift = safe_read_csv(os.path.join(out_dir, "result.005_1_2_filter_phase_shift_coherence.analysis.csv"))
    if df_phase_shift is not None and not df_phase_shift.empty:
        summary["wave_fractal"]["phase_shift_coherence"] = df_phase_shift.replace({np.nan: None}).to_dict(orient="records")

    df_fractal = safe_read_csv(os.path.join(out_dir, "result.005_2_1_filter_fractal_noise.analysis.csv"))
    if df_fractal is not None and not df_fractal.empty:
        summary["wave_fractal"]["fractal_noise"] = df_fractal.replace({np.nan: None}).to_dict(orient="records")
        
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
