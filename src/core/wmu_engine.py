"""
Wave Mechanics Utility (WMU) Core Engine
----------------------------------------
A thermodynamic and kinematic framework for macroscopic financial network analysis.
Converts asset state (Capitalization) and velocity (Transaction Flux) into 
complex phase space to identify systemic externalities (Leaders/Laggards).
"""

import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import numpy.lib.scimath as sm
import os
import time
import warnings
warnings.filterwarnings('ignore')

class WMUEngine:
    def __init__(self, tickers_dict):
        """
        Initialize the WMU Engine with a dictionary of {Ticker: Label}.
        """
        self.tickers_dict = tickers_dict
        self.t_list = list(tickers_dict.keys())
        self.data_A = None
        self.data_V = None
        self.Z = None
        
    def fetch_data(self, start_date, end_date, interval="1wk"):
        """Downloads historical data and calculates A (State) and V (Velocity)."""
        print(f"Fetching data for {len(self.t_list)} nodes from {start_date} to {end_date}...")
        data = yf.download(self.t_list, start=start_date, end=end_date, interval=interval, progress=False)
        
        if isinstance(data.columns, pd.MultiIndex):
            closes = data['Close']
            volumes = data['Volume']
        else:
            closes = pd.DataFrame(data['Close'])
            volumes = pd.DataFrame(data['Volume'])
            
        closes = closes.ffill().fillna(0)
        volumes = volumes.fillna(0)
        
        shares = {}
        for t in self.t_list:
            try:
                shares[t] = yf.Ticker(t).info.get('sharesOutstanding', 1e9)
            except:
                shares[t] = 1e9
            time.sleep(0.05)
            
        self.data_A = pd.DataFrame(index=closes.index)
        self.data_V = pd.DataFrame(index=closes.index)
        
        for t in self.t_list:
            if t in closes.columns and t in volumes.columns:
                self.data_A[t] = (closes[t] * shares[t]) / 1e9
                self.data_V[t] = (closes[t] * volumes[t]) / 1e9
                
        print("Data extraction complete.")
        
    def load_local_data(self, df_A, df_V=None):
        """Loads local DataFrames for State (A) and Velocity (V) directly."""
        print(f"Loading local data for {len(self.t_list)} nodes...")
        self.data_A = df_A[self.t_list].copy()
        
        if df_V is not None:
            self.data_V = df_V[self.t_list].copy()
        else:
            # If no volume/velocity provided (like macro rates), assume V=0 to trigger pure imaginary phase
            self.data_V = pd.DataFrame(0, index=self.data_A.index, columns=self.t_list)
            
        print("Local data injection complete.")
                
    def calculate_phase_space(self):
        """Transforms A and V into the complex Z domain."""
        if self.data_A is None or self.data_V is None:
            raise ValueError("Must run fetch_data first.")
            
        A_dot = self.data_A.diff().fillna(0)
        D = (self.data_V ** 2) - (A_dot ** 2)
        
        # Safe division for non-existent nodes (A=0)
        # If A=0, omega=0, phi=0, Z=0.
        A_safe = self.data_A.copy()
        A_safe[A_safe == 0] = np.inf
        
        omega = sm.sqrt(D) / A_safe
        phi = omega.cumsum()
        self.Z = self.data_A * np.exp(1j * phi)
        return self.Z
        
    def analyze_era(self, start_eval, end_eval):
        """Calculates the imaginary correlation matrix for a specific timeframe."""
        Z_era = self.Z.loc[start_eval:end_eval]
        Z_era = Z_era.replace([np.inf, -np.inf], np.nan).fillna(0)
        Z_era = Z_era.loc[:, (Z_era != 0).any(axis=0)]
        
        Z_centered = Z_era - Z_era.mean()
        C = np.dot(Z_centered.T, np.conj(Z_centered)) / (len(Z_centered) - 1)
        
        variances = np.diag(C).real.copy()
        variances[variances == 0] = 1e-10
        std_devs = np.sqrt(variances)
        Corr = C / np.outer(std_devs, std_devs)
        
        Imag_Corr = pd.DataFrame(np.imag(Corr), index=Z_era.columns, columns=Z_era.columns)
        Imag_Corr = Imag_Corr.replace([np.inf, -np.inf], np.nan).fillna(0)
        Imag_Corr = Imag_Corr.loc[(Imag_Corr != 0).any(axis=1), (Imag_Corr != 0).any(axis=0)]
        
        labels = [f"{self.tickers_dict.get(t, t)}" for t in Imag_Corr.columns]
        Imag_Corr.columns = labels
        Imag_Corr.index = labels
        
        return Imag_Corr
        
    def plot_matrix(self, Imag_Corr, title, filename):
        """Generates the thermodynamic clustermap."""
        plt.style.use('dark_background')
        g = sns.clustermap(Imag_Corr, cmap='coolwarm', center=0, 
                           figsize=(14, 12), annot=False, 
                           cbar_kws={'label': 'Thermodynamic Phase Difference'})
        g.fig.suptitle(title, fontsize=18, fontweight='bold', color='white', y=1.02)
        ax = g.ax_heatmap
        ax.tick_params(axis='both', colors='white', labelsize=9)
        
        os.makedirs('output_plots', exist_ok=True)
        out_path = f'output_plots/{filename}.png'
        g.savefig(out_path, dpi=300)
        print(f"Matrix saved to {out_path}")
        return g

    def generate_report(self, Imag_Corr):
        """Extracts and prints Leaders and Laggards."""
        lead_scores = Imag_Corr.sum(axis=1).sort_values(ascending=False)
        print("\n=== SYSTEMIC LEADERS (Heat Generators / Origin of Externality) ===")
        for idx, val in lead_scores.head(10).items():
            print(f"{idx.ljust(35)} : {val:.2f}")
            
        print("\n=== SYSTEMIC LAGGARDS (Sinks / Victims of Externality) ===")
        for idx, val in lead_scores.tail(10).items():
            print(f"{idx.ljust(35)} : {val:.2f}")
