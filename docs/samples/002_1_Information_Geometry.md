# 002_1. Information Geometry & Topology

This guide describes the information geometry analysis module (`002_1`) in the Tensor-Link Utility (TLU). It provides explanations based on the outputs and values of each sample for each chart type.

---

## 🔬 Theory of Information Geometry and Mass Conservation

Kirchhoff's first law (current law = mass conservation) holds in closed physical networks. The difference between total inflow and outflow at a node is defined as the "Conservation Residual" or "Relative Leak Ratio":

$$Residual_i = \sum Flux_{in} - \sum Flux_{out}$$

Under double-entry constraints in normal accounting or physical distribution, this residual is always `0.00`. If a positive residual persists over time, it indicates that mass (funds or vehicles) is leaking out of the system (e.g., off-book embezzlement).

The displacement of the system's probability distribution (velocity of structural change) is measured as "KL Divergence Drift" on the information manifold. This detects structural disruptions (phase transitions) that standard statistical Z-Scores cannot detect.

---

## 📊 Findings of Information Geometry & Topology Charts

### 1. Network Topology Time-Series (`002_1_2__network_topology.t*.png`)

This directed graph shows the time-series changes of the network topology. Edge thickness represents transaction volume or physical flow between nodes.

#### 🟢 Sample 0 (Healthy Metabolism)

**Clinical Commentary:**
Transaction flows (edges) are distributed and circulate throughout all periods. There is no topological bias where specific cycles become thick and fixed.
![Sample 0 Topology t0](Sample_0_Healthy/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 0 Topology t3](Sample_0_Healthy/readme_plots/002_1_2__network_topology.t.00003.png)

#### 🟡 Sample 1 (Wash Trade)

**Clinical Commentary:**
At the start of the anomalies ($t=0$ and $t=4$), bidirectional edges connect `ACC_Cash` and `ACC_Accounts_Receivable`.
![Sample 1 Topology t0](Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 1 Topology t3](Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00003.png)
![Sample 1 Topology t4](Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00004.png)
![Sample 1 Topology t5](Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00005.png)
![Sample 1 Topology t11](Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00011.png)

#### 🔴 Sample 2 (Embezzlement Leak)

**Clinical Commentary:**
The anomaly progresses. Funds leak from `Accounts_Receivable` to a node named `UNKNOWN_LEAK`. A unidirectional edge becomes persistent.
![Sample 2 Topology t0](Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 2 Topology t1](Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00001.png)
![Sample 2 Topology t2](Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00002.png)
![Sample 2 Topology t3](Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00003.png)

#### 🟡 Sample 3 (Unbalanced Mistake)

**Clinical Commentary:**
A single-sided input error occurs at $t=1$ (2020-02). Only one side of the accounts receivable node connects, indicating an unbalanced state. The mistake is corrected in the next period ($t \ge 2$). The topology returns to the normal distributed connection state.

- ![Sample 3 Topology t0 (Normal)](Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00000.png)
- ![Sample 3 Topology t1 (Error Occurs)](Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00001.png)
- ![Sample 3 Topology t2 (Post-Error)](Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00002.png)
- ![Sample 3 Topology t3 (Resolved Normal)](Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00003.png)
- ![Sample 3 Topology t4 (Post-Resolution)](Sample_3_Unbalanced_Mistake/readme_plots/002_1_2__network_topology.t.00004.png)

#### 🔴 Sample 4 (Composite Chaos)

**Clinical Commentary:**
Bidirectional wash trade edges and the bypass leak edge to `UNKNOWN_LEAK` appear simultaneously. This shows a polarization of the topology.
![Sample 4 Topology t0](Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 4 Topology t3](Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00003.png)
![Sample 4 Topology t4](Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00004.png)
![Sample 4 Topology t5](Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00005.png)
![Sample 4 Topology t8](Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00008.png)
![Sample 4 Topology t11](Sample_4_Composite_Chaos/readme_plots/002_1_2__network_topology.t.00011.png)

#### 🔴 Sample 5 (Kyoto Traffic)

**Clinical Commentary:**
Traffic deadlock occurs at $t=18$. Edges around bottlenecks like `23_Shijo_Karasuma` and `21_Shijo_Muromachi` become thick. Vehicles stay stuck there. Edges on surrounding roads disappear.

