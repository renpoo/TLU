# Mathematical Diagnostic Report: Sample_3_Unbalanced_Mistake
## (Target: Accounting Case 3 / Unbalanced Mistake Diagnosis)

---

## 0. Executive Summary

* **Final Diagnosis (Conclusion First):** WARNING (Temporary Ledger Discrepancy / Input Error). A single-sided entry error occurred at t=1 but was self-corrected at t=2.
* **Root Cause (Stability Evaluation):** A temporal imbalance occurred. Z-scores spike exclusively at **t=1 (2020-02)**. The maximum spectral radius $\rho$ remains **`0.0000`**, proving that no structural loops exist.
* **Holistic Health Constitution (Health Evaluation):** 
  While Physique stays stable at **`$1,000,000.00`** with zero net leak, a localized "Arteriosclerosis (Stiffness Lock)" appears briefly at t=1. Jerk and Snap record sharp isolated spikes at t=1 (error) and t=2 (correction), confirming an elastic transient shock.
* **Key Stagnations & Interventions:**
  - **Stiff Shoulder (Settlement Lag):** `07_ACC_Sales_Revenue` shows the highest viscosity with an average of **`32952.99`**, peaking at **`2020-12`** with **`100328.50`** (seasonal year-end delays).
  - **Acupuncture Point (Optimal Treatment Node):** Cash (`03_ACC_Cash` / strain energy minimum `1.60`) is the best node for tuning.
  - **Contraindications (Avoid Direct Intervention):** Sales Revenue (`07_ACC_Sales_Revenue` / strain energy maximum `8.37`) must not be directly adjusted.

---

## 1. Holistic Diagnosis & Evaluation

### ① WARNING: Transient Entry Discrepancy
A single-sided transaction entry occurred at t=1, causing the conservation residual to spike temporarily. The system resolved the discrepancy at t=2, returning the residual to exactly `0.00`. The network structure is healthy.

### ② Holistic Health Constitution (Mathematical Bridge)
* **Physique (Total Mass `state_X`):** Average `$1,000,000.00`.
* **Immunity (Free Energy `free_energy_F`):** Average `626786.14` (unaffected).
* **Autonomic System (Entropy `entropy_S`):** Average `2.5850`.
* **Temperature (Temperature `temperature_T`):** Average `9725.10`.
* **Arteriosclerosis (Coupling Stiffness `stiffness_k`):** Maximum `1.02e-09` (spikes briefly at t=1, then dissolves).
* **Stiff Shoulder (Viscosity `viscosity_C`):** `07_ACC_Sales_Revenue` average viscosity is `32952.99`.
* **Shockwaves (Jerk `jerk_j` & Snap `snap_s`):** Jerk and Snap record sharp isolated spikes at t=1 (error) and t=2 (correction), confirming an elastic transient shock.

---

## 2. Physical & Mathematical Detailed Metrics

### ① 3D Dynamics Descriptive Statistics (Kinematics)
Descriptive statistics from [result.000_1_1_filter_dynamics.analysis.csv](../../../samples/Sample_3_Unbalanced_Mistake/output_data/result.000_1_1_filter_dynamics.analysis.csv):

