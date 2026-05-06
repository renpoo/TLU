# Sample 6: Market Manipulation in the Stock Market (Bipartite Graph: Identification of Manipulated Stocks / Thermodynamics of Wash Trading)

> [!NOTE]
> **[IMPORTANT] Relationship Between Sample 6 and Sample 7 and Target Anomaly (Market Manipulation)**
> This sample (Sample 6) and the next sample (Sample 7) are a pair of experimental sets derived from exactly the same stock market dummy data.
> * **Sample 6 (This Report):** Projects logs onto a bipartite graph of "Users and Stocks." It verifies the perspective of **"Which stocks are being manipulated"** (the view from the left).
> * **Sample 7 (Next Report):** Projects the same logs onto a direct graph "between users." It verifies the perspective of **"Who is colluding with whom to conduct matched orders"** (the view from the right).

---

# 🔬 Meta-Analysis Synthesis Report / Laboratory Findings

## 1. Executive Summary
This system (stock market domain) is diagnosed as being in an extremely dangerous state (HIGH Severity) where the market's price formation function is completely destroyed, with the entire system exhibiting **"Extreme Topological Feedback Loops"** and accompanying **"Thermodynamic Energy Depletion."** It has been proven that the market's energy is dominated by fraudulent frictional heat due to repeated ultra-high-speed catch-balling (Wash Trade) of the same stock without substantive transfer of rights.

## 2. Limitations of Traditional Perspective

**[Cumulative Flow for the Entire Period (P/L Waterfall) & Balance Sheet (B/S)]**
![Sample 6 PL Waterfall](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_0_1__PL_Waterfall_Total.png)
![Sample 6 BS Block](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_0_1__BS_Block_Total.png)

Because the entirety of a stock market is a "pure kinetic system (closed system)," the net accumulation amount (B/S) for the entire period is plus/minus zero (blank slate). In the aggregation dashboards of traditional securities tools, a stock undergoing Wash Trade is merely displayed as an **"active and popular stock with rapidly increasing volume (massive P/L),"** inducing unrelated general investors to buy. Static aggregation tools cannot distinguish whether that massive volume is "meaningful economic activity" or "frictional heat orchestrated by a small number of people."

## 3. Fundamental Pathophysiology
The root cause of this sample is the intentional operation of a "Wash Trade" algorithm by a specific group of users.

* **Identified Evidence:**
  It was confirmed at the transaction level that two individuals, `USR_001` and `USR_006`, executed massive buy and sell orders of 1,000 to 3,000 shares (about $3000/share) for `STK_005` **9 consecutive times** within a mere **2.5 seconds**. The runaway state of this algorithm is the absolute source of the macroscopic abnormal indicators.

## 4. Physical and Mathematical Proof

### 4.1. Macro Forensics & Structural Stiffness

Because Wash Trade is a transaction completed within the market, mass leakage outside the system (macro residuals) does not occur. However, due to the recycling of funds at abnormal frequencies, the stiffness matrix (suspension) experiences a rigid lock (a market freeze where healthy external orders cannot be accepted) between specific nodes, falling into a state where it cannot receive healthy orders from the outside.

![Sample 6 Macro Forensics](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_2_1__macro_forensics_dashboard.png)
![Sample 6 External Force 3D](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_1_6__3d_dynamics_external_force.png)

* **1st Image [Start]**: `t.00000` (Normal stiffness)
* **2nd Image [Just Before Change]**: `t.00005` (Week 6)
* **3rd Image [At the Time of Change]**: `t.00006` (Week 7: Rigidity occurs due to fund recycling)
* **4th Image [Just After Change]**: `t.00007` (Week 8)
* **5th Image [End]**: `t.00051` (Week 52)

![Sample 6 Structural Stiffness Week 1](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_2_1__structural_stiffness.t.00000.png)
![Sample 6 Structural Stiffness Week 6](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_2_1__structural_stiffness.t.00005.png)
![Sample 6 Structural Stiffness Week 7](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_2_1__structural_stiffness.t.00006.png)
![Sample 6 Structural Stiffness Week 8](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_2_1__structural_stiffness.t.00007.png)
![Sample 6 Structural Stiffness Week 52](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/000_2_1__structural_stiffness.t.00051.png)

### 4.2. Topological Anomaly / Spectral Radius

The red line (Max Spectral Radius = intensity of the perfect fund recycling loop) is constantly pinned to the ceiling of `1.0` (theoretical limit). This mathematically proves that a perfect closed circuit (fund recycling loop) of `User A -> Stock X -> User B -> Stock X -> User A` has become normalized, and the market's energy is dominated not by "healthy investment from the outside" but by "internal self-orchestrated resonance (howling)."

![Sample 6 System Stability](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/004_1_2__system_stability.png)

* **1st Image [Start]**: `t.00000`
* **2nd Image [Just Before Change]**: `t.00005`
* **3rd Image [At the Time of Change]**: `t.00006`
* **4th Image [Just After Change]**: `t.00007`
* **5th Image [End]**: `t.00051`

![Sample 6 Network Topology W1](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_1_2__network_topology.t.00000.png)
![Sample 6 Network Topology W6](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_1_2__network_topology.t.00005.png)
![Sample 6 Network Topology W7](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_1_2__network_topology.t.00006.png)
![Sample 6 Network Topology W8](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_1_2__network_topology.t.00007.png)
![Sample 6 Network Topology W52](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_1_2__network_topology.t.00051.png)

### 4.3. Thermodynamic Energy Stack

Wash Trade keeps "substantive net increase/decrease of funds and positions (Internal Energy $U$)" near `0`, while astronomically increasing only the "gross transaction volume = frictional heat (Entropy $S$)." As a result, $F = 0 - T(\infty)$, and the free energy infinitely sinks into the negative. TLU accurately detects the contradiction of "high volume but no state change" as Thermodynamic Death (Heat Death = a state of only frictional heat without substantive economic activity).

*(Top: Sample 0 Healthy Economic Growth / Bottom: Sample 6 Thermodynamic Death)*
![Sample 0 Thermodynamics](../../../samples/Sample_0_Healthy/readme_plots/001_1_2__thermodynamics_energy_stack.png)
![Sample 6 Thermodynamics](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/001_1_2__thermodynamics_energy_stack.png)

### 4.4. 3D Micro Z-Score & KL Drift

In the 3D surface of Z-Score (degree of protrusion from past averages) and Information Geometric Mutation (KL Drift = extreme deviation from the past probability distribution of the market), extreme spikes protrude between certain specific stocks (Stock) and specific user groups (User), causing unnatural entropy to ripple across the entire market and visually demonstrating the contamination of the probability distribution.

![Sample 6 3D Z-Score](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_2_2_2__3d_micro_z_score_X.png)
![Sample 6 3D KL Drift](../../../samples/Sample_6_Market_Bipartite_Weekly/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

## 5. ⚠️ Falsification Analytics

* **Possibility of False Positives:** The possibility of an accidental resonance of market-making algorithms by HFT (High-Frequency Trading) firms is not zero. However, considering the extreme frequency of 9 times in 2.5 seconds and the perfect closed-circuit structure where the spectral radius is pinned at 1.0, it is extremely likely to be intentional market manipulation (Wash Trade).
* **Additional Verification Requirements:**
  Cross-reference the account opening information, IP addresses, MAC addresses, etc., of `USR_001` and `USR_006`, and request disclosure from regulatory authorities to confirm whether it is a Sybil attack where multiple accounts are recycled by the same person. Even if the method is unknown, fund recycling that contradicts the laws of physics cannot deceive TLU's eyes.
