# 🔬 Clinical Meta-Diagnostic Forensic Report: Flow Paralysis & Thermodynamic Death of Urban Traffic Network (Sample 5)

## 1. Executive Summary

* **Overall Diagnosis:** **Urban Traffic Network Localized Thermodynamic Freeze (Kyoto Traffic Grid Deadlock / Severe Localized Freeze)**
* **Severity:** 🟠 **HIGH (Extremely Serious Functional Failure)**
* **Clinical Overview:**
    This system (representing vehicle flow volume data across a 25-intersection network in the center of Kyoto) is a closed kinetic system where the total number of vehicles (mass) is strictly conserved at $U = 2,500,000.0$. However, due to a sudden physical closure of a major intersection (the Shijo-Karasuma bottleneck) in the later stages of the simulation (from Week 52 of 2020 onward), a severe stoppage of flow is occurring in part of the network.

    The physical feature of this anomaly is not macro thermal breakdown or mass leakage, but rather a **"local thermodynamic freeze (solidification/freezing)"**. While the local temperature (流量ボラティリティ $T_i$) at the bottleneck intersection `23_四条烏丸` (Shijo-Karasuma) plummeted from `32.58` to **`1.87`**, entering a "frozen state," an extremely sharp temperature gradient of **`+65.31`** (local thermal stress / cold-island effect) formed between it and the active surrounding intersections.

    Furthermore, at the surrounding upstream intersections (e.g., `21_四条室町` (Shijo-Muromachi)), the local entropy (spatial path dispersion $s_i$) decreased from `1.993` to **`1.674`** because the outflow route was blocked (loss of routing options), propagating severe congestion and deadlocks throughout the flow network. The macro free energy $F$ remains stable at a massive positive value (average $F = 2,480,816.31$), but this merely indicates that the entire system has entered a "thermally frozen state" where it is completely static and crystallized.

---

## 2. Limitations of Traditional Snapshots

If we force-apply the traditional accounting concepts (B/S and P/L) to a traffic network, static aggregated values alone cannot reveal this fatal traffic paralysis. Below are the cumulative flow volume (P/L equivalent) and stock (B/S equivalent) charts across the entire period:

* **P/L Equivalent (Total Traffic Volume per Intersection):**
    ![P/L Trend](readme_plots/000_0_1__PL_Trend.png)
* **B/S Equivalent (Unbalanced Stock Accumulation):**
    ![B/S Trend](readme_plots/000_0_1__BS_Trend.png)

**【Blind Spots of Traditional Aggregates】**
In a "Closed Kinetic System" like a traffic network, the cumulative residual stock of vehicles (B/S equivalent) net out to `$0.00` (zero net variance). On the other hand, the total passing flow volume (P/L equivalent) at each intersection displays a massive volume of `$2,500,000.00`.

A typical traffic monitoring dashboard can identify static rankings of "which intersection has the most traffic," but it cannot evaluate the dynamic health of the flow structure—such as capturing whether vehicles are simply cycling futilely between the same intersections without moving closer to their destinations, or calculating how many minutes remain before the entire system falls silent (countdown to thermodynamic heat death).

---

## 3. Fundamental Pathophysiology

The Physics-Mathematics Engine accurately captures the following structural changes and pathological bottlenecks embedded in the data generation logic (`_0_0_generate_dummy_traffic.py`):

1. **Dynamic Flow Blockage & Back-Up (Shijo-Karasuma Bottleneck)**:
    Starting from Day 360 of the simulation (Week 52 onward), the flow capacity of edges connecting to the major intersection "Shijo-Karasuma" was restricted to a mere **5%** of its normal capacity (simulating road construction or an accident). As inflow was severely restricted, a rapid backflow and accumulation of vehicles occurred at upstream intersections such as `08_三条烏丸` (Sanjo-Karasuma) and `21_四条室町` (Shijo-Muromachi). This was captured as a sudden change in spatiotemporal transition probabilities (a spike in `kl_divergence_drift` to **`1.7629`** in Week 53).
2. **Local Freezing & Topological Constraint (Cooling & Directional Restraint)**:
    Since `23_四条烏丸` (Shijo-Karasuma) itself was almost completely shut off from inflows and outflows, there was no vehicle turnover (flow volatility), causing its local temperature to drop near absolute zero ("thermal freeze"). At the same time, at surrounding intersections, vehicles struggled to find detours, restricting their progress directions (spatial outflow uncertainty) and triggering a significant drop in local entropy, which represents a "loss of topological degrees of freedom."

---

