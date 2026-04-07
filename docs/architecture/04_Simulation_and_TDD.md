# 04. Simulation and Test-Driven Development (TDD)

> **"A mathematical model that has never faced orchestrated chaos is merely a theoretical toy. Truth is verified through rigorous, adversarial simulation."**

The Tensor-Link Utility (TLU) is built on absolute mathematical laws. However, to trust these laws in a real-world business environment, they must be continuously tested.

Category **04 (Simulation)** defines TLU's advanced Dummy Data Generator. It does not simply output random numbers; it synthesizes complex, network-based "artificial realities" to rigorously verify the Core Analysis filters (Phase 2) under Extreme Programming (XP) and Test-Driven Development (TDD) protocols.

---

## 1. The Necessity of Artificial Synthesis

When dealing with concepts like Information Curvature or Partial Correlation Stiffness, it is difficult to know if the algorithm is correct by looking at real, messy business data alone.

To prove that a filter works, we must synthesize an input stream where the "true answer" is already known mathematically, feed it through the pipeline, and assert that the filter's output matches the expected truth exactly.

## 2. Generation Modes

The Simulator provides two distinct realities for testing the pipeline.

### Baseline (Null Hypothesis) Mode

* **Mechanism:** Generates a stream of pure, uniform white noise across all nodes.
* **Purpose:** This is the ultimate "Control Group." In this mode, TLU must gracefully calculate zero structural stiffness (000), maximum global entropy (001), and trigger absolutely zero anomaly flags (002). It verifies the system's ability to remain silent when there is no underlying structure, proving a low false-positive rate.

### Real Business (Causal) Mode

* **Mechanism:** Synthesizes a stream that mimics the messy physics of a real economy or corporate network.
* **Features:**
  * **Scale-Free Topology:** Creates massive "Hub" nodes (e.g., a central 'Cash' account) and "Sparse" peripheral nodes.
  * **Pareto Distribution:** Applies the 80/20 rule to flux volumes, ensuring realistic inequalities.
  * **Brownian Motion & 1/f Noise:** Integrates random walks to simulate cumulative stock levels and "pink noise" to mimic natural business cycles and trends.
* **Purpose:** Ensures the filters do not break or produce `NaN` errors when faced with extreme mathematical skewness, large variances, and complex causal delays.

## 3. Deterministic Anomaly Injection (The "Poison" Recipes)

The most critical part of TLU is its Forensics layer (002). To prove that TLU can catch fraud, data corruption, or regime shifts, the Simulator is equipped to inject deterministic "poison" into the data stream during the latter half of the simulation timeline.

By supplying the `--inject_anomalies` flag, the Simulator executes specific recipes designed to trigger exact mathematical alarms:

* **Triggering Micro Forensics (Z-Score):** The Simulator forcibly overwrites the flow of a single, normally quiet node with a massive $3\sigma$ spike for a specific duration. The `002_2_2` filter *must* catch this.
* **Triggering Micro Forensics (KL Drift):** The Simulator keeps a node's total volume identical, but silently alters the percentages of *where* it sends its flux. This synthesizes "embezzlement" or "silent diversion." The KL Drift filter *must* spike, proving it can catch topological changes that volume metrics miss.
* **Triggering Macro Forensics (Conservation Leak):** The Simulator intentionally breaks double-entry principles, injecting an inflow without a corresponding outflow ($\sum In \neq \sum Out$). The `002_2_1` filter *must* immediately flag the loss of systemic mass.
* **Triggering Time Lag Detection:** The Simulator perfectly copies the waveform of Node A, delays it by exactly $N$ time steps, and injects it into Node B. The `001_2_1` filter *must* correctly output an optimal lag of exactly $N$.

## 4. Integration with CI/CD

Because the simulator operates deterministically based on a `--seed` argument, these synthetic streams are integrated directly into TLU's automated testing suite (`batch_unittest.sh`). Every time a core mathematical function is updated, the pipeline is bombarded with these synthetic anomalies to ensure the analytical integrity of the entire system remains uncompromised.
