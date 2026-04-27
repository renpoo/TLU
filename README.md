# Tensor-Link Utility (TLU)

> **"Projecting Domain Complexity into Mathematical Clarity for Autonomous AI Auditing."**

TLU is an **Autonomous Auditing Engine powered by the Cognitive Triad (Physics + Financials + LLM)**. It is a high-fidelity mathematical analysis pipeline designed to project directed transaction data (such as financial ledgers or supply chain flows) into a pure tensor space to uncover hidden structural dynamics that traditional accounting models miss.

### The Limitations of Traditional Accounting
Traditional double-entry bookkeeping requires all journal entries to be perfectly consistent before any calculation can begin. Because of this absolute axiom, it is mathematically difficult to extract the underlying reality when records are missing or intentionally manipulated (e.g., Wash Trading).

TLU solves this by removing the requirement for a balanced state from the initial analysis phase. By redefining accounting data as a flow of energy—analogous to fluids in a pipe—TLU applies physical laws like Kirchhoff's Current Law and non-equilibrium thermodynamics to calculate true financial dynamics even from incomplete or "broken" datasets. 

## 🤖 The Cognitive Triad (AI Autonomous Auditing)

TLU is not merely a visual dashboarding tool; its ultimate value is serving as a physics engine for Large Language Models (LLMs).

By reading the [**LLM Meta-Diagnosis System Prompt & Operating Procedure**](docs/LLM_Diagnostic_Manual.md), any LLM (ChatGPT, Claude, Gemini) can be instantly transformed into a "Meta-Diagnostic Radiologist." The manual provides a strict, tier-based logical framework (Decision Matrix) that allows the AI to ingest the high-dimensional physical metrics (like Spectral Radius and Free Energy) and cross-reference them with traditional Financial Statements (B/S, P/L) to output a CPA-grade, human-readable Medical Chart without hallucinating.

Check out the `samples/` directories to see actual English audit reports generated autonomously by the LLM using this manual!

## Theoretical Foundation: The Ledger as a Coupled Oscillator Network

A common critique of applying physical equations to accounting is the risk of a "category error"—ledgers do not possess literal physical mass or friction. However, TLU's theoretical foundation rests not on literal physics, but on the universally applied mathematical abstraction of **Continuum Mechanics and Coupled Oscillators**.

When physicists model the stress propagation, heat dissipation, or resonant frequencies of a solid object, they discretize it into a network of **point masses ($M$)** connected by invisible **springs ($K$)** and **dampers ($C$)**. TLU applies this exact same mathematically rigorous abstraction to an organization:

* **Mass ($M$) / Inertia**: An account's capacity to store potential energy and resist sudden state changes (based on historical volume/volatility).
* **Stiffness ($K$) / Springs**: The structural strength and deterministic causal links of transaction channels (e.g., Sales $\to$ Accounts Receivable).
* **Viscosity ($C$) / Dampers**: The temporal friction, dissipation, and delays inherent in the transactional flow.

By treating the organization as a **discrete elastic medium (a Mass-Spring-Damper network)**, TLU legitimately applies the equation of motion ($M\ddot{x} + C\dot{x} + Kx = F$) to calculate how external financial shocks (anomalies, fraud, market shifts) propagate, resonate, and decay through the business structure. TLU does not claim that a company obeys Newton's laws; rather, it uses these equations as an extraordinarily sensitive **Physics-Informed Feature Extractor** to surface anomalies that traditional accounting X-rays miss.

<img width="2816" height="1536" alt="Gemini_Generated_Image_e285yee285yee285" src="https://github.com/user-attachments/assets/6de49c8b-f38a-4b9e-94fd-d6406496018b" />

---

## Core Philosophy & Architecture (Ver 8.0.0)

TLU avoids giant monoliths and is built upon the **Unix Philosophy**, connecting single-responsibility filters via standard streams.

