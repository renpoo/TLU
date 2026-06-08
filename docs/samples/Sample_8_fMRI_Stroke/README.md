# 🔬 Localized Cerebral Blood Flow Occlusion Report (Sample 8 - Brain Stroke fMRI Simulation)

> [!NOTE]
> **【Important】 Comparison between Sample 8 (Stroke) and Sample 9 (Seizure):**
>
> * **Sample 8 (This Report):** Models an ischemic pathology (stroke) where blood flow to a specific brain region (motor cortex) is blocked, causing local flow depletion.
> * **Sample 9 (Next Report):** Models a hyper-synchronous pathology (seizure) where blood flow synchronizes globally across the brain, starting from the temporal lobe.
> * For healthy brain activity, refer to the [Healthy Clinical Reference](../Sample_0_Healthy/README.md).

---

## 1. Executive Summary

* **Overall Status:** 🟡 **Acute Local Flow Deficiency Detected (Localized Brain Ischemia / Stroke)**
* **Severity:** 🟡 **HIGH (Ischemic Local Impairment)**
* **Summary:**
  The system (fMRI brain activity network) exhibits localized circulatory failure (ischemia) in the BOLD signal flow. Inflow to the motor cortex (`00_Motor_Cortex`) was blocked by approximately 95% at time step **`t=30` (10:05:00)**.
  The explanation variance ratio of the first principal component (PC1) in Principal Component Analysis (PCA) rose from **`37.60%`** ( $t=29$ ) to **`94.72%`** ( $t=30$ ). The principal component vector concentrated in the negative direction of the motor cortex (**`-0.8942`**), indicating stiffness locking. The motor cortex Z-Score reached **`51.04`** at $t=30$. Based on these metrics, we diagnose acute occlusion of the middle cerebral artery (MCA) branch supplying the motor cortex, causing local ischemia and metabolic collapse.

---

## 2. Limits of Traditional Analysis (Limitations of Traditional Snapshots)

Early identification of acute localized stroke is impossible using standard average-value monitoring or simple snapshot aggregations of total flow (P/L equivalent) and stock (B/S equivalent).

The following graphs show the cumulative flow and residuals:

### Balance Sheet Comparison (B/S Equivalent)

* **B/S Asset & Equity Cumulative Trend (Cumulative):**
  ![B/S Cumulative Trend](readme_plots/000_0_1__BS_Trend.png)

### Income Statement Comparison (P/L Equivalent)

* **P/L Volume Cumulative Trend:**
  ![P/L Cumulative Trend](readme_plots/000_0_1__PL_Trend.png)

#### 🔍 Blind Spot of Traditional Monitoring

When the overall activity level (total volume) is maintained, conventional methods miss local flow blockages.
At the final step, the cumulative balance of the motor cortex is `40,052.43`. This does not show a significant difference from other regions (prefrontal cortex: `115,078.12`, temporal lobe: `115,335.59`). This occurs because pre-occlusion data mixes with cumulative values, diluting the acute occlusion signal after $t=30$. Static average-value analysis cannot identify the occlusion node or the inflection point.

---

## 3. Pathophysiology

The physics engine analyzed joint connection stiffness to identify the mechanism of the acute stroke.

* **Mechanism of Stroke:**
  At time step **`t=30` (10:05:00)**, the blood inflow from other regions to the motor cortex (`00_Motor_Cortex`) dropped by approximately 95% (from an average of ~`540` to ~`29`).
  However, blood outflow from the motor cortex to other regions remained at `570` to `590`. Blood within the motor cortex was depleted instantly. This flow imbalance is evidence of middle cerebral artery occlusion.

---

## 4. Summary of Mathematical Analysis Results

### 4.1. Local Brain Flow Blockage and Kirchhoff Conservation Law Verification

The `System Conservation Residual` remains exactly **`0.0`** throughout the period, indicating no leaks outside the system. Only the motor cortex node in the internal topology suffers from flow deficiency.

* **Macro Forensics Dashboard:**
  ![Macro Forensics](readme_plots/002_2_1__macro_forensics_dashboard.png)

### 4.2. Connection Stiffness Shifts (Stiffness Lock) and Principal Vector Bias

