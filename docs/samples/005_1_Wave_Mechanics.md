# 005. Signal Processing and Wave Mechanics (Wave Mechanics & Coherence)

This guide describes the signal processing, wave mechanics, and phase coherence analysis module (`005_1`) in the Tensor-Link Utility (TLU). It includes the resonant frequency spectrum and phase drift heatmap for each validation sample. It organizes the explanations based on outputs and values for all 10 samples.

---

## 🔬 Physico-Mathematical Theory of Wave Mechanics and Phase Coherence

A healthy system involves countless independent decision-making nodes. Therefore, the combined frequency spectrum exhibits "1/f noise (fractal noise / pink noise)":

$$S(f) \propto \frac{1}{f^\beta} \quad (\beta \approx 1.0)$$

During collusion between USRs or states like epileptic seizures, specific nodes align their timing. This causes phase coherence. The fractal slope of the 1/f noise decreases, leading to a synchronous state.

TLU calculates the "phase drift" and coherence matrix to measure time-series changes in phase differences between nodes. It detects synchronization that traditional statistical models cannot find.

---

## 📊 Wave Mechanics and Signal Processing Analysis Results of Each Validation Sample

This section presents the analysis of the resonant frequency spectrum (`005_1_1_resonant_frequency.png`) and the phase drift heatmap (`005_1_2__phase_drift_heatmap.png`) for all 10 validation samples. It explains their physico-mathematical characteristics.

