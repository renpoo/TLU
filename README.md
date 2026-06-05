# 🔬 Tensor-Link Utility (TLU)

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-red.svg)](https://www.gnu.org/licenses/agpl-3.0.html)
[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Docker Status](https://img.shields.io/badge/Docker-Compatible-emerald.svg)](https://www.docker.com/)
[![Engine Status](https://img.shields.io/badge/System_Verification-Passing-brightgreen.svg)](#-verification-status)

### Unified Spatiotemporal Physics-Mathematics & Thermodynamic Engine for Multi-Domain Network Forensics

The ultimate conclusion of the **Tensor-Link Utility (TLU)** is the mathematical and physical proof that: **"No matter how perfectly transaction networks or ledgers are manipulated on the surface, it is absolutely impossible to deceive universal physical laws, such as the Law of Conservation of Mass and the Laws of Thermodynamics."**

TLU is an autonomous meta-diagnostic platform that redefines spatiotemporal datasets—such as financial ledgers, urban traffic flows, stock market transactions, and biological brain networks—as continuous "fluids" or "energy waves" moving through a **Mass-Spring-Damper Network**. By projecting raw transactions onto physical manifolds, TLU visualizes invisible anomalies (embezzlement, wash trading, congestion, stroke ischemia, and epilepsy) as objective **Physical Signatures** (mass leaks, stiffness locks, and abnormal resonance).

These mathematical invariants are then decoded by an integrated LLM (compliant with the [`LLM_Diagnostic_Manual.md`](docs/LLM_Diagnostic_Manual.md)) to automatically translate forensic evidence into clinical diagnostic reports for human experts.

---

## 📚 TLU Official Knowledge Portal (Documentation Map)

To guarantee reproducibility and prevent AI hallucination or human bias, TLU maintains a strictly structured knowledge portal. The documentation has been consolidated into **5 core guides** directly under `docs/`. Below is the portal map in both English and Japanese:

| # | Document Title (English Version) | Japanese Reference Version (日本語版) | Core Contents & Highlights |
| :---: | :--- | :--- | :--- |
| **1** | **[📂 01. Physics-Mathematics-Mathematics Engine Theory & Interpretation Guide](docs/01_Physics-Mathematics_Mathematics_Engine_Theory_and_Interpretation.md)** | **[01. 物理数学エンジン基礎理論と解釈ガイド](docs/ja/01_Physics-Mathematics_Mathematics_Engine_Theory_and_Interpretation.md)** | Mathematical foundations of TLU's 8 cores ($F = U - TS$, $K$, $\rho$) and how to visually read the generated 3D phase-space plots. |
| **2** | **[📂 02. System Architecture & Operations Guide](docs/System_Architecture_and_Operations.md)** | **[02. システム構造定義とパイプライン運用ガイド](docs/ja/System_Architecture_and_Operations.md)** | Pipeline container orchestration, HSL theme visualizers, anomaly dummy generators, and LQR control feedback simulation models. |
| **3** | **[📂 03. Market Forensics & Compliance Rules](docs/03_Market_Forensics_Rules.md)** | **[03. 市場フォレンジック・監査ルール定義](docs/ja/03_Market_Forensics_Rules.md)** | Millisecond-level order book dynamics, wash trades, and bipartite graph projection vs. direct user-to-user collusion network analysis. |
| **4** | **[📂 LLM Diagnostic Manual (Supreme prompt)](docs/LLM_Diagnostic_Manual.md)** | **[LLM臨床検査マニュアル (Supreme Prompt)](docs/ja/LLM_Diagnostic_Manual.md)** | The meta-level system instructions for AI agents to write clinical reports, handle statistical false alarms, and perform raw fact-checking. |
| **5** | **[📂 Verified Sample Registry & Catalog](docs/samples/README.md)** | **[検証サンプル比較・メタ検査総合カタログ](docs/ja/samples/README.md)** | Cross-verification registry, pathological groupings, and optimal LQR control therapy guidelines for all 10 validation samples. |

---

## ⚕️ Core Paradigm: Network Dynamics as Physical Media

TLU models transaction networks not as static ledgers, but as **continuous elastic media (networks of masses, springs, and dampers)**.

![Mass-Spring-Damper Model](docs/readme_plots/Mass-Spring-Damper-Model.jpg)
*Figure 1: Conceptual mapping of transaction flows onto a Mass-Spring-Damper physical system.*

### The Eastern Medicine Metaphor (SME Physician)

Rather than treating network analysis as cold statistics, TLU operates like a physician diagnosing the flow of **"Qi and Blood (気血水)"** (liquidity and flux) through **"Meridians (経絡)"** (transaction paths). TLU identifies where circulation is blocked (Stiffness Rigidity / Thrombus) or hemorrhaging (Mass Deficit / Bleeding), and uses **Control Theory (LQR Sensitivity)** to pinpoint the exact **"Acupoints (経穴)"** to apply feedback pulses to restore systemic health.

### Domain-to-Physics-Mathematics Mapping Matrix

| Physical Variable | Classical Mechanics / Thermo | Financial Ledger Domain | Urban Traffic Domain | Stock Market Domain | Biological Neural (fMRI) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mass ($m_i$)** | Inertia / Reservoir | Account Balance | Vehicles in Intersection | Account Capital | BOLD Signal Density |
| **Flux ($f_{ij}$)** | Velocity / Material Flow | Journal Transaction Amount | Traffic Volume (Vehicles/s) | Matching Fund Flow | Signal Connection Flux |
| **Stiffness ($k_{ij}$)** | Elasticity / Spring Constant | Transaction Rigidity | Road Flow Capacity | Matching Synchronization | Functional Coherence |
| **Viscosity ($c_{ij}$)** | Friction / Damper | Collection Latency | Congestion Resistance | Trade Latency / Slippage | Signal Propagation Delay |
| **Entropy ($S$)** | Disorder / Frictional Loss | Fictitious Circular Turnovers | Velocity Variance (Congestion) | Collusive Matched Orders | Pathological Hypersynchrony |
| **Free Energy ($F$)** | Useful Work Potential | Net Operating Income | Dynamic Vehicle Mobility | True Allocative Efficiency | Cognitive Processing Power |
| **Acupoints (LQR)** | Control Input Targets | Auditing Accounts | Intersection Signals | Target Bot Accounts | Transcranial Stim (TMS) Focus |

---

## 🔬 4 Core Physical Signatures (Visual Proofs)

TLU extracts **4 physical signatures** to detect systemic anomalies. These signatures act as objective mathematical invariants that bypass surface-level book manipulation.

### 1. Macro Forensics (Conservation of Mass & Kirchhoff's Law)

Monitors whether funds or resources have "unnaturally vanished or spawned" from the global system. Any off-book siphoning violates the Law of Conservation of Mass, exposing a massive spike in the System Conservation Residual.

* **🟢 Healthy Baseline (Sample 0):** The macro residual remains at absolute zero (`0.00`) throughout, proving no leakages exist.
* **🚨 Mass Leakage (Sample 2 / Embezzlement):** Accounts receivable collections bypass the cash account into an off-book leak. The system conservation residual violently spikes, capturing the exact moment of siphoned leakage.

| Healthy Normal State (Sample 0) | Pathological Mass Leakage (Sample 2) |
| :---: | :---: |
| ![Macro Forensics Normal](samples/Sample_0_Healthy/readme_plots/002_2_1__macro_forensics_dashboard.png) | ![Macro Forensics Abnormal](samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png) |
| *Figure 2a: Perfect mass conservation (residual = 0).* | *Figure 2b: Severe negative spike proving siphoned embezzlement.* |

---

### 2. Topology & System Stability (Spectral Radius $\rho$)

Monitors whether a closed loop (such as circular wash trades or traffic deadlocks) has formed. If the red trajectory line (Spectral Radius) approaches or breaches the warning threshold of `1.00`, it mathematically proves the system is locked in an out-of-control recirculation spiral.

* **🟢 Healthy Baseline (Sample 0):** The Spectral Radius constantly hovers in the safe zone below 1.0, meaning transaction flows organically disperse and self-converge.
* **🚨 Out-of-Control Loop (Sample 4 / Wash Trade):** High-speed circular fictitious trades force the Spectral Radius to saturate and lock onto the boundary limit of `1.00`, proving a state of empty recirculation.

| Healthy Normal State (Sample 0) | Pathological Recirculation Loop (Sample 4) |
| :---: | :---: |
| ![System Stability Normal](samples/Sample_0_Healthy/readme_plots/004_1_2__system_stability.png) | ![System Stability Abnormal](samples/Sample_4_Composite_Chaos/readme_plots/004_1_2__system_stability.png) |
| *Figure 3a: Spectral radius converging in the safe zone.* | *Figure 3b: Spectral radius locked at the Perron-Frobenius limit.* |

---

### 3. Thermodynamic Energy Stack (Organizational Exhaustion & Heat Death)

Monitors the system's useful potential—Free Energy ($F = U - TS$). If Free Energy (white line) plummets below zero, the system has entered **"Thermodynamic Heat Death"**—a pathological state where the system consumes massive amounts of energy (Gross Activity $U$) but wastes it entirely as frictional heat (Entropy $TS$) without doing useful work.

* **🟢 Healthy Baseline (Sample 0):** Free Energy (white layer) steadily accumulates and grows in proportion to internal energy, proving a healthy, generative metabolism.
* **🚨 Heat Death (Sample 6 / Market Manipulation):** Fictitious trade volume between bots generates massive entropy. Free Energy plummets into the deep negative zone, indicating a useless, self-consuming system convulsion.

| Healthy Normal State (Sample 0) | Pathological Heat Death (Sample 6) |
| :---: | :---: |
| ![Thermodynamics Normal](samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png) | ![Thermodynamics Abnormal](samples/Sample_6_Market_Stock_Flow/readme_plots/001_1_2__thermodynamics_energy_stack.png) |
| *Figure 4a: Healthy accumulation of Free Energy.* | *Figure 4b: Free Energy collapsing into the negative zone.* |

---

### 4. 3D Spatial Geometry (KL Drift & Local Temperature)

Models the spatiotemporal probability distribution of transaction networks as a smooth manifold. Localized anomalies (such as a sudden bottleneck, circular trade collusion, or brain infarction) deform this manifold, erecting sharp, yellow-green needle-like spikes in 3D space.

* **🟢 Healthy Baseline (Sample 0):** After the initial "Edge Effect" (a mathematical illusion due to lack of historical data at start step $t=0$), the 3D surface is a flat, peaceful landscape of minor normal fluctuations.
* **🚨 Spatiotemporal Mutation (Sample 5 / Traffic Deadlock):** A sharp, towering spike pierces the information manifold, pinpointing the exact node (intersection `23_四条烏丸`) and timestamp of the deadlock.

| Healthy Normal State (Sample 0) | Pathological Manifold Mutation (Sample 5) |
| :---: | :---: |
| ![3D Space Normal](samples/Sample_0_Healthy/readme_plots/002_2_2_2__3d_micro_z_score_X.png) | ![3D Space Abnormal](samples/Sample_5_Kyoto_Traffic/readme_plots/002_2_2_2__3d_micro_z_score_X.png) |
| *Figure 5a: Smooth, stable spatiotemporal manifold.* | *Figure 5b: Towering local anomaly spike piercing the space.* |

---

## 📂 The 10 Validation Case Studies

TLU includes **10 pre-configured sample datasets** simulating both socioeconomic systems (finance and traffic) and biological structures (brain networks) to demonstrate its cross-domain diagnostic power.

| Sample ID | Sample Case Study Name (README Link) | Main Domain | System Diagnosis | Core Diagnostic Metric | Eastern Medicine Metaphor |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **0** | **[🟢 Healthy Metabolism](samples/Sample_0_Healthy/README.md)** | Financial | **NORMAL** | $\rho = 0.00$, Residual = $0.00$ | Peace of Qi & Blood, Normal Convection |
| **1** | **[🟡 Wash Trade (Circular Ledger)](samples/Sample_1_Wash_Trade/README.md)** | Financial | **HIGH** | $\rho = 0.75$, $F$ depletion | Empty Recirculation of Qi, Recirculation Lock |
| **2** | **[🔴 Embezzlement Leak (Siphoned Leak)](samples/Sample_2_Embezzlement_Leak/README.md)** | Financial | **CRITICAL** | Max Residual = $364.53$ | Meridian Major Hemorrhage, Mass Deficit |
| **3** | **[🟡 Unbalanced Mistake (Input Error)](samples/Sample_3_Unbalanced_Mistake/README.md)** | Financial | **WARNING** | Transient residual & KL spike | Local Qi-Blood Imbalance, Meridian Sprain |
| **4** | **[🔴 Composite Chaos (Combined Anomalies)](samples/Sample_4_Composite_Chaos/README.md)** | Financial | **CRITICAL** | $\rho = 0.79$, Residual = $4,773.57$ | Depletion of Qi & Blood, Recirculation Collapse |
| **5** | **[🔴 Kyoto Traffic (Deadlocked Intersections)](samples/Sample_5_Kyoto_Traffic/README.md)** | Traffic | **CRITICAL** | $\rho = 1.00$, Temp $T = 547.06$ | Meridian Obstruction, Qi Stagnation & Blood Stasis |
| **6** | **[🟡 Market Bipartite (Matched Trades)](samples/Sample_6_Market_Stock_Flow/README.md)** | Stock Market | **HIGH** | $\rho = 1.00$, PC1 = $99.67\%$ | Market Meridian Recirculation, Recirculation Lock |
| **7** | **[🟡 Market Users (Collusion Syndicate)](samples/Sample_7_Market_Cash_Flow/README.md)** | Stock Market | **HIGH** | Free Energy Skew = $-2.72$ | Collusive Syndicate, Dark Undercurrent Recirculation |
| **8** | **[🔴 fMRI Stroke (Cerebral Infarction)](samples/Sample_8_fMRI_Stroke/README.md)** | Brain fMRI | **CRITICAL** | Inflow cut 95%, local Rigid Lock | Brain Meridian Obstruction, Local Qi-Blood Depletion |
| **9** | **[🔴 fMRI Seizure (Epileptic Seizure)](samples/Sample_9_fMRI_Seizure/README.md)** | Brain fMRI | **CRITICAL** | $\rho = 1.00$, Entropy collapse | Brain Meridian Hypersynchrony, Qi-Blood Runaway |

---

## ⚕️ Optimal Control Theory (LQR) dynamic treatment

TLU does not merely flag anomalies; it models the network as a state-space system and uses **LQR (Linear Quadratic Regulator)** control theory ($u(t) = -K_{lqr} \cdot X(t)$) to compute the **acupoints (nodes)** and control pulses required to damp the pathological waveforms and return the system to its healthy limit cycle.

* **Financial (Sample 7):** Target the matching engine of collusive accounts (`USR_003` ⇄ `USR_004`) to inject millisecond-level match latency, physically damping and disrupting the wash trade loop.
* **Biological (Sample 9):** Target the epileptic focus in the `Temporal_Lobe` with Transcranial Magnetic Stimulation (TMS) to emit anti-phase waves, neutralizing hypersynchrony.

---

## 🚀 Execution & Quick Start (Docker Environment)

TLU ensures 100% environment reproducibility and eliminates human bias using containerized pipelines and Test-Driven Development (TDD).

### Preparation: Custom Ingestion Requirements

To run TLU with your own data, place the following two CSV files inside the `workspace/` directory:

1. **Transaction Flux Stream (`workspace/input_stream/`)**: A chronological CSV containing the columns: `Trans_Date`, `Account_Name` (or node name), `Debit` (Inflow), and `Credit` (Outflow).
2. **Account Mapping Dictionary (`workspace/config/_account_mapping.csv`)**: Maps your custom nodes to TLU's standard physical categories (Asset, Liability, Revenue, etc.) for Phase 1 B/S and P/L block calculations.

### Automated Simulation Pipeline Steps

```bash
# 1. Clone the repository
git clone https://github.com/renpoo/TLU.git
cd TLU

# 2. Start the containerized environment
docker compose up -d

# 3. Execute the automated physical pipeline (Simulating Sample 1: Wash Trade)
# * Target environment can be swapped to any case under samples/
bash bin/batch_processing.sh --target_env "samples/Sample_1_Wash_Trade"
bash bin/batch_visualize_graphs.sh --target_env "samples/Sample_1_Wash_Trade"

# 4. View the LLM-generated clinical diagnostic report
cat workspace/output_data/_99_diagnosis_report.md
```

---

## ⚠️ Academic Rigor & Falsifiability

TLU is an **"Evidence Generator (Calculator)"** that produces mathematically and physically falsifiable facts (such as "this node violates conservation of mass by $X$ amount" or "this loop is locked at a spectral radius of 1.0").

It is **not** an AI that makes assumptions about moral intent (e.g. distinguishing between a simple clerical sprain and deliberate embezzlement). The mathematical and geometric coordinate outputs (such as Date, Account, and Magnitude) serve as objective forensic signposts. The human auditor or clinical investigator remains the ultimate "Judge," verifying these physical anomalies against real-world raw documentation (original bank statements, trading server logs, or tissue biopsies).

---

## 🔬 Verification Status

All unit tests and physical checks in the TLU environment are active and passing:

```bash
python3 scratch/verify_corrections.py
# Output: === Verification Successful: ALL CHECKS PASSED! ===
```

**License**: AGPL-3.0  
**Authors**: Renpoo & Google DeepMind Agent (Antigravity)
