# 🔬 Clinical Forensic Report: Composite System Failure (Wash Trade + Systematic Embezzlement) (Sample 4)

## 1. Executive Summary

* **Overall Status:** 🔴 **Composite System Failure (Coexistence of Wash Trade Loop and Embezzlement Leak / Composite Pathology)**
* **Severity:** 🔴 **CRITICAL (Dysfunctional State)**
* **Summary:**
  The system is in a "Composite Chaos" state. Circular wash trades inflate sales, and systematic embezzlement causes mass defects (leaks of cash).
  During the simulation, the maximum spectral radius indicating wash trades reached **`0.7861` at 2020-01 (t=0)** and **`0.7058` at 2020-02 (t=1)**, proving that the circular loop was active.
  Additionally, a mass conservation residual (Kirchhoff residual) appeared from 2020-06 (t=5) to 2020-09 (t=8). A **cumulative total of `$6,255.99`** in cash leaked out of the system and was directed to the `UNKNOWN_LEAK` node. In particular, a mass defect of **`$4,773.57`** occurred in **2020-09 (t=8)**.
  Traditional static audits cannot detect these anomalies because the B/S balances (total assets at `$1,296,558.10`) and the P/L shows a net profit of `$200,478.42`. The physics engine proved the presence of this composite scheme through the breakdown of conservation laws and structural stiffness.

---

## 2. Comparison of Financial Statements and Transaction Flows

We compare traditional cumulative financial statements with the periodic (single-month, non-cumulative) transaction flows.

When discrepancies occur, accountants balance the B/S using dummy accounts (`UNKNOWN_LEAK`) and blend the difference into the P/L. Audits looking only at cumulative values fail to detect this cash outflow.

### Balance Sheet (B/S) Comparison

* **B/S Asset & Equity Cumulative Trend & Block Chart (Cumulative):**
  ![B/S Cumulative Trend](readme_plots/000_0_1__BS_Trend.png)
  ![B/S Block Total](readme_plots/000_0_1__BS_Block_Total.png)

* **B/S Asset & Equity Periodic Trend (Monthly Non-Cumulative):**
  ![B/S Periodic Trend](readme_plots/000_0_1__BS_Trend_Periodic.png)

### Income Statement (P/L) Comparison

* **P/L Revenue & Expense Cumulative Trend:**
  ![P/L Cumulative Trend](readme_plots/000_0_1__PL_Trend.png)

* **P/L Revenue & Expense Periodic Trend (Monthly Non-Cumulative):**
  ![P/L Periodic Trend](readme_plots/000_0_1__PL_Trend_Periodic.png)

* **Observation:** The cumulative graphs show stable operations. However, the periodic graphs show flow spikes and structural distortions during the wash trade months (January to February) and embezzlement months (June to September).

---

## 3. Pathophysiology

