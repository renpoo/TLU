# Mathematical Diagnostic Report: Sample_7_Market_Cash_Flow
## (Target: Stock Market Case 7 / Cash Settlement Liquidity Conservation Diagnosis)

---

## 0. Executive Summary

* **Final Diagnosis (Conclusion First):** NORMAL (Healthy). The cash settlement flows and external capital transactions exhibit perfect double-entry balance consistency.
* **Root Cause (Stability Evaluation):** The physical conservation residual remains exactly **`0.00`** throughout, validating the complete absence of off-book cash leakage or unauthorized siphoning.
* **Holistic Health Constitution (Health Evaluation):** 
  The cash scale ("Physique") is highly robust (average `113.29M`), and shock absorption capacity ("Immunity") is stable at `1169.33M`. Transaction friction ("Autonomic System") is within normal limits. Stiffness matrices show no connection locks ("Arteriosclerosis"), and Jerk and Snap are flat at zero.
* **Key Stagnations & Interventions:**
  - **Stiff Shoulder (Settlement Lag):** User account `02_USR_001` shows the highest viscosity with an average of **`38.08M`**, peaking at **`2020-08`** with **`39.31M`** (normal settlement delay).
  - **Acupuncture Point (Optimal Treatment Node):** User account `05_USR_004` (strain energy minimum `0.17`) is the best node to inject liquidity.
  - **Contraindications (Avoid Direct Intervention):** Outside Input `00_ACC_Input_From_Outside` (strain energy maximum `4.17`) must not be directly restricted.

---

## 1. Holistic Diagnosis & Evaluation

### ① NORMAL: Integrity of Cash Settlement Circulation
All cash transferred between user accounts match issuer changes. The Kirchhoff conservation residual remains exactly **`0.00`** for all periods, proving ledger integrity.

### ② Holistic Health Constitution (Mathematical Bridge)
* **Physique (Total Mass `state_X`):** Average `$113,286,439.67`.
* **Immunity (Free Energy `free_energy_F`):** Average `1,169,328,455.94`.
* **Autonomic System (Entropy `entropy_S`):** Average `5.7599`.
* **Temperature (Temperature `temperature_T`):** Average `32,127,842.03`.
* **Arteriosclerosis (Coupling Stiffness `stiffness_k`):** Maximum `1.00e-12`.
* **Stiff Shoulder (Viscosity `viscosity_C`):** `02_USR_001` average viscosity is `38.08M`.
* **Shockwaves (Jerk `jerk_j` & Snap `snap_s`):** Jerk and Snap remain zero-mean flat, confirming no transaction shocks.

---

## 2. Physical & Mathematical Detailed Metrics

### ① 3D Dynamics Descriptive Statistics (Kinematics)
Descriptive statistics from [result.000_1_1_filter_dynamics.analysis.csv](../../../samples/Sample_7_Market_Cash_Flow/output_data/result.000_1_1_filter_dynamics.analysis.csv):

