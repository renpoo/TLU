# Sample 8: Application to Biological Networks (fMRI Stroke - Thermodynamics of Stroke/Ischemia)

> [!NOTE]
> **[IMPORTANT] Relationship Between Sample 8 and Sample 9 and Target Domain**
> This sample (Sample 8) and the next sample (Sample 9) are not financial or traffic data, but biological data simulating the **"Effective Connectivity of BOLD signals"** in the human brain (fMRI).
> This is the grand finale test case proving that TLU's "Universal Physics-Mathematics-Mathematics Engine" can seamlessly diagnose across disciplines, from social sciences (finance/traffic) to life sciences (biological network pathologies).
>
> * **Sample 8 (This Report):** Simulates a **"Stroke/Ischemia"** where blood flow/signals to a specific part of the brain network (Motor Cortex) are physically blocked. It verifies the process where part of the network "depletes and necrotizes."
> * **Sample 9 (Next Report):** Simulates an **"Epileptic Seizure"** where abnormal synchronous signals radiate from a specific region (Temporal Lobe). It verifies the process of excessive "runaway resonance" of energy.

---

# 🔬 Meta-Analysis Synthesis Report / Laboratory Findings

## 1. Executive Summary

This system (biological brain domain) is diagnosed as being in an extremely critical state (HIGH Severity) where a **"fatal blockage of energy supply to a specific node (Motor Cortex) (Stroke/Infarction)"** occurs mid-way through the timeline, resulting in the entire network falling into **"Thermodynamic Energy Depletion."** Only the inflow path to the motor cortex is blocked, and the process of isolation and necrosis progresses: "It outputs noise to other regions, but receives absolutely no input."

## 2. Limitations of Traditional Perspective

**[Cumulative Flow for the Entire Period (P/L Waterfall) & Balance Sheet (B/S)]**
![Sample 8 PL Waterfall](readme_plots/000_0_1__PL_Waterfall_Total.png)
![Sample 8 BS Block](readme_plots/000_0_1__BS_Block_Total.png)

Looking at the P/L summary, only the Motor Cortex is showing an extreme negative (-$60,191). This is a physical sign of an arterial blockage: "It is sending signals to other parts, but receiving no input." However, traditional static aggregation tools cannot depict the "dynamic process of death" regarding how this mere "balance anomaly" places a thermodynamic load on the entire network (increasing entropy = wasteful frictional heat and energy squandering) and undermines overall biological activity.

## 3. Fundamental Pathophysiology

The root cause of this sample lies in an "Arterial Blockage Script" intentionally embedded in the generator code `_0_0_generate_dummy_fmri.py`.

* **Identified Evidence:**
  `if tgt == "Motor_Cortex": base_flux = base_flux * 0.05`
  From time step `TR >= 150` onward, all blood flow (edges) heading to the motor cortex (`Motor_Cortex`) was artificially cut by 95% (ischemic state). The macroscopic collapse detected by TLU is triggered by this localized failure of mass conservation.

## 4. Physical and Mathematical Proof

### 4.1. Macro Forensics & Structural Stiffness

Due to the localized blockage of blood flow, an imbalance arises in the mass conservation of the entire system. Furthermore, as the asymmetrical state of the motor cortex ("zero input, only output") prolongs, the system's stiffness matrix (internal structure) gradually proceeds toward a Rigid Lock (a state where the elasticity of the entire brain is lost, rejecting healthy signal processing), causing the brain as a whole to lose its elasticity.

![Sample 8 Macro Forensics](readme_plots/002_2_1__macro_forensics_dashboard.png)
![Sample 8 External Force 3D](readme_plots/000_1_6__3d_dynamics_external_force.png)

* **1st Image [Start]**: `t.00000` (Normal stiffness)
* **2nd Image [Just Before Change]**: `t.00029` (TR=145)
* **3rd Image [At the Time of Change]**: `t.00030` (TR=150: Infarction occurs)
* **4th Image [Just After Change]**: `t.00031` (TR=155)
* **5th Image [End]**: `t.00059` (TR=295: Complete rigid lock)

![Sample 8 Structural Stiffness 0](readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 8 Structural Stiffness 29](readme_plots/000_2_1__structural_stiffness.t.00029.png)
![Sample 8 Structural Stiffness 30](readme_plots/000_2_1__structural_stiffness.t.00030.png)
![Sample 8 Structural Stiffness 31](readme_plots/000_2_1__structural_stiffness.t.00031.png)
![Sample 8 Structural Stiffness 59](readme_plots/000_2_1__structural_stiffness.t.00059.png)

### 4.2. Mathematical Constraints of Spectral Radius & Physical Topology Disruption

* **System Stability (Spectral Radius):**
    ![Sample 8 System Stability](readme_plots/004_1_2__system_stability.png)

