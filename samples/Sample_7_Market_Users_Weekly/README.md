# 🔬 Clinical Meta-Diagnostic Forensic Report: Collusive Syndicate Identification & Matched Orders via Direct Graph (Sample 7)

## 1. Executive Summary

* **Overall Diagnosis:** **Stock Market Collusive Syndicate / Collusive Syndicate Lock**
* **Severity:** 🟠 **HIGH (Extremely Serious Joint Market Manipulation)**
* **Clinical Overview:**
    Like Sample 6, this system displays **"extreme topological recirculation loops (spectral radius $\rho = 1.00$)"** and **"thermodynamic energy depletion."**

    While the bipartite graph was used to "identify manipulated tickers," this "direct user graph" mathematically exposes the cash recirculation structure between the colluding accounts.

    Additionally, a **"severe collapse of Free Energy Skewness (Skew = -2.72, Z-Score exceeded twice)"** indicating acute vulnerability to liquidity shock is detected. The fictitious round-trip fund transactions within the colluding group hijacked the liquidity (free energy) of the entire market, shutting out healthy external investment opportunities and exposing the system to sudden thermodynamic death (insolvency).

---

## 2. Limitations of Traditional Snapshots

It is extremely difficult to detect this anomaly using traditional management dashboards where users (investors) are nodes and fund inflows/outflows between users are edges. Below are the cumulative volume (P/L equivalent) and stock (B/S equivalent) charts and weekly trends across the entire period:

* **P/L Equivalent (Total Flow per User):**
    ![P/L Trend](readme_plots/000_0_1__PL_Trend.png)
* **B/S Equivalent (Unbalanced Stock Accumulation):**
    ![B/S Trend](readme_plots/000_0_1__BS_Trend.png)

**【Blind Spots of Traditional Audits】**
Aggregating the net income (net assets change from the initial state) of individual users (accounts) at Simulation Week 52 (final period) yields:

* `USR_003`: **+$63,749,388.51** (Net fund inflow surplus: HFT / Market Maker)
* `USR_004`: **+$56,953,245.82** (Net fund inflow surplus: HFT / Market Maker)
* `USR_002`: **-$85,868,979.65** (Net fund outflow deficit: Whale who executed large-scale sell-offs)
* `USR_010`: **-$3,757,695.68** (Net fund outflow deficit: Retail investor who fell into panic selling)

*Note: When these rapid asset/profit changes occurred can be roughly identified from the B/S and P/L trend graphs above (specifically, the large-scale sell-off by whale `USR_002` and retail panic selling in Week 3, and the transaction bursts between `USR_003`/`USR_004` around Week 40 and Week 46). These detailed timelines and causal relationships will be verified in "3. Fundamental Pathophysiology" and "4. Mathematical Evidence" below.*

Looking only at the balance sheet or customer account balance rankings at a single point in time, traditional compliance audits merely recognize superficial results like "USR_003 produced excellent returns" or "USR_002 suffered large trading losses."

However, the **"process of collusion (existence of a clique)"**—where `USR_003` and `USR_004` pass the same ticker back and forth at identical prices in milliseconds to artificially create volume—falls completely out of this static balance list, remaining invisible.

---

## 3. Fundamental Pathophysiology

By discarding the intermediate ticker nodes and tracking only the moving paths of capital (mass), the Physics-Mathematics-Mathematics Engine exposes the core of the collusive syndicate (matched order loop):

* **Identified Collusion Structure:**
    The pathological causal attractor detected across the stock market is the ultra-high-speed direct matching transactions between `USR_003` and `USR_004` in 2020-W40 (`t_idx=39`) on `STK_004` (approx. $1,917.08 × 1,693 shares, 20 executions, approx. 1.0 second) and in 2020-W46 (`t_idx=45`) on `STK_003` (approx. $2,066.28 × 5,000 shares, 20 executions, approx. 1.0 second, totaling 40 transactions).

    This closed "infinite cash catch-ball circuit" between the two parties is the cancer cell (collusive clique) that squeezes the liquidity of retail investors (e.g., `USR_010`) and the overall market, depleting the free energy of the system.

---

## 4. Mathematical Evidence from the Physics-Mathematics-Mathematics Engine

### 4.1. Collusion Topology & Spectral Radius

The maximum spectral radius computed from the adjacency connection matrix in the direct user network clings to the upper boundary of **`1.00`** in 2020-W07 (`t_idx=6`), and continues to record an abnormal value of `0.989942` in 2020-W52.

This is mathematical proof that instead of new capital entering the market and circulating, energy (mass) is permanently recycled only between the specific pair `USR_003 -> USR_004 -> USR_003`, causing recirculation lock (thrombosis / organized clot).

* **System Stability Index (Spectral Radius):**
    ![System Stability](readme_plots/004_1_2__system_stability.png)

