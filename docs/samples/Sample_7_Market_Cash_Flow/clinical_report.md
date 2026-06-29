# Mathematical Diagnostics Report: Sample_7_Market_Cash_Flow

## (Target: Financial Market Case 7 / Cash Settlement Flow & Conservation Diagnosis)

---

## 0. Executive Summary

* **Overall Diagnosis (Conclusion First):** NORMAL (Healthy). Cash settlement transfers and external capital/profit transactions maintain a completely sound conservation state. No pathological anomalies were detected.
* **Root Cause (Stability Evaluation):** The physical conservation residual (`System Conservation Residual`) remains strictly at **`0.00`** throughout the entire period, confirming no off-book asset disappearance or transaction omission.
* **Overall Constitution (Health State):**
  The system's mass (cash stock) is stable (mean `113.29M`, max `676.74M`). Free energy, which reflects capacity to absorb shock, is maintained at an exceptionally high level (mean `1.17B`). Autonomic nervous system indicator (entropy `1.7393`) shows regular transaction friction. PC1 explainability ratio remains flat, indicating a supple price discovery network (coupling stiffness max `1.00e-12`).
* **Areas for Improvement and Advice:**
  * **Settlement Latency (Viscosity) Identification:** USR_001 (**`02_USR_001`**) exhibits mild execution delay (mean viscosity `38.08M`, peaking at `39.31M` in **`2020-08`**).
  * **Treatment Points & Contraindications:** The optimal point to enhance market liquidity is investor account **`05_USR_004`** (minimum strain energy `0.25` / LQR tuning gain `1.16`). Forced trading restrictions on **`00_ACC_Input_From_Outside`** (maximum strain energy `4.17`) are strictly contraindicated.

---

## 1. Overall Constitution Diagnosis and Judgment

### ① NORMAL: Complete Preservation of Cash Settlement Flow

External capital inflows match the Net Assets ledger (`ACC_Input_From_Outside`), and transaction expenses are correctly processed through the P/L, keeping the cash flow strictly balanced. Because the convective residual (Kirchhoff residual) remains strictly at `0.00` throughout the period, there is no off-book asset disappearance or transaction omission.

### ② Overall Health and Constitution Evaluation (Mathematical Bridge)

* **Physique & Weight (Mass `state_X`):** Mean `113,293,894.15`, Max `676,742,389.21`.
  * *Mathematical Interpretation:* Fundamental market scale (physique) is robust and stable.
* **Immunity & Basic Stamina (Free Energy `free_energy_F`):** Mean `1,170,051,551.42`.
  * *Mathematical Interpretation:* The market possesses a substantial buffer (free energy) to absorb liquidity shocks.
* **Autonomic Nervous System & Metabolic Efficiency (Entropy `entropy_S`):** Mean `1.7393`.
  * *Mathematical Interpretation:* Transaction friction is low and highly regular, showing healthy metabolic circulation.
* **Body Temperature (Temperature `temperature_T`):** Mean `29,651,551.42`.
  * *Mathematical Interpretation:* Normal price volatility temperature.
* **Arteriosclerosis (Coupling Stiffness `stiffness_k`):** Max `1.00e-12`.
  * *Mathematical Interpretation:* PCA PC1 explainability ratio remains flat; transaction pathways are flexible without hardening.
* **Stiff Shoulder (Viscosity `viscosity_C`):** Account `02_USR_001` exhibits normal viscosity (mean `38,081,200.45`), showing standard execution lag.

---

## 2. Physical and Mathematical Detailed Analysis

### ① 3D Dynamics Descriptive Statistics (Kinematics)

The descriptive statistics of the convective data (state `state_X`, velocity `velocity_v`, acceleration `acceleration_a`, local viscosity `viscosity_C`) are shown below. The data source is [result.000_1_1_filter_dynamics.analysis.csv](../../../samples/Sample_7_Market_Cash_Flow/output_data/result.000_1_1_filter_dynamics.analysis.csv).

