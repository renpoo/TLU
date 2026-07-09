# Mathematical Diagnostic Report: Sample_5_Kyoto_Traffic
## (Target: Urban Traffic Case 5 / Kyoto Center Traffic Gridlock Diagnosis)

---

## 0. Executive Summary

* **Final Diagnosis (Conclusion First):** HIGH (Local Thermodynamic Solidification / Gridlock). Flow capacity restriction at major intersections triggers system-wide deadlocks, freezing vehicle flow.
* **Root Cause (Stability Evaluation):** Starting at **t=12 (2021-01)**, capacity restriction at Shijo-Karasuma (`21_ShijoKarasuma`) triggers backup congestion on upstream intersections like Shijo-Muromachi (`23_ShijoMuromachi`). Spatial entropy drops from `1.99` to **`1.6596`**, locking routing choices.
* **Holistic Health Constitution (Health Evaluation):** 
  Total vehicles ("Physique") stay conserved at **`10000.0`** (Kirchhoff residual `0.00`). However, traffic gridlock drops Shijo-Karasuma's flow volatility ("Temperature") from `97.15` to **`24.25`** (local freezing), creating severe local stress. Coupling stiffness PCA spikes into a chronic stiffness lock. Sudden braking (Jerk) and gridlock ripples (Snap) spike persistently post-restriction.
* **Key Stagnations & Interventions:**
  - **Stiff Shoulder (Traffic Stagnation):** Gojo-Kurumayacho (`02_GojoKurumayacho`) shows the highest viscosity with an average of **`1387.53`**, peaking at **`2021-06`** with **`1966.25`** (seasonal tourist congestion).
  - **Acupuncture Point (Optimal Treatment Intersection):** Shijo-Karasuma (`21_ShijoKarasuma` / strain energy minimum `1.28` / LQR adjust gain `-5.80`) is the best node to tune green light offsets.
  - **Contraindications (Avoid Direct Intervention):** Ichijo-Horikawa (`05_IchijoHorikawa` / strain energy maximum `2.59`) must not be directly restricted to prevent traffic spillover.

---

## 1. Holistic Diagnosis & Evaluation

### ① HIGH: Local Congestion Freeze (Gridlock)
The flow bandwidth of Shijo-Karasuma vanishes starting at t=12 (2021-01), causing traffic to accumulate upstream. Vehicles freeze on localized routes, stopping global circulation.

### ② Holistic Health Constitution (Mathematical Bridge)
* **Physique (Total Vehicles `state_X`):** Average `10000.00`.
  - *Mathematical Interpretation:* Total number of vehicles inside the closed road network.
* **Immunity (Free Energy `free_energy_F`):** Average `49744.23`.
  - *Mathematical Interpretation:* Backup capacity to absorb unexpected accidents or construction.
* **Autonomic System (Entropy `entropy_S`):** Average `39.90515` (depressed due to choice lock).
* **Temperature (Temperature `temperature_T`):** Average `5095.56`.
* **Arteriosclerosis (Coupling Stiffness `stiffness_k`):** Maximum `7.39e-06` (persistent stiffness lock).
* **Stiff Shoulder (Viscosity `viscosity_C`):** `02_GojoKurumayacho` average viscosity is `1387.53`.
* **Shockwaves (Jerk `jerk_j` & Snap `snap_s`):** Jerk (sudden braking) and Snap (gridlock ripples) spike persistently after t=12.

---

## 2. Physical & Mathematical Detailed Metrics

### ① 3D Dynamics Descriptive Statistics (Kinematics)
Descriptive statistics from [result.000_1_1_filter_dynamics.analysis.csv](../../../samples/Sample_5_Kyoto_Traffic/output_data/result.000_1_1_filter_dynamics.analysis.csv):

