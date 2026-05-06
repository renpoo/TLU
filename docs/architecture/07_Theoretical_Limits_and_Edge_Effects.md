# 07. Theoretical Limits and Edge Effects

## 🔬 Conclusion: "Computational Blind Spots" Exist in All Physical Models

The greatest conclusion in the final chapter of the TLU architecture is the unflinching observation of the cold fact that: **"No matter how advanced the thermodynamic or information-geometric engine is, in initial states where data volume is extremely low, or at the edges of the network, mathematical formulas are destined to break down and generate 'fake anomalies (Edge Effects)'."**

To prevent generating false audit results (false accusations) due to blind faith in the system, TLU openly states its own "computational limits" and warns auditors to discount and interpret the results in those areas.

---

## Extreme States of Data and Model Collapse

Physics and statistics models exhibit their greatest power in tranquil spaces (macro) where a certain "Law of Large Numbers (sufficient data volume)" and "continuity" are guaranteed.

### The Cold Start Problem (Data Vacuum)

* **Entropy of the Initial State:** Immediately after a company is established, or in the month a new account is opened (around $t=0$), there is too little data to establish comparisons with the past (Z-Score or KL Drift). In this data vacuum, a phenomenon known as "Cold Start Noise" occurs, where even the slightest transaction is detected as an "astronomical spike" of an anomaly.

### Edge Nodes (Isolated Singularities)

* **Stiffness of Depopulated Nodes:** Terminal nodes (edges) located far from the center of the transaction network, where transactions occur perhaps only once a year, do not have enough force (flux) to calculate the "spring constant" in a dynamic model. The stiffness of such nodes tends to diverge during calculation, sometimes emitting fake "collapse" signals.

---

## Addressing and Mitigating Edge Effects (Smoothing)

To address these theoretical limits (macro blind spots), TLU's core algorithms incorporate mathematical and engineering "buffers (cushions)" at the micro level.

### Laplace Smoothing and Injection of Minute Constants

* To prevent the system from crashing due to the denominator becoming zero (division by zero error) during the calculation of Z-Score, KL Drift, or the stiffness matrix, TLU injects a minute constant like `epsilon = 1e-6` (Laplace Smoothing) into the foundation of the math.
* This ensures that even in extreme states, the system does not halt with an error, but rather converts "computational singularities" into gentle slopes, allowing the auditor to visually and intuitively understand, "Ah, this is a depopulated zone with too little data."

---

## 🔬 Falsifiability and Model Limits

This document itself is the very embodiment of TLU's **"Falsifiability and Model Limits."** The physics engine asserts the calculation result that "the Z-Score of this node is extremely high," but mathematics alone cannot completely eliminate the possibility that it is a "fake spike caused by extremely low data (Edge Effect)."

When an abnormal spike is detected at an edge (in the initial period or at a terminal node with few transactions), auditors must hold a healthy skepticism (critical spirit)—asking "Is this a sign of massive fraud, or just cold start noise?"—and make a judgment by checking the raw data logs (Additional Verification). The system is a perfect "Calculator," but it is not a perfect "Judge."