* **Zero Local Dependency:** Does not pollute the host OS. All analysis engines are completely isolated within Docker containers.
* **Fail-Fast UX:** When data inconsistencies or missing parameters are detected, the system immediately halts without implicit fallbacks. This physically prevents erroneous management decisions caused by mismatched contexts.
* **Declarative Experiment Control (SSOT):** The entire experimental condition—including input datasets, kinematic constraints, LQR weights, and anomaly thresholds—is centrally defined in a single `workspace/config/_sys_params.csv`. Modifying this file is the *only* way to alter the pipeline's behavior, ensuring absolute clarity.
* **Immutable Archive Reproducibility:** Upon completion, the entire `workspace/` (including the executed `_sys_params.csv` and outputs) can be snapshotted into an `archives/` directory using `bash bin/archive_experimental_run.sh`. By simply pointing the pipeline to an archived workspace, the exact same mathematical conditions and visualizations can be reproduced anytime.

### The Pipeline Phases

* **Phase 0: Pre-processing:** Cleansing source data and aggregating it into directional flux formats.
* **Phase 0.5: Traditional Accounting (IR):** Automatically generating standard B/S and P/L statements to serve as a baseline for human analysts.
* **Phase 1: Projection:** Stripping domain vocabulary and projecting data into a pure tensor space (COO stream).
* **Phase 2: Core Analysis:** A suite of pure mathematical filters based on physical paradigms (Categories 000–004).
* **Phase 3: Presentation:** High-density dashboard rendering driven by the Fail-Fast theme engine.
* **Phase 4: Orchestration:** Pipeline control and audit trail preservation within the containerized environment.



## Visual Showcase (Empirical Evidence)

TLU offloads cognitive load through its advanced "Dark" visualization suite ("Light" and "Colorblind-safe" themes are also available). Below are analytical trajectories based on the new taxonomy representing the lineage of natural sciences.

### 000_ Classical Mechanics & Solid Mechanics

Observe the "pulse" and "stiffness" of your organization. TLU calculates **Velocity ($v$)** and **Acceleration ($a$)** from pure flux, estimates **Inertia (Virtual Mass)** and **Viscosity** from historical activity scales, and plots them in a phase space.

<img width="1666" height="1324" alt="1_3_1__3d_dynamics_velocity" src="https://github.com/user-attachments/assets/4a2f33e2-4a1a-460c-b88b-33186868f7f6" />
<img width="1666" height="1324" alt="1_3_2__3d_dynamics_acceleration" src="https://github.com/user-attachments/assets/006abbf9-c505-4888-9809-c0908f04226a" />
<img width="1666" height="1324" alt="1_3_3__3d_dynamics_inertia" src="https://github.com/user-attachments/assets/7b84f2a0-86c5-4a79-a918-ce37c413d136" />
<img width="1666" height="1324" alt="1_3_4__3d_dynamics_viscosity" src="https://github.com/user-attachments/assets/fda0249f-bf17-4288-a1c0-e9934dda2ee8" />
<img width="1666" height="1324" alt="1_3_8__phase_portrait_3d" src="https://github.com/user-attachments/assets/e6e380a3-2cd8-4402-b727-14842359f2ab" />

### Principal Axes (PCA)

TLU also extracts the **Principal Axes** of the network by calculating the eigenvalues and eigenvectors of the covariance matrix. This reveals the dominant "dimensions" of variance—the primary directions in which the organization's resources naturally flow and fluctuate.

<img width="1674" height="1018" alt="000_2_2__principal_axes_ratio" src="https://github.com/user-attachments/assets/e24452b1-757b-4d61-acc9-490da73ea7a8" />

### 001_ Thermodynamics & Statistical Mechanics

Is your organization efficient? We measure global **Free Energy ($F$)** and **Entropy ($S$)**. High entropy with low work output indicates "Heat" (dissipative costs/waste) building up in the system. Local complexity and volatility are also captured as 3D manifolds.

