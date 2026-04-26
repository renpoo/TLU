#!/usr/bin/env python3
# vis_meta_cross_environment.py
# TLU System: Cross-Environment Meta-Analysis Engine

import os
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def parse_args():
    parser = argparse.ArgumentParser(description="TLU Cross-Environment Meta-Analysis")
    parser.add_argument("--envs", nargs='+', required=True, help="List of environment directories to compare")
    parser.add_argument("--out", type=str, default="workspace/meta_analysis", help="Output directory")
    parser.add_argument("--theme", type=str, default="dark", help="Visualization theme")
    return parser.parse_args()

def safe_max(df, column, abs_val=False, default=0.0):
    if df is not None and column in df.columns:
        if abs_val:
            return df[column].abs().max()
        return df[column].max()
    return default

def safe_min(df, column, default=0.0):
    if df is not None and column in df.columns:
        return df[column].min()
    return default

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
    os.makedirs(args.out, exist_ok=True)
    
    results = []
    
    for env_dir in args.envs:
        # Strip trailing slashes
        env_dir = env_dir.rstrip('/')
        env_name = os.path.basename(env_dir)
        
        output_data_dir = os.path.join(env_dir, "output_data")
        if not os.path.exists(output_data_dir):
            print(f"[WARN] Skipped {env_name}: {output_data_dir} not found.")
            continue
            
        print(f"Processing: {env_name}...")
        
        # Load necessary CSVs
        df_macro_for = safe_read_csv(os.path.join(output_data_dir, "result.002_2_1_filter_macro_forensics.analysis.csv"))
        df_stability = safe_read_csv(os.path.join(output_data_dir, "result.004_1_2_filter_system_stability.analysis.csv"))
        df_thermo    = safe_read_csv(os.path.join(output_data_dir, "result.001_1_1_filter_macro_thermodynamics.analysis.csv"))
        df_micro_for = safe_read_csv(os.path.join(output_data_dir, "result.002_2_2_filter_micro_forensics.analysis.csv"))
        
        # Extract Signature Metrics
        # 1. Unbalanced Mistake (Max Conservation Residual)
        max_residual = safe_max(df_macro_for, 'conservation_residual', abs_val=True)
        
        # 2. Wash Trade (Max Spectral Radius)
        max_spectral = safe_max(df_stability, 'spectral_radius')
        
        # 3. Embezzlement Leak (Min Free Energy)
        min_free_energy = safe_min(df_thermo, 'free_energy_F')
        
        # 4. Local Anomaly (Max Z-Score)
        max_z_score = safe_max(df_micro_for, 'node_univariate_z_score')
        
        results.append({
            "Environment": env_name,
            "Max_Conservation_Residual": max_residual,
            "Max_Spectral_Radius": max_spectral,
            "Min_Free_Energy": min_free_energy,
            "Max_Local_Z_Score": max_z_score
        })
        
    if not results:
        print("[ERROR] No valid environments processed.")
        return
        
    df_results = pd.DataFrame(results)
    
    # Save CSV
    csv_path = os.path.join(args.out, "meta_comparison.csv")
    df_results.to_csv(csv_path, index=False)
    print(f"✅ Saved CSV: {csv_path}")
    
    # Save Markdown
    md_path = os.path.join(args.out, "meta_comparison.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# TLU Cross-Environment Meta-Analysis\n\n")
        f.write("This table compares the maximum (or minimum) physical anomaly signatures across the specified environments.\n\n")
        f.write("| Environment | Max Conservation Residual (Unbalanced) | Max Spectral Radius (Wash Trade) | Min Free Energy (Leak) | Max Local Z-Score (Micro Anomaly) |\n")
        f.write("|-------------|----------------------------------------|----------------------------------|------------------------|-----------------------------------|\n")
        for _, row in df_results.iterrows():
            f.write(f"| {row['Environment']} | {row['Max_Conservation_Residual']:.2f} | {row['Max_Spectral_Radius']:.4f} | {row['Min_Free_Energy']:.2f} | {row['Max_Local_Z_Score']:.2f} |\n")
    print(f"✅ Saved Markdown: {md_path}")
    
    # Generate Comparison Plot (Grouped Bar Chart)
    generate_plot(df_results, args.out, args.theme)
    
def generate_plot(df, out_dir, theme):
    if theme == "dark":
        plt.style.use('dark_background')
        bg_color = '#121212'
        text_color = '#ffffff'
        grid_color = '#333333'
    else:
        plt.style.use('default')
        bg_color = '#ffffff'
        text_color = '#000000'
        grid_color = '#e0e0e0'
        
    fig, axes = plt.subplots(2, 2, figsize=(16, 10), facecolor=bg_color)
    fig.suptitle('TLU Cross-Environment Physical Signatures', color=text_color, fontsize=18, fontweight='bold')
    
    envs = df['Environment'].tolist()
    # Ensure labels are somewhat readable
    short_envs = [e.replace("Sample_", "").replace("_", "\n") for e in envs]
    x = np.arange(len(envs))
    
    def setup_ax(ax, title, ylabel, data, color):
        ax.set_facecolor(bg_color)
        ax.bar(x, data, color=color, alpha=0.8)
        ax.set_title(title, color=text_color, fontsize=14)
        ax.set_ylabel(ylabel, color=text_color)
        ax.set_xticks(x)
        ax.set_xticklabels(short_envs, rotation=0, color=text_color, fontsize=10)
        ax.tick_params(axis='y', colors=text_color)
        ax.grid(True, linestyle='--', alpha=0.5, color=grid_color)
        for spine in ax.spines.values():
            spine.set_color(grid_color)
            
    # Top Left: Conservation Residual
    setup_ax(axes[0, 0], 'Mass Conservation Violation (Unbalanced Mistake)', 'Max Abs Residual', df['Max_Conservation_Residual'], '#ff5252')
    
    # Top Right: Spectral Radius
    setup_ax(axes[0, 1], 'System Instability (Wash Trade Loop)', 'Max Spectral Radius', df['Max_Spectral_Radius'], '#ffb142')
    # Add critical threshold line at 1.0
    axes[0, 1].axhline(y=1.0, color='#ff0000', linestyle='--', linewidth=2, label='Critical Limit (1.0)')
    axes[0, 1].legend(loc='upper right', facecolor=bg_color, edgecolor=grid_color, labelcolor=text_color)
    
    # Bottom Left: Free Energy
    setup_ax(axes[1, 0], 'Thermodynamic Energy Depletion (Embezzlement/Leak)', 'Min Free Energy (F)', df['Min_Free_Energy'], '#34ace0')
    # Add zero baseline
    axes[1, 0].axhline(y=0.0, color='#ff0000', linestyle='--', linewidth=1)
    
    # Bottom Right: Micro Forensics Z-Score
    setup_ax(axes[1, 1], 'Local Pathological Stress (Micro Forensics)', 'Max Z-Score', df['Max_Local_Z_Score'], '#706fd3')
    # Add normal threshold line around 3.0
    axes[1, 1].axhline(y=3.0, color='#ff0000', linestyle='--', linewidth=1, label='Statistical Outlier (3.0)')
    axes[1, 1].legend(loc='upper right', facecolor=bg_color, edgecolor=grid_color, labelcolor=text_color)
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    plot_path = os.path.join(out_dir, "meta_comparison_signatures.png")
    plt.savefig(plot_path, dpi=150, bbox_inches='tight', facecolor=bg_color)
    plt.close()
    print(f"✅ Saved Plot: {plot_path}")

if __name__ == "__main__":
    main()