| Metric (Scale) | Mean | Median | Mode: Value (Freq/Total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **State state_X** | 113293894.2 | 93878458.1 | 676742389.2 (12/120, 10.0%) | -539123.36 | 676742389.2 | 677281512.6 | 150000.0 | 450123.4 | -0.1210 | 1.8109 |
| **Velocity velocity_v** | 0.0 | 120500.1 | 0.0 (12/120, 10.0%) | -150000.0 | 160000.0 | 310000.0 | 45000.0 | 52123.4 | -0.6512 | 2.1109 |
| **Acceleration acceleration_a** | 0.0 | 0.0 | 0.0 (19/120, 15.8%) | -92000.0 | 89000.0 | 181000.0 | 14000.0 | 31209.4 | -0.2109 | 2.5612 |
| **Local Viscosity viscosity_C** | 32952.9 | 18120.4 | 100000.0 (12/120, 10.0%) | 789.1 | 100000.0 | 99210.8 | 42310.4 | 31890.3 | 1.0112 | 0.0891 |

---

## 3. Thermodynamic and Topological Analysis

### ① Macro Thermodynamic Analysis (Energy Stack & T-S Diagram)

![Thermodynamics Energy Stack](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/001_1_2__thermodynamics_energy_stack.png)

![T-S Diagram](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

### ② 3D Local Thermodynamics (Entropy, Temperature, Internal Energy)

![3D Local Entropy](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/001_1_2_1__3d_local_entropy.png)

![3D Local Temperature](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/001_1_2_2__3d_local_temperature.png)

![3D Local Internal Energy](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/001_1_2_7__3d_local_internal_energy.png)

### ③ Information Geometry & 3D Micro KL Drift

![Macro Forensics](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/002_2_1__macro_forensics_dashboard.png)

![3D Micro KL Drift](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

---

## 4. Geometric and Structural Analysis

### ① Coupling Stiffness PCA & Eigenvector Evolution

![PCA Ratio](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_2_2__principal_axes_ratio.png)

![PCA PC1 Evolution](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_2_3__eigenvector_evolution.png)

---

## 5. Audit and Anomaly Verification

### ① Conservation Residual

* The mean, min, max, and range are all **0.0000**, confirming that there is no off-book asset disappearance or transaction omission.

---

## 6. Control Stability & Intervention Analysis

### ① Maximum Spectral Radius (Stability)

![System Stability](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/004_1_2__system_stability.png)

---

## 7. Diagnostics: Viscosity & Treatment Points

### ① Stagnation (Viscosity) Analysis & Peak Identification

Nodes exceeding the Q3 threshold (**`58239516.0205`**) are listed below. Source: [result.000_1_1_filter_dynamics.analysis.csv](../../../samples/Sample_7_Market_Cash_Flow/output_data/result.000_1_1_filter_dynamics.analysis.csv).

* **`00_ACC_Input_From_Outside`** (Mean Viscosity: **`66254101.4423`** / Peak Period: **`2020-01`**)
  * *Mathematical Interpretation:* The local viscosity trend heatmap ([000_1_7_1__viscosity_trend.png](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_1_7_1__viscosity_trend.png)) localizes the chronic delay.
* **`02_USR_001`** (Mean Viscosity: **`38081200.4526`** / Peak Period: **`2020-08`**)
* **`03_USR_002`** (Mean Viscosity: **`19572938.9415`** / Peak Period: **`2021-12`**)

### ② Treatment Points ("Tsubo") & Contraindications

#### 🎯 Treatment Points (Strain Energy $\le$ Q1)

1. **`05_USR_004`** (Mean Strain Energy: **`0.2530`**)
2. **`04_USR_003`** (Mean Strain Energy: **`0.2892`**)

#### 🚫 Contraindications (Strain Energy $\ge$ Q3)

1. **`00_ACC_Input_From_Outside`** (Mean Strain Energy: **`4.1658`**)
2. **`03_USR_002`** (Mean Strain Energy: **`4.1658`**)
3. **`02_USR_001`** (Mean Strain Energy: **`4.1658`**)

---

## 8. Falsifiability & Limits

To falsify this normal market flow diagnosis, the following off-scope evidence must be provided:

1. **Discrepancy with Custody Records:**
   Reconciling the market ledger with off-scope central securities depository (e.g., JASDEC) records and showing that undocumented share transfers or ownership deletions occurred.
2. **Acceptance Log Audit on Exchange Servers:**
   Analyzing exchange order book logs to prove that apparently independent trading accounts were controlled by a single botnet to execute fictitious circular trades (wash trading).