### 🟢 Sample 0 (Healthy Metabolism: Healthy)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** No resonant peaks exist at specific frequencies. Energy is distributed across all bands as smooth noise (fluctuations), indicating a steady state.
  * ![Sample 0 Resonant Frequency](Sample_0_Healthy/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** Phase differences diffuse randomly across all regions without biasing any specific pair. No artificial synchronization or phase coherence is detected.
  * ![Sample 0 Phase Drift](Sample_0_Healthy/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🟡 Sample 1 (Wash Trade: Wash Trade)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** A resonant peak (single spike) occurs at a specific frequency corresponding to the wash trade cycle. This shows the presence of an artificial circulation cycle.
  * ![Sample 1 Resonant Frequency](Sample_1_Wash_Trade/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** A steady synchronization band forms between account pairs involved in wash trading, where the phase difference is locked to a constant value. This indicates persistent transaction synchronization.
  * ![Sample 1 Phase Drift](Sample_1_Wash_Trade/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🔴 Sample 2 (Embezzlement Leak: Embezzlement Leak)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** Resonance spikes occur at multiple locations due to changes in network stiffness from the leak. This shows resonance of local flow fluctuations around the leaking node.
  * ![Sample 2 Resonant Frequency](Sample_2_Embezzlement_Leak/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** Phase difference alignment is observed between the leak target and specific accounts. Synchronous transaction fluctuations occur only through the specific leak path.
  * ![Sample 2 Phase Drift](Sample_2_Embezzlement_Leak/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🟡 Sample 3 (Unbalanced Mistake: Unbalanced Mistake)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** Temporary high-frequency noise is excited only at the step when the mistake occurs. Persistent resonance at specific frequencies does not occur.
  * ![Sample 3 Resonant Frequency](Sample_3_Unbalanced_Mistake/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** The phase difference of the affected account is temporarily distorted only during the error period. It returns to a random diffusion state (normal) in the next step after self-correction.
  * ![Sample 3 Phase Drift](Sample_3_Unbalanced_Mistake/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🔴 Sample 4 (Composite Chaos: Composite Chaos)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** The resonant peak of wash trading and asymmetric multi-resonant peaks of embezzlement occur simultaneously. The entire spectrum shows multiple spikes.
  * ![Sample 4 Resonant Frequency](Sample_4_Composite_Chaos/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** The synchronization band of the wash trading pairs and the alignment pattern of the embezzlement nodes intersect. This shows a double hack of the network.
  * ![Sample 4 Phase Drift](Sample_4_Composite_Chaos/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🔴 Sample 5 (Kyoto Traffic: Kyoto Traffic)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** With deadlock from congestion, all power concentrates near the DC component (zero frequency). High-frequency flow disappears.
  * ![Sample 5 Resonant Frequency](Sample_5_Kyoto_Traffic/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** Phase difference drift stops between major intersections. A frozen phase-locked band dominates the entire area, showing that vehicles cannot move.
  * ![Sample 5 Phase Drift](Sample_5_Kyoto_Traffic/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🟢 Sample 6 (Market Stock Flow: Market Stock Flow)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** No resonant peaks exist. Energy is distributed across all bands as fluctuations, indicating healthy flow.
  * ![Sample 6 Resonant Frequency](Sample_6_Market_Stock_Flow/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** Phase differences diffuse randomly across all regions without biasing any specific pair. No artificial synchronization is detected.
  * ![Sample 6 Phase Drift](Sample_6_Market_Stock_Flow/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🟢 Sample 7 (Market Cash Flow: Market Cash Flow)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** No resonant peaks exist. Energy is distributed across all bands as fluctuations.
  * ![Sample 7 Resonant Frequency](Sample_7_Market_Cash_Flow/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** No pathological locking of phase differences (synchronization band) is observed between transaction accounts. Phase differences diffuse randomly, showing no signs of collusion.
  * ![Sample 7 Phase Drift](Sample_7_Market_Cash_Flow/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🔴 Sample 8 (fMRI Stroke: fMRI Stroke)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** Following topological disruption from the stroke, functional signal frequencies around the motor cortex disappear. An extreme bias to low frequencies (inactivation) occurs.
  * ![Sample 8 Resonant Frequency](Sample_8_fMRI_Stroke/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** Phase drift stops between the stroke area and other regions. Alternatively, it turns into random drift (loss of coherence), indicating functional disconnection.
  * ![Sample 8 Phase Drift](Sample_8_fMRI_Stroke/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🔴 Sample 9 (fMRI Seizure: fMRI Seizure)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** All power spectral energy concentrates at a single frequency corresponding to the synchronous burst of the seizure, forming a resonant spike.
  * ![Sample 9 Resonant Frequency](Sample_9_fMRI_Seizure/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** Phase differences align across the entire brain (especially around the temporal lobe). A strong phase coherence (global brain coherence) forms. Individual regions lose independent activity.
  * ![Sample 9 Phase Drift](Sample_9_fMRI_Seizure/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🔴 Sample 5 (Kyoto Traffic: Kyoto Traffic)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** With deadlock from congestion (saturation at the Perron-Frobenius boundary), all power concentrates near the DC component (zero frequency). High-frequency flow (movement) disappears.
  * ![Sample 5 Resonant Frequency](Sample_5_Kyoto_Traffic/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** Phase difference drift stops between major intersections. A pathological frozen phase-locked band dominates the entire area, showing that vehicles cannot move.
  * ![Sample 5 Phase Drift](Sample_5_Kyoto_Traffic/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🟢 Sample 6 (Market Stock Flow: Market Stock Flow)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** No prominent resonant peaks exist. Energy is distributed across all bands as natural fluctuations, indicating healthy flow.
  * ![Sample 6 Resonant Frequency](Sample_6_Market_Stock_Flow/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** Phase differences diffuse randomly across all regions without biasing any specific pair. No artificial synchronization (forced alignment) is detected.
  * ![Sample 6 Phase Drift](Sample_6_Market_Stock_Flow/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🟢 Sample 7 (Market Cash Flow: Market Cash Flow)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** No prominent resonant peaks exist. Energy is distributed across all bands as gentle fluctuations.
  * ![Sample 7 Resonant Frequency](Sample_7_Market_Cash_Flow/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** No pathological locking of phase differences (steady band) is observed between direct transfer accounts. Phase differences diffuse randomly, showing no signs of collusion.
  * ![Sample 7 Phase Drift](Sample_7_Market_Cash_Flow/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🔴 Sample 8 (fMRI Stroke: fMRI Stroke)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** Following topological disruption from the stroke, functional signal frequencies around the motor cortex disappear. An extreme bias to low frequencies (inactivation) occurs.
  * ![Sample 8 Resonant Frequency](Sample_8_fMRI_Stroke/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** Phase drift stops between the stroke area and other regions. Alternatively, it turns into random drift (loss of coherence), indicating functional disconnection.
  * ![Sample 8 Phase Drift](Sample_8_fMRI_Stroke/readme_plots/005_1_2__phase_drift_heatmap.png)

---

### 🔴 Sample 9 (fMRI Seizure: fMRI Seizure)

* **Resonant Frequency Spectrum (`005_1_1_resonant_frequency.png`)**
  * **Clinical Commentary:** All power spectral energy concentrates at a single frequency corresponding to the forced synchronization (pathological burst) of the seizure, forming a large resonant spike.
  * ![Sample 9 Resonant Frequency](Sample_9_fMRI_Seizure/readme_plots/005_1_1_resonant_frequency.png)

* **Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)**
  * **Clinical Commentary:** Phase differences align across the entire brain (especially around the temporal lobe). A strong phase coherence (global brain coherence) forms. Individual regions lose independent activity.
  * ![Sample 9 Phase Drift](Sample_9_fMRI_Seizure/readme_plots/005_1_2__phase_drift_heatmap.png)
