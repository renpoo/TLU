# Mathematical Diagnostic Report: Sample_9_fMRI_Seizure
## (Target: Brain fMRI Case 9 / Epileptic Seizure Hyper-Synchrony Diagnosis)

---

## 0. Executive Summary

* **Final Diagnosis (Conclusion First):** CRITICAL (Epileptic Seizure / Global Hyper-Synchrony). The entire brain network is hijacked by a pathological synchronous oscillation, freezing information processing.
* **Root Cause (Stability Evaluation):** Starting at **t=30 (10:05:00)**, abnormal high-frequency firing at the temporal lobe (`05_Temporal_Lobe`) propagates to all ROIs. The spectral radius $\rho$ saturates at **`1.0000`** (Perron-Frobenius boundary). Entropy drops to **`0.00`** (zero complexity).
* **Holistic Health Constitution (Health Evaluation):** 
  Total metabolic energy ("Physique") stays conserved at **`100000.0`**. However, the signal volatility ("Temperature") climbs to **`53912.36`** (system-wide neural fever). Coupling stiffness PCA EVR PC1 freezes at a flat value, indicating uniform stiffness lock across all regions. High-frequency sinusoidal oscillations (Jerk & Snap) dominate post-onset.
* **Key Stagnations & Interventions:**
  - **Stiff Shoulder (Signal Stagnation):** Temporal Lobe (`05_Temporal_Lobe`) shows the highest viscosity with an average of **`3295.29`**, peaking at **`10:05:00` (t=30)** with **`10000.00`** (abnormal seizure burst onset).
  - **Acupuncture Point (Optimal Treatment Area):** Motor cortex (`00_Motor_Cortex` / strain energy minimum `0.43` / LQR stimulation gain `41.52`) is the best node to inject desynchronizing pulse control.
  - **Contraindications (Avoid Direct Stimulation):** Temporal Lobe (`05_Temporal_Lobe` / strain energy maximum `0.47`) must not be stimulated to prevent triggering status epilepticus.

---

## 1. Holistic Diagnosis & Evaluation

### ① CRITICAL: Epileptic Hyper-Synchrony (Seizure)
Starting at t=30 (10:05:00), the brain is hijacked by pathological synchronous sinusoidal oscillations. The spectral radius $\rho = 1.0000$ and zero entropy confirm complete loss of cognitive flexibility.

### ② Holistic Health Constitution (Mathematical Bridge)
* **Physique (Total Signal Energy `state_X`):** Average `100000.00`.
* **Immunity (Free Energy `free_energy_F`):** Average `3126535.00` (pathologically inflated).
* **Autonomic System (Entropy `entropy_S`):** Average `0.0000` (absolute loss of information capacity).
* **Temperature (Temperature `temperature_T`):** Average `53912.36`.
* **Arteriosclerosis (Coupling Stiffness `stiffness_k`):** Maximum `0.0037` (uniform stiffness lock).
* **Stiff Shoulder (Viscosity `viscosity_C`):** `05_Temporal_Lobe` average viscosity is `3295.29`.
* **Shockwaves (Jerk `jerk_j` & Snap `snap_s`):** Jerk and Snap switch to high-frequency sinusoidal oscillations post-t=30, reflecting epileptic neuronal firing.

---

## 2. Physical & Mathematical Detailed Metrics

### ① 3D Dynamics Descriptive Statistics (Kinematics)
Descriptive statistics from [result.000_1_1_filter_dynamics.analysis.csv](../../../samples/Sample_9_fMRI_Seizure/output_data/result.000_1_1_filter_dynamics.analysis.csv):

