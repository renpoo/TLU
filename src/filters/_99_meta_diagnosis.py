#!/usr/bin/env python3
# _99_meta_diagnosis.py
# TLU System: Automated Meta-Diagnosis Engine (Statistical Upgrade V2)
import os
import json
import argparse
import pandas as pd
import numpy as np
import scipy.stats as stats
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser(description="TLU Meta-Diagnosis Engine V2")
    return parser.parse_args()

def safe_read_csv(filepath):
    if os.path.exists(filepath):
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            print(f"[WARN] Error reading {filepath}: {e}")
            return None
    return None

def analyze_timeseries(df, col_name, z_threshold=3.0):
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
    
    return {
        "max": series.max(),
        "min": series.min(),
        "mean": mean_val,
        "median": series.median(),
        "std": std_val,
        "skewness": stats.skew(series, nan_policy='omit'),
        "kurtosis": stats.kurtosis(series, nan_policy='omit'),
        "max_z_score": z_scores.abs().max(),
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
    df_macro_for = safe_read_csv(os.path.join(output_data_dir, "result.002_2_1_filter_macro_forensics.analysis.csv"))
    df_stability = safe_read_csv(os.path.join(output_data_dir, "result.004_1_2_filter_system_stability.analysis.csv"))
    df_thermo    = safe_read_csv(os.path.join(output_data_dir, "result.001_1_1_filter_macro_thermodynamics.analysis.csv"))
    df_micro_for = safe_read_csv(os.path.join(output_data_dir, "result.002_2_2_filter_micro_forensics.analysis.csv"))
    df_dynamics  = safe_read_csv(os.path.join(output_data_dir, "result.000_1_1_filter_dynamics.analysis.csv"))
    df_network   = safe_read_csv(os.path.join(output_data_dir, "result.002_1_2_filter_network_topology.analysis.csv"))

    # 2. Extract Statistical Metrics
    metrics = {
        "mean_gross_activity": 1e-9,
        "relative_leak_ratio": 0.0,
        "max_spectral": 0.0,
        "min_stress": 999999.0,
        "max_viscosity": 0.0,
        "min_viscosity": 0.0,
    }
    
    stats_entropy = None
    stats_free_energy = None
    
    if df_thermo is not None:
        if 'gross_activity_U' in df_thermo.columns:
            metrics["mean_gross_activity"] = df_thermo['gross_activity_U'].mean()
        
        stats_entropy = analyze_timeseries(df_thermo, 'entropy_S')
        stats_free_energy = analyze_timeseries(df_thermo, 'free_energy_F')

    if df_macro_for is not None and 'conservation_residual' in df_macro_for.columns:
        max_abs_res = float(df_macro_for['conservation_residual'].abs().max())
        metrics["relative_leak_ratio"] = max_abs_res / metrics["mean_gross_activity"]
        
    if df_stability is not None and 'spectral_radius' in df_stability.columns:
        metrics["max_spectral"] = df_stability['spectral_radius'].max()
        
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

    # 3. Decision Tree Logic (Statistical V2)
    diagnoses = []
    
    # [Entropy Statistics Analysis]
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
            
        if stats_entropy["skewness"] < -1.5:
            diagnoses.append({
                "pathology": "Abnormal Synchronization (Negative Entropy Skew)",
                "severity": "HIGH",
                "evidence": f"Entropy Skewness: {stats_entropy['skewness']:.2f}.",
                "interpretation": "Entropy occasionally drops far below its median, suggesting periodic forced synchronization (e.g., market manipulation or forced liquidation)."
            })

    # [Free Energy Statistics Analysis]
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
        
    if metrics["max_spectral"] >= 0.60:
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

    # 4. Generate Report
    report_path = os.path.join(output_data_dir, "_99_diagnosis_report.md")
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# TLU Meta-Diagnosis Report (Statistical Upgrade V2)\n\n")
        f.write(f"**Target Environment:** `{env_dir}`\n")
        f.write(f"**Date Analyzed:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
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

        f.write("---\n## 2. Statistical Array Forensics (Time-Series Diagnostics)\n\n")
        f.write("### Entropy (S) Dynamics\n")
        if stats_entropy:
            f.write(f"- **Baseline (Mean / Median):** {stats_entropy['mean']:.2f} / {stats_entropy['median']:.2f}\n")
            f.write(f"- **Volatility (Std Dev):** {stats_entropy['std']:.2f}\n")
            f.write(f"- **Distribution Shape (Skew / Kurtosis):** {stats_entropy['skewness']:.2f} / {stats_entropy['kurtosis']:.2f}\n")
            f.write(f"- **Anomaly Count (Z > 3.0):** {stats_entropy['exceedance_count']} times\n\n")
            
        f.write("### Free Energy (F) Dynamics\n")
        if stats_free_energy:
            f.write(f"- **Baseline (Mean / Median):** {stats_free_energy['mean']:,.2f} / {stats_free_energy['median']:,.2f}\n")
            f.write(f"- **Volatility (Std Dev):** {stats_free_energy['std']:,.2f}\n")
            f.write(f"- **Distribution Shape (Skew / Kurtosis):** {stats_free_energy['skewness']:.2f} / {stats_free_energy['kurtosis']:.2f}\n")
            f.write(f"- **Anomaly Count (Z > 3.0):** {stats_free_energy['exceedance_count']} times\n\n")

        f.write("### Topological & Conservation Constraints\n")
        f.write(f"- **Max Spectral Radius:** {metrics['max_spectral']:.4f}\n")
        f.write(f"- **Min Edge Stress:** {metrics['min_stress']:.4f}\n")
        f.write(f"- **Relative Mass Leak Ratio:** {metrics['relative_leak_ratio']:.6f}\n\n")

        f.write("## 3. Structural Evolution (Viscosity Classification)\n\n")
        v_max = metrics['max_viscosity']
        f.write(f"- **Viscosity Range:** `{metrics['min_viscosity']:.2f} ~ {v_max:.2f}`\n")
        if v_max > 50:
            f.write("  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.\n")
        elif v_max < 20:
            f.write("  - 🧊 **Diagnosis:** Superfluidity / Low-Friction (New-Generation Structure). The system is highly automated/algorithmic. A shock will likely cause an instant thermal death without friction to slow it down.\n")
        else:
            f.write("  - 🟢 **Diagnosis:** Standard systemic viscosity.\n")

        f.write("\n> *Generated automatically by the TLU Meta-Diagnosis Engine (Statistical Upgrade).* \n\n")

    print(f"✅ Diagnosis Complete! Report saved to: {report_path}")

if __name__ == "__main__":
    main()
