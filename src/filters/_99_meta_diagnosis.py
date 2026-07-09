#!/usr/bin/env python3
# _99_meta_diagnosis.py
# TLU System: Automated Meta-Diagnosis Engine (Statistical Upgrade V3)
import os
import json
import argparse
import pandas as pd
import numpy as np
import scipy.stats as stats
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser(description="TLU Meta-Diagnosis Engine V3")
    return parser.parse_args()

def safe_read_csv(filepath):
    if os.path.exists(filepath):
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            print(f"[WARN] Error reading {filepath}: {e}")
            return None
    return None

def analyze_timeseries(df, col_name, z_threshold=3.0, decimals=2):
    """Calculate comprehensive statistical metrics for a time-series column."""
    if df is None or col_name not in df.columns or df.empty:
        return None
        
    series = df[col_name].dropna()
    if len(series) < 2:
        return None
        
    mean_val = series.mean()
    std_val = series.std()
    
    # Avoid division by zero
    if std_val == 0 or pd.isna(std_val):
        z_scores = pd.Series(0, index=series.index)
    else:
        z_scores = (series - mean_val) / std_val
        
    exceedances = (z_scores.abs() > z_threshold).sum()
    
    # Range
    min_val = float(series.min())
    max_val = float(series.max())
    range_val = max_val - min_val
    
    # IQR
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr_val = q3 - q1
    
    # Mode (rounded to specified decimal places)
    rounded = series.round(decimals)
    mode_series = rounded.mode()
    if not mode_series.empty:
        mode_val = float(mode_series.iloc[0])
        mode_count = int((rounded == mode_val).sum())
    else:
        mode_val = 0.0
        mode_count = 0
        
    return {
        "max": max_val,
        "min": min_val,
        "range": range_val,
        "mean": mean_val,
        "median": series.median(),
        "mode_val": mode_val,
        "mode_count": mode_count,
        "total_count": len(series),
        "std": std_val,
        "iqr": iqr_val,
        "skewness": float(stats.skew(series, nan_policy='omit')),
        "kurtosis": float(stats.kurtosis(series, nan_policy='omit')),
        "max_z_score": float(z_scores.abs().max()),
        "exceedance_count": int(exceedances)
    }