## 4. Mathematical Evidence from the Physics-Mathematics Engine

### 4.1. Strict Mass Conservation & Verification

The Kirchhoff conservation residual (**`System Conservation Residual`** / relative leak ratio) measuring vehicle total mass discrepancy remains at **`0.00` (perfect zero)** throughout the period. This physically proves that this system is defined as a strict closed kinetic system equivalent to double-entry bookkeeping, and not a single vehicle leaked or was created in the data (unlike Samples 2 and 3 where embezzlement or input errors occurred).

* **Macro Forensics Dashboard:**
    ![Macro Forensics](readme_plots/002_2_1__macro_forensics_dashboard.png)

### 4.2. Total Rigidification of Traffic & 3D External Force Resonance

The time-series sequence of the Stiffness Matrix documents how the entire network rigidifies fatally over time.

* **Stiffness Matrix 5-Point Sequence (centered around 2020-W52):**
  * **① Start (t=0 / 2020-W01):**
        ![Stiffness t0](readme_plots/000_2_1__structural_stiffness.t.00000.png)
        At the start of the simulation, no overall stiffness lock has occurred, maintaining a flexible, low-stiffness flow state.
  * **② Pre-Anomaly (t=50 / 2020-W51):**
        ![Stiffness t50](readme_plots/000_2_1__structural_stiffness.t.00050.png)
        Immediately before bottleneck injection. Under daily flow patterns, the PC1 contribution ratio is **`81.41%`** (eigenvalue **`63735.4365`**), with the primary stiffness axes concentrating on `13_二条烏丸` (Nijo-Karasuma) (`-0.5750`) and `07_三条新町` (Sanjo-Shinmachi) (`0.3907`).
  * **③ Onset (t=51 / 2020-W52):**
        ![Stiffness t51](readme_plots/000_2_1__structural_stiffness.t.00051.png)
        Anomaly week. The capacity restriction (5%) at Shijo-Karasuma starts, introducing local strain to the transition probability balance.
  * **④ Paralysis / Peak Drift (t=52 / 2020-W53):**
        ![Stiffness t52](readme_plots/000_2_1__structural_stiffness.t.00052.png)
        Full paralysis occurs. Shijo-Karasuma is completely blocked, creating irreversible bias in upstream transition probabilities and peaking the KL Drift at `1.7629`.
  * **⑤ Chronic Deadlock (t=53 / 2021-W01):**
        ![Stiffness t53](readme_plots/000_2_1__structural_stiffness.t.00053.png)
        Solidification of paralysis. The KL Drift remains high at `0.9154` in the first week of the new year, the local temperature at Shijo-Karasuma remains frozen at `1.87`, and the temperature gradient (`local_grad_t`) reaches `+87.54`, showing transition to a chronic deadlock where local flow friction is permanently fixed.

### 4.3. Topological Strong Connectivity & Spectral Radius Constancy

The "Spectral Radius," which is the maximum eigenvalue of the adjacency connection matrix, remains perfectly fixed at **`1.00`** throughout the period. This is a mathematical consequence (Perron-Frobenius theorem) of the fact that the intersection network is a closed, strongly connected network with bidirectional flows and no external drains.

* **Time-Series Trend of System Stability (Spectral Radius):**
    ![System Stability](readme_plots/004_1_2__system_stability.png)

As shown in the graph, the spectral radius draws a flat line at exactly `1.00`, proving that the network's connection topology is preserved. The occurrence of this anomaly is instead convicted by the **distortion of the adjacency topology transition (KL Divergence Drift) and the sudden shift of the PCA dominant axes**. At the moment of bottleneck injection in Week 52 of 2020, the KL Drift measuring transition probability displacement jumped from a normal average of `0.08` to **`1.7629`** (Week 53), proving a sudden structural phase transition.

