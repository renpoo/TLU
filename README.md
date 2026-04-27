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
![Mass-Spring-Damper-Modle](docs/readme_plots/Mass-Spring-Damper-Modle.jpg)

---

## Core Philosophy & Architecture (Ver 8.0.0)

TLU avoids giant monoliths and is built upon the **Unix Philosophy**, connecting single-responsibility filters via standard streams.

* **Zero Local Dependency:** Does not pollute the host OS. All analysis engines are completely isolated within Docker containers.
* **Fail-Fast UX:** When data inconsistencies or missing parameters are detected, the system immediately halts without implicit fallbacks. This physically prevents erroneous management decisions caused by mismatched contexts.
* **Declarative Experiment Control (SSOT):** The entire experimental condition—including input datasets, kinematic constraints, LQR weights, and anomaly thresholds—is centrally defined in a single `workspace/config/_sys_params.csv`. Modifying this file is the *only* way to alter the pipeline's behavior, ensuring absolute clarity.
* **Immutable Archive Reproducibility:** Upon completion, the entire `workspace/` (including the executed `_sys_params.csv` and outputs) can be snapshotted into an `archives/` directory using `bash bin/archive_experimental_run.sh`. By simply pointing the pipeline to an archived workspace, the exact same mathematical conditions and visualizations can be reproduced anytime.

### The Pipeline Phases

* **Phase 0: Pre-processing:** Cleansing source data and aggregating it into directional flux formats.
* **Phase 1: Traditional Accounting (IR):** Automatically generating standard B/S and P/L statements to serve as a baseline for human analysts.
* **Phase 3: Projection:** Stripping domain vocabulary and projecting data into a pure tensor space (COO stream).
* **Phase 4: Core Analysis:** A suite of pure mathematical filters based on physical paradigms (Categories 000–005).
* **Phase 5: Presentation:** High-density dashboard rendering driven by the Fail-Fast theme engine.
* **Phase 6: Orchestration:** Pipeline control and audit trail preservation within the containerized environment.

## Visual Showcase (Empirical Evidence)

TLU offloads cognitive load through its advanced "Dark" visualization suite ("Light" and "Colorblind-safe" themes are also available). Below are analytical trajectories based on the new taxonomy representing the lineage of natural sciences.

### 000_ Classical Mechanics & Solid Mechanics

Observe the "pulse" and "stiffness" of your organization. TLU calculates **Velocity ($v$)** and **Acceleration ($a$)** from pure flux, estimates **Inertia (Virtual Mass)** and **Viscosity** from historical activity scales, and plots them in a phase space.

![1_3_1__3d_dynamics_velocity](docs/readme_plots/000_1_1__3d_dynamics_velocity.png)
![1_3_2__3d_dynamics_acceleration](docs/readme_plots/000_1_2__3d_dynamics_acceleration.png)
![1_3_3__3d_dynamics_inertia](docs/readme_plots/000_1_3__3d_dynamics_inertia.png)
![1_3_4__3d_dynamics_viscosity](docs/readme_plots/000_1_4__3d_dynamics_viscosity.png)
![1_3_8__phase_portrait_3d](docs/readme_plots/000_1_8__phase_portrait_3d.png)

### Principal Axes (PCA)

TLU also extracts the **Principal Axes** of the network by calculating the eigenvalues and eigenvectors of the covariance matrix. This reveals the dominant "dimensions" of variance—the primary directions in which the organization's resources naturally flow and fluctuate.

![000_2_2__principal_axes_ratio](docs/readme_plots/000_2_2__principal_axes_ratio.png)

### 001_ Thermodynamics & Statistical Mechanics

Is your organization efficient? We measure global **Free Energy ($F$)** and **Entropy ($S$)**. High entropy with low work output indicates "Heat" (dissipative costs/waste) building up in the system. Local complexity and volatility are also captured as 3D manifolds.

