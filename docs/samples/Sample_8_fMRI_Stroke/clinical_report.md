# Mathematical Diagnostic Report: Sample_8_fMRI_Stroke
## (Target: Brain fMRI Case 8 / Focal Ischemia Stroke Diagnosis)

---

## 0. Executive Summary

* **Final Diagnosis (Conclusion First):** HIGH (Focal Ischemia / Stroke). Blood flow to the motor cortex drops abruptly, triggering local cellular deactivation.
* **Root Cause (Stability Evaluation):** At **t=30 (10:05:00)**, BOLD signals in the motor cortex (`00_Motor_Cortex`) drop by ~95%. PC1 EVR climbs from `37.60%` to **`94.72%`**, and PC1 eigenvector weight freezes at **`-0.8942`** (stiffness lock).
* **Holistic Health Constitution (Health Evaluation):** 
  Total blood flow ("Physique") stays conserved at **`100000.0`** (Kirchhoff residual `0.00`). However, local temperature drops to **`0.00`** (local cold spot) at the motor cortex. High-amplitude Jerk (flow deceleration shock) and Snap (neuronal ripples) spike at t=30.
* **Key Stagnations & Interventions:**
  - **Stiff Shoulder (Signal Delay):** Prefrontal cortex (`02_Prefrontal_Cortex`) shows the highest viscosity with an average of **`10099.00`**, peaking at **`10:09:50` (t=59)** with **`10408.23`** (ischemia-induced latency).
  - **Acupuncture Point (Optimal Treatment Area):** Motor cortex (`00_Motor_Cortex` / strain energy minimum `0.43` / LQR gain `41.5234`) is the best node for targeted TMS stimulation.
  - **Contraindications (Avoid Direct Stimulation):** Parietal Lobe (`01_Parietal_Lobe` / strain energy maximum `0.47`) must not be stimulated to prevent tissue necrosis expansion.

---

## 1. Holistic Diagnosis & Evaluation

### ① HIGH: Focal Ischemia (Stroke)
The BOLD signal in the motor cortex drops by 95% at t=30 (10:05:00). Chronological PCA and stiffness PCA confirm that functional connectivity freezes locally, locking the motor cortex.

### ② Holistic Health Constitution (Mathematical Bridge)
* **Physique (Total Blood Flow `state_X`):** Average `100000.00`.
  - *Mathematical Interpretation:* Total brain metabolic volume, strictly conserved inside the skull.
* **Immunity (Free Energy `free_energy_F`):** Average `413922.35` (severely depressed).
  - *Mathematical Interpretation:* The brain's capability to recover from external neural shocks.
* **Autonomic System (Entropy `entropy_S`):** Average `9.3573`.
* **Temperature (Temperature `temperature_T`):** Average `9854.16` (local freeze at motor cortex).
* **Arteriosclerosis (Coupling Stiffness `stiffness_k`):** Maximum `0.0037` (vascular stiffness lock).
* **Stiff Shoulder (Viscosity `viscosity_C`):** `02_Prefrontal_Cortex` average viscosity is `10098.99`.
* **Shockwaves (Jerk `jerk_j` & Snap `snap_s`):** Jerk (deceleration shock) and Snap (neuronal ripples) spike at t=30.

---

## 2. Physical & Mathematical Detailed Metrics

### ① 3D Dynamics Descriptive Statistics (Kinematics)
Descriptive statistics from [result.000_1_1_filter_dynamics.analysis.csv](../../../samples/Sample_8_fMRI_Stroke/output_data/result.000_1_1_filter_dynamics.analysis.csv):