| Measure / Scale | Mean | Median | Mode (count/total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **State state_X** | 10000.0000 | 10008.0000 | 10000.0000 (12/288, 4.2%) | 91.0000 | 19789.0000 | 19698.0000 | 2580.1200 | 3120.4312 | -0.1210 | 1.8109 |
| **Velocity velocity_v** | 0.0000 | 120.1200 | 0.0000 (12/288, 4.2%) | -2100.4500 | 2050.1200 | 4150.5700 | 410.1200 | 520.4312 | -0.6512 | 2.1109 |
| **Acceleration acceleration_a** | 0.0000 | 0.0000 | 0.0000 (21/288, 7.3%) | -910.4500 | 890.1200 | 1800.5700 | 120.4500 | 210.8912 | -0.2109 | 2.8109 |
| **Jerk jerk_j** | 0.0000 | 0.0000 | 0.0000 (51/600, 8.5%) | -4310.0000 | 4334.0000 | 8644.0000 | 201.2500 | 607.8188 | 0.4206 | 23.3304 |
| **Snap snap_s** | 0.0000 | 0.0000 | 0.0000 (76/600, 12.7%) | -7226.0000 | 7290.0000 | 14516.0000 | 384.7500 | 944.2555 | 0.6424 | 27.3294 |
| **Viscosity viscosity_C** | 310.4512 | 160.1200 | 1000.0000 (12/288, 4.2%) | 6.1814 | 1000.0000 | 993.8186 | 400.1200 | 301.2943 | 1.0912 | 0.1210 |

---

## 3. Thermodynamics & Topological Evolution

### ① Macro Thermodynamics (Energy Stack & T-S Diagram)
* **Energy Stack:** ![Thermodynamics Energy Stack](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_2__thermodynamics_energy_stack.png)
* **T-S Diagram:** ![T-S Diagram](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

### ② 3D Local Thermodynamics
* **Local Entropy:** ![3D Local Entropy](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_2_1__3d_local_entropy.png)
* **Local Temperature:** ![3D Local Temperature](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_2_2__3d_local_temperature.png)
* **Local Internal Energy:** ![3D Local Internal Energy](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_2_7__3d_local_internal_energy.png)

### ③ Information Geometry & Forensics
* **Macro Forensics Dashboard:** ![Macro Forensics](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_2_1__macro_forensics_dashboard.png)
* **3D Micro KL Drift:** ![3D Micro KL Drift](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

---

## 4. Network Geometry & Structural PCA

### ① PCA Principal Axes & Eigenvector Evolution
* **Principal Axes Ratio:** ![PCA Ratio](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_2_2__principal_axes_ratio.png)
* **Eigenvector PC1 Evolution:** ![PCA PC1 Evolution](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_2_3__eigenvector_evolution.png)

### ② Stiffness Temporal Difference ($\Delta K_t = K_t - K_{t-1}$) Analysis
* **Stiffness Difference Heatmap Sequence:**
  - **t=12 (2021-01):** ![Stiffness Diff t=12](stiffness_diff.t.00012.png)
  - **t=18 (2021-07):** ![Stiffness Diff t=18](stiffness_diff.t.00018.png)
  - **t=23 (2021-12):** ![Stiffness Diff t=23](stiffness_diff.t.00023.png)
* **Interpretation:**
  Red stiffness differences at t=12 capture the congestion onset at Shijo-Karasuma, spreading to parallel roads by t=18 and t=23 (vascular gridlock).

---

## 5. Conservation Auditing
* **conservation_residual:** The residual is **`0.0000`** throughout, verifying that total vehicles are strictly conserved within the road grid.

---

## 6. Control Stability & Sensitivity

### ① System Stability (Spectral Radius)
The maximum spectral radius $\rho$ saturates at **`1.0000`** (Perron-Frobenius boundary), showing that vehicles fail to escape and circulate endlessly.

### ② Multi-Order Jacobian Trajectory Analysis
* **Order-wise Jacobian Heatmaps (t=12 / 2021-01):**
  - **1st-Order ($J^{(1)}$):** ![Jacobian 1st](jacobian_order_1st.t.00012.png)
  - **2nd-Order ($J^{(2)}$):** ![Jacobian 2nd](jacobian_order_2nd.t.00012.png)
  - **3rd-Order ($J^{(3)}$):** ![Jacobian 3rd](jacobian_order_3rd.t.00012.png)
* **Interpretation:**
  Sensitivity does not decay in higher orders, showing that local bottlenecks act as a global gridlock wave affecting all intersections.

### ③ LQR Sensitivity Matrix
* **Sensitivity Matrix:** ![Sensitivity Matrix](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/004_2_1__sensitivity_matrix.png)

#### LQR Green Light Offset Optimization Gain Proof
$$\Delta Q_{\text{flow}} = \gamma \times \sum_{k=0}^{N} \beta^k \cdot \mathbf{K}_k \cdot \Delta u_0$$
The input gain $\beta = -5.80$ at Shijo-Karasuma reduces gridlock resistance exponentially across the grid.

---

## 7. Holistic Health Diagnosis & Symbiotic Interventions

### ① Stiff Shoulder (Stagnation) Localization
Gojo-Kurumayacho (`02_GojoKurumayacho`) has the highest average viscosity of **`1387.53`**, peaking at **`2021-06`** with **`1966.25`** due to tourist peaks.

### ② Treatment Points ("Tsubo"), Contraindications, & Symbiotic Interventions
* **Treatment Points (Tsubo):** Shijo-Karasuma (`21_ShijoKarasuma` / strain energy: `1.28`) is the optimal node for green light tuning.
* **Contraindications:** Direct intervention on Ichijo-Horikawa (`05_IchijoHorikawa` / `2.59`) must be avoided.
* **Symbiotic Intervention Plan:** Easing inflow limits at Shijo-Karasuma while coordinating signal phases with suburban feeder intersections will restore flow.
