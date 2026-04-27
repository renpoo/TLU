#!/usr/bin/env python3
# ==========================================
# _0_3_auto_calibrate.py
# TLU System: Auto-Calibration (Burn-in) Engine
# ==========================================
import os
import sys
import json
import pandas as pd
import numpy as np
from scipy.stats import kurtosis

from src.filters.cli_parser import load_sys_params

def main():
    env_dir = os.environ.get("TARGET_ENV", "workspace")
    sys_params_path = os.path.join(env_dir, "config", "_sys_params.csv")
    coo_path = os.path.join(env_dir, "ephemeral", "_coo_stream.csv")
    out_json = os.path.join(env_dir, "ephemeral", "_tuned_params.json")
    
    # 1. Check if auto-tuning is enabled
    sys_params = load_sys_params(sys_params_path)
    
    auto_tune = str(sys_params.get("auto_tune_enabled", "False")).lower() in ['true', '1', 'yes', 'y']
    if not auto_tune:
        print("💡 Auto-Calibration is disabled in _sys_params.csv. Using manual static thresholds.")
        # Create empty tuned params to prevent errors down the line
        with open(out_json, "w") as f:
            json.dump({}, f)
        return

    burn_in_period = int(sys_params.get("auto_tune_burn_in_period", 24))
    
    print(f"🚀 Auto-Calibration Enabled! Analyzing the first {burn_in_period} time steps to tune system thresholds...")
    
    # 2. Read COO stream
    if not os.path.exists(coo_path):
        print(f"[ERROR] COO stream not found at {coo_path}. Cannot auto-calibrate.")
        sys.exit(1)
        
    try:
        df = pd.read_csv(coo_path)
    except pd.errors.EmptyDataError:
        print("[WARN] Empty COO stream. Cannot auto-calibrate.")
        with open(out_json, "w") as f:
            json.dump({}, f)
        return
        
    # 3. Filter for Burn-in Period
    min_t = df['t_idx'].min()
    max_t = df['t_idx'].max()
    burn_in_end = min(min_t + burn_in_period - 1, max_t)
    
    df_burn_in = df[df['t_idx'] <= burn_in_end]
    
    if df_burn_in.empty:
        print("[WARN] Insufficient data in burn-in period.")
        with open(out_json, "w") as f:
            json.dump({}, f)
        return
        
    # Calculate Gross Systemic Activity (U) per time step
    U_series = df_burn_in.groupby('t_idx')['value'].sum()
    
    # Reindex to ensure continuous time steps
    t_index = np.arange(min_t, burn_in_end + 1)
    U_series = U_series.reindex(t_index, fill_value=0.0).values
    
    tuned_params = {}
    
    # ==========================================
    # A. TUNE PHASE SHIFT FREQUENCY (FFT)
    # ==========================================
    if len(U_series) >= 8: # Need some minimum data for FFT
        # Remove DC component (mean)
        U_ac = U_series - np.mean(U_series)
        
        # Apply Hanning window to reduce spectral leakage
        window = np.hanning(len(U_ac))
        U_windowed = U_ac * window
        
        # Compute FFT
        fft_result = np.fft.rfft(U_windowed)
        magnitudes = np.abs(fft_result)
        
        # Get frequencies
        freqs = np.fft.rfftfreq(len(U_ac))
        
        # Find dominant frequency (excluding DC if it somehow leaked)
        if len(magnitudes) > 1:
            magnitudes[0] = 0 # Force DC to 0
            peak_idx = np.argmax(magnitudes)
            peak_freq = freqs[peak_idx]
            
            if peak_freq > 0.01: # Ignore extremely low frequencies (trends)
                # target_phase_frequency is basically peak_freq
                tuned_params["target_phase_frequency"] = round(float(peak_freq), 4)
                print(f"  🔍 [FFT Analysis] Dominant periodicity detected: Frequency = {peak_freq:.4f}")

    # ==========================================
    # B. TUNE Z-SCORE THRESHOLD (Kurtosis)
    # ==========================================
    if len(U_series) >= 12:
        # Calculate Excess Kurtosis (Normal distribution = 0)
        # If kurtosis is high, the data is heavy-tailed (spiky), so 3.0 sigma is too tight.
        k = kurtosis(U_series, fisher=True)
        
        base_z = float(sys_params.get("thresh_z_score", 3.0))
        
        if k > 1.0:
            # Data is leptokurtic (heavy-tailed). Relax the threshold.
            # For every unit of excess kurtosis, add 0.5 to the Z-score threshold, max 7.0.
            new_z = base_z + 0.5 * k
            new_z = min(new_z, 7.0)
            tuned_params["thresh_z_score"] = round(float(new_z), 2)
            print(f"  🌊 [Statistical Analysis] Heavy-tailed distribution detected (Kurtosis={k:.2f}). Relaxing Z-Score threshold to {new_z:.2f}")
        elif k < -1.0:
            # Data is platykurtic (flat). Tighten the threshold.
            new_z = base_z - 0.2
            new_z = max(new_z, 2.0)
            tuned_params["thresh_z_score"] = round(float(new_z), 2)
            print(f"  📊 [Statistical Analysis] Flat distribution detected (Kurtosis={k:.2f}). Tightening Z-Score threshold to {new_z:.2f}")

    # 4. Save tuned parameters
    with open(out_json, "w") as f:
        json.dump(tuned_params, f, indent=4)
        
    print(f"✅ Auto-Calibration Complete. Tuned parameters saved to ephemeral storage.")

if __name__ == "__main__":
    main()