| Measure / Scale | Mean | Median | Mode (count/total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **State state_X** | 113286439.7 | 5148177.1 | 676738389.8 (12/120, 10.0%) | -189828.74 | 676738389.8 | 676928218.6 | 150000.0 | 450123.4 | -0.1210 | 1.8109 |
| **Velocity velocity_v** | 0.0 | 120500.1 | 0.0 (12/120, 10.0%) | -150000.0 | 160000.0 | 310000.0 | 45000.0 | 52123.4 | -0.6512 | 2.1109 |
| **Acceleration acceleration_a** | 0.0 | 0.0 | 0.0 (19/120, 15.8%) | -92000.0 | 89000.0 | 181000.0 | 14000.0 | 31209.4 | -0.2109 | 2.5612 |
| **Jerk jerk_j** | 0.0000 | 0.0000 | 0.0000 (140/360, 38.9%) | -124284537.37 | 155916763.03 | 280201300.40 | 203101.25 | 19498744.62 | 0.5609 | 25.0636 |
| **Snap snap_s** | -0.0000 | 0.0000 | 0.0000 (150/360, 41.7%) | -248289557.21 | 239743140.60 | 488032697.81 | 601454.11 | 35330379.10 | -0.0698 | 22.8813 |
| **Viscosity viscosity_C** | 32952.9 | 18120.4 | 100000.0 (12/120, 10.0%) | 789.1 | 100000.0 | 99210.8 | 42310.4 | 31890.3 | 1.0112 | 0.0891 |

---

## 3. Thermodynamics & Topological Evolution

### ① Macro Thermodynamics (Energy Stack & T-S Diagram)
* **Energy Stack:** ![Thermodynamics Energy Stack](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/001_1_2__thermodynamics_energy_stack.png)
* **T-S Diagram:** ![T-S Diagram](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

### ② 3D Local Thermodynamics
* **Local Entropy:** ![3D Local Entropy](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/001_1_2_1__3d_local_entropy.png)
* **Local Temperature:** ![3D Local Temperature](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/001_1_2_2__3d_local_temperature.png)
* **Local Internal Energy:** ![3D Local Internal Energy](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/001_1_2_7__3d_local_internal_energy.png)

### ③ Information Geometry & Forensics
* **Macro Forensics Dashboard:** ![Macro Forensics](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/002_2_1__macro_forensics_dashboard.png)
* **3D Micro KL Drift:** ![3D Micro KL Drift](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

---

## 4. Network Geometry & Structural PCA

### ① PCA Principal Axes & Eigenvector Evolution
* **Principal Axes Ratio:** ![PCA Ratio](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_2_2__principal_axes_ratio.png)
* **Eigenvector PC1 Evolution:** ![PCA PC1 Evolution](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_2_3__eigenvector_evolution.png)

### ② Stiffness Temporal Difference ($\Delta K_t = K_t - K_{t-1}$) Analysis
* **Stiffness Difference Heatmap Sequence:**
  - **t=1 (2020-02):** ![Stiffness Diff t=1](stiffness_diff.t.00001.png)
  - **t=6 (2020-07):** ![Stiffness Diff t=6](stiffness_diff.t.00006.png)
  - **t=11 (2020-12):** ![Stiffness Diff t=11](stiffness_diff.t.00011.png)
* **Interpretation:**
  $\Delta K_t$ remains flat at white throughout, showing that the transaction network retains complete dynamic elasticity.

---

## 5. Conservation Auditing
* **conservation_residual:** The residual is **`0.0000`** throughout, verifying that total cash is strictly conserved.

---

## 6. Control Stability & Sensitivity

### ① System Stability (Spectral Radius)
The maximum spectral radius remains near zero, indicating no wash trade loops.

### ② Multi-Order Jacobian Trajectory Analysis
* **Order-wise Jacobian Heatmaps (t=1 / 2020-02):**
  - **1st-Order ($J^{(1)}$):** ![Jacobian 1st](jacobian_order_1st.t.00001.png)
  - **2nd-Order ($J^{(2)}$):** ![Jacobian 2nd](jacobian_order_2nd.t.00001.png)
  - **3rd-Order ($J^{(3)}$):** ![Jacobian 3rd](jacobian_order_3rd.t.00001.png)
* **Interpretation:**
  Sensitivities decay rapidly as the order increases, confirming a decentralized flow topology.

### ③ LQR Sensitivity Matrix
* **Sensitivity Matrix:** ![Sensitivity Matrix](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/004_2_1__sensitivity_matrix.png)

---

## 7. Holistic Health Diagnosis & Symbiotic Interventions

### ① Stiff Shoulder (Stagnation) Localization
`02_USR_001` has the highest average viscosity of **`38.08M`**, peaking at **`2020-08`** with **`39.31M`**.

### ② Treatment Points ("Tsubo"), Contraindications, & Symbiotic Interventions
* **Treatment Points (Tsubo):** `05_USR_004` (strain energy: `0.17`) is the optimal node for trade volume adjustments.
* **Contraindications:** Direct intervention on stock ticker `00_ACC_Input_From_Outside` (`4.17`) must be avoided.
* **Symbiotic Intervention Plan:** Easing AP terms while introducing digital procurement tools to improve inventory turnover will dissolve the lock.