* **Diagnosis:** **Coexistence of Wash Trade and Embezzlement Leak (Composite Chaos)**
* **Sequence of Fraud (Dummy_Journal_Stream.csv Origin Verified):**
  Two schemes co-occur and interfere with each other in this system:
  1. **Wash Trade Loop:** Self-reflux between cash, AR, and sales revenue inflates sales in January and February. The loop peaks in March with a cash velocity Z-Score of `z_score_v = 491.40`.
  2. **Systematic Embezzlement:** AR collections are routed off-book (cash debit is `$0.0`), or cash is directly withdrawn.
     The source data reveals the following 9 mass loss transactions from June to September:
     * **2020-06-04 (t=5)**: `E_001403` (AR decreases by `$130.55` but cash increases by `$0.00`, causing a leak of **`$130.55`**)
     * **2020-07-13 (t=6)**: `E_001725` (AR decreases by `$279.78` but cash increases by `$0.00`, causing a leak of **`$279.78`**)
     * **2020-07-25 (t=6)**: `E_001859` (AR decreases by `$362.39` but cash increases by `$0.00`, causing a leak of **`$362.39`**. July total is **`$642.17`**)
     * **2020-08-07 (t=7)**: `E_002002` (AR decreases by `$861.39` but cash increases by `$509.57`, causing a leak of **`$351.82`**)
     * **2020-08-17 (t=7)**: `E_002126` (AR decreases by `$477.53` but cash increases by `$394.49`, causing a leak of **`$83.04`**)
     * **2020-08-19 (t=7)**: `E_002154` (AR decreases by `$274.84` but cash increases by `$0.00`, causing a leak of **`$274.84`**. August total is **`$709.70`**)
     * **2020-09-09 (t=8)**: `E_002432` (Cash decreases by **`$4,534.35`** but AP decreases by `$0.00`. Direct cash withdrawal)
     * **2020-09-10 (t=8)**: `E_002437` (AR decreases by `$460.76` but cash increases by `$304.22`, causing a leak of **`$156.54`**)
     * **2020-09-22 (t=8)**: `E_002575` (AR decreases by `$82.68` but cash increases by `$0.00`, causing a leak of **`$82.68`**. September total is **`$4,773.57`**)
     * **Cumulative Leak Amount**: **`$6,255.99`**
  The physics engine directs this lost mass to the `UNKNOWN_LEAK` node and tracks the resulting structural stiffness changes.

---

## 4. Summary of Mathematical Analysis Results

### 4.1. Mass Conservation and Network Topology

The `System Conservation Residual` is non-zero after June, peaking at **`$4,773.57`** in September (cumulative: `$6,255.99`). The `UNKNOWN_LEAK` node connects to the network topology after June, and the edges indicating off-book leaks are visualized.

* **Macro Forensics Dashboard:**
  ![Macro Forensics](readme_plots/002_2_1__macro_forensics_dashboard.png)

* **Network Topology Evolution:**
  * **2020-01 (t=0 - Start of loop; circular circuit forms between Cash and AR):**
    ![Network Topology t0](readme_plots/002_1_2__network_topology.t.00000.png)
  * **2020-05 (t=4 - Before embezzlement starts; wash trade loop persists):**
    ![Network Topology t4](readme_plots/002_1_2__network_topology.t.00004.png)
  * **2020-06 (t=5 - Initial mass defect occurs, creating a bypass to `UNKNOWN_LEAK`):**
    ![Network Topology t5](readme_plots/002_1_2__network_topology.t.00005.png)
  * **2020-09 (t=8 - Peak embezzlement; drain edge to `UNKNOWN_LEAK` opens):**
    ![Network Topology t8](readme_plots/002_1_2__network_topology.t.00008.png)
  * **2020-12 (t=11 - Final step; persistent connections form the final topology):**
    ![Network Topology t11](readme_plots/002_1_2__network_topology.t.00011.png)

### 4.2. Stiffness Connection & PCA (Stiffness & PCA)

After embezzlement begins in June 2020 (`t=5`), the stiffness balance collapses, and stiffness between major nodes disappears. In the final step ( $t=11$ ), key hubs lock completely (**Stiffness Lock**), indicating permanent structural damage.
Because the system loses elasticity, it cannot damp external energy inputs, causing **abnormal resonance (knocking exceeding `1e9`)** in later steps.
In PCA, the PC0 eigenvalue reaches `1.59e10` (100% variance) in March (`t=2`), dominated by AR, Sales, and Cash. In September (`t=8`), the eigenvector contribution of the `UNKNOWN_LEAK` node appears, indicating that the leak channel has settled as part of the structure.