The intrinsic structure of the system shifted at the moment of the anomaly.

* **PCA Axis Ratio:**
  ![PCA Ratio](readme_plots/000_2_2__principal_axes_ratio.png)

* **PC1 Principal Eigenvector Component Ratio Evolution:**
  ![PC1 Eigenvector](readme_plots/000_2_3__eigenvector_evolution.png)

#### 📊 Five-Point Stiffness Matrix Sequence Analysis

* **① Normal Period (t=0 / 10:00:00):**
  ![Stiffness t0](readme_plots/000_2_1__structural_stiffness.t.00000.png)
  Functional connectivity is uniform, maintaining joint stiffness.
* **② Before Occlusion (t=29 / 10:04:50):**
  ![Stiffness t29](readme_plots/000_2_1__structural_stiffness.t.00029.png)
  The PC1 explanation ratio is **`37.60%`** (eigenvalue: **`6296.66`**), showing distributed energy.
* **③ Acute Stroke Onset (t=30 / 10:05:00):**
  ![Stiffness t30](readme_plots/000_2_1__structural_stiffness.t.00030.png)
  The inflow path is blocked. The PC1 explanation ratio rose to **`94.72%`** (eigenvalue: **`201,402.52`**). The principal component vector concentrated at `00_Motor_Cortex` with a weight of **`-0.8942`**.
* **④ Post-Occlusion (t=31 / 10:05:10):**
  ![Stiffness t31](readme_plots/000_2_1__structural_stiffness.t.00031.png)
  The PC1 ratio remains locked at **`94.71%`** with the motor cortex load at **`-0.8943`**. The motor cortex dominates the dynamics (stiffness lock).
* **⑤ Final State (t=59 / 10:09:50):**
  ![Stiffness t59](readme_plots/000_2_1__structural_stiffness.t.00059.png)
  The PC1 ratio is **`92.33%`**, showing permanent functional loss.

### 4.3. Network Topology and Connectivity Collapse

* **System Stability Indicator (Spectral Radius):**
  ![System Stability](readme_plots/004_1_2__system_stability.png)

#### Spectral Radius "1.00" Constraint of Probability Transition Matrix

The brain network is a connected system without isolated nodes. Due to mathematical properties of the probability transition matrix, the spectral radius remains locked at `1.0000`.
Therefore, the spectral radius alone cannot detect this pathology. Local topological destruction is indicated by the "reduction of connection edges (inflow cutoff)" and the "stiffness lock of the PC1 eigenvector."

* **Five-Point Network Topology Sequence:**
  * **① Initial State (t=0 / 10:00:00):**
    ![Topology t0](readme_plots/002_1_2__network_topology.t.00000.png)
  * **② Before Occlusion (t=29 / 10:04:50):**
    ![Topology t29](readme_plots/002_1_2__network_topology.t.00029.png)
  * **③ Acute Stroke Onset (t=30 / 10:05:00):**
    ![Topology t30](readme_plots/002_1_2__network_topology.t.00030.png)
    Inflow edges to the motor cortex (`00_Motor_Cortex`) decrease, disrupting the topological connection.
  * **④ Post-Occlusion (t=31 / 10:05:10):**
    ![Topology t31](readme_plots/002_1_2__network_topology.t.00031.png)
  * **⑤ Final State (t=59 / 10:09:50):**
    ![Topology t59](readme_plots/002_1_2__network_topology.t.00059.png)

### 4.4. Metabolic Entropy and Free Energy Collapse

Statistical physics metrics show the collapse of brain metabolism.

* **Thermodynamics Energy Stack:**
  ![Thermodynamics Energy Stack](readme_plots/001_1_2__thermodynamics_energy_stack.png)

* **T-S Diagram:**
  ![T-S Diagram](readme_plots/001_1_3__thermodynamics_ts_diagram.png)

The average entropy $S$ is **`9.36`** and average free energy $F$ is **`413,922.35`** across the period. Following the block at $t=30$, free energy $F$ decreased, reaching a minimum of **`167,265.39`** at the final step ( $t=59$ ). The potential energy to maintain activity is depleted.
The T-S diagram shows temperature and entropy decreasing after the occlusion, contracting the potential energy.