* **Network Topology 5-Point Sequence (centered around 2020-W52):**
  * **① Start (t=0 / 2020-W01):**
        ![Topology t0](readme_plots/002_1_2__network_topology.t.00000.png)
        Initial state. Probability flows are evenly dispersed, maintaining healthy dynamic circulation.
  * **② Pre-Anomaly (t=50 / 2020-W51):**
        ![Topology t50](readme_plots/002_1_2__network_topology.t.00050.png)
        Immediately before bottleneck injection. Although seasonal fluctuations exist, the connection patterns show a stable steady state.
  * **③ Onset (t=51 / 2020-W52):**
        ![Topology t51](readme_plots/002_1_2__network_topology.t.00051.png)
        Anomaly week. The capacity restriction (5%) at Shijo-Karasuma starts, introducing local strain to the transition probability balance.
  * **④ Paralysis / Peak Drift (t=52 / 2020-W53):**
        ![Topology t52](readme_plots/002_1_2__network_topology.t.00052.png)
        Full paralysis occurs. Shijo-Karasuma is completely blocked, creating irreversible bias in upstream transition probabilities and peaking the KL Drift at `1.7629`.
  * **⑤ Chronic Deadlock (t=53 / 2021-W01):**
        ![Topology t53](readme_plots/002_1_2__network_topology.t.00053.png)
        Solidification of paralysis. The KL Drift remains high at `0.9154` in the first week of the new year, the local temperature at Shijo-Karasuma remains frozen at `1.87`, and the temperature gradient (`local_grad_t`) reaches `+87.54`, showing transition to a chronic deadlock where local flow friction is permanently fixed.

### 4.4. Thermodynamic "Freezing" & Local Entropy/Temperature Analysis

In macro thermodynamic metrics, for the total number of vehicles (internal energy $U = 2,500,000.0$), the macro free energy $F$ remains stable at a **very high positive value of approximately `2.48 × 10^6`** due to the very small $TS$ term.

Following the gridlock onset in Week 52 of 2020, flow restriction caused the macro entropy $S$ to decrease slightly from `40.50` to **`38.70`**, but local intense friction (velocity variance) drove the macro temperature $T$ up from `457.24` to **`547.06`**, reducing the free energy $F = U - TS$ from `2,481,482` to **`2,478,826`**. This is thermodynamic proof of energy dissipation (entropy loss) due to flow friction.

* **Thermodynamics Energy Stack & 3D Local Plots:**
    ![Thermodynamics Energy Stack](readme_plots/001_1_2__thermodynamics_energy_stack.png)
    ![3D Local Entropy](readme_plots/001_1_2_1__3d_local_entropy.png)
    ![3D Local Temperature](readme_plots/001_1_2_2__3d_local_temperature.png)

The 3D spatiotemporal plots and local spatiotemporal analysis clearly prove the pathological mechanism of this "local freeze":

1. **Local Cooling of the Bottleneck Intersection (Temperature Freeze):**
    At **`23_四条烏丸`** (Shijo-Karasuma) where passing activity was blocked, the local temperature (流量ボラティリティ $T_i$ of flow) plummeted from `32.58` to **`1.87`**, causing a complete thermal freeze. This formed a massive local temperature gradient (`local_grad_t`) of **`+65.31`** (a yellow spire) between it and active neighboring nodes, showing that flow friction is heavily localized.
    ![3D Local Gradient](readme_plots/001_1_2_3__3d_local_gradient.png)
    ![Local Thermo Gradient](readme_plots/001_1_2_6__local_thermo_gradient.png)
2. **Topological Restriction at Upstream Intersections (Entropy Decay):**
    At the upstream intersection **`21_四条室町`** (Shijo-Muromachi) feeding vehicles into Shijo-Karasuma, the options for turn/straight routing (spatial dispersion $s_i$ of outflows) were closed off, dropping local entropy from `1.993` to **`1.674`**. This mathematically indicts the topological rigidity where vehicles are robbed of routing freedom and forced into stagnation.

* **T-S Diagram:**
    ![T-S Diagram](readme_plots/001_1_3__thermodynamics_ts_diagram.png)

The T-S diagram draws an abnormal closed cycle that contracts from the upper-right layer (FY2020) to the lower-left layer (post-accident FY2021), decreasing both entropy and temperature. This is clear evidence that the system's flexible flow capacity (elasticity) has frozen, lock-stepping major intersections into a static gridlock.

### 4.5. 3D Geometric Anomaly Identification & Information Geometric Spikes

The 3D spatiotemporal plots visualize where and when the structural phase transition of the flow (local congestion and backflow) occurred.

* **3D Micro Z-Score (Position):**
    ![3D Micro Z-Score](readme_plots/002_2_2_2__3d_micro_z_score_X.png)
* **3D Micro KL Drift:**
    ![3D Micro KL Drift](readme_plots/002_2_2_1__3d_micro_kl_drift.png)

#### Interpretation of the 3D Plots

1. **3D Micro KL Drift (Phase Transition of Transition Probabilities):**
    In **`2020-W53` (t=52)** when the bottleneck occurred, a giant spatiotemporal spike rises around `23_四条烏丸` (Shijo-Karasuma). This physically identifies the exact moment the flow structure changed due to A/R capacity restriction (5%) that altered upstream routing probabilities.
