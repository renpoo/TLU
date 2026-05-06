# 06. Dummy Data Generators

## 🔬 Conclusion: Anomalies Cannot Be Defined Without a "Sterile Baseline"

The ultimate conclusion of the "Dummy Data Generation (Data Simulation)" phase in the TLU architecture is the design philosophy that: **"To make the system detect anomalies, we must first mathematically create a 'perfectly healthy state containing absolutely no noise (Sample 0),' and use it as the primary standard (baseline) for comparison."**

TLU's dummy data generation scripts (`_0_0_generate_dummy_*.py`) are not just random lists of numbers; they function as virtual space simulators that strictly obey the "laws of nature" of thermodynamics and kinematics.

---

## Simulation Obeying the Laws of Nature

The Dummy Data Generation Engine implements the physical and commercial "gravity (rules)" of the target domain (finance, traffic, etc.) as code.

### Domain-Specific Generation Logic

* **Finance (Financial Ledger):** Automatically generates journal data that perfectly complies with the "Principle of Balancing Debits/Credits (Law of Conservation of Mass)" of double-entry bookkeeping and "economic rationality," such as the relationship between sales and accounts receivable, payment cycles, and reinvestment of profits.
* **Traffic Flow:** Generates a "normal flow of cars" based on fluid dynamics and queuing theory, considering the inflow and outflow of vehicles and the processing capacity of intersections (spring strength).

When analyzed through the TLU physics engine, these generated data are tuned to ALWAYS show up as a **"Healthy Natural Growth (Sample 0)"** exhibiting upward-trending Free Energy and stable stiffness.

---

## Deterministic Injection of Anomalies (Simulating Pathology)

After generating the sterile baseline (macro), we deterministically (intentionally) inject micro anomalies to carve specific "pathologies (signatures)" into the system.

### Injecting "Poison (Anomalies)" for Forensics

* After calling the generating function that serves as the baseline, the script pinpoints a specific period (e.g., Week 30 to Week 40) or specific nodes (e.g., Branch A and a phantom company), and forcibly overwrites and injects data representing a "malicious infinite loop (Wash Trading)" or "mass deficit to the outside (Embezzlement)."
* This completes validation samples (Samples 1 to 10) possessing an **Absolute Ground Truth** of "when, where, who, and what kind of physical destruction was performed."

---

## 🔬 Falsifiability and Model Limits

The Dummy Data Generation Architecture asserts the **engineering fact** that "it created a perfectly controlled virtual dataset according to predefined mathematical formulas and probability distributions."
However, this simulation does not 100% mimic the "complex and unreasonable noise of the real world (human capricious mistakes, the impact of unknown viruses, etc.)."

Even if the system achieves perfect anomaly detection scores on synthetic data (Samples), when applied to real-world raw data, false positives may occur due to noise the simulator did not anticipate. In such cases, engineers must recognize that "the simulator's mathematical model has not caught up with the complexity of the real world" and return to improving the data generation pipeline itself (Additional Verification).
