# 01. Physics Engine Theory & Data Interpretation Guide

Tensor-Link Utility (TLU) is equipped with 8 main analytical modules (physics-mathematical filters) that assign physical reality such as "mass," "force," "energy," and "viscosity" to abstract network data, and determine systemic anomalies based on structural deformation and energy balance.

This document is a core manual of the TLU system that integrates the **mathematical and physical theoretical foundations (Physics Theory)** of each filter with the **forensic interpretation guide (Data Interpretation)** of the output visualization graphs. We explain the concepts by contrasting and citing actual charts from validation samples (healthy, traffic deadlock, embezzlement, market manipulation, etc.).

---

## 🧭 Table of Contents

0.  [Basic Statistics & Foundation (Prefix: `000_0`)](#0-basic-statistics--foundation-prefix-000_0)
1.  [Structural Stiffness & PCA / Classical Mechanics (Prefix: `000_2`)](#1-structural-stiffness--pca--classical-mechanics-prefix-000_2)
2.  [Kinematics & Dynamic State-Space (Prefix: `000_1`)](#2-kinematics--dynamic-state-space-prefix-000_1)
3.  [Thermodynamics & Entropy (Prefix: `001_1`, `001_2`)](#3-thermodynamics--entropy-prefix-001_1-001_2)
4.  [Information Geometry & Relative Conservation Laws (Prefix: `002_1`, `002_2`)](#4-information-geometry--relative-conservation-laws-prefix-002_1-002_2)
5.  [Inverse Kinematics & Target Reachability (Prefix: `003_1`)](#5-inverse-kinematics--target-reachability-prefix-003_1)
6.  [System Stability & Feedback Control (Prefix: `004_1`, `004_2`)](#6-system-stability--feedback-control-prefix-004_1-004_2)
7.  [Signal Processing & Wave Mechanics (Prefix: `005_1`, `005_2`)](#7-signal-processing--wave-mechanics-prefix-005_1-005_2)

---

## 0. Basic Statistics & Foundation (Prefix: `000_0`)

### 🔬 Physics & Mathematical Theory
Grabs the overall absolute activity level (revenue, assets, total vehicles, etc.) of the system as the "baseline physical capacity and size," and then applies traditional statistical analysis (Probability Density Function KDE, Rolling Quantiles, Skewness, Kurtosis) to temporal variations of the state variables.

In particular, the Z-Score for the system's volatility is defined by the following formula:

$$Z = \frac{x_t - \mu_{window}}{\sigma_{window}}$$

Where $\mu_{window}$ and $\sigma_{window}$ are the rolling mean and standard deviation of a past window (e.g., 12 weeks). An extremely high Z-Score ($Z > 3.0$) or an abnormally high kurtosis (fat tail) indicates vulnerability to "sudden seizures" (Black Swan predisposition) that the system cannot normally tolerate.

### 📊 Data Interpretation & Sample Comparison

*   **Financial & Basic State Graphs:** `000_0_1__BS_Block_Total.png`, `000_0_1__PL_Waterfall_Total.png`, `000_0_1__PL_Trend_Revenue_vs_Expenses.png`
*   **Statistical Distribution Graphs:** `000_0_2_3__histogram_kde.png`, `000_0_2_4__rolling_quantiles.png`, `000_0_2_5__kurtosis_vs_phase.png`

#### 🟢 Healthy Seasonal Fluctuation (Sample 0) vs. 🔴 Camouflaged Wash Trade (Sample 1)
*   **Sample 0:** [Sample 0 P/L Waterfall](../samples/Sample_0_Healthy/readme_plots/000_0_1__PL_Waterfall_Total.png) - Due to seasonal settlement spikes, the liquidity Z-Score temporarily surges to a maximum of `4.90` (July), but since the Kirchhoff residual is `0.00`, it is classified as a "statistical false positive."
*   **Sample 1:** [Sample 1 P/L Trend](../samples/Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Trend.png) - Due to wash trading, revenue appears to be growing steadily, but the supporting SG&A expenses are "completely flat," revealing it is a fictitious journal entry that contradicts the physical expansion of activities.

#### ⚕️ Audit Criteria & Primary Findings
1.  **Skewness and Kurtosis Anomalies:** In KDE distributions and Rolling Quantiles, an extremely long tail (Fat-tail / High Kurtosis) indicates a "fragile constitution where the system is usually calm but suddenly suffers a fatal shock."
2.  **Boiled Frog (Baseline Adaptation):** If the Z-Score remains flat despite chronic pathological activities (high viscosity or mass leakage) detected by other metrics, it indicates that the "statistical model has mistakenly learned the anomaly as the normal baseline."

---

## 1. Structural Stiffness & PCA / Classical Mechanics (Prefix: `000_2`)

### 🔬 Physics & Mathematical Theory
Models the transaction relationships (edges) between nodes in the network as **"Elastic Springs"** based on Hooke's Law.
Calculates the "Stiffness Matrix" $K$ of the system from the partial correlations and flow volatility between nodes:

$$F_{external} = K \cdot \Delta X$$

Where $\Delta X$ is the state displacement of each node (cash balance volatility, intersection congestion, etc.) and $F_{external}$ is the external force.

In a healthy system, the springs flexibly expand and contract to absorb external shocks (elastic state). However, when specific recirculation loops or bottlenecks occur, some springs contract to their limit and solidify, causing **"Stiffness Lock."**

Applying Principal Component Analysis (PCA) to the stiffness matrix $K$ and tracking the time-series evolution of the Explained Variance Ratio of the dominant eigenspace mathematically proves the "mismatched concentration of binding stiffness" across the system.

### 📊 Data Interpretation & Sample Comparison

*   **Stiffness Matrix & PCA Graphs:** `000_2_1__structural_stiffness.t.*.png`, `000_2_2__principal_axes_ratio.png`, `000_2_3__eigenvector_evolution.png`

#### 🟢 Healthy Behavior (Sample 0)
In healthy metabolism (Sample 0), the stiffness matrix between accounts (nodes) exhibits a gentle, unbiased distribution, and the PCA dominance ratio is not hijacked near 100% by any single principal component.
*   **Stiffness Matrix:** [Sample 0 Stiffness (t=6)](../samples/Sample_0_Healthy/readme_plots/000_2_1__structural_stiffness.t.00006.png)
*   **PCA Principal Axes Ratio (PCA Ratio):** [Sample 0 PCA Ratio](../samples/Sample_0_Healthy/readme_plots/000_2_2__principal_axes_ratio.png)
    *   *Key Insight:* Shows a "pliant" topological structure with smooth decay of eigenvalue ratios and no extreme transaction synchronization between specific pairs.

#### 🔴 Abnormal Behavior: Traffic Deadlock (Sample 5)
In urban traffic gridlocks (Sample 5), the structure of the stiffness matrix changes dramatically (phase transition) before and after the bottleneck occurs.
*   **Onset (t=51 / W52):** [Sample 5 Stiffness t51](../samples/Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00051.png) - The outflow capacity of the bottleneck node `23_四条烏丸` (Shijo-Karasuma) is suddenly restricted to 5%, and stiffness load begins to concentrate around `13_二条烏丸` (Nijo-Karasuma).
*   **Paralysis (t=52 / W53):** [Sample 5 Stiffness t52](../samples/Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00052.png) - Full traffic paralysis occurs, with the PC1 contribution ratio marking **`71.77%`** (eigenvalue `56931.13`), strongly locking the surrounding area (thrombus state).
*   **Chronic (t=53 / W54):** [Sample 5 Stiffness t53](../samples/Sample_5_Kyoto_Traffic/readme_plots/000_2_1__structural_stiffness.t.00053.png) - The stiffness lock propagates to detour routes such as `22_四条新町` (Shijo-Shinmachi) and `17_五条新町` (Gojo-Shinmachi), leaving the entire network in "chronic joint rigidity."

#### 🟡 Abnormal Behavior: Market Manipulation Collusion Lock (Sample 7)
In the user funding network (Sample 7), when colluding bot accounts (`USR_003` and `USR_004`) begin matched trades, the PC1 contribution ratio instantly spikes to **`99.67%`**.
*   **Eigenvector Evolution:** [Sample 7 Eigenvector Evolution](../samples/Sample_7_Market_Users_Weekly/readme_plots/000_2_3__eigenvector_evolution.png)
    *   *Key Insight:* At the moment of W41 (`t=40`), the PC1 loading (eigenvector direction) concentrates abnormally on `USR_004` (`0.7287`) and `USR_003` (`-0.6820`), clearly exposing how the mechanical stiffness between these two accounts is locked to almost 100% (dominance by matched orders).

#### ⚕️ Audit Criteria & Primary Findings
1.  **Stiffness Anomalies:** If stiffness is extremely high, we conclude that the "system is rigidified (Rigidity) and fragile to external shocks."
2.  **Principal Axis Collapse (Eigenvector Shift):** If the first and second principal components of PCA swap rapidly, we conclude that the "primary energy route of the organization (main pipe of meridians) has physically reorganized (structural transition)."

---

## 2. Kinematics & Dynamic State-Space (Prefix: `000_1`)

### 🔬 Physics & Mathematical Theory
Visualizes the dynamic process of the system as a state-space trajectory (Phase Portrait). Defines flow resistance or mass transfer delay between nodes as "Viscosity $C$," and defines the scale or inertial mass as "Inertia $J$" based on the equations of motion:

$$F_{external} = J \cdot \ddot{X} + C \cdot \dot{X} + K \cdot X$$

*   **Viscosity:** Flow resistance caused by manual transcription, time lags in accounts receivable collection, road lane reductions, etc.
*   **Inertia:** The overall weight/inertia of the system (huge capital, excess inventory, heavy infrastructure) that slows down direction changes.

The system's behavior is projected onto a 3D state-space phase portrait (Phase Portrait Ribbon Plot) constructed from state variables (position $X$, velocity $v = \dot{X}$, acceleration $a = \ddot{X}$).

### 📊 Data Interpretation & Sample Comparison

*   **Dynamic State-Space Graphs:** `000_1_8__phase_portrait_3d.png`, `000_1_4__3d_dynamics_inertia.png`, `000_1_5__3d_dynamics_viscosity.png`, `000_1_6__3d_dynamics_external_force.png`

#### 🟢 Healthy Convergence (Sample 0) vs. 🔴 Catastrophic Divergence (Sample 4) vs. 🔴 Destructive Resonance (Sample 2)
*   **Sample 0:** [Sample 0 3D Phase Portrait](../samples/Sample_0_Healthy/readme_plots/000_1_8__phase_portrait_3d.png) - The trajectory ribbon stably converges to a very smooth closed loop (limit cycle), showing no irregular bursts or trajectory distortions.
*   **Sample 4:** [Sample 4 3D Dynamics External Force](../samples/Sample_4_Composite_Chaos/readme_plots/000_1_6__3d_dynamics_external_force.png) - As wash trading (over-recirculation) and cash drainage occur simultaneously, the trajectory escapes the stable attractor and diverges infinitely into outer space, representing a "systemic meltdown."
*   **Sample 2:** [Sample 2 3D Dynamics External Force](../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_6__3d_dynamics_external_force.png) - Due to the loss of elastic springs caused by mass (cash) outflow, **a catastrophic abnormal resonance (knocking) reaching the 1 billion (1e9) scale** occurs under external excitation.

#### ⚕️ Audit Criteria & Primary Findings
1.  **Viscosity Levels:** If viscosity (Viscosity) is high, we conclude that the "system relies heavily on analog manual labor and friction, which breeds costs and errors."
2.  **Inertia Mismatch:** If inertia (Inertia) is abnormally concentrated at specific nodes, we conclude that "part of the system is metabolically bloated, robbing the entire system of agility."
3.  **Trajectory (Phase Portrait) Anomalies:** If the trajectory in phase space falls into unpredictable chaos, we determine that the "system's autonomous brakes have failed."

---

## 3. Thermodynamics & Entropy (Prefix: `001_1`, `001_2`)

### 🔬 Physics & Mathematical Theory
Defines the total system activity as "Internal Energy $U$," the dispersion of transition probabilities between nodes (disorder) as "Entropy $S$," and the rate of change of the system over time (flow volatility) as "Temperature $T$." Using these variables, we define the **"Free Energy $F$"**—the remaining potential for the system to maintain its structure and carry out activities:

$$F = U - T \cdot S$$

According to the Second Law of Thermodynamics (entropy increase), friction ($T \times S$) occurs with activity in an irreversible system, causing healthy dissipation of free energy.

However, when pathological recirculation loops exist, the internal energy $U$ is maintained at a high level (futile, rapid movement of money or cars), but it does not lead to meaningful external value transfer or metabolism. Instead, all of it is consumed as useless "frictional heat (entropy loss $T \times S$)," resulting in a rapid depletion of free energy $F$.

Additionally, the "response delay" between nodes is calculated as a "Lag Matrix" to identify meridian blockages (stagnant sectors).

### 📊 Data Interpretation & Sample Comparison

*   **Thermodynamics & Lag Matrix Graphs:** `001_1_1__thermodynamics_dashboard.png`, `001_1_2__thermodynamics_energy_stack.png`, `001_1_3__thermodynamics_ts_diagram.png`, `001_2_1__local_thermo_scatter.png`, `001_2_2__lag_matrix_correlation.png`

#### 🟢 Healthy Growth (Sample 0)
In a healthy business entity (Sample 0), no futile round-trip transactions (friction) occur, so the free energy $F$ grows healthily in tandem with internal energy $U$.
*   **Thermodynamics Energy Stack:** [Sample 0 Energy Stack](../samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png)
    *   *Key Insight:* The solid white line (Free Energy $F$) is not crushed by the maroon area (Friction Loss $TS$), showing healthy metabolism rising strongly as $U$ increases.

#### 🔴 "Freezing" by Traffic Deadlock (Sample 5)
Under intersection capacity restrictions (Sample 5), the overall system entropy $S$ decreased slightly from `40.50` to `38.70`, but local intense friction (velocity variance) caused the macro temperature $T$ to spike from `457.24` to **`547.06`**.
Consequently, dissipation loss ($TS$) increased, and free energy $F$ dropped from `2,481,482` to **`2,478,826`**.
*   **Thermodynamics Energy Stack:** [Sample 5 Energy Stack](../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_2__thermodynamics_energy_stack.png)
*   **T-S Diagram:** [Sample 5 T-S Diagram](../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_3__thermodynamics_ts_diagram.png)
    *   *Key Insight:* In the T-S diagram, a "closed abnormal loop" is drawn after the anomaly triggers, shifting from the upper-right layer (FY2020) to the lower-left layer (post-accident FY2021). This indicates "thermal death" where the entire system has lost its flexible flow capability.
*   **3D Local Temperature & Entropy Plots:**
    *   [Sample 5 3D Local Temperature](../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_2_2__3d_local_temperature.png) - The local temperature $T_i$ of the accident intersection `23_四条烏丸` (Shijo-Karasuma) plummeted from `32.58` to **`1.87`**, forming a chilled "cold island (frozen state)."
    *   [Sample 5 3D Local Entropy](../samples/Sample_5_Kyoto_Traffic/readme_plots/001_1_2_1__3d_local_entropy.png) - The local entropy $s_i$ of the upstream node `21_四条室町` (Shijo-Muromachi) decreased from `1.993` to **`1.674`** (topological restriction where vehicles are robbed of routing options).

#### ⚕️ Audit Criteria & Primary Findings
1.  **Negative Skewness of Entropy:** If entropy exhibits extreme negative skewness, we conclude that "artificial market manipulation or heavy-handed intervention has forcibly suppressed the natural fluctuations of the system."
2.  **Free Energy Depletion:** If F decreases while S increases, we conclude that the organization is "swallowed by inefficient chaos (wasted overhead and friction)."
3.  **Lag (Delay) Concentration:** If lag is abnormally high between specific nodes in the Lag Matrix (`001_2_2__lag_matrix_correlation.png`), we determine that "information transfer or financial settlement is bottlenecked there (meridian blockage)."

---

## 4. Information Geometry & Relative Conservation Laws (Prefix: `002_1`, `002_2`)

### 🔬 Physics & Mathematical Theory
In a closed network, Kirchhoff's First Law (Current Law = Mass Conservation Law) holds strictly.
The difference between the total inflow and total outflow at any node is defined as the **"Conservation Residual"** or the **"Relative Leak Ratio"**:

$$Residual_i = \sum Flux_{in} - \sum Flux_{out}$$

In healthy accounting or physical distribution, this value is always `0.00` (zero error). If a positive value occurs, it mathematically proves that unexplained mass (funds, blood) is bypassing the system (major hemorrhage, embezzlement).

Furthermore, the displacement of the system's state probability distribution (the momentum of structural change) is measured as **"KL Divergence Drift"** on the information manifold. This allows sharp detection of structural ruptures even in situations where the traditional statistical Z-score remains silent due to model pollution (boiled frog syndrome).

### 📊 Data Interpretation & Sample Comparison

*   **Topology & Forensic Graphs:** `002_1_2__info_stress_scatter.png`, `002_1_2__network_topology.t.*.png`, `002_1_3__manifold_dimensionality.png`, `002_2_1__macro_forensics_dashboard.png`, `002_2_2__micro_forensics_scatter.png`, `002_2_2_1__3d_micro_kl_drift.png`, `002_2_2_2__3d_micro_z_score_X.png`

#### 🔴 "Mass Deficit" due to Financial Embezzlement (Sample 2)
In cash embezzlement (Sample 2), collected funds are not deposited into the correct bank account but are siphoned off-book.
*   **Macro Forensics Monitoring Dashboard:**
    *   [Sample 0 Healthy Dashboard](../samples/Sample_0_Healthy/readme_plots/002_2_1__macro_forensics_dashboard.png) - Residuals remain perfectly on a flat `0.00` line.
    *   [Sample 2 Embezzlement Dashboard](../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png) - Residuals spike to a maximum of **`364.53`** during embezzlement steps, exposing a cumulative **`$1,353.48`** "mass deficit" with flawless mathematical precision.

#### 🟡 "Temporary Distortion" due to Input Error (Sample 3)
In a single-sided journal entry error (Sample 3), residuals temporarily spike up to **`906.29`** and KL Drift reaches **`20.68`**, but the system self-heals (reverts to zero) immediately in the next step when the correction entry is made.
*   **3D Micro KL Drift (Transient Spike):** [Sample 3 3D Micro KL Drift](../samples/Sample_3_Unbalanced_Mistake/readme_plots/002_2_2_1__3d_micro_kl_drift.png)
    *   *Key Insight:* A very sharp single needle-like spike (castle wall) towers only in `2020-02` when the anomaly occurred, but it returns to a completely flat meadow in the next step. This is easily identified as a "temporary noise" where system elasticity is preserved.

#### 🟡 Information Geometric Spike due to Collusive Trading (Sample 7)
In market manipulation (Sample 7), high-speed matched orders by a collusive group trigger drastic changes in information geometric transition probabilities.
*   **3D Micro KL Drift (Clique Wall):** [Sample 7 3D Micro KL Drift](../samples/Sample_7_Market_Users_Weekly/readme_plots/002_2_2_1__3d_micro_kl_drift.png)
    *   *Key Insight:* Along the coordinate axes of retail investors who fell into panic selling (e.g., `USR_010`), a **"geometric fortress wall"** stands tall, far exceeding the background noise of normal trading. This proves the aftermath of the market's liquidity being hijacked by the specific collusive relationship (PC1).

#### ⚕️ Audit Criteria & Primary Findings
1.  **Meridian Rupture (Edge Stress):** If transaction (edge) stress becomes `0.00`, it means that the substantive trade or vehicle flow between nodes has stopped, paralyzing (thrombosing) the pipe.
2.  **Major Hemorrhage (Mass Leakage):** If the mass conservation residual is greater than `0.00`, we immediately draw the most serious forensic alert: "physical off-book mass leakage."
3.  **Source Identification:** Locate sharp temporal and spatial peaks in the 3D Micro KL Drift / Z-Score plots to identify the exact transaction and time steps as the "true anomaly source (pathological focus)."

---

## 5. Inverse Kinematics & Target Reachability (Prefix: `003_1`)

### 🔬 Physics & Mathematical Theory
Maps business targets (KPIs) or network control targets as the **"End-Effector (hand position)"** of a multi-joint robot arm, and models the operating potential of each sector or transaction account as **"Arm Joint Angles (joints)."**

Using Forward Kinematics (FK), we calculate the performance space reachable from the current structure, and conversely, solve the **"Inverse Kinematics (IK)"** for ambitious target KPIs to backtrack the required joint angles (load allocation for each department).

$$Target\_KPI = FK(Joint\_Angles)$$
$$Joint\_Angles_{required} = IK(Target\_KPI)$$

If IK cannot be solved due to geometrical limits of the arm (singularities or joint range limits), or if the Reachability Error is abnormally high, it objectively proves that the target is "physically unreachable" under the current organizational or traffic infrastructure.

### 📊 Data Interpretation & Sample Comparison

*   **IK Optimization Simulation Plot:** `003_1_2__3d_kinematics_ik.png`

#### 🔴 Visualization of Target Reachability Limit (Sample 5)
In urban traffic with injected bottlenecks (Sample 5), no matter how vehicles are rerouted, it is difficult to achieve target vehicle throughput due to the fluid dynamic saturation limits around the bottleneck.
*   **3D Kinematics IK Space Ribbon:** [Sample 5 3D Kinematics IK](../samples/Sample_5_Kyoto_Traffic/readme_plots/003_1_2__3d_kinematics_ik.png)
    *   *Key Insight:* Shows "range collapse" where the arm's trajectory ribbon folds into a specific plane and is sucked into a singularity (loss of degrees of freedom due to deadlock).

---

## 6. System Stability & Feedback Control (Prefix: `004_1`, `004_2`)

### 🔬 Physics & Mathematical Theory
Describes network state transitions using discrete state equations:

$$X(t+1) = A \cdot X(t) + B \cdot u(t)$$

Where $A$ is the network adjacency connection probability matrix, $u(t)$ is the control input, and $B$ is the input path.
Monitors the **"Spectral Radius (Spectral Radius $\rho$)"**, which is the maximum eigenvalue of the connection matrix $A$:

$$\rho = \max_{i} |\lambda_i|$$

If $\rho < 1.0$, the system has self-damping capability (stability). However, if a fictitious fund recirculation loop (wash trade) or intersection gridlock is formed, the spectral radius saturates at (or approaches) the boundary value of **`1.0`**, trapping the system's energy in a closed loop and making it uncontrollable.

Using Linear Quadratic Regulator (LQR) control theory, TLU calculates the feedback gain $K_{lqr}$ required to pull the system back to a healthy steady state, and identifies the **"most effective intervention node (acupoint: node with maximum Acupressure Score)"** from the sensitivity matrix (Sensitivity Matrix):

$$u(t) = -K_{lqr} \cdot X(t)$$

### 📊 Data Interpretation & Sample Comparison

*   **Stability & LQR Control Graphs:** `004_1_2__system_stability_dashboard.png`, `004_1_3__control_lqr_performance_space.png`, `004_2_1__sensitivity_matrix.png`

#### 🔴 Boundary Saturation of System Stability (Sample 5, 7)
*   **Traffic Gridlock Stability:** [Sample 5 Stability Graph](../samples/Sample_5_Kyoto_Traffic/readme_plots/004_1_2__system_stability.png)
*   **Collusive Fund Transfer Stability:** [Sample 7 Stability Graph](../samples/Sample_7_Market_Users_Weekly/readme_plots/004_1_2__system_stability.png)
    *   *Key Insight:* The spectral radius clings to a flat horizontal line at exactly `1.00`, proving that the system has completely lost its autonomous damping capability and has formed a closed permanent attractor (deadlock) due to pathological recirculation.

#### ⚕️ Acupoint Identification via LQR Sensitivity
*   **Sample 5 LQR Control Sensitivity Space:** [Sample 5 LQR Space](../samples/Sample_5_Kyoto_Traffic/readme_plots/004_1_3__control_lqr_performance_space.png)
*   **Sample 7 LQR Control Sensitivity Space:** [Sample 7 LQR Space](../samples/Sample_7_Market_Users_Weekly/readme_plots/004_1_3__control_lqr_performance_space.png)
    *   *Key Insight:* "Sharp yellow peaks" on the graph point to nodes with the highest intervention sensitivity. In Sample 5, these are `23_四条烏丸` (Shijo-Karasuma) and `13_二条烏丸` (Nijo-Karasuma) (sensitivity `41.52`), and in Sample 7, they are the recirculation hubs `USR_003` and `USR_004`. This indicates that applying dynamic limits to these nodes can disrupt the recirculation loop at the lowest intervention cost.

---

## 7. Signal Processing & Wave Mechanics (Prefix: `005_1`, `005_2`)

### 🔬 Physics & Mathematical Theory
In a healthy system (natural commerce, daily traffic, resting brain neurons), countless independent decision-making nodes are involved, so the combined frequency spectrum exhibits **"1/f noise (Fractal Noise)."**

In contrast, in pathological states like collusion between malicious trading bots or epileptic seizures, specific nodes coordinate timing down to the millisecond, causing wave-mechanical **"Phase Coherence"** and a sharp drop in the fractal slope of the 1/f noise, resulting in the "death of diversity."

TLU calculates **"Phase Drift"** and coherence matrices to measure time-series changes in phase differences between nodes, exposing "hidden forced synchronization" that statistical models cannot detect.

### 📊 Data Interpretation & Sample Comparison

*   **Wave & Noise Spectrum Graphs:** `005_1_1__resonant_frequency.png`, `005_1_2__phase_drift_heatmap.png`, `005_2_1__fractal_noise_spectrum.png`

#### 🟡 Exposing Bot Synchronous Trading (Sample 7)
In ultra-high-speed matched orders in stock markets (Sample 7), the phase difference between two colluding parties is locked close to zero.
*   **Phase Drift Heatmap:** [Sample 7 Phase Drift Heatmap](../samples/Sample_7_Market_Users_Weekly/readme_plots/005_1_2__phase_drift_heatmap.png)
    *   *Key Insight:* Only between the specific user pair (`USR_003` and `USR_004`) does the variance in phase difference completely vanish, creating a pitch-black band (phase difference `0.00`) on the heatmap. This is wave-mechanical proof of market manipulation, showing they are not ordering independently and randomly, but are "perfectly synchronized to play catch in milliseconds."

#### ⚕️ Audit Criteria & Primary Findings
1.  **1/f Noise Slope Anomaly:** If the frequency spectrum deviates from healthy pink noise and becomes completely flat (white) or Brownian (brown), we conclude that "diversity is lost, and the system is synchronized and dominated by specific algorithms or powerful players."
2.  **Detection of Complete Synchronization:** If the waveforms of specific nodes are perfectly synchronized (phase difference `0.00`) in the phase heatmap, we diagnose it as "abnormal phase co-occurrence impossible in nature, representing artificially orchestrated recirculation fraud (Wash Trade)."