| Measure / Scale | Mean | Median | Mode (count/total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **State state_X** | 100000.0000 | 100103.4500 | 1000000.0000 (12/240, 5.0%) | 40052.4300 | 115335.5900 | 75283.1600 | 15000.0 | 25000.0 | -0.1210 | 1.8109 |
| **Velocity velocity_v** | 0.0 | 120.1 | 0.0 (12/240, 5.0%) | -1500.0 | 1600.0 | 3100.0 | 450.0 | 520.4 | -0.6512 | 2.1109 |
| **Acceleration acceleration_a** | 0.0 | 0.0 | 0.0 (19/240, 7.9%) | -92.0 | 89.0 | 181.0 | 14.0 | 31.2 | -0.2109 | 2.5612 |
| **Jerk jerk_j** | 0.0000 | 0.0000 | 0.0000 (10/300, 3.3%) | -2076.7100 | 1890.3600 | 3967.0700 | 140.49 | 205.58 | -0.7932 | 57.0344 |
| **Snap snap_s** | -0.0000 | 0.0000 | 0.0000 (15/300, 5.0%) | -1987.9600 | 3967.0700 | 5955.0300 | 218.45 | 350.04 | 3.6015 | 59.1670 |
| **Viscosity viscosity_C** | 3295.2 | 1812.0 | 10000.0 (12/240, 5.0%) | 78.9 | 10000.0 | 9921.1 | 4231.0 | 3189.0 | 1.0112 | 0.0891 |

---

## 3. Thermodynamics & Topological Evolution

### ① Macro Thermodynamics (Energy Stack & T-S Diagram)
* **Energy Stack:** ![Thermodynamics Energy Stack](../../../samples/Sample_8_fMRI_Stroke/readme_plots/001_1_2__thermodynamics_energy_stack.png)
* **T-S Diagram:** ![T-S Diagram](../../../samples/Sample_8_fMRI_Stroke/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

### ② 3D Local Thermodynamics
* **Local Entropy:** ![3D Local Entropy](../../../samples/Sample_8_fMRI_Stroke/readme_plots/001_1_2_1__3d_local_entropy.png)
* **Local Temperature:** ![3D Local Temperature](../../../samples/Sample_8_fMRI_Stroke/readme_plots/001_1_2_2__3d_local_temperature.png)
* **Local Internal Energy:** ![3D Local Internal Energy](../../../samples/Sample_8_fMRI_Stroke/readme_plots/001_1_2_7__3d_local_internal_energy.png)

### ③ Information Geometry & Forensics
* **Macro Forensics Dashboard:** ![Macro Forensics](../../../samples/Sample_8_fMRI_Stroke/readme_plots/002_2_1__macro_forensics_dashboard.png)
* **3D Micro KL Drift:** ![3D Micro KL Drift](../../../samples/Sample_8_fMRI_Stroke/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

---

## 4. Network Geometry & Structural PCA

### ① PCA Principal Axes & Eigenvector Evolution
* **Principal Axes Ratio:** ![PCA Ratio](../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_2_2__principal_axes_ratio.png)
* **Eigenvector PC1 Evolution:** ![PCA PC1 Evolution](../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_2_3__eigenvector_evolution.png)

### ② Stiffness Temporal Difference ($\Delta K_t = K_t - K_{t-1}$) Analysis
* **Stiffness Difference Heatmap Sequence:**
  - **t=30 (10:05:00):** ![Stiffness Diff t=30](stiffness_diff.t.00030.png)
  - **t=45 (10:07:30):** ![Stiffness Diff t=45](stiffness_diff.t.00045.png)
  - **t=59 (10:09:50):** ![Stiffness Diff t=59](stiffness_diff.t.00059.png)
* **Interpretation:**
  Red stiffness differences at t=30 capture the vascular occlusion at the motor cortex, stabilizing into a static stiffness lock (white) by t=45 and t=59.

---

## 5. Conservation Auditing
* **conservation_residual:** The residual is **`0.0000`** throughout, confirming zero vascular leakage and identifying the event strictly as an ischemic stroke.

---

## 6. Control Stability & Sensitivity

### ① System Stability (Spectral Radius)
The spectral radius spikes to **`1.0000`** post-t=30, indicating abnormal functional connectivity.

### ② Multi-Order Jacobian Trajectory Analysis
* **Order-wise Jacobian Heatmaps (t=30 / 10:05:00):**
  - **1st-Order ($J^{(1)}$):** ![Jacobian 1st](jacobian_order_1st.t.00030.png)
  - **2nd-Order ($J^{(2)}$):** ![Jacobian 2nd](jacobian_order_2nd.t.00030.png)
  - **3rd-Order ($J^{(3)}$):** ![Jacobian 3rd](jacobian_order_3rd.t.00030.png)
* **Interpretation:**
  1st-order Jacobian captures the motor cortex connectivity drop. High-order Jacobian sensitivity fails to propagate, validating localized signal block (sink).

### ③ LQR Sensitivity Matrix
* **Sensitivity Matrix:** ![Sensitivity Matrix](../../../samples/Sample_8_fMRI_Stroke/readme_plots/004_2_1__sensitivity_matrix.png)

#### LQR TMS Control Design
$$\mathbf{u}_{\text{TMS}}(t) = - \mathbf{R}^{-1} \mathbf{B}^T \mathbf{P} \cdot \mathbf{x}(t)$$
State cost gain `41.5234` at `Motor_Cortex` optimizes local stimulation offsets without overloading adjacent cortexes.

---

## 7. Holistic Health Diagnosis & Symbiotic Interventions

### ① Stiff Shoulder (Stagnation) Localization
Prefrontal cortex (`02_Prefrontal_Cortex`) shows the highest viscosity with an average of **`10098.99`**, peaking at **`10:09:50` (t=59)** with **`10408.23`**.

### ② Treatment Points ("Tsubo"), Contraindications, & Symbiotic Interventions
* **Treatment Points (Tsubo):** Motor cortex (`00_Motor_Cortex` / strain energy: `0.43`) is the optimal node for TMS pulses.
* **Contraindications:** Direct stimulation on `01_Parietal_Lobe` (`0.47`) must be avoided.
* **Symbiotic Intervention Plan:** Easing input limits at sensory visual cortexes while applying targeted TMS pulses to the motor cortex will restore normal neural pathway flexibility.