- ![Sample 5 Topology t0](Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00000.png)
- ![Sample 5 Topology t10](Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00010.png)
- ![Sample 5 Topology t11](Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00011.png)
- ![Sample 5 Topology t12](Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00012.png)
- ![Sample 5 Topology t14](Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00014.png)
- ![Sample 5 Topology t23](Sample_5_Kyoto_Traffic/readme_plots/002_1_2__network_topology.t.00023.png)

#### 🟢 Sample 6 (Market Stock Flow)

**Clinical Commentary:**
We analyze the market bipartite graph. Directed edges connecting cooperating USR accounts and target stock nodes increase. These mask the autonomous order edges of the whole market.

- ![Sample 6 Topology t0](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00000.png)
- ![Sample 6 Topology t6](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00006.png)
- ![Sample 6 Topology t12](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00012.png)
- ![Sample 6 Topology t18](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00018.png)

#### 🟢 Sample 7 (Market Cash Flow)

**Clinical Commentary:**
Payment liquidity convection occurs. A bidirectional edge connects `USR_003` and `USR_004`. Liquidity is locked between them for a long time.

- ![Sample 7 Topology t0](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00000.png)
- ![Sample 7 Topology t6](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00006.png)
- ![Sample 7 Topology t12](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00012.png)
- ![Sample 7 Topology t18](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00018.png)

#### 🔴 Sample 8 (fMRI Stroke)

**Clinical Commentary:**
A stroke occurs at $t=30$. Functional connectivity edges flowing into or out of the stroke region (motor area) disappear. This visualizes the topological disruption.
![Sample 8 Topology t0](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 8 Topology t29](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00029.png)
![Sample 8 Topology t30](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00030.png)
![Sample 8 Topology t31](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00031.png)
![Sample 8 Topology t59](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00059.png)

#### 🔴 Sample 9 (fMRI Seizure)

**Clinical Commentary:**
An epileptic seizure burst occurs. BOLD activity edges across all brain regions change into a hyper-synchronous pattern. The whole brain is hijacked by this single oscillatory pattern.
![Sample 9 Topology t0](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 9 Topology t29](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00029.png)
![Sample 9 Topology t30](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00030.png)
![Sample 9 Topology t31](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00031.png)
![Sample 9 Topology t32](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00032.png)
![Sample 9 Topology t33](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00033.png)
![Sample 9 Topology t34](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00034.png).

- ![Sample 6 Topology t0](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00000.png)
- ![Sample 6 Topology t6](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00006.png)
- ![Sample 6 Topology t12](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00012.png)
- ![Sample 6 Topology t18](Sample_6_Market_Stock_Flow/readme_plots/002_1_2__network_topology.t.00018.png)

#### 🟢 Sample 7 (Market Cash Flow)

**Clinical Commentary:**
During payment liquidity convection, a thick bidirectional edge directly connects `USR_003` and `USR_004`. It shows funds bouncing between them, locking liquidity for a long time.

- ![Sample 7 Topology t0](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00000.png)
- ![Sample 7 Topology t6](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00006.png)
- ![Sample 7 Topology t12](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00012.png)
- ![Sample 7 Topology t18](Sample_7_Market_Cash_Flow/readme_plots/002_1_2__network_topology.t.00018.png)

#### 🔴 Sample 8 (fMRI Stroke)

**Clinical Commentary:**
A stroke occurs at $t=30$. Functional connectivity edges flowing into or out of the stroke region (motor area) disappear. This visualizes the topological disruption.
![Sample 8 Topology t0](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 8 Topology t29](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00029.png)
![Sample 8 Topology t30](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00030.png)
![Sample 8 Topology t31](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00031.png)
![Sample 8 Topology t59](Sample_8_fMRI_Stroke/readme_plots/002_1_2__network_topology.t.00059.png)

#### 🔴 Sample 9 (fMRI Seizure)

**Clinical Commentary:**
With the epileptic seizure synchrony burst, BOLD activity edges across all brain regions change into a hyper-synchronous pattern. The whole brain is hijacked by this single oscillatory pattern.
![Sample 9 Topology t0](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 9 Topology t29](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00029.png)
![Sample 9 Topology t30](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00030.png)
![Sample 9 Topology t31](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00031.png)
![Sample 9 Topology t32](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00032.png)
![Sample 9 Topology t33](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00033.png)
![Sample 9 Topology t34](Sample_9_fMRI_Seizure/readme_plots/002_1_2__network_topology.t.00034.png)