* **Evolution of Structural Stiffness Matrix:**
  * **2020-01 (t=0 - Initial Stiffness):**
    ![Stiffness t0](readme_plots/000_2_1__structural_stiffness.t.00000.png)
  * **2020-05 (t=4 - Before embezzlement; local stress from wash trading is detected):**
    ![Stiffness t4](readme_plots/000_2_1__structural_stiffness.t.00004.png)
  * **2020-06 (t=5 - Inflection point where initial mass defect occurs; stiffness shifts):**
    ![Stiffness t5](readme_plots/000_2_1__structural_stiffness.t.00005.png)
  * **2020-09 (t=8 - Peak embezzlement; stiffness balance collapses):**
    ![Stiffness t8](readme_plots/000_2_1__structural_stiffness.t.00008.png)
  * **2020-12 (t=11 - Final step; broken stiffness cannot recover, locking key nodes):**
    ![Stiffness t11](readme_plots/000_2_1__structural_stiffness.t.00011.png)

* **Principal Axis Ratios & Eigenvector Evolution (PC1, PC2, PC3):**
  ![PCA Ratio](readme_plots/000_2_2__principal_axes_ratio.png)
  ![PCA PC1 Evolution](readme_plots/000_2_3__eigenvector_evolution.png)
  ![PCA PC2 Evolution](readme_plots/000_2_3__eigenvector_evolution_pc2.png)
  ![PCA PC3 Evolution](readme_plots/000_2_3__eigenvector_evolution_pc3.png)

* **3D Dynamics External Force Resonance Map:**
  ![External Force 3D](readme_plots/000_1_6__3d_dynamics_external_force.png)

### 4.3. Evaluation of Wash Trades (Spectral Radius)

The maximum spectral radius reached **`0.7861` at 2020-01 (t=0)** and **`0.7058` at 2020-02 (t=1)**, exceeding the warning threshold (`0.6`). This provides topological evidence of the wash trade loop at the start. The radius decreased as the embezzlement scheme took over, but rose again to **`0.5951` in 2020-11 (t=10)**.

* **System Stability Indicator:**
  ![System Stability](readme_plots/004_1_2__system_stability.png)

### 4.4. Thermodynamic Indicators and 3D Topology

Although revenue grows, the net free energy $F$ (white line) flattens completely after June in sync with the cash leak.
The T-S diagram displays a closed loop in the first half (wash trade signature) and an open trajectory in the second half (embezzlement signature). These combine into a "twisted trajectory." This physically proves the overlay of wash trade synchronization and cash dissipation.

* **Thermodynamic Characteristics & 3D Trajectory:**
  ![Thermodynamics Energy Stack](readme_plots/001_1_2__thermodynamics_energy_stack.png)
  ![T-S Diagram](readme_plots/001_1_3__thermodynamics_ts_diagram.png)
  ![3D Phase Portrait](readme_plots/000_1_8__phase_portrait_3d.png)
  ![3D Local Entropy](readme_plots/001_1_2_1__3d_local_entropy.png)
  ![3D Local Temperature](readme_plots/001_1_2_2__3d_local_temperature.png)
  ![3D Micro KL Drift](readme_plots/002_2_2_1__3d_micro_kl_drift.png)

**【Information Geometry Phase Transition and Z-Score Model Pollution】**

* **3D Micro KL Drift:**
  In **2020-02 (t=1)**, the cash node triggers a KL Drift spike of **`4.2076`** (start of the loop). In the recovery period of **2020-11 (t=10)**, it reaches a peak of **`6.7072`** (structure returning to normal).
* **3D Micro Z-Score:**
  In **2020-03 (t=2)**, the cash node reaches **`z_score_X = 52.26`** and **`z_score_v = 491.40`**. Due to embezzlement, the `UNKNOWN_LEAK` node reaches a maximum Z-Score of **`16.55`** in **2020-09 (t=8)**. However, in later periods, the statistical model is polluted by anomalous data, causing Z-Scores to drop (false negatives). Physical and topological indicators (residuals and stiffness) continued to detect the anomalies.

---

## 5. Control Interventions and Recommended Actions (LQR & Operations)