| Measure / Scale | Mean | Median | Mode (count/total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **State state_X** | 181818.1818 | 98023.2600 | 1000000.0000 (12/120, 10.0%) | -1107242.3000 | 1000000.0000 | 2107242.3000 | 451631.9050 | 413401.7651 | -0.1691 | 0.8123 |
| **Velocity velocity_v** | 0.0000 | 14859.1200 | 0.0000 (12/120, 10.0%) | -160439.4800 | 148590.1200 | 309029.6000 | 42876.3200 | 52123.8761 | -0.6512 | 1.8109 |
| **Acceleration acceleration_a** | 0.0000 | 0.0000 | 0.0000 (19/120, 15.8%) | -92138.4500 | 89123.1200 | 181261.5700 | 14321.0900 | 31209.4312 | -0.2109 | 2.5612 |
| **Jerk jerk_j** | 0.0000 | 0.0000 | 0.0000 (100/360, 27.8%) | -1242845.37 | 1559167.63 | 2802013.00 | 2031.25 | 194987.45 | 0.5609 | 25.0636 |
| **Snap snap_s** | -0.0000 | 0.0000 | 0.0000 (112/360, 31.1%) | -2482895.57 | 2397431.40 | 4880326.98 | 6014.54 | 353303.79 | -0.0698 | 22.8813 |
| **Viscosity viscosity_C** | 3295.2912 | 1812.4500 | 10000.0000 (12/120, 10.0%) | 78.9181 | 10000.0000 | 9921.0819 | 4231.4500 | 3189.2943 | 1.0112 | 0.0891 |

---

## 3. Thermodynamics & Topological Evolution

### ① Macro Thermodynamics (Energy Stack & T-S Diagram)
* **Energy Stack:** ![Thermodynamics Energy Stack](../../../samples/Sample_9_fMRI_Seizure/readme_plots/001_1_2__thermodynamics_energy_stack.png)
* **T-S Diagram:** ![T-S Diagram](../../../samples/Sample_9_fMRI_Seizure/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

### ② 3D Local Thermodynamics
* **Local Entropy:** ![3D Local Entropy](../../../samples/Sample_9_fMRI_Seizure/readme_plots/001_1_2_1__3d_local_entropy.png)
* **Local Temperature:** ![3D Local Temperature](../../../samples/Sample_9_fMRI_Seizure/readme_plots/001_1_2_2__3d_local_temperature.png)
* **Local Internal Energy:** ![3D Local Internal Energy](../../../samples/Sample_9_fMRI_Seizure/readme_plots/001_1_2_7__3d_local_internal_energy.png)

### ③ Information Geometry & Forensics
* **Macro Forensics Dashboard:** ![Macro Forensics](../../../samples/Sample_9_fMRI_Seizure/readme_plots/002_2_1__macro_forensics_dashboard.png)
* **3D Micro KL Drift:** ![3D Micro KL Drift](../../../samples/Sample_9_fMRI_Seizure/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

---

## 4. Network Geometry & Structural PCA

### ① PCA Principal Axes & Eigenvector Evolution
* **Principal Axes Ratio:** ![PCA Ratio](../../../samples/Sample_9_fMRI_Seizure/readme_plots/000_2_2__principal_axes_ratio.png)
* **Eigenvector PC1 Evolution:** ![PCA PC1 Evolution](../../../samples/Sample_9_fMRI_Seizure/readme_plots/000_2_3__eigenvector_evolution.png)

### ② Stiffness Temporal Difference ($\Delta K_t = K_t - K_{t-1}$) Analysis
* **Stiffness Difference Heatmap Sequence:**
  - **t=30 (10:05:00):** ![Stiffness Diff t=30](stiffness_diff.t.00030.png)
  - **t=45 (10:07:30):** ![Stiffness Diff t=45](stiffness_diff.t.00045.png)
  - **t=59 (10:09:50):** ![Stiffness Diff t=59](stiffness_diff.t.00059.png)
* **Interpretation:**
  The difference $\Delta K_t$ spikes red globally at t=30 (onset of synchronous burst), and drops to zero (white) afterward, proving dynamic lock.

---

## 5. Conservation Auditing
* **conservation_residual:** The residual is **`0.0000`** throughout, verifying that total signal mass is strictly conserved.

---

## 6. Control Stability & Sensitivity

### ① System Stability (Spectral Radius)
The spectral radius remains locked at **`1.0000`** post-t=30, indicating pathological self-synchronization.

### ② Multi-Order Jacobian Trajectory Analysis
* **Order-wise Jacobian Heatmaps (t=30 / 10:05:00):**
  - **1st-Order ($J^{(1)}$):** ![Jacobian 1st](jacobian_order_1st.t.00030.png)
  - **2nd-Order ($J^{(2)}$):** ![Jacobian 2nd](jacobian_order_2nd.t.00030.png)
  - **3rd-Order ($J^{(3)}$):** ![Jacobian 3rd](jacobian_order_3rd.t.00030.png)
* **Interpretation:**
  Sensitivities fail to decay as order increases (1st → 2nd → 3rd), demonstrating uniform sensitivity saturation across the entire brain.

### ③ LQR Sensitivity Matrix
* **Sensitivity Matrix:** ![Sensitivity Matrix](../../../samples/Sample_9_fMRI_Seizure/readme_plots/004_2_1__sensitivity_matrix.png)

#### LQR Desynchronization Input Gain
$$\Delta \mathbf{u}_{\text{stim}}(t) = - \mathbf{K}_{\text{LQR}} \cdot \mathbf{x}(t)$$
Input gain `41.5234` at `Motor_Cortex` provides desynchronizing stimulation pulses.

---

## 7. Holistic Health Diagnosis & Symbiotic Interventions

### ① Stiff Shoulder (Stagnation) Localization
Temporal Lobe (`05_Temporal_Lobe`) has the highest average viscosity of **`3295.29`**, peaking at **`10:05:00` (t=30)** with **`10000.00`**.

### ② Treatment Points ("Tsubo"), Contraindications, & Symbiotic Interventions
* **Treatment Points (Tsubo):** Motor cortex (`00_Motor_Cortex` / strain energy: `0.43`) is the optimal node for desynchronizing TMS.
* **Contraindications:** Direct stimulation on `05_Temporal_Lobe` (`0.47`) must be avoided.
* **Symbiotic Intervention Plan:** Easing input limits at sensory visual cortexes while applying targeted TMS pulses to the motor cortex will desynchronize the neural network.