<img width="1666" height="1324" alt="1_3_5__3d_dynamics_entropy" src="https://github.com/user-attachments/assets/21bc777f-7f61-4846-ba24-0a7df2a77e6e" />
<img width="1666" height="1324" alt="1_3_6__3d_dynamics_complexity" src="https://github.com/user-attachments/assets/98054228-61d1-4db2-9f2d-f2a154e84243" />
<img width="1784" height="1780" alt="1_5_1__thermodynamics_dashboard" src="https://github.com/user-attachments/assets/0c905567-6bb5-45a9-8273-3da58f973dd1" />
<img width="1781" height="1030" alt="1_5_2__thermodynamics_energy_stack" src="https://github.com/user-attachments/assets/ae8cdbcd-d984-45a9-bb97-42f1212c2e25" />
<img width="1614" height="976" alt="1_5_3__thermodynamics_ts_diagram" src="https://github.com/user-attachments/assets/2a43d059-5bef-4f0a-afb5-94024d78252b" />

### 002_ Information Geometry & Forensics

Unmask anomalies hiding in the data's "blood vessels." TLU calculates **Topological Edge Stress** based on Z-scores, revealing excessive load (rupture risk) on specific pathways and visualizing structural distortions as network graphs.

<img width="2187" height="1335" alt="1_12__network_topology t 00000" src="https://github.com/user-attachments/assets/0e00ce03-5507-4f6b-841b-c4b6f9991eb3" />
<img width="2187" height="1335" alt="1_12__network_topology t 00001" src="https://github.com/user-attachments/assets/de605f2e-45c0-475b-b16a-97c7a9e155d3" />
<img width="2187" height="1335" alt="1_12__network_topology t 00002" src="https://github.com/user-attachments/assets/5e7b7ba6-acea-4a65-9d80-c9c5a7cdf9e5" />
<img width="2187" height="1335" alt="1_12__network_topology t 00003" src="https://github.com/user-attachments/assets/f418bac3-b032-4983-9121-7cd62080c38c" />

### Manifold Dimensionality (SVD)

By performing Singular Value Decomposition (SVD) on the transition matrix, TLU calculates the **Effective Rank** of the network. If the network becomes over-centralized or collapses into a few hubs, the effective dimensionality drops, acting as an early warning for structural fragility.

<img width="1688" height="1018" alt="002_1_3__manifold_dimensionality" src="https://github.com/user-attachments/assets/3ed10e21-82c7-4d1c-b1bf-58cbdfabe4d5" />

### 003_ Applied Kinematics & Robotics

*(Supports Forward Kinematics for simulating the ripple effects of virtual investments, and Inverse Kinematics for calculating the required target intervention while considering stiffness penalties.)*

<img width="1717" height="1324" alt="1_1__3d_kinematics_fk" src="https://github.com/user-attachments/assets/47fe78fa-5d1e-4935-95c1-3324ff9e6dd9" />
<img width="1717" height="1324" alt="1_2__3d_kinematics_ik" src="https://github.com/user-attachments/assets/8f2022ea-50e0-4cd4-8ef5-b102cf7cc359" />

### 004_ Control Theory & Systems Engineering

Stop guessing. Use **Linear-Quadratic Regulator (LQR)** theory to calculate the mathematically optimal resource allocation trajectory to reach a target state while minimizing organizational friction (strain energy).

<img width="1781" height="1026" alt="1_7_2__control_error_convergence" src="https://github.com/user-attachments/assets/93fd6e45-940e-435d-9777-ce99502e1eaa" />
<img width="1997" height="1124" alt="1_7_3__control_lqr_performance_space" src="https://github.com/user-attachments/assets/98f2dc6b-3034-4520-90d2-bb887449b4eb" />

### System Stability (Spectral Radius)

Is the system spinning out of control? By calculating the maximum eigenvalue (**Spectral Radius**) of the transition matrix, TLU detects topological cycles (e.g., Wash Trading or recursive loops). If the radius approaches or exceeds 1.0, the system is mathematically unstable and prone to exponential divergence.

<img width="1680" height="1018" alt="004_1_2__system_stability" src="https://github.com/user-attachments/assets/b4944e8d-8253-409a-b6a4-79c234efed57" />

---

## Sample Datasets & Hands-on Tutorials

To help you understand how TLU works in practice without the cognitive overload of mixed signals, we provide a suite of **6 isolated sample datasets**. These datasets simulate both financial ledgers and spatial traffic networks under various controlled pathological conditions (e.g., Wash Trades, Embezzlement, Journaling Errors).