* **Intervention Protocol: Break Reflux Paths and Freeze Leak Nodes**
* **Operational Control Interventions:**
  1. **Sever Reflux Paths:**
     Block advance payments (e.g., prepayments, advanced outsourcing costs) from `ACC_Cash` to `ACC_Accounts_Receivable` in the payment system. This destroys the start of the wash trade loop.
  2. **Restrict Unbalanced Entries:**
     Enforce system controls to reject journals where Debit does not equal Credit, preventing transfers of cash differences to `UNKNOWN_LEAK`.
  3. **Targeted Forensic Investigation:**
     Trace the approval records and target bank account of transaction **`E_002432`** (cash withdrawal of `$4,534.35`) in **2020-09 (t=8)**, which corresponds to the peak leak.

* **LQR Control Space:**
  ![LQR Control Space](readme_plots/004_1_3__control_lqr_performance_space.png)

### 💡 Quantitative Evaluation of Leverage Points for Cost Reduction

Based on Inverse Kinematics (IK) and LQR control effort, the leverage effect of reducing the three expense types (payroll, rent, travel) is ranked as follows:

1. **Rank 1: Payroll Expense (`ACC_Payroll_Exp`)**
   * **Quantitative Feature:** The joint strain energy (`ik_strain_energy`) is **`41.6848`** at $t=0$ (lowest). This represents high flexibility for adjustment. The absolute adjustment scale is also the largest, making it the most effective target with minimal friction.
2. **Rank 2: Rent Expense (`ACC_Rent_Exp`)**
   * **Quantitative Feature:** The joint strain energy is **`48.7840`** at $t=0$. Although it is a fixed cost, it displays less adjustment distortion than travel expenses.
3. **Rank 3: Travel Expense (`ACC_Travel_Exp`)**
   * **Quantitative Feature:** The joint strain energy is **`48.9643`** at $t=0$ (highest). This indicates a large resistance to reduction. Short-term flat cuts on this node should be avoided.

---

## 6. Alerts & Falsifiability

### 6.1. Triaging Anomalies and Overcoming Model Pollution

* **Rejecting False Positives:** Reject minor Z-Score warnings in July and August as statistical false positives. During those periods, the underlying Kirchhoff physical residual remained `0.00` and the topology remained stable.
* **Confirming Real Anomalies:** Warnings on `Cash` and `UNKNOWN_LEAK` nodes sync with the peak spectral radius of `0.7861` and non-zero conservation residuals (cumulative: `$6,255.99`). We confirm this as a true anomaly (wash trade and embezzlement). Physical indicators successfully bypassed the Z-Score silence caused by model pollution.

### 6.2. Falsification Conditions

To reject the diagnosis of circular trading and systematic embezzlement, the following evidence must be provided:

1. **Delivery Records for Circular Trades:**
   Original shipping bills with tracking numbers and customer inspection receipts proving that physical goods moved between the entities.
2. **Bank Records for Mass Defect:**
   Original bank statements or online banking API logs proving that the cash leak of **`$6,255.99`** was a regular payment to corporate accounts. In particular, the following 9 mismatch entries must be verified:
   * **2020-06-04:** `E_001403` (AR decreases by `$130.55` but cash increases by `$0.00`)
   * **2020-07-13:** `E_001725` (AR decreases by `$279.78` but cash increases by `$0.00`)
   * **2020-07-25:** `E_001859` (AR decreases by `$362.39` but cash increases by `$0.00`)
   * **2020-08-07:** `E_002002` (AR decreases by `$861.39` but cash increases by `$509.57`. Difference: `$351.82`)
   * **2020-08-17:** `E_002126` (AR decreases by `$477.53` but cash increases by `$394.49`. Difference: `$83.04`)
   * **2020-08-19:** `E_002154` (AR decreases by `$274.84` but cash increases by `$0.00`)
   * **2020-09-09:** `E_002432` (Cash decreases by `$4,534.35` but AP decreases by `$0.00`)
   * **2020-09-10:** `E_002437` (AR decreases by `$460.76` but cash increases by `$304.22`. Difference: `$156.54`)
   * **2020-09-22:** `E_002575` (AR decreases by `$82.68` but cash increases by `$0.00`)