2. **Astronomical Z-Score Spike at `2021-W18` (t=70):**
    In this plot, long after the accident, a single spatiotemporal spire with a Z-Score of **`612,559.82`** explodes at `23_四条烏丸` (Shijo-Karasuma). This is not a physical influx of vehicles or a breakdown of conservation, but rather a statistical false positive (mathematical illusion of the Z-Score) caused by **"boiled frog syndrome (baseline adaptation)"**.

    * **Mechanism Proof**:
      * After the bottleneck onset (`2020-W52`), flow through Shijo-Karasuma was suppressed, and the net flow velocity (`velocity_v`) flattened to nearly `0` or `1` (complete deadlock).
      * Consequently, the rolling standard deviation (`std`) over the 12-week past window **shrank close to absolute zero (`0.0`)**.
      * In `2021-W18`, a minor fluctuation occurred: passing vehicles increased by only 5 cars (net velocity `velocity_v` increased from `1.0` to `6.0`).
      * Because the standard deviation in the denominator was extremely small, this minor variation was amplified by division, manifesting as a Z-Score spike exceeding **610,000**.
      * By `2021-W19`, this variation was integrated into the past window, resetting the Z-Score to a normal `1.13`.

    This phenomenon demonstrates that static statistical models (Z-scores) adapt to chronic paralysis and misinterpret minor fluctuations as disasters, proving the necessity of information-geometric metrics (such as KL Drift, which remained flat at `0.0004` during W18) to reliably capture structural phase transitions.

---

## 5. LQR Control Treatment

* **Treatment Plan:** **Dynamic Signal Phase Adjustment & Stiffness Lock Mitigation**
* **LQR Sensitivity Intervention (Acupoint Identification):**
    In LQR flow control sensitivity analysis, the nodes showing the highest dynamic intervention sensitivities are `00_一条堀川` (Ichijo-Horikawa), `13_二条烏丸` (Nijo-Karasuma), and `23_四条烏丸` (Shijo-Karasuma) (with sensitivity `41.5234`).
    ![LQR Sensitivity](readme_plots/004_1_3__control_lqr_performance_space.png)
* **Specific Intervention Plan:**
    1. **Signal Phase Disruption:**
       Implement phase offsets (cycle time-difference adjustments) to traffic signal cycles at the bottleneck intersections (Ichijo-Horikawa, Nijo-Karasuma, Shijo-Karasuma) based on LQR feedback. This physically interferes with and breaks up the vehicle recirculation waves, clearing the deadlock.
    2. **Stiffness Softening:**
       Apply temporary gate controls (inflow restrictions) at intersections upstream of stiffness lock hubs (such as `17_五条新町` and `22_四条新町`). Relaxing local joint rigidity restores normal traffic flow (circulation of Qi) across the entire network.

---

## 6. 🚨 Forensic Alert & Falsification Analytics

### 6.1. Triaging Statistical Anomalies

* **Triaging Decision:**
    Temporary surges in traffic (seasonal fluctuations) during tourist seasons scale the entire network's volume, but do not freeze specific intersections or drop local entropy, keeping KL Drift stable.

    Conversely, the data starting from Week 52 satisfies:
    1. **Kirchhoff Residual Conservation:** Macro and micro residuals remain `0.00` (no data corruption).
    2. **Structural Phase Transition:** KL Drift jumps 20-fold to **`1.7629`** (Week 53), indicating structural transition.
    3. **Local Thermodynamic Stress:** Shijo-Karasuma's local temperature drops to `1.87` (freeze) and the temperature gradient (**`+65.31`**) spikes, forming a cold island (bottleneck).

    Thus, we triage this case as a **"flow paralysis due to physical bottleneck closure"** rather than "seasonal congestion."

### 6.2. Falsifiability

To disprove the "paralysis due to Shijo-Karasuma bottleneck" hypothesis, the auditor must present the following **"original documents from outside the database"**:

1. **Road Traffic Logs / Infrastructure Logs:**
    Original management records proving that no road construction, accidents, lane restrictions, or signal failures occurred around Shijo-Karasuma during the target period (especially Week 52 onward), and that lane capacity was 100% maintained.
2. **Taxi Probe GPS logs:**
    Original vehicle GPS trajectory logs (time-series velocity/position data) proving that taxis and probe cars passed through Shijo-Karasuma at normal speeds (e.g., 20–30 km/h) instead of decelerating to 0–5% of normal speeds during the bottleneck weeks.