### 4.5. Identifying the Ischemic Lesion via 3D Spatio-Temporal Plots

The 3D information geometry and statistical plots show where the occlusion occurs.

* **3D Micro Z-Score (Position):**
  ![3D Micro Z-Score](readme_plots/002_2_2_2__3d_micro_z_score_X.png)
* **3D Micro KL Drift:**
  ![3D Micro KL Drift](readme_plots/002_2_2_1__3d_micro_kl_drift.png)

In the 3D Micro Z-Score plot, a warning spike of **`51.04`** appears at the `00_Motor_Cortex` coordinates at $t=30$.
Adjacent nodes (prefrontal cortex: `12.36`, parietal lobe: `17.12`) also show synchronized shifts. This records how the strain from the motor cortex block propagates across the brain.

---

## 5. Local Treatment Plan (Optimal Treatment / LQR Control)

* **Treatment Protocol: Re-open Occluded Path (Thrombolysis) and Support Perfusion via LQR Feedback**
* **LQR Sensitivity Intervention (Identifying Control Nodes):**
  LQR sensitivity analysis designates `Motor_Cortex` as the target node. The sensitivity index (`fk_total_ripple`) is **`41.5234`**.

  > **【Mathematical Proof of `41.5234`】**
  > Parameters are: damping rate $\gamma = 0.85$, maximum steps $k_{max} = 5$, and input displacement $\Delta q = 10.0$.
  > Under the ischemia stiffness lock state where connection leaks approach zero, input signals propagate synchronously. The total ripple effect is:
  > $$fk\_total\_ripple = \Delta q \times \sum_{k=0}^{5} \gamma^k = 10.0 \times \left(1.0 + 0.85 + 0.85^2 + 0.85^3 + 0.85^4 + 0.85^5\right) = 41.5234$$

  At $t=30$, external force changes at `00_Motor_Cortex` have the maximum impact on `02_Prefrontal_Cortex` (`fk_max_impact = 7.8304`), which acts as the control point.

* **Specific Intervention Plan:**
  1. **Thrombolytic Therapy (tPA Infusion):**
     Immediately after occlusion ( $t=30$ to $33$ ), reduce the connection stiffness of the inflow path to the motor cortex (revascularization). This restores inflow to the normal level (~`540`) and pulls the PC1 ratio back to the normal range (~37%).
  2. **Phase Support via Transcranial Magnetic Stimulation (TMS LQR Feedback):**
     Apply anti-phase stimulation pulses to the prefrontal cortex (`02_Prefrontal_Cortex`) and parietal lobe (`01_Parietal_Lobe`) based on the LQR sensitivity matrix. This offsets the load on the motor cortex via collateral pathways, preventing free energy collapse.
     ![Control LQR](readme_plots/004_1_3__control_lqr_performance_space.png)

---

## 6. Forensic Alert & Falsifiability (Falsification Analytics)

### 6.1. Triaging Model Pollution and Artifacts

* **Limits of Statistical Models and Triage:**
  The Z-Score triggered a warning of $Z=51.04$ at $t=30$. Later, the warning level fell to **`6.31`** at $t=31$ and **`4.54`** at $t=32$. This occurs because the statistical model learns the ischemic state as the new baseline (model pollution).
  However, physical indicators—the free energy drop (`167,265.39`) and the PC1 bias (~92.3%)—continue to indicate the anomaly. In triaging, we reject the silent Z-Scores and confirm the ischemic stroke state.
* **Distinguishing Artifacts:**
  Head movement or scanner vibrations cause uniform variations across all nodes. In contrast, the local PC1 concentration of 94.72% on the motor cortex cannot be replicated by noise. We confirm this as stroke pathology.

### 6.2. Falsification Conditions

To reject the stroke diagnosis and prove that the flow reduction is normal or noise, the following evidence is required:

1. **DWI and T2-weighted MRI Data:**
   MRI scans at $t=30$ showing no high signal (white intensity change) in the motor cortex (`Motor_Cortex`) and no decrease in water diffusion (ADC map).
2. **Angiography Data (MRA / CTA):**
   MRA or CTA logs showing that the middle cerebral artery (MCA) branches supplying the motor cortex are open, with no organic occlusion (thrombus or embolus).