* **Network Topology 5-Point Sequence:**
  * **① Start (t=0 / 2020-W01):**
        ![Topology t0](readme_plots/002_1_2__network_topology.t.00000.png)
        Initial state. All users disperse and circulate funds evenly; no recirculation loop exists.
  * **② Just Before Change (t=38 / 2020-W39):**
        ![Topology t38](readme_plots/002_1_2__network_topology.t.00038.png)
        Before the anomaly. Topological stability is maintained.
  * **③ The Exact Point of Change (t=39 / 2020-W40):**
        ![Topology t39](readme_plots/002_1_2__network_topology.t.00039.png)
        The moment collusive trading triggers. An extremely thick bidirectional edge forms between `USR_003` and `USR_004`, clearly visualizing the collusive group.
  * **④ Immediately After Change (t=40 / 2020-W41):**
        ![Topology t40](readme_plots/002_1_2__network_topology.t.00040.png)
        Immediately after collusive trading. The collusive edge persists as the topological attractor of the entire system.
  * **⑤ End (t=51 / 2020-W52):**
        ![Topology t51](readme_plots/002_1_2__network_topology.t.00051.png)
        Final state. Although the temporary burst has ended, connection stiffness between users remains distorted.

### 4.2. Rigidity of Collusive Group & Proof of Stiffness Lock via Eigenvector Evolution

In the direct user graph, since no physical structural connections exist, Stiffness Matrix and partial correlation values during calm periods net out to `0.0`.

However, tracking the spatiotemporal evolution of the dominant eigenspace of the Stiffness Matrix using PCA (**"Eigenvector Evolution Chart (`000_2_3__eigenvector_evolution.png`)"**) vividly depicts how the PC1 component grows abnormally and locks the colluding accounts.

* **Eigenvector Evolution:**
    ![Eigenvector Evolution](readme_plots/000_2_3__eigenvector_evolution.png)

**【Anomaly Analysis based on the Eigenvector Evolution Chart】**

1. **Before the Anomaly (t=0 to 38 / 2020-W01 to W39):**
   Initial state `t=0` is zero, but subsequent steps show capital flows concentrating around `USR_002` (whale) and `USR_003` (HFT). Immediately before the anomaly at `t=38` (W39), the PC1 contribution ratio is **`85.15%`** (eigenvalue `1.0530e+15`), with PC1 loadings concentrating on `USR_002` (`-0.7499`) and `USR_003` (`0.6475`).
2. **At Anomaly Onset (t=39 to 40 / 2020-W40 to W41):**
   At `t=39` (W40), the PC1 contribution ratio is **`67.24%`** (eigenvalue `3.3610e+14`), with loadings shifting to `USR_002` (`-0.7720`), `USR_004` (`0.5166`), and `USR_003` (`0.3645`).
   At `t=40` (W41), the PC1 contribution ratio surges to **`99.67%`** (eigenvalue `3.2624e+14`), completing a powerful "Stiffness Lock" that dominates almost 100% of the system. The PC1 vector loadings concentrate abnormally on the wash trade colluders **`USR_004` (`0.7287`)** and **`USR_003` (`-0.6820`)**, proving that the closed recirculation lock between the two parties hijacked the degrees of freedom (liquidity) of the entire market.
3. **Evacuation to PC2 during Calm Periods (t=41 to 44 / 2020-W42 to W45):**
   Between the first (W40) and second (W46) waves of matched orders, the loadings of `USR_003` and `USR_004` on the PC1 chart temporarily drop near `0.0`.
   This is because their wash trading paused, letting the system's dominant variation (PC1, contribution ratio `87.84%`) shift back to normal large-scale fund transfers between `USR_001` and `USR_002`. However, their collusive relationship did not disappear. During this period (specifically at `t=42` (`2020-W43`)), `USR_003` and `USR_004` evacuated to **PC2 (contribution ratio `12.16%`)**, maintaining high loadings of **`USR_004` (`-0.6965`)** and **`USR_003` (`0.6921`)**.
4. **Final Step (t=51 / 2020-W52):**
   PC1 contribution ratio is **`97.59%`** (eigenvalue `2.0151e+15`), with the connection between `USR_002` (`-0.7135`) and `USR_003` (`0.6992`) locked.

* **PCA Principal Axes Ratio:**
    ![PCA Ratio](readme_plots/000_2_2__principal_axes_ratio.png)

### 4.3. Recirculation Thermodynamics & Anomaly Friction Detection

This market network is a closed kinetic system, so the internal energy $U$ (blue area) showing overall activity remains constant at **`3.725665e+09`** throughout the period. The free energy $F$ (solid white line) showing actual resources also remains stable at a high positive range of `3.3e+09` to `3.7e+09`, indicating that the market's basic structure remains robust.

