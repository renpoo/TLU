#!/usr/bin/env python3
# _99_meta_diagnosis.py
# TLU System: Automated Meta-Diagnosis Engine
import os
import json
import argparse
import pandas as pd
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser(description="TLU Meta-Diagnosis Engine")
    # Environment will be picked up from TARGET_ENV if not specified
    return parser.parse_args()

def safe_read_csv(filepath):
    if os.path.exists(filepath):
        try:
            return pd.read_csv(filepath)
        except Exception as e:
            print(f"[WARN] Error reading {filepath}: {e}")
            return None
    return None

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

    # 2. Extract Metrics & Convert to Scale-Invariant Ratios
    metrics = {
        "max_abs_residual": 0.0,
        "mean_gross_activity": 1e-9,  # Prevent div-by-zero
        "relative_leak_ratio": 0.0,
        "max_spectral": 0.0,
        "min_free_energy": 0.0,
        "min_relative_free_energy": 0.0,
        "max_z_score": 0.0
    }
    
    if df_thermo is not None and 'gross_activity_U' in df_thermo.columns:
        metrics["mean_gross_activity"] = df_thermo['gross_activity_U'].mean()
        if 'free_energy_F' in df_thermo.columns:
            metrics["min_free_energy"] = df_thermo['free_energy_F'].min()
            # Calculate Relative Energy Depletion
            # We want the minimum (most negative) ratio of Free Energy to Gross Activity
            metrics["min_relative_free_energy"] = (df_thermo['free_energy_F'] / df_thermo['gross_activity_U']).min()

    if df_macro_for is not None and 'conservation_residual' in df_macro_for.columns:
        metrics["max_abs_residual"] = df_macro_for['conservation_residual'].abs().max()
        # Calculate Relative Mass Leakage
        metrics["relative_leak_ratio"] = metrics["max_abs_residual"] / metrics["mean_gross_activity"]
        
    if df_stability is not None and 'spectral_radius' in df_stability.columns:
        metrics["max_spectral"] = df_stability['spectral_radius'].max()
        
    if df_micro_for is not None and 'node_univariate_z_score' in df_micro_for.columns:
        metrics["max_z_score"] = df_micro_for['node_univariate_z_score'].max()

    # 3. Decision Tree Logic (Using SCALE-INVARIANT Thresholds)
    # Dimensionless Ratios
    T_REL_LEAK = 0.001          # 0.1% systemic mass leak
    T_SPECTRAL = 0.90           # Nearing 1.0 instability
    T_REL_FREE_ENERGY = -0.10   # Free energy drops to -10% of total activity
    T_Z_SCORE = 3.0             # 3 Sigma anomaly
    
    diagnoses = []
    
    # Rule 1: Mass Conservation (Syntax Error / Direct Leak)
    if metrics["relative_leak_ratio"] > T_REL_LEAK:
        diagnoses.append({
            "pathology": "Unbalanced Journal Mistake (Conservation Violation)",
            "severity": "CRITICAL",
            "evidence": f"Relative Leak Ratio reached {metrics['relative_leak_ratio']:.4f} (Threshold: {T_REL_LEAK}). Raw residual: {metrics['max_abs_residual']:.2f}",
            "interpretation": "The fundamental law of mass conservation is broken. A statistically significant percentage of systemic flux is disappearing or materializing from nowhere."
        })
        
    # Rule 2: Topological Loop (Wash Trade / Cycling)
    if metrics["max_spectral"] >= T_SPECTRAL:
        diagnoses.append({
            "pathology": "Topological Feedback Loop (Wash Trade)",
            "severity": "HIGH",
            "evidence": f"Spectral Radius reached {metrics['max_spectral']:.4f} (Threshold: {T_SPECTRAL}).",
            "interpretation": "An artificial loop of funds has formed in the network, creating infinite mathematical resonance. This is the structural signature of cyclical fraud (e.g., Wash Trading)."
        })
        
    # Rule 3: Thermodynamic Depletion (Embezzlement / Leak)
    if metrics["min_relative_free_energy"] < T_REL_FREE_ENERGY:
        diagnoses.append({
            "pathology": "Thermodynamic Energy Depletion (Embezzlement/Leak)",
            "severity": "HIGH",
            "evidence": f"Relative Free Energy Ratio sank to {metrics['min_relative_free_energy']:.4f} (Threshold: {T_REL_FREE_ENERGY}). Raw F: {metrics['min_free_energy']:.2f}",
            "interpretation": "Despite high transaction volume, the operational 'blood' of the system is leaking outwards. The network's capacity to perform work has collapsed relative to its scale."
        })
        
    # Rule 4: Local Pathological Stress
    if metrics["max_z_score"] > T_Z_SCORE:
        # Only report this as primary if no systemic anomalies were found, otherwise it's just supporting.
        severity = "MEDIUM" if len(diagnoses) > 0 else "HIGH"
        diagnoses.append({
            "pathology": "Local Pathological Stress (Micro Singularity)",
            "severity": severity,
            "evidence": f"Maximum local Z-Score reached {metrics['max_z_score']:.2f} (Threshold: {T_Z_SCORE}).",
            "interpretation": "Specific nodes (departments) are experiencing statistical strain far beyond their historical norm."
        })

    # Rule 5: Healthy System
    if not diagnoses:
        diagnoses.append({
            "pathology": "Healthy System (No Structural Pathologies Detected)",
            "severity": "NORMAL",
            "evidence": "All physical parameters remained within stable thresholds.",
            "interpretation": "The system is functioning efficiently without any detectable structural anomalies, leaks, or loops."
        })

    # 4. Generate Report
    report_path = os.path.join(output_data_dir, "_99_diagnosis_report.md")
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# TLU Meta-Diagnosis Report (Attending Physician's Summary)\n\n")
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

        f.write("---\n## 2. Scale-Invariant Diagnostic Metrics\n\n")
        f.write("| Physical Domain | Extracted Metric | Value | Threshold |\n")
        f.write("|-----------------|------------------|-------|-----------|\n")
        f.write(f"| Macro Forensics | Relative Mass Leak Ratio | {metrics['relative_leak_ratio']:.4f} | > {T_REL_LEAK} |\n")
        f.write(f"| Control Theory  | Max Spectral Radius      | {metrics['max_spectral']:.4f} | >= {T_SPECTRAL} |\n")
        f.write(f"| Thermodynamics  | Relative Free Energy Ratio| {metrics['min_relative_free_energy']:.4f} | < {T_REL_FREE_ENERGY} |\n")
        f.write(f"| Micro Forensics | Max Local Z-Score        | {metrics['max_z_score']:.2f} | > {T_Z_SCORE} |\n")
        
        f.write("\n> *Generated automatically by the TLU Meta-Diagnosis Engine.*\n\n")

        # 5. Generate LLM Context Block
        f.write("<!--\n")
        f.write("<LLM_DIAGNOSTIC_CONTEXT>\n")
        
        # Try to load financial statements for LLM context
        financial_summary = None
        fin_path = os.path.join(output_data_dir, "_00_financial_statements.json")
        if os.path.exists(fin_path):
            try:
                with open(fin_path, 'r') as jf:
                    fin_data = json.load(jf)
                    if fin_data and len(fin_data) > 0:
                        financial_summary = fin_data[-1] # The last period represents the cumulative state
            except Exception as e:
                pass

        llm_context = {
            "timestamp": datetime.now().isoformat(),
            "environment": env_dir,
            "physics_metrics": metrics,
            "detected_pathologies": diagnoses,
            "financial_baseline": financial_summary
        }
        f.write(json.dumps(llm_context, indent=2))
        f.write("\n</LLM_DIAGNOSTIC_CONTEXT>\n")
        f.write("-->\n")

    print(f"✅ Diagnosis Complete! Report saved to: {report_path}")

if __name__ == "__main__":
    main()
