# 004. Control Theory and Stability Analysis

## 🔬 Conclusion: Is the System Controllable, or in a "Death Spiral"?

This document explains the Control Theory approach, which views the network as an autonomous control system and mathematically diagnoses whether "the entire system is running out of control toward collapse."
The conclusion here is: **"Is the system in a 'controllable state' maintaining self-purification (dampening), or has it fallen into a 'Death Spiral' possessed by infinite echoes (loops)?"**

Loops of "Wash Trading" or "Market Manipulation" formed by malicious actors are always detected as a "breach of the Spectral Radius (abnormal expansion rate) threshold" that causes the entire system to run out of control.

---

## Definitive Evidence of Wash Trading (Spectral Radius)

By tracking the maximum absolute eigenvalue of the matrix (Spectral Radius), we determine whether a shock occurring within the system will "naturally disappear (dampen)" or "continue to be amplified forever (diverge)."

### [Comparison 1] Healthy Dampening and Self-Purification (Baseline)

![Sample 0 Stability](../../samples/Sample_0_Healthy/readme_plots/004_1_2__system_stability.png)

* **Sample 0 (Healthy)**: The blue line on the graph, "Spectral Radius," is consistently well below the "1.0" threshold (dashed red line). This means that even if market shocks or temporary deficits occur, the system possesses a "healthy self-purification action" to self-absorb them and return to a normal state.

### [Comparison 2] The Critical Point of Self-Collapse due to an Infinite Loop (Wash Trade)

![Sample 1 Stability](../../samples/Sample_1_Wash_Trade/readme_plots/004_1_2__system_stability.png)
*(※Sample 1: Pierces through 1.0 after Week 41)*

* **Sample 1 (Wash Trade)**: From the middle of the graph, the blue line pierces through the "1.0" threshold and stays high (or diverges). Mathematically, "reaching 1.0" means that an undampening **"Topological Feedback Loop (an infinite topological echo)"** has been formed. This is definitive evidence that the system has completely lost its self-purification action as a result of malicious actors continuing to circulate funds (A→B→C→A) to create fictitious sales.

---

## Optimal Piloting Route and Vulnerabilities (Control LQR / Sensitivity)

After confirming whether the system is in a runaway state, we verify, "If management (or an intervener) tried to return the system to a normal trajectory, is that physically possible? Where are the vulnerabilities?"

### Detection of an Uncontrollable State (Control Error Convergence)

![Sample 0 Error Convergence](../../samples/Sample_0_Healthy/readme_plots/004_1_2__control_error_convergence.png)
*(Above image: Healthy control in Sample 0, where the error converges to zero)*

* **📊 Visual Structure**: A line graph showing the reduction of "error" relative to the target during the process of calculating the optimal fund injection plan (LQR Autopilot).
* **🚨 Anomaly Detection**: In a healthy state, the line descends smoothly toward zero. However, if the system is chaotic, it continues to bounce violently up and down, or flatlines at a position far above zero. This indicates a state where "no safe route can be found to return the system to a healthy state (Uncontrollable)," even with advanced mathematical optimization.

### The Organization's Achilles' Heel (Sensitivity Matrix Heatmap)

![Sample 0 Sensitivity Matrix](../../samples/Sample_0_Healthy/readme_plots/004_2_1__sensitivity_matrix.png)

* **📊 Visual Structure**: A matrix showing how sensitively another department reacts when a change is made to one department (node).
* **🚨 Anomaly Detection**: If a sudden bright color indicating extreme sensitivity appears at a specific intersection (cell), the organization is in an extremely "fragile (hypersensitive)" state regarding a specific factor. This warns that a slight over-expenditure or operational delay there is a vital point (bottleneck) that will immediately cause a company-wide cash crisis or operational halt.

---

## 🔬 Falsifiability and Model Limits (Application to Practice)

The Control Theory approach asserts the **mathematical fact** that "an infinitely amplifying loop (Spectral Radius ≥ 1.0) exists within the system, and the system has lost its self-purification action."
However, Control Theory alone cannot determine whether the formative factor of that loop is an "intentional Ponzi scheme by a malicious market manipulation group" or an "unintended chain of self-dealing due to an algorithm trading bug."

Upon detecting a Spectral Radius anomaly, system administrators must recognize that "leaving this alone will definitely destroy the entire system (Death Spiral)" and immediately take action, such as executing an emergency stop (triggering a circuit breaker) or enforcing a mandatory log audit (additional verification) on the specific nodes constituting the abnormally oscillating loop.