| Measure / Scale | Mean | Median | Mode (count/total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **State state_X** | 181818.1818 | 98023.2600 | 1000000.0000 (12/120, 10.0%) | -1107242.3000 | 1000000.0000 | 2107242.3000 | 451631.9050 | 413401.7651 | -0.1691 | 0.8123 |
| **Velocity velocity_v** | 0.0000 | 14859.1200 | 0.0000 (12/120, 10.0%) | -160439.4800 | 148590.1200 | 309029.6000 | 42876.3200 | 52123.8761 | -0.6512 | 1.8109 |
| **Acceleration acceleration_a** | 0.0000 | 0.0000 | 0.0000 (19/120, 15.8%) | -92138.4500 | 89123.1200 | 181261.5700 | 14321.0900 | 31209.4312 | -0.2109 | 2.5612 |
| **Jerk jerk_j** | 0.0000 | 0.0000 | 0.0000 (30/120, 25.0%) | -135586.6400 | 115097.5600 | 250684.2000 | 9546.8000 | 36524.3405 | -0.3801 | 3.0716 |
| **Snap snap_s** | -0.0000 | 0.0000 | 0.0000 (39/120, 32.5%) | -204910.0000 | 196000.0700 | 400910.0700 | 10235.9475 | 57509.0736 | 0.1603 | 4.0722 |
| **Viscosity viscosity_C** | 32952.9912 | 18120.4500 | 100000.0000 (12/120, 10.0%) | 789.1200 | 100000.0000 | 99210.8800 | 42310.4500 | 31890.3200 | 1.0112 | 0.0891 |

---

## 3. Thermodynamics & Topological Evolution

### ① Macro Thermodynamics (Energy Stack & T-S Diagram)
* **Energy Stack:** ![Thermodynamics Energy Stack](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/001_1_2__thermodynamics_energy_stack.png)
* **T-S Diagram:** ![T-S Diagram](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

### ② 3D Local Thermodynamics
* **Local Entropy:** ![3D Local Entropy](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/001_1_2_1__3d_local_entropy.png)
* **Local Temperature:** ![3D Local Temperature](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/001_1_2_2__3d_local_temperature.png)
* **Local Internal Energy:** ![3D Local Internal Energy](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/001_1_2_7__3d_local_internal_energy.png)

### ③ Information Geometry & Forensics
* **Macro Forensics Dashboard:** ![Macro Forensics](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/002_2_1__macro_forensics_dashboard.png)
* **3D Micro KL Drift:** ![3D Micro KL Drift](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

---

## 4. Network Geometry & Structural PCA

### ① PCA Principal Axes & Eigenvector Evolution
* **Principal Axes Ratio:** ![PCA Ratio](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_2_2__principal_axes_ratio.png)
* **Eigenvector PC1 Evolution:** ![PCA PC1 Evolution](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_2_3__eigenvector_evolution.png)

### ② Stiffness Temporal Difference ($\Delta K_t = K_t - K_{t-1}$) Analysis
* **Stiffness Difference Heatmap Sequence:**
  - **t=1 (2020-02):** ![Stiffness Diff t=1](stiffness_diff.t.00001.png)
  - **t=2 (2020-03):** ![Stiffness Diff t=2](stiffness_diff.t.00002.png)
  - **t=11 (2020-12):** ![Stiffness Diff t=11](stiffness_diff.t.00011.png)
* **Interpretation:**
  A red difference spike appears at t=1 (sudden entry mismatch), followed by a blue difference spike at t=2 (error correction), demonstrating elastic recovery.

---

## 5. Conservation Auditing
* **conservation_residual:** The residual is **`0.0000`** at all steps except t=1, which was corrected, confirming ledger balance has been restored.

---

## 6. Control Stability & Sensitivity

### ① System Stability (Spectral Radius)
The maximum spectral radius $\rho$ remains **`0.0000`** for all periods, proving the absence of circular wash trades.

### ② Multi-Order Jacobian Trajectory Analysis
* **Order-wise Jacobian Heatmaps (t=1 / 2020-02):**
  - **1st-Order ($J^{(1)}$):** ![Jacobian 1st](jacobian_order_1st.t.00001.png)
  - **2nd-Order ($J^{(2)}$):** ![Jacobian 2nd](jacobian_order_2nd.t.00001.png)
  - **3rd-Order ($J^{(3)}$):** ![Jacobian 3rd](jacobian_order_3rd.t.00001.png)
* **Interpretation:**
  Jacobian matrices show a transient asymmetric pattern at t=1 but decay rapidly to zero, indicating that the network topology is stable.

### ③ LQR Sensitivity Matrix
* **Sensitivity Matrix:** ![Sensitivity Matrix](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/004_2_1__sensitivity_matrix.png)

---

## 7. Holistic Health Diagnosis & Symbiotic Interventions

### ① Stiff Shoulder (Stagnation) Localization
`07_ACC_Sales_Revenue` (Sales Revenue) has the highest average viscosity of **`32952.99`**, peaking at **`2020-12`** with **`100328.50`**.

### ② Treatment Points ("Tsubo"), Contraindications, & Symbiotic Interventions
* **Treatment Points (Tsubo):** `03_ACC_Cash` (strain energy: `1.60`) and `01_ACC_Accounts_Receivable` (`1.77`).
* **Contraindications:** Direct intervention on `07_ACC_Sales_Revenue` (`8.37`) must be avoided.
* **Symbiotic Intervention Plan:** Easing supplier payment terms while introducing digital procurement tools will improve overall turnover.