def main():
    args = parse_args()
    env_dir = os.environ.get("TARGET_ENV", "workspace")
    output_data_dir = os.path.join(env_dir, "output_data")
    
    print(f"🩺 TLU Meta-Diagnosis Engine: Analyzing {env_dir} ...")
    
    if not os.path.exists(output_data_dir):
        print(f"[ERROR] Output data directory not found: {output_data_dir}")
        return

    # 1. Load Data
    df_dynamics  = safe_read_csv(os.path.join(output_data_dir, "result.000_1_1_filter_dynamics.analysis.csv"))
    df_stiffness = safe_read_csv(os.path.join(output_data_dir, "result.000_2_1_filter_structural_stiffness.analysis.csv"))
    df_thermo    = safe_read_csv(os.path.join(output_data_dir, "result.001_1_1_filter_macro_thermodynamics.analysis.csv"))
    df_macro_for = safe_read_csv(os.path.join(output_data_dir, "result.002_2_1_filter_macro_forensics.analysis.csv"))
    df_network   = safe_read_csv(os.path.join(output_data_dir, "result.002_1_2_filter_network_topology.analysis.csv"))
    df_stability = safe_read_csv(os.path.join(output_data_dir, "result.004_1_2_filter_system_stability.analysis.csv"))
    df_sens      = safe_read_csv(os.path.join(output_data_dir, "result.004_2_1_filter_sensitivity.analysis.csv"))

    # 2. Extract Comprehensive Descriptive Statistics for all parsed measures
    all_stats = {}
    
    # 2.1 Dynamics Metrics (prefix: 000_1)
    if df_dynamics is not None:
        all_stats["Dynamics: state_X"] = analyze_timeseries(df_dynamics, "state_X", decimals=1)
        all_stats["Dynamics: velocity_v"] = analyze_timeseries(df_dynamics, "velocity_v", decimals=1)
        all_stats["Dynamics: acceleration_a"] = analyze_timeseries(df_dynamics, "acceleration_a", decimals=1)
        all_stats["Dynamics: jerk_j"] = analyze_timeseries(df_dynamics, "jerk_j", decimals=1)
        all_stats["Dynamics: snap_s"] = analyze_timeseries(df_dynamics, "snap_s", decimals=1)
        all_stats["Dynamics: viscosity_C"] = analyze_timeseries(df_dynamics, "viscosity_C", decimals=2)
        
    # 2.2 Stiffness Metrics (prefix: 000_2)
    if df_stiffness is not None:
        all_stats["Stiffness: stiffness_k"] = analyze_timeseries(df_stiffness, "stiffness_k", decimals=2)
        all_stats["Stiffness: partial_corr"] = analyze_timeseries(df_stiffness, "partial_corr", decimals=3)

    # 2.3 Thermodynamics Metrics (prefix: 001_1)
    if df_thermo is not None:
        all_stats["Thermo: gross_activity_U"] = analyze_timeseries(df_thermo, "gross_activity_U", decimals=0)
        all_stats["Thermo: entropy_S"] = analyze_timeseries(df_thermo, "entropy_S", decimals=1)
        all_stats["Thermo: temperature_T"] = analyze_timeseries(df_thermo, "temperature_T", decimals=1)
        all_stats["Thermo: free_energy_F"] = analyze_timeseries(df_thermo, "free_energy_F", decimals=0)
        
    # 2.4 Forensics Metrics (prefix: 002_2)
    if df_macro_for is not None:
        all_stats["Forensics: conservation_residual"] = analyze_timeseries(df_macro_for, "conservation_residual", decimals=3)
        all_stats["Forensics: kl_divergence_drift"] = analyze_timeseries(df_macro_for, "kl_divergence_drift", decimals=3)
        
    # 2.5 Topology Metrics (prefix: 002_1)
    if df_network is not None:
        all_stats["Topology: stress"] = analyze_timeseries(df_network, "stress", decimals=3)
        all_stats["Topology: weight"] = analyze_timeseries(df_network, "weight", decimals=3)
        
    # 2.6 Stability Metrics (prefix: 004_1)
    if df_stability is not None:
        all_stats["Stability: spectral_radius"] = analyze_timeseries(df_stability, "spectral_radius", decimals=3)

    # 3. Extract Specific Metrics for Decision Tree Logic
    metrics = {
        "mean_gross_activity": 1e-9,
        "relative_leak_ratio": 0.0,
        "max_spectral": 0.0,
        "min_stress": 999999.0,
        "max_viscosity": 0.0,
        "min_viscosity": 0.0,
    }
    
    if "Thermo: gross_activity_U" in all_stats and all_stats["Thermo: gross_activity_U"]:
        metrics["mean_gross_activity"] = all_stats["Thermo: gross_activity_U"]["mean"]
        
    if all_stats.get("Forensics: conservation_residual"):
        max_abs_res = max(abs(all_stats["Forensics: conservation_residual"]["min"]), 
                          abs(all_stats["Forensics: conservation_residual"]["max"]))
        metrics["relative_leak_ratio"] = max_abs_res / metrics["mean_gross_activity"]
        
    if all_stats.get("Stability: spectral_radius"):
        metrics["max_spectral"] = all_stats["Stability: spectral_radius"]["max"]
        
    if df_dynamics is not None and 'viscosity_C' in df_dynamics.columns:
        if 'time_label' in df_dynamics.columns:
            visc_grouped = df_dynamics.groupby('time_label')['viscosity_C'].sum()
            metrics["max_viscosity"] = visc_grouped.max()
            metrics["min_viscosity"] = visc_grouped.min()
            
    if df_network is not None and 'stress' in df_network.columns:
        if 'time_label' in df_network.columns and 't_idx' in df_network.columns:
            valid_network = df_network[df_network['t_idx'] >= 2]
            if not valid_network.empty:
                stress_grouped = valid_network.groupby('time_label')['stress'].sum()
                metrics["min_stress"] = stress_grouped.min()

    # 3.1 Quartile-based Candidate Analysis (Viscosity & Sensitivity)
    stiff_candidates = []
    tsubo_candidates = []
    kinki_candidates = []
    
    q3_visc = 0.0
    q1_strain = 0.0
    q3_strain = 0.0
    
    if df_dynamics is not None and "viscosity_C" in df_dynamics.columns and "node_label" in df_dynamics.columns:
        mean_visc = df_dynamics.groupby("node_label")["viscosity_C"].mean()
        real_visc = mean_visc[~mean_visc.index.str.contains("Equity|Capital|Equity_Capital", case=False)]
        if not real_visc.empty:
            q3_visc = float(np.percentile(real_visc.values, 75))
            stiff_nodes = real_visc[real_visc >= q3_visc].sort_values(ascending=False)
            for node, avg_val in stiff_nodes.items():
                node_df = df_dynamics[df_dynamics["node_label"] == node]
                peak_row = node_df.loc[node_df["viscosity_C"].idxmax()]
                stiff_candidates.append({
                    "node": node,
                    "avg_viscosity": float(avg_val),
                    "peak_time": str(peak_row["time_label"]) if "time_label" in peak_row else "unknown",
                    "peak_val": float(peak_row["viscosity_C"])
                })
                
    if df_sens is not None and "ik_strain_energy" in df_sens.columns and "node_label" in df_sens.columns:
        mean_strain = df_sens.groupby("node_label")["ik_strain_energy"].mean()
        if not mean_strain.empty:
            q1_strain = float(np.percentile(mean_strain.values, 25))
            q3_strain = float(np.percentile(mean_strain.values, 75))
            
            tsubo_nodes = mean_strain[mean_strain <= q1_strain].sort_values()
            for node, avg_val in tsubo_nodes.items():
                tsubo_candidates.append({
                    "node": node,
                    "avg_strain": float(avg_val)
                })
                
            kinki_nodes = mean_strain[(mean_strain >= q3_strain) | (mean_strain >= 49.90)].sort_values(ascending=False)
            for node, avg_val in kinki_nodes.items():
                kinki_candidates.append({
                    "node": node,
                    "avg_strain": float(avg_val)
                })

    # 4. Decision Tree Logic (Tier System V3)
    diagnoses = []
    
    # [Entropy Statistics Analysis]
    stats_entropy = all_stats.get("Thermo: entropy_S")
    if stats_entropy:
        if stats_entropy["kurtosis"] > 3.0 and stats_entropy["exceedance_count"] > 0:
            diagnoses.append({
                "pathology": "Fat-Tailed Entropy Spikes (Systemic Flash Crashes)",
                "severity": "CRITICAL",
                "evidence": f"Kurtosis: {stats_entropy['kurtosis']:.2f}, Anomalies (Z>3): {stats_entropy['exceedance_count']} times.",
                "interpretation": "The system experiences sudden, extreme bursts of friction (Black Swan events). The distribution is heavy-tailed, indicating unpredictable structural tearing rather than steady friction."
            })
        elif stats_entropy["mean"] > 10.0:
            diagnoses.append({
                "pathology": "Chronic High Friction (Baseline Tearing)",
                "severity": "HIGH",
                "evidence": f"Mean Entropy: {stats_entropy['mean']:.2f}.",
                "interpretation": "The system's baseline is inherently chaotic and highly viscous. Long-term structural integrity is doubtful due to constant energy dissipation."
            })
            
        if stats_entropy["skewness"] < -1.2:
            diagnoses.append({
                "pathology": "Abnormal Synchronization (Negative Entropy Skew)",
                "severity": "HIGH",
                "evidence": f"Entropy Skewness: {stats_entropy['skewness']:.2f}.",
                "interpretation": "Entropy occasionally drops far below its median, suggesting periodic forced synchronization (e.g., market manipulation or forced liquidation)."
            })

    # [Free Energy Statistics Analysis]
    stats_free_energy = all_stats.get("Thermo: free_energy_F")
    if stats_free_energy:
        if stats_free_energy["skewness"] < -1.0 and stats_free_energy["exceedance_count"] > 0:
            diagnoses.append({
                "pathology": "Structural Energy Decay (Negative Skewness)",
                "severity": "CRITICAL",
                "evidence": f"Free Energy Skew: {stats_free_energy['skewness']:.2f}, Z-Exceedances: {stats_free_energy['exceedance_count']}.",
                "interpretation": "The system's capacity to absorb shocks periodically collapses. This negative skewness indicates sudden, severe systemic vulnerability."
            })
        if stats_free_energy["min"] < -1000.0:
             diagnoses.append({
                "pathology": "Thermal Death (Absolute Energy Depletion)",
                "severity": "CRITICAL",
                "evidence": f"Min Free Energy: {stats_free_energy['min']:.2f}.",
                "interpretation": "The system has exhausted its resilience. External intervention is required."
             })

    # [Topology & Conservation Analysis]
    if metrics["min_stress"] < 0.1:
        diagnoses.append({
            "pathology": "Network Severance (Stress Zeroing)",
            "severity": "CRITICAL",
            "evidence": f"Min Edge Stress: {metrics['min_stress']:.4f}.",
            "interpretation": "Circulation between nodes has stopped. The network's connective tissue has snapped."
        })

    if metrics["relative_leak_ratio"] > 1e-6:
        diagnoses.append({
            "pathology": "Mass Conservation Violation (Leakage)",
            "severity": "CRITICAL",
            "evidence": f"Relative Leak Ratio: {metrics['relative_leak_ratio']:.6f}.",
            "interpretation": "Systemic flux is disappearing or materializing from nowhere."
        })
        
    if metrics["max_spectral"] >= 0.75:
        diagnoses.append({
            "pathology": "Topological Feedback Loop (Wash Trade / Resonance)",
            "severity": "HIGH",
            "evidence": f"Max Spectral Radius: {metrics['max_spectral']:.4f}.",
            "interpretation": "An artificial loop of funds or extreme resonance has formed in the network."
        })
        
    if not diagnoses:
        diagnoses.append({
            "pathology": "Healthy System (Statistically Stable)",
            "severity": "NORMAL",
            "evidence": "All statistical moments (Mean, Variance, Skew, Kurtosis) remain within stable thresholds.",
            "interpretation": "The system is functioning efficiently with normal random-walk volatility."
        })

    # 5. Generate Report
    report_path = os.path.join(output_data_dir, "_99_diagnosis_report.md")
    json_path = os.path.join(output_data_dir, "_99_diagnosis_report.json")
    
    diag_data = {
        "env_dir": env_dir,
        "date_analyzed": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "diagnoses": diagnoses,
        "metrics": metrics,
        "quartiles": {
            "viscosity_q3": q3_visc,
            "strain_q1": q1_strain,
            "strain_q3": q3_strain,
            "stiff_candidates": stiff_candidates,
            "tsubo_candidates": tsubo_candidates,
            "kinki_candidates": kinki_candidates
        }
    }
    with open(json_path, "w", encoding="utf-8") as jf:
        json.dump(diag_data, jf, indent=2, ensure_ascii=False)
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# TLU Meta-Diagnosis Report (Descriptive Statistics V3)\n\n")
        f.write(f"**Target Environment:** `{env_dir}`\n")
        f.write(f"**Date Analyzed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # 5.1 Final Diagnosis
        f.write("## 1. Final Diagnosis\n\n")
        if len(diagnoses) > 1 and "Healthy System" not in [d["pathology"] for d in diagnoses]:
            f.write("### ⚠️ COMPOSITE PATHOLOGY DETECTED\n")
            f.write("The system is suffering from multiple overlapping structural failures.\n\n")
        
        for d in diagnoses:
            icon = "🔴" if d["severity"] == "CRITICAL" else "🟠" if d["severity"] == "HIGH" else "🟡" if d["severity"] == "MEDIUM" else "🟢"
            f.write(f"### {icon} {d['pathology']}\n")
            f.write(f"- **Severity:** {d['severity']}\n")
            f.write(f"- **Evidence:** {d['evidence']}\n")
            f.write(f"- **Interpretation:** {d['interpretation']}\n\n")

        # 5.2 Comprehensive descriptive statistics table (all parsed measures)
        f.write("---\n## 2. Comprehensive Descriptive Statistics Table\n\n")
        f.write("The table below details the descriptive statistics computed individually for all active analytical scales across the TLU mathematical modules:\n\n")
        
        # Table Header
        f.write("| Measure / Scale | Mean | Median | Mode (count / total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis | Z-Exceed |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")
        
        for col_label, stats_dict in sorted(all_stats.items()):
            if stats_dict is None:
                continue
            
            # Formatting decimals based on scale type
            fmt = ".4f"
            if "gross_activity_U" in col_label or "free_energy_F" in col_label:
                fmt = ".1f"
            
            mean_str = f"{stats_dict['mean']:{fmt}}"
            median_str = f"{stats_dict['median']:{fmt}}"
            
            # Mode with count, total, and percentage
            total = stats_dict['total_count']
            pct = (stats_dict['mode_count'] / total) * 100 if total > 0 else 0.0
            mode_str = f"{stats_dict['mode_val']:{fmt}} ({stats_dict['mode_count']}/{total}, {pct:.1f}%)"
            min_str = f"{stats_dict['min']:{fmt}}"
            max_str = f"{stats_dict['max']:{fmt}}"
            range_str = f"{stats_dict['range']:{fmt}}"
            iqr_str = f"{stats_dict['iqr']:{fmt}}"
            std_str = f"{stats_dict['std']:{fmt}}"
            skew_str = f"{stats_dict['skewness']:.4f}"
            kurt_str = f"{stats_dict['kurtosis']:.4f}"
            exceed_str = str(stats_dict['exceedance_count'])
            
            f.write(f"| {col_label} | {mean_str} | {median_str} | {mode_str} | {min_str} | {max_str} | {range_str} | {iqr_str} | {std_str} | {skew_str} | {kurt_str} | {exceed_str} |\n")
            
        f.write("\n---\n## 3. Structural Evolution (Viscosity Classification)\n\n")
        v_max = metrics['max_viscosity']
        f.write(f"- **Viscosity Range:** `{metrics['min_viscosity']:.2f} ~ {v_max:.2f}`\n")
        if v_max > 50:
            f.write("  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.\n")
        elif v_max < 20:
            f.write("  - 🧊 **Diagnosis:** Superfluidity / Low-Friction (New-Generation Structure). The system is highly automated/algorithmic. A shock will likely cause an instant thermal death without friction to slow it down.\n")
        else:
            f.write("  - 🟢 **Diagnosis:** Standard systemic viscosity.\n")

        f.write("\n---\n## 4. Quartile-based Diagnostic Candidates\n\n")
        f.write(f"### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `{q3_visc:.4f}`)\n")
        if stiff_candidates:
            f.write("| Node | Average Viscosity | Peak Time | Peak Viscosity |\n")
            f.write("| :--- | :---: | :---: | :---: |\n")
            for c in stiff_candidates:
                f.write(f"| `{c['node']}` | {c['avg_viscosity']:.4f} | `{c['peak_time']}` | {c['peak_val']:.4f} |\n")
        else:
            f.write("No candidates identified.\n")
            
        f.write(f"\n### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `{q1_strain:.4f}`)\n")
        if tsubo_candidates:
            f.write("| Node | Average Strain Energy |\n")
            f.write("| :--- | :---: |\n")
            for c in tsubo_candidates:
                f.write(f"| `{c['node']}` | {c['avg_strain']:.4f} |\n")
        else:
            f.write("No candidates identified.\n")
            
        f.write(f"\n### 🚫 Contraindications (Kinki/Strain >= Q3: `{q3_strain:.4f}` or limit)\n")
        if kinki_candidates:
            f.write("| Node | Average Strain Energy |\n")
            f.write("| :--- | :---: |\n")
            for c in kinki_candidates:
                f.write(f"| `{c['node']}` | {c['avg_strain']:.4f} |\n")
        else:
            f.write("No candidates identified.\n")

        f.write("\n> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* \n\n")
        
    print(f"✅ Diagnosis Complete! Report saved to: {report_path}")

if __name__ == "__main__":
    main()
