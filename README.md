# 🔬 Tensor-Link Utility (TLU)

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-red.svg)](https://www.gnu.org/licenses/agpl-3.0.html)
[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Docker Status](https://img.shields.io/badge/Docker-Compatible-emerald.svg)](https://www.docker.com/)

### Visualizing "Interaction Data" via Mathematical Physics Analysis

Tensor-Link Utility (TLU) is a platform. It models and visualizes time-series transaction streams as forces flowing through an elastic network.
The core physical principle is that no matter how transaction streams are manipulated, they cannot violate the laws of conservation of mass or thermodynamics. Physics exposes the fraud.
TLU redefines transaction streams from bookkeeping, urban traffic, stock markets, and brain fMRI as flows in a spring-mass-damper system. It extracts physical signatures like stiffness locking, resonance, and thermal anomalies to detect embezzlement, wash trading, deadlocks, market manipulation, strokes, and seizures.
The system metrics are parsed by a companion AI agent using [LLM_Diagnostic_Manual.md](docs/LLM_Diagnostic_Manual.md) to generate a clinical-style meta-diagnosis report.

---

## 📚 Documentation Map

All documents are in `docs/`. Below is the integrated mapping between the English and Japanese versions:

| # | Document Title (English) | Corresponding Japanese Version | Core Content |
| :---: | :--- | :--- | :--- |
| **1** | - **[000_0: Statistics](docs/samples/000_0_Basic_Statistics.md)** <br>- **[000_1: Kinematics](docs/samples/000_1_Dynamics_Kinematics.md)** <br>- **[000_2: Stiffness & PCA](docs/samples/000_2_Stiffness_PCA.md)**<br>- **[001_1: Thermodynamics](docs/samples/001_1_Thermodynamics.md)** <br>- **[001_2: Local Entropy](docs/samples/001_2_Local_Entropy.md)** <br>- **[001_3: Local Temperature](docs/samples/001_3_Local_Temperature.md)** <br>- **[001_4: Local Energy Gradient](docs/samples/001_4_Local_Gradient.md)**<br>- **[001_5: Local Internal Energy](docs/samples/001_5_Local_Internal_Energy.md)**<br>- **[002_1: Information Geometry](docs/samples/002_1_Information_Geometry.md)** <br>- **[002_2: Conservation & Auditing](docs/samples/002_2_Forensics.md)**<br>- **[003_1: Kinematics](docs/samples/003_1_Kinematics.md)**<br>- **[004_1: LQR Control](docs/samples/004_1_Control_Theory.md)** <br>- **[004_2: Intervention Sensitivity](docs/samples/004_2_Stability.md)**<br>- **[005_1: Wave Mechanics](docs/samples/005_1_Wave_Mechanics.md)** / **[005_2: 1/f Fluctuation](docs/samples/005_2_Coherence.md)** | - **[JA Link (000_0)](docs/ja/samples/000_0_Basic_Statistics.md)**<br>- **[JA Link (000_1)](docs/ja/samples/000_1_Dynamics_Kinematics.md)**<br>- **[JA Link (000_2)](docs/ja/samples/000_2_Stiffness_PCA.md)**<br>- **[JA Link (001_1)](docs/ja/samples/001_1_Thermodynamics.md)**<br>- **[JA Link (001_2)](docs/ja/samples/001_2_Local_Entropy.md)**<br>- **[JA Link (001_3)](docs/ja/samples/001_3_Local_Temperature.md)**<br>- **[JA Link (001_4)](docs/ja/samples/001_4_Local_Gradient.md)**<br>- **[JA Link (001_5)](docs/ja/samples/001_5_Local_Internal_Energy.md)**<br>- **[JA Link (002_1)](docs/ja/samples/002_1_Information_Geometry.md)**<br>- **[JA Link (002_2)](docs/ja/samples/002_2_Forensics.md)**<br>- **[JA Link (003_1)](docs/ja/samples/003_1_Kinematics.md)**<br>- **[JA Link (004_1)](docs/ja/samples/004_1_Control_Theory.md)**<br>- **[JA Link (004_2)](docs/ja/samples/004_2_Stability.md)**<br>- **[JA Link (005_1)](docs/ja/samples/005_1_Wave_Mechanics.md)** / **[JA Link (005_2)](docs/ja/samples/005_2_Coherence.md)** | Mathematical physics theory and diagnostic manual for the 8 core modules (000 to 005 series) with visualizations for the 10 validation samples. |
| **2** | **[📂 System Architecture & Operations Guide](docs/System_Architecture_and_Operations.md)** | **[JA Link (System Guide)](docs/ja/System_Architecture_and_Operations.md)** | Covers pipelines, stateless container setups, JSON design themes, custom data generators, and LQR control models. |
| **3** | **[📂 LLM Diagnostic Manual (Supreme prompt)](docs/LLM_Diagnostic_Manual.md)** | **[JA Link (LLM Manual)](docs/ja/LLM_Diagnostic_Manual.md)** | System prompt for LLM meta-diagnosis. It contains protocols to generate clinical reports and verify data facts. |
| **4** | **[📂 Verified Sample Registry & Catalog](docs/samples/README.md)** | **[JA Link (Catalog)](docs/ja/samples/README.md)** | Catalog of the 10 validation samples. It lists detection parameters, parameter thresholds, and LQR intervention guides. |

---

## ⚕️ Core Paradigm: Network Dynamics as a Physical Medium

TLU models transaction data as a continuous elastic network. Nodes are connected via mass-spring-damper elements.

![Mass-Spring-Damper Model](docs/readme_plots/Mass-Spring-Damper-Model.jpg)
*Figure 1: Conceptual diagram modeling ledger accounts as a mass-spring-damper system*

### Clinical Metaphor: Eastern Medicine (Qi, Blood, and Fluids)

To simplify complex physical parameters for users, TLU adopts Eastern medicine terms. It treats the network as meridians (transaction paths). Qi and Blood (funds and activity flows) circulate through them.
TLU identifies path blocks (stiffness and deadlocks) and active bleeding (capital leaks or embezzlement). It uses Linear Quadratic Regulator (LQR) control theory to suggest intervention points (acupuncture points) to restore normal circulation.

### Mapping Table: From Target Domains to Physical Space

| Physical Variable | Definition in Classical Mechanics & Thermodynamics | Financial Accounting Domain | Urban Traffic Domain | Financial Market Domain | Biological Brain fMRI Domain |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mass ( $m_i$ )** | Inertia / Energy storage tank | Account balance | Vehicles at intersection | Account assets | BOLD signal change |
| **Flux ( $f_{ij}$ )** | Velocity / Mass transport | Transaction amount | Vehicles per second | Trade value | Effective connectivity |
| **Stiffness ( $k_{ij}$ )** | Elasticity / Spring constant | Account connection strength | Road capacity limit | Synchronization level | Functional coherence |
| **Viscosity ( $c_{ij}$ )** | Friction / Damper damping | Payment terms (30-90 days) | Traffic drag / Delay | Execution delay (latency) | Signal propagation latency |
| **Entropy ( $S$ )** | Disorder / Frictional heat loss | Sham circular trading | Frictional heat from congestion | Wash trading between USRs | Neural hyper-synchrony (seizure) |
| **Free Energy ( $F$ )** | Available work potential | Net operating profit after tax | Vehicle flow potential | Market allocation efficiency | Brain cognitive capacity |
| **Acupuncture Point (LQR)** | Control input vector | Key audit accounts | Traffic light timing adjustment | Specific USR trade restriction | Target TMS stimulation point |

---

## 🔬 4 Spatiotemporal Physical Signatures

TLU extracts 4 physical signatures to detect systemic anomalies. These metrics bypass manual manipulation.

### 1. Macro Forensics (Conservation of Mass & Kirchhoff's Law)

Verifies whether inflow and outflow balance. When funds leak outside the system, mass conservation breaks. This triggers sharp spikes in the forensic residual plots.

* **🟢 Healthy (Sample 0):** The residual is exactly `0.00` across all steps. This physically proves there are no cash leaks.
* **🚨 Mass Leak (Sample 2 / Embezzlement):** Recovered cash is bypassed to a hidden node. Mass conservation breaks. TLU detects this as a negative residual spike.

| Healthy steady-state (Sample 0) | Pathological Mass Leak (Sample 2) |
| :---: | :---: |
| ![Macro Forensics Normal](samples/Sample_0_Healthy/readme_plots/002_2_1__macro_forensics_dashboard.png) | ![Macro Forensics Abnormal](samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png) |
| *Figure 2a: Conservation is maintained (residual = 0)* | *Figure 2b: Residual spike detected during embezzlement* |

---

### 2. Topology & System Stability (Spectral Radius $\rho$ )

Calculates the spectral radius (the maximum eigenvalue of the transition matrix) to detect circular loops. A spectral radius locked at the warning boundary of `1.00` indicates that the network is trapped in a closed loop.

* **🟢 Healthy (Sample 0):** The spectral radius stays near `0.00`. Transactions do not cycle and converge normally.
* **🚨 Locked Loop (Sample 4 / Composite Chaos):** Circular transactions lock the spectral radius at the boundary of `1.00` (Perron-Frobenius saturation), proving the existence of a sham loop.

| Healthy steady-state (Sample 0) | Locked Loop (Sample 4) |
| :---: | :---: |
| ![System Stability Normal](samples/Sample_0_Healthy/readme_plots/004_1_2__system_stability.png) | ![System Stability Abnormal](samples/Sample_4_Composite_Chaos/readme_plots/004_1_2__system_stability.png) |
| *Figure 3a: Spectral radius converges in a safe zone* | *Figure 3b: Spectral radius locked at the limit boundary of 1.00* |

---

### 3. Thermodynamic Energy Stack (System Fatigue & Thermal Death)

Calculates free energy ( $F = U - TS$ ), representing the work capacity of the system. If $F$ drops below zero, the system falls into thermal death. High activity ( $U$ ) without useful output generates friction (entropy $TS$ ), exhausting the system.

* **🟢 Healthy (Sample 0):** The free energy stays positive. It grows proportionally with system activity.
* **🚨 Thermal Death (Sample 8 / fMRI Stroke):** Blocked flow freezes connections. Entropy ( $S$ ) drops while macro temperature ( $T$ ) spikes. Free energy ( $F$ ) plummets to zero, causing thermal death.

| Healthy steady-state (Sample 0) | Pathological Thermal Death (Sample 8) |
| :---: | :---: |
| ![Thermodynamics Normal](samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png) | ![Thermodynamics Abnormal](samples/Sample_8_fMRI_Stroke/readme_plots/001_1_2__thermodynamics_energy_stack.png) |
| *Figure 4a: Healthy accumulation of free energy* | *Figure 4b: Free energy plunging to zero (thermal death)* |

---

### 4. 3D Spatiotemporal Geometry Distortion (KL Drift & Local Temperature)

Models probability distributions as a 3D geometric manifold. Local deadlocks, bot collusion, and strokes distort the manifold. TLU visualizes these as a sharp, yellow-green tower in a flat space.

* **🟢 Healthy (Sample 0):** The manifold remains flat and blue (except for initial edge effects from small sample sizes).
* **🚨 Manifold Distortion (Sample 5 / Traffic Deadlock):** Blocking intersection `23_Shijo_Karasuma` collapses the distribution. A sharp tower rises at the exact coordinates and time step, reaching over 600,000.

| Healthy steady-state (Sample 0) | Spatiotemporal Manifold Distortion (Sample 5) |
| :---: | :---: |
| ![3D Space Normal](samples/Sample_0_Healthy/readme_plots/002_2_2_2__3d_micro_z_score_X.png) | ![3D Space Abnormal](samples/Sample_5_Kyoto_Traffic/readme_plots/002_2_2_2__3d_micro_z_score_X.png) |
| *Figure 5a: Flat and calm geometric manifold* | *Figure 5b: Manifold distortion pointing to the anomaly origin* |

---

## 📂 10 Verification Case Studies

TLU includes 10 sample datasets across domains to verify the accuracy of the mathematical physics engine.

| ID | Case Study (Report Link) | Domain | Status | Key Metrics | Clinical Metaphor |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **0** | **[🟢 Healthy Metabolism (Healthy)](docs/samples/Sample_0_Healthy/README.md)** | Finance | **NORMAL** | $\rho$ = 0.00, Residual = $0.00$ | Smooth flow of Qi and Blood |
| **1** | **[🟡 Circular Trade / Wash Trade](docs/samples/Sample_1_Wash_Trade/README.md)** | Finance | **HIGH** | $\rho$ = 0.75, Depleted Free Energy | Qi and Blood running in a closed loop |
| **2** | **[🔴 Embezzlement Leak](docs/samples/Sample_2_Embezzlement_Leak/README.md)** | Finance | **CRITICAL** | Max Residual = $364.53, Terminal resonance | Bleeding from meridian, mass leak |
| **3** | **[🟡 Simple Bookkeeping Mistake (Unbalanced Mistake)](docs/samples/Sample_3_Unbalanced_Mistake/README.md)** | Finance | **WARNING** | Transient residual and KL tower | Temporary imbalance, self-healing |
| **4** | **[🔴 Composite Chaos](docs/samples/Sample_4_Composite_Chaos/README.md)** | Finance | **CRITICAL** | $\rho$ = 0.79, Max Residual = $4,773.57$ | Bleeding and looping of Qi and Blood |
| **5** | **[🔴 Urban Traffic Deadlock (Kyoto Traffic)](docs/samples/Sample_5_Kyoto_Traffic/README.md)** | Traffic | **CRITICAL** | $\rho$ = 1.00, Macro Temp $T = 16,264.61$ | Blocked meridian, stasis, static convection |
| **6** | **[🟢 Market Stock Flow](docs/samples/Sample_6_Market_Stock_Flow/README.md)** | Market | **NORMAL** | $\rho$ = 1.00, Residual = $0.00$ | Stock fluid equilibrium |
| **7** | **[🟢 Market Cash Flow](docs/samples/Sample_7_Market_Cash_Flow/README.md)** | Market | **NORMAL** | $\rho$ = 1.00, Residual = $0.00$ | Cash fluid equilibrium |
| **8** | **[🔴 Brain stroke model fMRI (fMRI Stroke)](docs/samples/Sample_8_fMRI_Stroke/README.md)** | Brain | **CRITICAL** | 95% path block, Stiffness Lock | Blocked brain meridian, local necrosis |
| **9** | **[🔴 Seizure model fMRI (fMRI Seizure)](docs/samples/Sample_9_fMRI_Seizure/README.md)** | Brain | **CRITICAL** | $\rho$ = 1.00, Falling entropy | Neural hyper-synchrony, runaway Qi |

---

## ⚕️ LQR Optimal Control for Dynamic Intervention

TLU detects anomalies and designs interventions. It uses a state-space model to calculate Linear Quadratic Regulator (LQR) control. This identifies acupuncture points (sensitive nodes). Targeting these nodes stabilizes the system with minimal effort.

| Financial Market (Sample 7) | Neuroscience (Sample 9) |
| :---: | :---: |
| ![Intervention in Market Hubs](samples/Sample_7_Market_Cash_Flow/readme_plots/support/004_1_3__control_lqr_performance_space.png) | ![Intervention in Seizure Focus](samples/Sample_9_fMRI_Seizure/readme_plots/support/004_1_3__control_lqr_performance_space.png) |
| *Figure 6a: Identifying market manipulation hubs (`USR_010` etc.)* | *Figure 6b: Identifying the epilepsy seizure focus in the temporal lobe (`Temporal_Lobe`)* |

---

## 🚀 Environment & Quick Start (Docker)

TLU uses stateless Docker containers and Test-Driven Development (TDD) to ensure reproducible mathematical analysis.

#### Setup: Custom Data Analysis

To analyze custom data, place these files in the `workspace/` directory:

1. **Transaction Flow Data (`workspace/input_stream/`)**: A time-series CSV. It requires `Trans_Date` (Date), `Account_Name` (Account Name), `Debit` (Inflow), and `Credit` (Outflow). Columns are specified in `workspace/config/_set_params.csv`.
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

TLU acts as an evidence generator. It only outputs physical and mathematical facts, such as mass conservation failures or spectral radius saturation.
TLU and the AI agent do not judge intent. They do not classify actions as legal or illegal. Humans must investigate. Use the physical metrics and spatiotemporal coordinates to check real-world proof (bank statements, order logs, or tissue biopsies) to confirm the final diagnosis.

---

**License**: AGPL-3.0  
**Developer**: Renpoo & Google Gemini Agent (Antigravity)
