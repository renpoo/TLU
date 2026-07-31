# Mathematical Diagnostic Report: Sample_2_Embezzlement_Leak
## (Target: Accounting Case 2 / Embezzlement Leak Diagnosis)

---

## 0. Executive Summary

* **Final Diagnosis (Conclusion First):** CRITICAL (Off-Book Mass Leakage / Embezzlement). Capital is siphoned out of the system without registration.
* **Root Cause (Stability Evaluation):** A terminal sink (`UNKNOWN_LEAK`) has siphoned a total of **`$6,255.99`** starting at **t=4 (2020-05)**. Maximum leak occurs at **t=8 (2020-09)** with a residual spike of **`$4,773.57`**.
* **Holistic Health Constitution (Health Evaluation):** 
  The B/S scale ("Physique") is declining due to off-book leakage, with a cumulative conservation residual of `$6,255.99`. Autonomic system is highly disturbed ("Entropy" average `1.5804` represents abnormal flow). Stiffness lock develops on the `Cash` → `UNKNOWN_LEAK` edge. 3rd-order Jacobian maps the siphoned flow to the Terminal Sink.
* **Key Stagnations & Interventions:**
  - **Stiff Shoulder (Settlement Lag):** Cash (`03_ACC_Cash`) shows the highest viscosity with an average of **`46085.30`**, peaking at **`2020-06`** with **`48161.87`**.
  - **Acupuncture Point (Optimal Treatment Node):** Cash (`03_ACC_Cash` / strain energy minimum `1.60`) is the best node to dissolve the lock.
  - **Contraindications (Avoid Direct Intervention):** Leak node (`09_UNKNOWN_LEAK` / strain energy maximum `8.34`) must not be adjusted directly.

---

## 1. Holistic Diagnosis & Evaluation

### ① CRITICAL: Active Capital Leakage (Embezzlement)
The double-entry bookkeeping balances show a total residual leakage of `$6,255.99`. The conservation residual is non-zero, mathematically proving that capital has siphoned out of the system.

### ② Holistic Health Constitution (Mathematical Bridge)
* **Physique (Total Mass `state_X`):** Average `$181818.18` (declining).
* **Immunity (Free Energy `free_energy_F`):** Average `3126535.00` (rapidly depleting).
* **Autonomic System (Entropy `entropy_S`):** Average `1.5804`.
* **Temperature (Temperature `temperature_T`):** Average `245043.44` (abnormal friction heat).
* **Arteriosclerosis (Coupling Stiffness `stiffness_k`):** Maximum `1.02e-09` (severe local stiffness lock).
* **Stiff Shoulder (Viscosity `viscosity_C`):** `03_ACC_Cash` average viscosity is `46085.30`.
* **Shockwaves (Jerk `jerk_j` & Snap `snap_s`):** Jerk and Snap spike at t=4 (onset) and t=8 (maximum leak) as the siphoning path activates.

---

## 2. Physical & Mathematical Detailed Metrics

### ① 3D Dynamics Descriptive Statistics (Kinematics)
Descriptive statistics from [result.000_1_1_filter_dynamics.analysis.csv](../../../samples/Sample_2_Embezzlement_Leak/output_data/result.000_1_1_filter_dynamics.analysis.csv):

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
* **Energy Stack:** ![Thermodynamics Energy Stack](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_2__thermodynamics_energy_stack.png)
* **T-S Diagram:** ![T-S Diagram](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

### ② 3D Local Thermodynamics
* **Local Entropy:** ![3D Local Entropy](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_2_1__3d_local_entropy.png)
* **Local Temperature:** ![3D Local Temperature](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_2_2__3d_local_temperature.png)
* **Local Internal Energy:** ![3D Local Internal Energy](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_2_7__3d_local_internal_energy.png)

### ③ Information Geometry & Forensics
* **Macro Forensics Dashboard:** ![Macro Forensics](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png)
* **3D Micro KL Drift:** ![3D Micro KL Drift](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

---

## 4. Network Geometry & Structural PCA

### ① PCA Principal Axes & Eigenvector Evolution
* **Principal Axes Ratio:** ![PCA Ratio](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_2__principal_axes_ratio.png)
* **Eigenvector PC1 Evolution:** ![PCA PC1 Evolution](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_3__eigenvector_evolution.png)

### ② Stiffness Temporal Difference ($\Delta K_t = K_t - K_{t-1}$) Analysis
* **Stiffness Difference Heatmap Sequence:**
  - **t=1 (2020-02):** ![Stiffness Diff t=1](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_4__stiffness_diff.t.00001.png)
  - **t=4 (2020-05):** ![Stiffness Diff t=4](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_4__stiffness_diff.t.00004.png)
  - **t=11 (2020-12):** ![Stiffness Diff t=11](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_4__stiffness_diff.t.00011.png)
* **Interpretation:**
  Red stiffness difference spikes at t=4 show the active establishment of the leak bypass, locking into a static lock (white) in later periods.

---

## 5. Conservation Auditing
* **conservation_residual:** The residual is non-zero, confirming off-book siphoning:
  - 2020-06-05 (t=5): **`$280.50`** (ID: `E_001654` / Cash Leak)
  - 2020-07-29 (t=6): **`$320.10`**
  - 2020-08-09 (t=7): **`$440.35`**
  - 2020-08-10 (t=7): **`$120.40`**
  - 2020-08-30 (t=7): **`$321.07`**
  - 2020-09-29 (t=8): **`$4,773.57`** (Maximum Leak)
  - **Total Cumulative Leak:** **`$6,255.99`**

---

## 6. Control Stability & Sensitivity

### ① System Stability (Spectral Radius)
The maximum spectral radius $\rho$ remains **`0.7861`** for all periods, indicating active feedback loops.

### ② Multi-Order Jacobian Trajectory Analysis
* **Order-wise Jacobian Heatmaps (t=4 / 2020-05):**
  - **1st-Order ($J^{(1)}$):** ![Jacobian 1st](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/jacobian_order_1st.t.00004.png)
  - **2nd-Order ($J^{(2)}$):** ![Jacobian 2nd](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/jacobian_order_2nd.t.00004.png)
  - **3rd-Order ($J^{(3)}$):** ![Jacobian 3rd](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/jacobian_order_3rd.t.00004.png)
* **Interpretation:**
  Non-zero sensitivity exists in 1st/2nd orders but drops to exactly zero in 3rd order, confirming `UNKNOWN_LEAK` acts as a Terminal Sink.

### ③ LQR Sensitivity Matrix
* **Sensitivity Matrix:** ![Sensitivity Matrix](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/004_2_1__sensitivity_matrix.png)

---

## 7. Holistic Health Diagnosis & Symbiotic Interventions

### ① Stiff Shoulder (Stagnation) Localization
`03_ACC_Cash` (Cash) has the highest average viscosity of **`46085.30`**, peaking at **`2020-06`** with **`48161.87`**.

### ② Treatment Points ("Tsubo"), Contraindications, & Symbiotic Interventions
* **Treatment Points (Tsubo):** `03_ACC_Cash` (strain energy: `1.60`) and `01_ACC_Accounts_Receivable` (`1.77`).
* **Contraindications:** Direct intervention on `09_UNKNOWN_LEAK` (`8.34`) must be avoided.
* **Symbiotic Intervention Plan:** Easing AP terms while introducing digital collaboration tools to improve inventory turnover will dissolve the lock.
