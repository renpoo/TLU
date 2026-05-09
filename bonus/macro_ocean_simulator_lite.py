"""
TLU Bonus Feature: Macro Ocean Simulator (Lite Edition)
======================================================
This is a feature-limited demonstration of using the TLU Wave Mechanics Unit (WMU) 
on macroscopic financial data rather than corporate accounting data.

It treats major global indices as interacting waves in a complex phase space 
to calculate the "Systemic Tension" of the global economy.

*Note: This lite version is restricted to 6 major indices and does not include 
the advanced multi-harmonic orbital extrapolation or socioeconomic decoupling nodes.*
"""

import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import warnings

warnings.filterwarnings("ignore")
# Ensure the script can find the core engine when run from the bonus directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from src.core.wmu_engine import WMUEngine

def main():
    # Feature-Limited Node List (Basic Macro Only)
    tickers = ['SPY', 'QQQ', 'TLT', 'GLD', 'CL=F', 'UUP']
    
    print("Fetching Basic Macro Nodes (Lite Version)...")
    data = yf.download(tickers, start='2010-01-01', end='2026-05-08', progress=False)
    if isinstance(data.columns, pd.MultiIndex):
        df_A = data['Close']
    else:
        df_A = data
        
    df_A = df_A.resample('W-FRI').last().ffill().dropna()
    print(f"Data aligned. Shape: {df_A.shape}")
    
    # Initialize WMU Engine
    tickers_dict = {col: col for col in df_A.columns}
    engine = WMUEngine(tickers_dict)
    
    engine.data_A = df_A
    engine.data_V = pd.DataFrame(0, index=df_A.index, columns=df_A.columns)
    engine.t_list = df_A.columns
    
    print("Running WMU Engine...")
    Z = engine.calculate_phase_space()
    
    window = 52 # 1-year rolling
    dates = df_A.index
    results = []
    
    for i in range(window, len(dates)):
        start_date = dates[i-window]
        end_date = dates[i-1]
        Z_win = Z.loc[start_date:end_date]
        
        C = np.corrcoef(Z_win.values, rowvar=False)
        sync = np.nanmean(np.abs(np.real(C)))
        asyn = np.nanmean(np.abs(np.imag(C)))
        
        results.append({
            'Date': dates[i-1],
            'Synchronicity': sync,
            'Asynchronicity': asyn
        })
        
    df_res = pd.DataFrame(results).set_index('Date')
    
    # Simple Z-Score
    df_res['Tension'] = df_res['Asynchronicity'] - df_res['Synchronicity']
    z_score = (df_res['Tension'] - df_res['Tension'].rolling(156).mean()) / df_res['Tension'].rolling(156).std()
    
    plt.figure(figsize=(12, 5))
    plt.plot(z_score.index, z_score, label='Systemic Tension (Z-Score)', color='purple')
    plt.fill_between(z_score.index, z_score, 0, where=(z_score > 0), color='purple', alpha=0.3)
    plt.fill_between(z_score.index, z_score, 0, where=(z_score <= 0), color='red', alpha=0.3)
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title("TLU Macro Ocean Simulator (Lite Edition) - Historical Tension")
    plt.ylabel("Tension Z-Score")
    plt.grid(True)
    plt.legend()
    
    out_dir = './bonus_output'
    os.makedirs(out_dir, exist_ok=True)
    plt.savefig(f'{out_dir}/macro_ocean_lite.png')
    print(f"Done! Plot saved to {out_dir}/macro_ocean_lite.png")

if __name__ == "__main__":
    main()
