# Neural Stroke Final Report (Case 8)

> [!NOTE]
> A more detailed technical clinical report is available in [clinical_report.md](clinical_report.md).

## Target Brain Activity: Sample 8 (fMRI Stroke)

---

## 0. Executive Summary

* **Final Diagnosis:** 【Warning / Required Action】 Focal cerebral ischemia (stroke) has occurred in the motor cortex, triggering sudden localized deactivation.
* **Holistic Health Constitution:** 
  Total blood flow volume (**"Physique"**) remains conserved. However, the brain's shock absorption capacity (**"Immunity"**) is severely depleted. Local signal flexibility (**"Autonomic System"**) is lost, showing localized cold spots. PCA EVR PC1 climbs to 94.72%, and eigenvector weights freeze (stiffness lock). Sudden deceleration shocks (**"Jerk"**) and neuronal ripples (**"Snap"**) spike at t=30.
* **Key Stagnations & Interventions:**
  - **Stiff Shoulder (Signal Stagnation):** **`02_Prefrontal_Cortex`** (viscosity upper 25% boundary) shows severe signal delays, peaking at **10:09:50** (t=59).
  - **Acupuncture Points (Treatment Areas):** **`00_Motor_Cortex`** (strain energy lower 25% boundary) is the optimal node for Transcranial Magnetic Stimulation (TMS).
  - **Contraindications (Avoid Direct Stimulation):** Directly stimulating **`01_Parietal_Lobe`** will expand the tissue necrosis area and must be avoided.

---

## 1. Final Diagnosis (Warning)

### 【Diagnosis】: Neural Stroke (Focal Ischemia)
![System Stability (Maximum Spectral Radius)](../../../samples/Sample_8_fMRI_Stroke/readme_plots/004_1_2__system_stability.png)

At t=30 (10:05:00), blood flow (BOLD signal) in the motor cortex drops by 95%. Functional connectivity is lost, and the spectral radius $\rho$ spikes, proving neural pathway failure.

---

## 2. Holistic Health Constitution Analysis

The brain network's flow capacity maps to the following constitutional parameters:

### ① Physique (Total Blood Flow Scale)
Total BOLD signal volume (Physique) remains strictly conserved at `100000` with zero residual, proving that no cranial bleeding has occurred.

### ② Immunity (Recovery Buffer Capacity)
![P/L Cumulative Trend](../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_0_1__PL_Trend.png)

Recovery buffer capacity (Free Energy) drops severely post-stroke. The brain lacks the capacity to absorb additional neural shocks.

### ③ Autonomic System (Entropy & Choice Diversity)
![T-S Diagram](../../../samples/Sample_8_fMRI_Stroke/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

The T-S diagram shows a locked trajectory post-stroke, representing a loss of local signal variety (depressed Entropy).

### ④ Arteriosclerosis (PCA Stiffness Evaluation)
![PCA Ratio](../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_2_2__principal_axes_ratio.png)

PCA PC1 EVR spikes to 94.72% and eigenvector weights freeze on the motor cortex, proving localized functional connectivity lock (Arteriosclerosis).

### ⑤ Shockwaves (Jerk and Snap Trends)
![3D Jerk](000_1_9__3d_dynamics_jerk.png)

![3D Snap](000_1_10__3d_dynamics_snap.png)

* **Mathematical Bridge:**
  Jerk and Snap exhibit sharp spikes at t=30. This mathematically proves that the motor cortex suffers from a sudden blood flow deceleration shock and subsequent neuronal ripples at the stroke onset.

---

## 3. Key Stagnations & Interventions

### ⚠️ Stiff Shoulder (Chronic Delays)
![3D Phase Portrait](../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_1_8__phase_portrait_3d.png)

* **Stagnation Nodes:** Upper 25% viscosity includes **`02_Prefrontal_Cortex`** and **`03_Parietal_Lobe`**.
  - **`02_Prefrontal_Cortex`**: Peaked at **`t=59`** due to ischemic signal transmission delays.

### 🎯 Acupuncture Points (Optimal Treatment Areas)
![Sensitivity Matrix](../../../samples/Sample_8_fMRI_Stroke/readme_plots/004_2_1__sensitivity_matrix.png)

* **Treatment Nodes:** Strain energy lower 25% includes **`00_Motor_Cortex`** and **`04_Occipital_Lobe`**.
  - **Intervention Advice:** Targeted TMS pulses applied to the motor cortex (LQR gain: `41.5234`) will help restore signal flexibility with minimal surrounding stress.

### 🚫 Contraindications
* **Avoid Direct Stimulation:** High strain energy (upper 25%) nodes include **`01_Parietal_Lobe`** and **`05_Temporal_Lobe`**.
  - **Intervention Advice:** Stimulating these areas directly will trigger neural overload, expanding the tissue necrosis.

### ⚡ Stiffness Temporal Difference ($\Delta K_t$)
* **Stiffness Difference Heatmap Sequence:**
  - **t=30**: ![Stiffness Diff t=30](stiffness_diff.t.00030.png)
  - **t=45**: ![Stiffness Diff t=45](stiffness_diff.t.00045.png)
  - **t=59**: ![Stiffness Diff t=59](stiffness_diff.t.00059.png)

* **Mathematical Bridge:**
  The difference $\Delta K_t$ spikes red at t=30 on the motor cortex, marking the active establishment of the ischemia block, which then freezes into a static lock.

---

## 4. Falsifiability Conditions

To falsify this "Stroke" diagnosis, one must present:

1. **Independent EEG Signal Logs:**
   Simultaneous EEG logs showing normal alpha and beta waves in the motor cortex during the deactivation window.
2. **Post-Event CT Angiography Images:**
   Independent CT imaging showing complete vascular patency (no occlusions) in the middle cerebral artery.

---
*Published by: TLU Brain Diagnostics Engine*
