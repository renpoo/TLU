#!/usr/bin/env python3
# _99_meta_diagnosis.py
# TLU System: Automated Meta-Diagnosis Engine (Appendix A Enhanced)
import os
import json
import argparse
import pandas as pd
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser(description="TLU Meta-Diagnosis Engine")
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
    df_dynamics  = safe_read_csv(os.path.join(output_data_dir, "result.000_1_1_filter_dynamics.analysis.csv"))
    df_network   = safe_read_csv(os.path.join(output_data_dir, "result.002_1_2_filter_network_topology.analysis.csv"))

    # 2. Extract Metrics
    metrics = {
        "max_abs_residual": 0.0,
        "mean_gross_activity": 1e-9,
        "relative_leak_ratio": 0.0,
        "max_spectral": 0.0,
        "min_free_energy": 0.0,
        "min_relative_free_energy": 0.0,
        "max_z_score": 0.0,
        "max_entropy": 0.0,
        "min_entropy": 0.0,
        "max_viscosity": 0.0,
        "min_viscosity": 0.0,
        "min_stress": 999999.0
    }
    
    if df_thermo is not None and 'gross_activity_U' in df_thermo.columns:
        metrics["mean_gross_activity"] = df_thermo['gross_activity_U'].mean()
        if 'free_energy_F' in df_thermo.columns:
            metrics["min_free_energy"] = df_thermo['free_energy_F'].min()
            metrics["min_relative_free_energy"] = (df_thermo['free_energy_F'] / df_thermo['gross_activity_U']).min()
        if 'entropy_S' in df_thermo.columns:
            metrics["max_entropy"] = df_thermo['entropy_S'].max()
            metrics["min_entropy"] = df_thermo['entropy_S'].min()

    if df_macro_for is not None and 'conservation_residual' in df_macro_for.columns:
        metrics["max_abs_residual"] = float(df_macro_for['conservation_residual'].abs().max())
        metrics["relative_leak_ratio"] = metrics["max_abs_residual"] / metrics["mean_gross_activity"]
        
    if df_stability is not None and 'spectral_radius' in df_stability.columns:
        metrics["max_spectral"] = df_stability['spectral_radius'].max()
        
    if df_micro_for is not None and 'node_univariate_z_score' in df_micro_for.columns:
        metrics["max_z_score"] = float(df_micro_for['node_univariate_z_score'].max())
        
    if df_dynamics is not None and 'viscosity_C' in df_dynamics.columns:
        if 'time_label' in df_dynamics.columns:
            visc_grouped = df_dynamics.groupby('time_label')['viscosity_C'].sum()
            metrics["max_viscosity"] = visc_grouped.max()
            metrics["min_viscosity"] = visc_grouped.min()
            
    if df_network is not None and 'stress' in df_network.columns:
        if 'time_label' in df_network.columns:
            stress_grouped = df_network.groupby('time_label')['stress'].sum()
            metrics["min_stress"] = stress_grouped.min()

    # 3. Decision Tree Logic (Appendix A + Theoretical Thresholds)
    T_REL_LEAK = 1e-6
    T_SPECTRAL = 0.60
    T_REL_FREE_ENERGY = -0.10
    T_Z_SCORE = 3.0
    T_ENTROPY_HIGH = 10.0
    T_ENTROPY_LOW = -100.0
    T_STRESS_MIN = 0.1
    T_FREE_ENERGY_DEATH = -1000.0
    
    diagnoses = []
    
    # [Appendix A #1] Macro Entropy Explosion/Collapse
    if metrics["max_entropy"] > T_ENTROPY_HIGH:
        diagnoses.append({
            "pathology": "Macro Entropy Explosion (Systemic Tearing)",
            "severity": "CRITICAL",
            "evidence": f"Entropy reached {metrics['max_entropy']:.2f} (Threshold: > {T_ENTROPY_HIGH}).",
            "interpretation": "The system is experiencing extreme internal friction. Sectors are tearing apart and moving in completely disconnected directions, typical of a massive systemic crash."
        })
    elif metrics["min_entropy"] < T_ENTROPY_LOW:
        diagnoses.append({
            "pathology": "Extreme Forced Synchronization (Bubble/Panic Peak)",
            "severity": "HIGH",
            "evidence": f"Entropy dropped to {metrics['min_entropy']:.2f} (Threshold: < {T_ENTROPY_LOW}).",
            "interpretation": "The system is unnaturally synchronized. All nodes are moving in the exact same direction, indicating either a blind speculative bubble or a forced liquidation panic."
        })

    # [Appendix A #4] Absolute Free Energy Thermal Death
    if metrics["min_free_energy"] < T_FREE_ENERGY_DEATH:
        diagnoses.append({
            "pathology": "Thermal Death (Absolute Energy Depletion)",
            "severity": "CRITICAL",
            "evidence": f"Absolute Free Energy sank to {metrics['min_free_energy']:.2f} (Threshold: < {T_FREE_ENERGY_DEATH}).",
            "interpretation": "The system has completely exhausted its capacity to absorb shocks. It requires immediate external intervention (e.g., Central Bank liquidity) to survive."
        })

    # [Appendix A #5] Network Edge Stress Loss
    if metrics["min_stress"] < T_STRESS_MIN:
        diagnoses.append({
            "pathology": "Network Severance (Stress Zeroing)",
            "severity": "CRITICAL",
            "evidence": f"Edge stress vanished to {metrics['min_stress']:.4f} (Threshold: < {T_STRESS_MIN}).",
            "interpretation": "Circulation between nodes has completely stopped. The network's connective tissue has snapped, resulting in simultaneous free-fall without any counter-tension."
        })

    # Legacy Theoretical Rules
    if metrics["relative_leak_ratio"] > T_REL_LEAK:
        diagnoses.append({
            "pathology": "Unbalanced Journal Mistake (Conservation Violation)",
            "severity": "CRITICAL",
            "evidence": f"Relative Leak Ratio: {metrics['relative_leak_ratio']:.4f}.",
            "interpretation": "Violation of mass conservation. Systemic flux is disappearing or materializing from nowhere."
        })
        
    if metrics["max_spectral"] >= T_SPECTRAL:
        diagnoses.append({
            "pathology": "Topological Feedback Loop (Wash Trade / Resonance)",
            "severity": "HIGH",
            "evidence": f"Spectral Radius: {metrics['max_spectral']:.4f}.",
            "interpretation": "An artificial loop of funds or extreme resonance has formed in the network."
        })
        
    # Healthy Check
    if not diagnoses:
        diagnoses.append({
            "pathology": "Healthy System (No Structural Pathologies Detected)",
            "severity": "NORMAL",
            "evidence": "All physical parameters remained within stable thresholds.",
            "interpretation": "The system is functioning efficiently without any detectable anomalies."
        })

    # 4. Generate Report
    report_path = os.path.join(output_data_dir, "_99_diagnosis_report.md")
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# TLU Meta-Diagnosis Report (Appendix A Enhanced)\n\n")
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

        f.write("---\n## 2. Scale-Invariant Diagnostic Metrics (Appendix A Core)\n\n")
        f.write("| Physical Domain | Extracted Metric | Value | Threshold |\n")
        f.write("|-----------------|------------------|-------|-----------|\n")
        f.write(f"| Thermodynamics  | Max Entropy (S)          | {metrics['max_entropy']:.2f} | > {T_ENTROPY_HIGH} |\n")
        f.write(f"| Thermodynamics  | Min Free Energy (F)      | {metrics['min_free_energy']:.2f} | < {T_FREE_ENERGY_DEATH} |\n")
        f.write(f"| Network Topology| Min Edge Stress          | {metrics['min_stress']:.4f} | < {T_STRESS_MIN} |\n")
        f.write(f"| Macro Forensics | Relative Mass Leak Ratio | {metrics['relative_leak_ratio']:.4f} | > {T_REL_LEAK} |\n")
        f.write(f"| Control Theory  | Max Spectral Radius      | {metrics['max_spectral']:.4f} | >= {T_SPECTRAL} |\n")

        f.write("\n## 3. Structural Evolution (Viscosity Classification)\n\n")
        v_max = metrics['max_viscosity']
        f.write(f"- **Viscosity Range:** `{metrics['min_viscosity']:.2f} ~ {v_max:.2f}`\n")
        if v_max > 50:
            f.write("  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction, prone to 'clogging' during panics.\n")
        elif v_max < 20:
            f.write("  - 🧊 **Diagnosis:** Superfluidity / Low-Friction (New-Generation Structure). The system is highly automated/algorithmic. A shock will likely cause an instant thermal death without friction to slow it down.\n")
        else:
            f.write("  - 🟢 **Diagnosis:** Standard systemic viscosity.\n")

        f.write("\n> *Generated automatically by the TLU Meta-Diagnosis Engine (ML-Optimized).*\n\n")

        # 5. Generate LLM Context Block
        f.write("<!--\n<LLM_DIAGNOSTIC_CONTEXT>\n")
        financial_summary = None
        fin_path = os.path.join(output_data_dir, "_00_financial_statements.json")
        if os.path.exists(fin_path):
            try:
                with open(fin_path, 'r') as jf:
                    fin_data = json.load(jf)
                    if fin_data and len(fin_data) > 0:
                        financial_summary = fin_data[-1]
            except Exception:
                pass

        llm_context = {
            "timestamp": datetime.now().isoformat(),
            "environment": env_dir,
            "physics_metrics": metrics,
            "detected_pathologies": diagnoses,
            "financial_baseline": financial_summary
        }
        f.write(json.dumps(llm_context, indent=2))
        f.write("\n</LLM_DIAGNOSTIC_CONTEXT>\n-->\n")

    print(f"✅ Diagnosis Complete! Report saved to: {report_path}")

if __name__ == "__main__":
    main()