You can find them in the `samples/` directory. Each sample includes a dedicated `README.md` explaining the anomaly injected, the physical reasoning behind it, and **the exact command you need to run to generate the visualization graphs** on your local machine.

* `samples/Sample_0_Healthy/`: A perfectly balanced baseline.
* `samples/Sample_1_Wash_Trade/`: Explains System Stability (Eigenvalues).
* `samples/Sample_2_Embezzlement_Leak/`: Explains Thermodynamics (Free Energy).
* `samples/Sample_3_Unbalanced_Mistake/`: Explains Macro Forensics (Conservation Law).
* `samples/Sample_4_Composite_Chaos/`: A real-world chaotic mix of all anomalies.
* `samples/Sample_5_Kyoto_Traffic/`: A pure spatial network (Open System) control experiment.

---

## Documentation (Hub & Spoke)

For detailed mathematical logic, operational protocols, and API references, please consult the "Spoke" manuals linked below:

* [01_System_Philosophy_and_Operations.md](docs/architecture/01_System_Philosophy_and_Operations.md)
* [02_Data_Topology_and_Projection.md](docs/architecture/02_Data_Topology_and_Projection.md)
* [03_Visualizer_and_Theme_Engine.md](docs/architecture/03_Visualizer_and_Theme_Engine.md)
* [04_Simulation_and_TDD.md](docs/architecture/04_Simulation_and_TDD.md)
* [05_Meta_Analytical_Methodology_and_AI_Collaboration.md](docs/architecture/05_Meta_Analytical_Methodology_and_AI_Collaboration.md)
* [06_Dummy_Data_Generators.md](docs/architecture/06_Dummy_Data_Generators.md)
* [07_Theoretical_Limits_and_Edge_Effects.md](docs/architecture/07_Theoretical_Limits_and_Edge_Effects.md)

* [000_Classical_Mechanics.md](docs/physics/000_Classical_Mechanics.md)
* [001_Thermodynamics_and_Fluctuations.md](docs/physics/001_Thermodynamics_and_Fluctuations.md)
* [002_Information_Geometry_and_Forensics.md](docs/physics/002_Information_Geometry_and_Forensics.md)
* [003_Applied_Kinematics.md](docs/physics/003_Applied_Kinematics.md)
* [004_Control_Theory_and_Systems_Engineering.md](docs/physics/004_Control_Theory_and_Systems_Engineering.md)

* [Graph_Interpretation_Guide.md](docs/interpretations/Graph_Interpretation_Guide.md)
* [LLM_Diagnostic_Manual.md](docs/LLM_Diagnostic_Manual.md)

---

## Quick Start

TLU is fully containerized. You can go from zero to a full 3D analysis dashboard in minutes.

```bash
# 1. Clone the repository
git clone https://github.com/renpoo/TLU.git
cd TLU

# 2. Spin up the environment (Zero Local Dependency)
docker compose up -d

# 3. Run the full pipeline with generated sample data
# (To run unit tests: bash bin/batch_unittest.sh)
bash bin/batch_generate_dummy_journal_data.sh
bash bin/batch_processing.sh
bash bin/batch_visualize_graphs.sh

# 4. Check the Diagnosis
# The batch_processing.sh script automatically runs the Meta-Diagnosis Engine 
# at the very end. Check your output directory for the final medical chart:
cat workspace/output_data/_99_diagnosis_report.md

# 5. Snapshot the experiment for perfect reproducibility
bash bin/archive_experimental_run.sh

# 6. (Optional) Cross-Environment Comparison
# Compare multiple experiments or samples side-by-side
bash bin/batch_meta_analysis.sh --envs "samples/Sample_*" --out "samples"
```

# License: AGPL-3.0

This project is a legacy of mathematical transparency. Under the AGPL-3.0 license, we ensure that the core logic remains open and verifiable by the community. If you build upon this engine, the world deserves to see the math.

# Built by Renpoo & Google Gemini

TLU is developed with a strict adherence to XP (Extreme Programming) and TDD (Test-Driven Development) protocols. Every core mathematical function is verified against theoretical edge cases.
