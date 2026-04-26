# 06. Dummy Data Generators

> **"A diagnostic engine is only as good as the anomalies it can detect."**

To validate the analytical power of the Tensor-Link Utility (TLU), the system includes two sophisticated dummy data generators. These are not simple random number generators; they are designed to simulate complex, real-world network dynamics and inject mathematically precise anomalies to test the limits of TLU's detection capabilities.

---

## 1. Dummy Journal Generator (Financial/Organizational Flow)
**Script:** `src/filters/_0_0_generate_dummy_journal.py`  
**Execution:** `bash bin/batch_generate_dummy_journal_data.sh`

This generator simulates the daily accounting journal entries of a medium-sized enterprise over a multi-year period. It models departments (Sales, R&D, Ops, etc.) and accounts (Cash, AR, AP, etc.) as nodes in a network.

### Natural Base Dynamics
* **Scale-Free Network Topology:** Transactions follow power-law distributions. A few nodes (like `Cash` or `Accounts_Payable`) act as massive hubs, while others are peripheral.
* **Causal Event Queues (Viscosity):** A sale today (`Sales -> AR`) schedules a collection event 30-60 days in the future (`AR -> Cash`). This temporal delay creates natural "Viscosity" in the Phase Space mechanics.
* **Pink Noise (1/f Noise):** Transaction volumes are modulated by fractal noise to simulate natural business cycles and macroeconomic trends, avoiding artificial "flatness."

### Anomaly Injection Mechanisms
The generator deliberately injects specific structural and volume anomalies to trigger TLU's Forensics and Topology filters:

1. **Z-Spike (Outlier Expenditure):** A sudden, massive one-off transaction. Easily caught by standard Z-score analysis (Micro Forensics).
2. **Leak (Embezzlement/Conservation Loss):** Funds are moved out of the system without a balancing entry. Caught by the Macro Forensics Conservation Leak detector.
3. **Drift (Silent Supplier Swap):** The total expenditure of a department remains perfectly normal, but the *destination* of the funds suddenly shifts to a new vendor. Invisible to Z-scores, but creates a massive spike in **Local KL Drift**.
4. **Wash Trading (Circular Transactions):** A series of transactions specifically designed to form a closed loop (e.g., `Cash -> AR -> Sales -> Cash`). This breaks the natural Directed Acyclic Graph (DAG) structure of the accounting ledger and is instantly flagged by the **System Stability (Spectral Radius)** filter.

---

## 2. Dummy Traffic Generator (Physical/Logistical Flow)
**Script:** `src/filters/_0_0_generate_dummy_traffic.py`  
**Execution:** `bash bin/batch_generate_dummy_traffic_data.sh`

While the Journal Generator focuses on accounting, this generator simulates physical object flow, modeled after the grid-like intersections of Kyoto's street plan (e.g., Shijo-Karasuma).

### Characteristics
* **Spatial Grid Network:** Nodes represent physical intersections, and edges represent road segments. Flow is restricted to physically adjacent nodes.
* **Centralized Gravity:** Traffic volume naturally clusters around the center of the grid (simulating downtown Kyoto), generating steep "valleys" in the Information Curvature manifold.
* **Congestion Simulation:** Allows testing of Structural Stiffness (how a shock at one intersection ripples to adjacent ones) and Manifold Dimensionality (how traffic jams cause the effective rank of the network to collapse).

This generator proves that TLU's mathematical abstractions (Mass, Viscosity, Entropy) are domain-agnostic and apply equally well to physical logistics as they do to financial ledgers.