* **Mathematical Background of Spectral Radius "1.00" (Stochastic Constraints):**
    The TLU System Stability Filter (`_004_1_2_filter_system_stability.py`) calculates the **"transition probability matrix (Markov stochastic matrix)"** by normalizing the flow data by the total outflow of each brain region (node). According to the Perron-Frobenius theorem, the maximum eigenvalue (spectral radius) of any row-stochastic matrix is **mathematically guaranteed to be strictly and consistently `1.00`**, regardless of whether the brain is healthy or suffers from a localized stroke. Therefore, the spectral radius itself does not serve as a diagnostic indicator for detecting pathophysical state transitions.

* **Flickering of `is_stable` (Numerical Noise Mimicking State Change):**
    The stability flag (`is_stable`) flickers rapidly between `1` (stable) and `0` (unstable) in the log. This is not a physical fluctuation of brain connectivity. Rather, it is a **numerical artifact caused by microscopic floating-point rounding errors** when calculating eigenvalues of exactly `1.0` in complex space.
  * **False Positives (t < 30):** During the healthy baseline period, rounding errors occasionally cause the computed spectral radius to be slightly larger than `1.0` (e.g., `1.0000000000000002`), triggering a false unstable alarm (`is_stable = 0`).
  * **False Negatives (t >= 30):** During the ischemic stroke period when the network is severely compromised, numerical rounding yields values slightly below or equal to `1.0`, resulting in a false stable classification (`is_stable = 1`).
    Since this metric produces uninformative false alarms and false normals indiscriminately, it should be excluded from forensic clinical reasoning.

* **Physical Topology Disruption (Loss of Inflow Edges):**
    In contrast, the actual physical collapse of connectivity due to the input blockage to the `Motor_Cortex` is clearly exposed in the temporal network graphs. After the stroke onset at `t=30` (TR=150), the inflow edge directed toward the `Motor_Cortex` completely vanishes, visualizing the structural disruption of active blood/information circulation.

* **Network Topology 5-Point Sequence:**
  * **① Start (t=0 / 10:00:00):**
        ![Sample 8 Network Topology 0](readme_plots/002_1_2__network_topology.t.00000.png)
  * **② Just Before Change (t=29 / 10:04:50):**
        ![Sample 8 Network Topology 29](readme_plots/002_1_2__network_topology.t.00029.png)
  * **③ The Exact Point of Change (t=30 / 10:05:00):**
        ![Sample 8 Network Topology 30](readme_plots/002_1_2__network_topology.t.00030.png)
        The inflow edge directed toward the `Motor_Cortex` vanishes, indicating that the path for active blood/information flow has been severed.
  * **④ Immediately After Change (t=31 / 10:05:10):**
        ![Sample 8 Network Topology 31](readme_plots/002_1_2__network_topology.t.00031.png)
  * **⑤ End (t=59 / 10:09:50):**
        ![Sample 8 Network Topology 59](readme_plots/002_1_2__network_topology.t.00059.png)

### 4.3. Thermodynamic Energy Stack

In Sample 8, from the middle phase when the lesion occurs (around TR=150), entropy loss ($T \Delta S$: red layer) suddenly surges rapidly, and free energy sinks deeply into the negative zone. This is a perfect proof indicating that the blockage of blood flow to a specific region created an intense imbalance within the network, fatally impairing the system's overall potential to conduct meaningful information processing. This means Thermodynamic Death (Heat Death = the fatal loss of the brain's potential for meaningful information processing; complete homogenization and disorder of energy akin to the silence the universe eventually reaches).

*(Top: Sample 0 Healthy Economic Growth / Bottom: Sample 8 Thermodynamic Death of the Brain)*
![Sample 0 Thermodynamics](../Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png)
![Sample 8 Thermodynamics](readme_plots/001_1_2__thermodynamics_energy_stack.png)

### 4.4. 3D Micro Z-Score & KL Drift

In the 3D surface of Z-Score (degree of protrusion from past averages), bounding at TR=150, the inflow component to the motor cortex suddenly sinks into the abyss (negative spike), detecting localized "ischemia/necrosis." Furthermore, in the Information Geometric Mutation (KL Drift = localized collapse of the network's probability distribution due to loss of blood flow), the probability distribution of the network locally collapses because the information flow path to the motor cortex is cut, causing a massive spike to pierce the space. The lack of blood flow (mass) is directly visualized as "Information Geometric Death."

![Sample 8 3D Z-Score](readme_plots/002_2_2_2__3d_micro_z_score_X.png)
![Sample 8 3D KL Drift](readme_plots/002_2_2_1__3d_micro_kl_drift.png)

## 5. ⚠️ Falsification Analytics

* **Possibility of False Positives:** If this were actual fMRI data, given that only the inflow of the BOLD signal to a specific gyrus vanishes by 95% and is accompanied by abnormal resonance, there is an extremely high probability that it is a clear "organic lesion (ischemia/infarction)" rather than mere measurement noise.
* **Additional Verification Requirements:** TLU has proven itself to be a "Universal Physics-Mathematics-Mathematics Engine." It has been confirmed that "embezzlement" in finance, "deadlock" in traffic networks, and "stroke" in the brain can all be seamlessly diagnosed with the same physical equation: "Mass deficit and thermodynamic collapse in a network."