However, during the anomalies and position adjustments, the system detects a prominent increase in "frictional heat ($-TS$: maroon area)."

* **Thermodynamics Energy Stack:**
    ![Thermodynamics Energy Stack](readme_plots/001_1_2__thermodynamics_energy_stack.png)

**【Thermodynamic Friction Detection Mechanism】**
When wash trading or rapid fund transfers occur, they temporarily raise local flow distribution dispersion (entropy $S$) and volatility (temperature $T$), expanding friction ($TS = U - F$) as dissipative energy.

The Physics-Mathematics-Mathematics Engine successfully extracts and visualizes this "hollow local friction" as a clean energy loss signal, without disrupting the overall market structure.

The Temperature-Entropy (T-S) diagram clearly shows the "counterclockwise closed oval trajectory" triggered by circular trading. This represents a "fictitious recirculation engine" that merely spins capital internally, generating fee costs (friction) without delivering economic value.

* **T-S Diagram:**
    ![T-S Diagram](readme_plots/001_1_3__thermodynamics_ts_diagram.png)

### 4.4. 3D Information Geometry Surface identifying Collusive Group

In the **3D spatiotemporal information geometry plot (`002_2_2_1__3d_micro_kl_drift.png`)**, following the massive panic dump by whale `USR_002` in W03, giant KL Drift spikes (local_kl_drift = 20.7233) tower from the coordinates of retail investors `USR_007` and `USR_010` in 2020-W07 (`t_idx=6`). Spikes are also captured at `USR_010` and `USR_005` in W40 and W46, highlighting the aftermath of the market manipulation (wash trading) and panic selling across the entire system.

* **3D Micro Z-Score (Position):**
    ![3D Micro Z-Score](readme_plots/002_2_2_2__3d_micro_z_score_X.png)
* **3D Micro KL Drift:**
    ![3D Micro KL Drift](readme_plots/002_2_2_1__3d_micro_kl_drift.png)

---

## 5. LQR Control Treatment

* **Treatment Plan:** **Blocking of Collusive Path & Disruption of Phase Synchronization via Dynamic Latencies**
* **LQR Sensitivity Intervention (Acupoint Identification):**
    In LQR flow control sensitivity analysis, the nodes showing the maximum dynamic intervention sensitivities are `02_USR_003` and `03_USR_004` (with sensitivity `41.5234`).
* **Specific Intervention Plan:**
    1. **Dynamic Interlock on Matched Orders (Phase Disruption):**
       When opposite buy/sell orders of identical prices and volumes are matched between `USR_003` and `USR_004` within a short window (e.g., 1 minute), force-inject a random execution latency (tens of milliseconds) in the matching engine. This physically breaks up the algorithm's phase synchronization (circular catch-ball), dismantling the loop.
    2. **Acupoint-based Trading Limit on Colluding Nodes (Stiffness Softening):**
       Implement dynamic credit reduction or individual approval flows for the accounts `USR_003` and `USR_004` acting as the hubs of recirculation, only during suspected periods. This targets the pathological nodes without reducing the overall liquidity of other market participants.
        ![LQR Performance Space](readme_plots/004_1_3__control_lqr_performance_space.png)

---

## 6. 🚨 Forensic Alert & Falsification Analytics

### 6.1. Model Pollution Assessment (Boiled Frog Syndrome)

* **Statistical Baseline Pollution:**
    Consolidated accounts (`USR_003`, `USR_004`) matching orders over weeks or months adapts the statistical AI model to the abnormal volume, flatlining the Z-Score warning alerts (boiled frog syndrome / false negatives).
* **Triage based on Physical Invariants:**
    However, regardless of how statistics are manipulated, the spatiotemporal physical invariants—"maximum spectral radius $\rho \ge 0.95$" and the "closed T-S cycle trajectory"—continue to robustly convict the ongoing circular collusion. During triage, the statistical silence is rejected, and the collusive state is determined to be ongoing.

### 6.2. Falsifiability

To prove that "these fund transfers represent legitimate business transactions and not collusive matched orders," the parties must present the following **"original physical evidence from outside the database"**:

1. **Bank Wire API Logs / SWIFT Records:**
    Original bank statements or SWIFT transfer logs issued directly by financial institutions that match the transaction amounts (representing W40's $1,917.08 × 1,693 shares × 20 times, and W46's $2,066.28 × 5,000 shares × 20 times). This provides physical proof that actual, independent, real-time fund settlements were executed (not just book-entry offsetting).
2. **Communications Records between Entities:**
    Original message logs (such as Slack, WeChat, etc.) certified by the telecommunications carrier proving that no agreements to coordinate prices existed between `USR_003` and `USR_004`, and that each party ordered independently based on their own analysis.
