# 002. Information Geometry & Forensics

> **"Anomalies do not merely spike in volume; they distort the very fabric of the network."**

Category **002** represents the audit, security, and anomaly detection layer of TLU. While previous layers treat data as physical entities (mass and energy), this paradigm moves into the realm of **Information Geometry** and **Statistical Forensics**.

It treats the network as a statistical manifold—a mathematical "space" shaped by probability distributions. By measuring how this space warps, stretches, or breaks its own conservation laws, TLU can detect both sudden shocks and silent, structural regime shifts.

---

## 1. Information Geometry (Manifold Distortion)

How does the network route its resources? If we treat the historical allocation percentages as a probability distribution, we can map the entire organization as a multidimensional landscape.

### Information Curvature (002_1_1)
*Implementation: `src/filters/_002_1_1_filter_info_curvature.py`*

Just as mass bends spacetime in general relativity, heavy concentrations of activity warp the organizational manifold. TLU calculates the **Information Curvature** by measuring the rate of change in the Fisher Information Metric against local volatility.

* When visualized in 3D, high curvature appears as sharp "peaks" or steep "valleys."
* A sudden spike in curvature indicates an unnatural concentration of flux or a severe stagnation point—resources are pooling somewhere they historically haven't, creating a localized gravity well.

![002_1_1__3d_info_curvature](../readme_plots/002_1_1__3d_info_curvature.png)
![002_1_2__info_stress_scatter](../readme_plots/002_1_2__info_stress_scatter.png)

### Topological Edge Stress (002_1_2)
*Implementation: `src/filters/_002_1_2_filter_network_topology.py`*

While curvature looks at regions, this filter looks at the specific "blood vessels" connecting them. TLU calculates the **Topological Edge Stress** by converting the flux of every single edge into a rolling Z-score compared to its historical baseline.

* It highlights critical bypasses and hidden bottlenecks that are carrying a historically unprecedented load, warning of an impending "rupture" (processing failure or supply chain breakdown) before the node itself fails.

![002_1_2__network_topology t 00000](../readme_plots/002_1_2__network_topology.t.00000.png)
![002_1_2__network_topology t 00001](../readme_plots/002_1_2__network_topology.t.00001.png)
![002_1_2__network_topology t 00002](../readme_plots/002_1_2__network_topology.t.00002.png)
![002_1_2__network_topology t 00003](../readme_plots/002_1_2__network_topology.t.00003.png)
![002_1_2__network_topology t 00004](../readme_plots/002_1_2__network_topology.t.00004.png)

### Manifold Dimensionality (SVD) (002_1_3)
*Implementation: `src/filters/_002_1_3_filter_manifold_dimensionality.py`*

While Curvature identifies local stress points, **Manifold Dimensionality** assesses the global structural integrity of the network using Singular Value Decomposition (SVD).

* **Effective Rank:** TLU calculates the number of significant singular values of the transition matrix. If a network with 100 nodes suddenly drops to an effective rank of 5, it means the entire manifold has "collapsed." 
* **Detection of Over-Centralization:** This collapse indicates that instead of resources flowing naturally across the diverse network, almost all traffic is being artificially routed through just a handful of dominant hubs (e.g., a monopoly forming, or a massive traffic jam freezing the logistics grid).

## 2. Statistical Forensics & Conservation Laws

Forensics relies on mathematical invariants. If a fundamental law of the system is broken, it flags an anomaly—whether caused by data corruption, sudden market shifts, or intentional fraud.

### Macro Forensics: The Global Watchdog (002_2_1)
*Implementation: `src/filters/_002_2_1_filter_macro_forensics.py`*

* **Conservation Leak ($L$):** In systems like double-entry accounting or closed supply chains, the sum of all inflows and outflows should theoretically net to zero. TLU continuously monitors the absolute sum of all net fluxes. If the system "leaks" mass beyond a defined tolerance threshold, it instantly flags a violation of the conservation of energy.
* **Global KL Drift ($D_{KL}$):** Using Kullback-Leibler (KL) Divergence, TLU compares the current network-wide allocation distribution against a historical baseline. A slow, steady rise in Global KL Drift means the organization is undergoing a "Regime Shift"—its fundamental operating model is changing, even if total volumes remain exactly the same.

![002_2_1__macro_forensics_dashboard](../readme_plots/002_2_1__macro_forensics_dashboard.png)

### Micro Forensics: The Local Investigator (002_2_2)
*Implementation: `src/filters/_002_2_2_filter_micro_forensics.py`*

* **Local Z-Score Spikes:** TLU calculates a Mahalanobis-like standardized score for every individual node. This catches traditional anomalies: a department suddenly spending $3\sigma$ above its norm.
* **Local KL Drift:** This is the ultimate tool for detecting "silent diversion." If a node still receives and spends $10,000 a month (so its Z-score is normal), but it suddenly changes *who* it sends that money to (e.g., stopping payments to Vendor A and routing everything to new Vendor B), the Local KL Drift will spike violently, catching anomalies that pure volume metrics completely miss.

![002_2_2_2__micro_Z_Score_heatmap](../readme_plots/002_2_2_2__micro_Z_Score_heatmap.png)
![002_2_2_1__micro_KL_drift_heatmap](../readme_plots/002_2_2_1__micro_KL_drift_heatmap.png)

## 3. Business Implications

By applying Information Geometry and Forensics, risk managers and leadership can answer:

1. **Is there a silent regime shift occurring?** (High KL Drift without volume changes).
2. **Where is the system about to break?** (High Topological Edge Stress and Curvature peaks).
3. **Has the data integrity been compromised?** (Spikes in Conservation Leaks or anomalous local distributions pointing to potential fraud or missing data streams).