![1_3_5__3d_dynamics_entropy](docs/readme_plots/001_1_2_1__3d_local_entropy.png)
![1_3_6__3d_dynamics_complexity](docs/readme_plots/001_1_2_5__local_thermo_complexity.png)
![1_5_1__thermodynamics_dashboard](docs/readme_plots/001_1_1__thermodynamics_dashboard.png)
![1_5_2__thermodynamics_energy_stack](docs/readme_plots/001_1_2__thermodynamics_energy_stack.png)
![1_5_3__thermodynamics_ts_diagram](docs/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

### 002_ Information Geometry & Forensics

Unmask anomalies hiding in the data's "blood vessels." TLU calculates **Topological Edge Stress** based on Z-scores, revealing excessive load (rupture risk) on specific pathways and visualizing structural distortions as network graphs.

![1_12__network_topology t 00000](docs/readme_plots/002_1_2__network_topology.t.00000.png)
![1_12__network_topology t 00001](docs/readme_plots/002_1_2__network_topology.t.00001.png)
![1_12__network_topology t 00002](docs/readme_plots/002_1_2__network_topology.t.00002.png)
![1_12__network_topology t 00003](docs/readme_plots/002_1_2__network_topology.t.00003.png)

### Manifold Dimensionality (SVD)

By performing Singular Value Decomposition (SVD) on the transition matrix, TLU calculates the **Effective Rank** of the network. If the network becomes over-centralized or collapses into a few hubs, the effective dimensionality drops, acting as an early warning for structural fragility.

![002_1_3__manifold_dimensionality](docs/readme_plots/002_1_3__manifold_dimensionality.png)

### 003_ Applied Kinematics & Robotics

*(Supports Forward Kinematics for simulating the ripple effects of virtual investments, and Inverse Kinematics for calculating the required target intervention while considering stiffness penalties.)*

![1_1__3d_kinematics_fk](docs/readme_plots/003_1_1__3d_kinematics_fk.png)
![1_2__3d_kinematics_ik](docs/readme_plots/003_1_2__3d_kinematics_ik.png)

### 004_ Control Theory & Systems Engineering

Stop guessing. Use **Linear-Quadratic Regulator (LQR)** theory to calculate the mathematically optimal resource allocation trajectory to reach a target state while minimizing organizational friction (strain energy).

![1_7_2__control_error_convergence](docs/readme_plots/004_1_2__control_error_convergence.png)
![1_7_3__control_lqr_performance_space](docs/readme_plots/004_1_3__control_lqr_performance_space.png)

### System Stability (Spectral Radius)

Is the system spinning out of control? By calculating the maximum eigenvalue (**Spectral Radius**) of the transition matrix, TLU detects topological cycles (e.g., Wash Trading or recursive loops). If the radius approaches or exceeds 1.0, the system is mathematically unstable and prone to exponential divergence.

![004_1_2__system_stability](docs/readme_plots/004_1_2__system_stability.png)

---

## Sample Datasets & Hands-on Tutorials

To help you understand how TLU works in practice without the cognitive overload of mixed signals, we provide a suite of **6 isolated sample datasets**. These datasets simulate both financial ledgers and spatial traffic networks under various controlled pathological conditions (e.g., Wash Trades, Embezzlement, Journaling Errors).

You can find them in the `samples/` directory. Each sample includes a dedicated `README.md` explaining the anomaly injected, the physical reasoning behind it, and **the exact command you need to run to generate the visualization graphs** on your local machine.

* [`samples/Sample_0_Healthy/`](samples/Sample_0_Healthy/): A perfectly balanced baseline.
* [`samples/Sample_1_Wash_Trade/`](samples/Sample_1_Wash_Trade/): Explains System Stability (Eigenvalues).
* [`samples/Sample_2_Embezzlement_Leak/`](samples/Sample_2_Embezzlement_Leak/): Explains Thermodynamics (Free Energy).
* [`samples/Sample_3_Unbalanced_Mistake/`](samples/Sample_3_Unbalanced_Mistake/): Explains Macro Forensics (Conservation Law).
* [`samples/Sample_4_Composite_Chaos/`](samples/Sample_4_Composite_Chaos/): A real-world chaotic mix of all anomalies.
* [`samples/Sample_5_Kyoto_Traffic/`](samples/Sample_5_Kyoto_Traffic/): A pure spatial network (Open System) control experiment.

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
* [005_Signal_Processing_and_Wave_Mechanics.md](docs/physics/005_Signal_Processing_and_Wave_Mechanics.md)

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
