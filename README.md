# 🔬 Tensor-Link Utility (TLU)

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-red.svg)](https://www.gnu.org/licenses/agpl-3.0.html)
[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Docker Status](https://img.shields.io/badge/Docker-Compatible-emerald.svg)](https://www.docker.com/)

### Visualizing "Interaction Data" via Mathematical Physics Analysis

Tensor-Link Utility (TLU) is a platform that visualizes pathological anomalies within data.
The mathematical physics conclusion of TLU is as follows:
"Even if you perform sham transactions or window dressing on journal ledgers, it is impossible to deceive the law of conservation of mass (balance-sheet equivalence principle) or the laws of thermodynamics."

TLU redefines time-series data as "force flows." Targets include double-entry bookkeeping, urban traffic, stock markets, and brain fMRI. TLU uses an elastic network model. Various anomalies occur within the system (embezzlement, wash trading, deadlock, market manipulation, brain stroke, and seizures). TLU visualizes these as mathematical physics signatures (stiffness collapse, pathological resonance, thermal anomalies, correlation anomalies, etc.).

The mathematical physics engine outputs various metrics. An AI agent decodes these metrics using [`LLM_Diagnostic_Manual.md`](docs/LLM_Diagnostic_Manual.md) to translate them into a clinical-style diagnostic report.

---

## 📚 Documentation Map

All documents are integrated under the `docs/` directory. Below is the mapping between the English and Japanese versions:

| # | Document Title (English) | Corresponding Japanese Version | Core Content |
| :---: | :--- | :--- | :--- |
| **1** | **000-005 Mathematical Analysis Guides** (placed in `samples/`):<br>・**[000_0: Statistics](docs/samples/000_0_Basic_Statistics.md)** / **[000_1: Kinematics](docs/samples/000_1_Dynamics_Kinematics.md)** / **[000_2: Stiffness & PCA](docs/samples/000_2_Stiffness_PCA.md)**<br>・**[001_1: Thermodynamics](docs/samples/001_1_Thermodynamics.md)** / **[001_2: Local Entropy](docs/samples/001_2_Local_Entropy.md)** / **[001_3: Local Temperature](docs/samples/001_3_Local_Temperature.md)** / **[001_4: Local Energy Gradient](docs/samples/001_4_Local_Gradient.md)** / **[001_5: Local Internal Energy](docs/samples/001_5_Local_Internal_Energy.md)**<br>・**[002_1: Information Geometry](docs/samples/002_1_Information_Geometry.md)** / **[002_2: Conservation & Auditing](docs/samples/002_2_Forensics.md)**<br>・**[003_1: Kinematics](docs/samples/003_1_Kinematics.md)**<br>・**[004_1: LQR Control](docs/samples/004_1_Control_Theory.md)** / **[004_2: Intervention Sensitivity](docs/samples/004_2_Stability.md)**<br>・**[005_1: Wave Mechanics](docs/samples/005_1_Wave_Mechanics.md)** / **[005_2: 1/f Fluctuation](docs/samples/005_2_Coherence.md)** | 000〜005番系 数理解析ガイド（`samples/` 以下に配置）：<br>・**[000_0: 統計](docs/ja/samples/000_0_Basic_Statistics.md)** / **[000_1: 運動学](docs/ja/samples/000_1_Dynamics_Kinematics.md)** / **[000_2: 剛性・PCA](docs/ja/samples/000_2_Stiffness_PCA.md)**<br>・**[001_1: 熱力学](docs/ja/samples/001_1_Thermodynamics.md)** / **[001_2: 局所エントロピー](docs/ja/samples/001_2_Local_Entropy.md)** / **[001_3: 局所温度](docs/ja/samples/001_3_Local_Temperature.md)** / **[001_4: 局所エネルギー・勾配](docs/ja/samples/001_4_Local_Gradient.md)** / **[001_5: 局所内部エネルギー](docs/ja/samples/001_5_Local_Internal_Energy.md)**<br>・**[002_1: 情報幾何](docs/ja/samples/002_1_Information_Geometry.md)** / **[002_2: 保存則・監査](docs/ja/samples/002_2_Forensics.md)**<br>・**[003_1: 逆運動学](docs/ja/samples/003_1_Kinematics.md)**<br>・**[004_1: LQR制御](docs/ja/samples/004_1_Control_Theory.md)** / **[004_2: 介入感度](docs/ja/samples/004_2_Stability.md)**<br>・**[005_1: 波動力学](docs/ja/samples/005_1_Wave_Mechanics.md)** / **[005_2: 1/fゆらぎ](docs/ja/samples/005_2_Coherence.md)** | Core theory and diagnostic guidelines for TLU's 8 major core modules (000–005 series), reorganized into diagnostic guides containing visualization plots for all 10 validation samples. |
| **2** | **[System Architecture & Simulation Operations Guide](docs/System_Architecture_and_Operations.md)** | **[システムアーキテクチャとシミュレーション運用ガイド](docs/ja/System_Architecture_and_Operations.md)** | Operations guide for pipelines/containers, JSON theme management, custom data generators with built-in anomalies, and LQR optimal control models. |
| **3** | **[LLM Diagnostic Manual (Supreme prompt & Operations)](docs/LLM_Diagnostic_Manual.md)** | **[LLM メタ検査マニュアル（最高メタレベルシステムプロンプト＆運用手順）](docs/ja/LLM_Diagnostic_Manual.md)** | Protocol for AI to automatically generate objective diagnostic reports from metrics output by the math-physics engine, enforcing false-positive verification and raw data fact-checking. |
| **4** | **[Universal Forensic Cross-Verification Registry](docs/samples/README.md)** | **[数理解析ガイド＆検証サンプル総合目次](docs/ja/samples/README.md)** | Diagnostic matrix, mathematical parameter threshold limits, and LQR intervention point guidelines for all 10 validation samples. |

---

## ⚕️ Core Paradigm: Network Dynamics as a Physical Medium

TLU models transaction data as a continuous elastic network connected by mass-spring-damper elements.

![Mass-Spring-Damper Model](docs/readme_plots/Mass-Spring-Damper-Model.jpg)
*Figure 1: Conceptual diagram modeling ledger accounts as a mass-spring-damper system*

### Clinical Metaphor: Eastern Medicine (Qi, Blood, and Fluids)

TLU uses terminology from Eastern medicine. The system is diagnosed as a network of "meridians" (transaction paths) where "Qi, Blood, and Fluids" (funds and activity flows) circulate. TLU identifies locations where blood flow is blocked and clots are formed (stiffness locking or traffic deadlock) or where severe bleeding is occurring (capital leaks or embezzlement). It uses Linear Quadratic Regulator (LQR) control theory to identify "acupuncture points" (critical intervention points) to restore normal circulation.

### Mapping Table: From Target Domains to Physical Space

| Physical Variable | Definition in Classical Mechanics & Thermodynamics | Financial Accounting Domain | Urban Traffic Domain | Financial Market Domain | Biological Brain fMRI Domain |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mass ( $m_i$ )** | Inertia / Energy storage tank | Account balance | Vehicles at intersection | Account assets | BOLD signal change |
| **Flux ( $f_{ij}$ )** | Velocity / Mass transport | Transaction amount | Vehicles per second | Trade value | Effective connectivity |
| **Stiffness ( $k_{ij}$ )** | Elasticity / Spring constant | Account connection strength | Road capacity limit | Synchronization level | Functional coherence |
| **Viscosity ( $c_{ij}$ )** | Friction / Damper damping | Payment terms (30–90 days) | Traffic drag / Delay | Execution delay (latency) | Signal propagation latency |
| **Entropy ( $S$ )** | Disorder / Frictional heat loss | Sham circular trading (revenue inflation) | Frictional heat from congestion | Wash trading between USRs | Neural hyper-synchrony (seizure) |
| **Free Energy ( $F$ )** | Available work potential | Net operating profit after tax | Vehicle flow potential | Market allocation efficiency | Brain cognitive capacity |
| **Acupuncture Point (LQR)** | Control input vector | Key audit accounts | Traffic light timing adjustment | Specific USR trade restriction | Target TMS stimulation point |

---

## 🔬 4 Spatiotemporal Physical Signatures

TLU extracts 4 physical signatures to detect anomalies within the system.

### 1. Macro Forensics (Conservation of Mass & Kirchhoff's Law)

Verifies whether the inflow and outflow of the entire system balance. When funds are hidden outside the ledger, the conservation of mass breaks, causing a massive spike in the forensic residual plots.

* **🟢 Healthy (Sample 0):** The residual remains exactly `0.00` across all steps. This physically proves there are no cash leaks.
* **🚨 Mass Leak (Sample 2 / Embezzlement):** Bypasses recovered accounts-receivable cash to a hidden node. Mass conservation breaks, and the absolute value of the residual is detected as a positive spike.

| Healthy steady-state (Sample 0) | Pathological Mass Leak (Sample 2) |
| :---: | :---: |
| ![Macro Forensics Normal](samples/Sample_0_Healthy/readme_plots/002_2_1__macro_forensics_dashboard.png) | ![Macro Forensics Abnormal](samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png) |
| *Figure 2a: (Top) Conservation is maintained (residual = 0)* | *Figure 2b: (Top) Residual spike detected during embezzlement* |

---

### 2. Topology & System Stability (Spectral Radius $\rho$ )

Calculates the spectral radius, which is the maximum eigenvalue of the transition matrix, to verify whether circular loops (self-cycling) are formed in the network. If the spectral radius locks at the warning boundary of `1.00`, the system is locked in a closed loop and diverges. TLU mathematically proves this.

* **🟢 Healthy (Sample 0):** The spectral radius stays below `0.00` across all steps. This indicates that transactions do not cycle and converge normally.
* **🚨 Locked Loop (Sample 4 / Composite Chaos):** Circular transactions cause the spectral radius to rise sharply to a maximum of `0.79`, proving the formation of a sham loop.

| Healthy steady-state (Sample 0) | Pathological Loop (Sample 4) |
| :---: | :---: |
| ![System Stability Normal](samples/Sample_0_Healthy/readme_plots/004_1_2__system_stability.png) | ![System Stability Abnormal](samples/Sample_4_Composite_Chaos/readme_plots/004_1_2__system_stability.png) |
| *Figure 3a: Spectral radius converging in a safe zone* | *Figure 3b: Spectral radius rising toward the limit boundary* |

---

### 3. Thermodynamic Energy Stack (System Fatigue & Thermal Death)

Calculates the free energy ($F = U - TS$), representing the work capacity of the system. If $F$ drops below zero, the system falls into thermal death. The more activity ($U$) the system performs, the more useless frictional heat (entropy $TS$) is generated, exhausting the system.

* **🟢 Healthy (Sample 0):** The free energy stays positive. It shows a metabolic process where stored energy grows proportionally with activity.
* **🚨 Thermal Death (Sample 8 / fMRI Stroke):** Blood flow to the motor cortex is blocked, freezing functional connectivity and causing entropy $S$ to plunge. Meanwhile, frictional heat (macro temperature $T$) spikes, causing free energy $F$ to plunge. The system sinks into thermal death.

| Healthy steady-state (Sample 0) | Pathological Thermal Death (Sample 8) |
| :---: | :---: |
| ![Thermodynamics Normal](samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png) | ![Thermodynamics Abnormal](samples/Sample_8_fMRI_Stroke/readme_plots/001_1_2__thermodynamics_energy_stack.png) |
| *Figure 4a: Healthy accumulation of free energy* | *Figure 4b: Free energy plunging to zero (thermal death)* |

---

### 4. 3D Spatiotemporal Geometry Distortion (KL Drift & Local Temperature)

Models the probability distribution of each node as a 3D geometric manifold. When anomalies occur (traffic deadlock at an intersection, collusion among specific accounts, or stroke), a sharp, yellow-green "needle tower" rises in a flat space.

* **🟢 Healthy (Sample 0):** Except for edge effects in the initial steps due to data sparsity, the manifold remains flat and blue.
* **🚨 Manifold Distortion (Sample 5 / Traffic Deadlock):** Blocking intersection `23_Shijo_Karasuma` collapses the distribution. A sharp tower rises at the exact coordinates and time step, reaching over 600,000.

| Healthy steady-state (Sample 0) | Spatiotemporal Manifold Distortion (Sample 5) |
| :---: | :---: |
| ![3D Space Normal](samples/Sample_0_Healthy/readme_plots/002_2_2_2__3d_micro_z_score_X.png) | ![3D Space Abnormal](samples/Sample_5_Kyoto_Traffic/readme_plots/002_2_2_2__3d_micro_z_score_X.png) |
| *Figure 5a: Flat and calm geometric manifold* | *Figure 5b: Geometric distortion pointing precisely to the anomaly origin and timestamp* |

---

## 📂 10 Verification Case Studies

TLU includes 10 sample datasets to verify the accuracy of the mathematical physics engine.

| ID | Case Study (Report Link) | Domain | Status | Key Metrics | Clinical Metaphor |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **0** | **[🟢 Healthy Metabolism (Healthy)](samples/Sample_0_Healthy/README.md)** | Finance | **NORMAL** | $\rho$ = 0.00, Residual = 0.00 | Qi and Blood running smoothly |
| **1** | **[🟡 Circular Trade / Wash Trade](samples/Sample_1_Wash_Trade/README.md)** | Finance | **HIGH** | $\rho$ = 0.75, Depleted Free Energy | Qi and Blood idling in a closed loop |
| **2** | **[🔴 Embezzlement Leak](samples/Sample_2_Embezzlement_Leak/README.md)** | Finance | **CRITICAL** | Max Residual = 364.53, Terminal resonance | Bleeding from meridian, mass leak |
| **3** | **[🟡 Simple Bookkeeping Mistake (Unbalanced Mistake)](samples/Sample_3_Unbalanced_Mistake/README.md)** | Finance | **WARNING** | Transient residual and KL tower | Temporary imbalance, self-healing |
| **4** | **[🔴 Composite Chaos](samples/Sample_4_Composite_Chaos/README.md)** | Finance | **CRITICAL** | $\rho$ = 0.79, Max Residual = 4,773.57 | Bleeding and looping of Qi and Blood |
| **5** | **[🔴 Urban Traffic Deadlock (Kyoto Traffic)](samples/Sample_5_Kyoto_Traffic/README.md)** | Traffic | **CRITICAL** | $\rho$ = 1.00, Macro Temp $T$ = 16,264.61 | Blocked meridian, stasis, static convection |
| **6** | **[🟢 Market Stock Flow (Market Bipartite)](samples/Sample_6_Market_Stock_Flow/README.md)** | Market | **NORMAL** | $\rho$ = 1.00, Residual = 0.00 | Stock fluid equilibrium, steady convection |
| **7** | **[🟢 Market Cash Flow](samples/Sample_7_Market_Cash_Flow/README.md)** | Market | **NORMAL** | $\rho$ = 1.00, Residual = 0.00 | Cash fluid equilibrium, steady convection |
| **8** | **[🔴 Brain stroke model fMRI (fMRI Stroke)](samples/Sample_8_fMRI_Stroke/README.md)** | Brain | **CRITICAL** | 95% path block, Stiffness Lock | Blocked brain meridian, local necrosis |
| **9** | **[🔴 Seizure model fMRI (fMRI Seizure)](samples/Sample_9_fMRI_Seizure/README.md)** | Brain | **CRITICAL** | $\rho$ = 1.00, falling entropy | Neural hyper-synchrony, runaway Qi |

---

## ⚕️ LQR Optimal Control for Dynamic Intervention

TLU detects anomalies and designs interventions. It uses a state-space model to calculate Linear Quadratic Regulator (LQR) control. This identifies acupuncture points (sensitive nodes). Targeting these nodes stabilizes the system with minimal effort (Cumulative Control Effort > 0.00).

| Financial Market (Sample 7) | Neuroscience (Sample 9) |
| :---: | :---: |
| ![Intervention in Market Hubs](samples/Sample_7_Market_Cash_Flow/readme_plots/004_1_3__control_lqr_performance_space.png) | ![Intervention in Seizure Focus](samples/Sample_9_fMRI_Seizure/readme_plots/004_1_3__control_lqr_performance_space.png) |
| *Figure 6a: Identifying market manipulation hubs (`USR_004` and `USR_005`)* | *Figure 6b: Identifying the epilepsy seizure focus in the temporal lobe (`Temporal_Lobe`)* |

---

## 🚀 Environment & Quick Start (Docker)

TLU uses stateless Docker containers and Test-Driven Development (TDD) to eliminate environment bias and human error.

#### Setup: Custom Data Analysis

To analyze custom data, place these files in the `workspace/` directory:

1. **Transaction Flow Data (`workspace/input_stream/`)**: A time-series CSV. It requires `Trans_Date` (Date), `Account_Name` (Account Name), `Debit` (Inflow), and `Credit` (Outflow).
2. **Account Mapping Dictionary (`workspace/config/_account_mapping.csv`)**: Defines mappings of ledger accounts to TLU categories (Asset, Liability, Revenue, etc.).

#### Pipeline Execution Steps

```bash
# 1. Clone the repository
git clone https://github.com/renpoo/TLU.git
cd TLU

# 2. Start Docker containers
docker compose up -d

# 3. Run the pipeline (Sample 1: Wash Trade simulation example)
bash bin/batch_processing.sh --target_env "samples/Sample_1_Wash_Trade"
bash bin/batch_visualize_graphs.sh --target_env "samples/Sample_1_Wash_Trade"
```

---

## ⚠️ Falsifiability & Limits of Clinical Models

TLU acts as an evidence generator. It only outputs physical and mathematical facts.

Legal or moral intent (whether an anomaly represents a crime like embezzlement/window dressing/manipulation, or a benign clerical error/legitimate transaction) is not for TLU or the AI to decide. Humans must investigate. Use the calculated physical metrics and spatiotemporal coordinates to check real-world proof (bank statements, raw exchange logs, tissue biopsies, etc.) to confirm the final diagnosis. This field investigation remains the decisive factor.

---

**License**: AGPL-3.0  
**Developer**: Renpoo & Google Gemini Agent (Antigravity)
