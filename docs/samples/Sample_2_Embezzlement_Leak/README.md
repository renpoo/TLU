# 🔬 Clinical Meta-Diagnostic Forensic Report: Mass Deficit & Fraudulent Embezzlement due to Fund Outflow (Sample 2)

## 1. Executive Summary

* **Overall Diagnosis:** **Violation of Mass Conservation Law (Off-Book Fund Outflow / Mass Conservation Violation)**
* **Severity:** 🔴 **CRITICAL (Extremely Serious Internal Leakage)**
* **Clinical Overview:**
    This system suffers from "mass deficit (embezzlement / off-book fund outflow)" where unexplained funds continuously leak from the double-entry bookkeeping system, which should behave as a closed-network system.

    Throughout the simulation period, **a cumulative total of `$1,353.48`** of mass disappeared from the system, siphoned into unknown regions. Although this leakage is relatively minor (representing about 0.05% of the total activity, a micro-leakage), it is physically and mathematically proven that this "small wound" degrades the tension of double-entry balance, ultimately driving the entire system into "absolute rigidity (Rigid Lock / cash shortage)" and "catastrophic resonance (knocking)" in the later steps.

    Traditional statistical Z-scores suffered from a critical blind spot (false negative), classifying the system as "normal (healthy)" because they failed to capture the outflow to a previously unrecorded route. However, the **`System Conservation Residual`** computed by the Physics-Mathematics Engine established ironclad forensic proof by showing discrepancies reaching a maximum of `364.53` (August 2020).

---

## 2. Limitations of Traditional Audits

It is impossible to detect this clever "off-book fund outflow" early through traditional financial audits or financial statement analysis (monitoring static aggregated data). Below are the B/S and P/L configuration and trend charts at the final step:

* **B/S Assets/Capital Trends:**
    ![B/S Trend](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_0_1__BS_Trend.png)
    ![B/S Block Total](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_0_1__BS_Block_Total.png)
* **P/L Revenue/Expenses Trends:**
    ![P/L Trend](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_0_1__PL_Trend.png)
    ![P/L Waterfall Total](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_0_1__PL_Waterfall_Total.png)

**【Blind Spots of Static Audits】**
In practice, when such unexplained differences occur, accountants may temporarily dump the difference into a dummy account (like `UNKNOWN_LEAK`) representing "suspense payments" or "miscellaneous losses" to force the B/S to balance at "Total Assets `$1,320,721.40`" to close the books.

Consequently, this leak is camouflaged as an **operating profit** on the P/L. Monitoring only static ratios fails to visually highlight the fact that a fatal "hole (leakage)" has opened and that the company's blood (capital) is draining away.

---

## 3. Fundamental Pathophysiology

The mechanism of the fraudulent leakage injected into this sample is as follows:

* **Execution of Fraud (timesteps 2020-02, 03, 08, 09, 11)**:
  * Accounts receivable (`ACC_Accounts_Receivable`) is decreased (credited), indicating that it was collected from customers.
  * However, the collected cash is bypassed (embezzled) to an off-book personal account instead of being deposited into cash and deposits (`ACC_Cash`) (e.g., the debit side is recorded as $0.0).

The Physics-Mathematics Engine corrects for this "disappearing mass" mathematically to maintain a dynamic closed system, constructing a virtual garbage-bin node **`UNKNOWN_LEAK`** in memory and routing the lost mass there. Below we prove how this causes dynamic anomalies.

---

## 4. Mathematical Evidence from the Physics & Math Engine

### 4.1. Breakdown of Conservation & Kirchhoff Physical Residual

The overall system's spatiotemporal mass conservation discrepancy, **`System Conservation Residual`**, recorded sharp spikes in the months when leakage occurred: `307.30` in 2020-02, `359.73` in 2020-03, a maximum of `364.53` in 2020-08, `260.74` in 2020-09, and `61.18` in 2020-11. This is a decisive physical signature of debit-credit imbalance (disappearing cash via one-sided entries).

* **Macro Forensics Dashboard:**
    ![Macro Forensics](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_1__macro_forensics_dashboard.png)

Looking at the time-series sequence of the Stiffness Matrix, from 2020-02 (`t_idx=1`) onward (when the leak began), the normal "mosaic pattern" of connection flexibility is lost, and specific hubs dye deep red, triggering **Rigid Lock (absolute rigidity / halted liquidity due to cash shortages)**.

A system that has lost its elasticity cannot damp the input energy (excitation) of normal transactions, causing a **catastrophic resonance (knocking / systemic runaway) reaching the 1 billion (1e9) scale** on the late-stage 3D maps. This proves that a mere 0.05% cash leak can shake and destroy the entire system structure.

* **3D Dynamic External Force Resonance Map:**
    ![External Force 3D](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_6__3d_dynamics_external_force.png)

* **Stiffness Matrix 5-Point Cinematic Sequence:**
  * **① Start (t=0 / 2020-01):**
        ![Stiffness t0](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00000.png)
        Initial state. Nodes are flexibly coupled, displaying a healthy stiffness distribution.
  * **② Just Before Change (t=1 / 2020-02):**
        ![Stiffness t1](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00001.png)
        The moment the first mass deficit (fund outflow) occurs. The appearance of `UNKNOWN_LEAK` begins to distort the stiffness distribution.
  * **③ The Exact Point of Change (t=2 / 2020-03):**
        ![Stiffness t2](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00002.png)
        The point where leakage continues (embezzled amount of `359.73`). The surrounding stiffness of `ACC_Cash` and `ACC_Accounts_Receivable` shows abnormal solidification (red lock cells), marking a prominent stiffness lock.
  * **④ Immediately After Change (t=3 / 2020-04):**
        ![Stiffness t3](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00003.png)
        Immediately after the leakage temporarily stops. However, the damage from the lost mass (cash) is not recovered, and rigidity propagates throughout the network.
  * **⑤ End (t=11 / 2020-12):**
        ![Stiffness t11](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_1__structural_stiffness.t.00011.png)
        Final observation point. Due to the unrecovered mass deficit, the entire network remains in a state of "chronic rigidity."

In the PCA analysis, the PC0 eigenvalue in 2020-03 (`t_idx=2`) reaches `6.6203e9`, and the explained variance ratio is **`100.0%`**. The PC1 loadings are dominated by `ACC_Accounts_Receivable` (`0.6221`) and `ACC_Cash` (`-0.5138`). This shows that the shock of the leak has occupied the primary principal component axis, creating extreme bias in the system.

* **PCA Principal Axes Ratio:**
    ![PCA Ratio](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_2_2__principal_axes_ratio.png)

### 4.2. Topological Transformation & Recirculation Stability

On the network topology map, an edge representing off-book leakage is visualized going from `ACC_Cash` (Cash) toward `UNKNOWN_LEAK` (the unknown leakage destination).

* **System Stability Index (Spectral Radius):**
    ![System Stability](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/004_1_2__system_stability.png)

* **Network Topology 5-Point Sequence:**
  * **① Start (t=0 / 2020-01):**
        ![Topology t0](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00000.png)
        Healthy topology. The `UNKNOWN_LEAK` node has not yet appeared.
  * **② Just Before Change (t=1 / 2020-02):**
        ![Topology t1](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00001.png)
        The first leakage occurs, connecting the `UNKNOWN_LEAK` node to the topological space, and funds begin to drain.
  * **③ The Exact Point of Change (t=2 / 2020-03):**
        ![Topology t2](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00002.png)
        The leakage vector toward `UNKNOWN_LEAK` becomes double-thick, and the conservation discrepancy breaks the topological shape.
  * **④ Immediately After Change (t=3 / 2020-04):**
        ![Topology t3](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00003.png)
        The phase where the leak temporarily stops. However, `UNKNOWN_LEAK` remains connected, and structural distortion from mass shortage persists.
  * **⑤ End (t=11 / 2020-12):**
        ![Topology t11](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_1_2__network_topology.t.00011.png)
        Final state. Even at the end of the simulation, the drain (leakage pipe) outside the system boundary remains chronic.

### 4.3. Thermodynamic Dissipation Energy & Open Trajectories

With the off-book leakage of cash, the system's internal energy $U$ (gross metabolism) and free energy $F$ (business effective resources) are shaved away.

* **Thermodynamics Energy Stack:**
    ![Thermodynamics Energy Stack](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_2__thermodynamics_energy_stack.png)
* **T-S Diagram:**
    ![T-S Diagram](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

1. **Energy Stack Behavior:**
    In months where mass deficit occurs (2020-02, 03, 08, 09, 11), the rise of free energy $F$ (solid white line) is significantly suppressed compared to the healthy growth model (Sample 0). This indicates that no matter how high the revenue appears on paper, deep energy resources are leaking out, meaning the "stamina (equity reserves)" required to maintain the system is essentially withered.
2. **T-S Trajectory (Proof of an Open Dissipative Trajectory):**
    While wash trading (Sample 1) draws a closed loop, the T-S diagram of this sample draws an **"open trajectory to the right that never returns (dissipative curve)"**. This is objective proof that energy is not recirculating but is unilaterally discharged outside the system boundary, causing a permanent loss of the system's lifeline.

### 4.4. Unified Approach via 3D Ribbon / Surface Plots

The 3D plots visualize spatiotemporal variations and the local thermodynamic impact of the "zero-to-one" anomaly missed by statistical AI models.

* **① 3D Local Thermodynamics Plots:**
    ![3D Local Entropy](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_2_1__3d_local_entropy.png)
    ![3D Local Temperature](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/001_1_2_2__3d_local_temperature.png)
  * **Local Entropy ($s_i$):** Indicates spatial path dispersion. During months with fund outflows (embezzlement), an abnormal drainage channel opens from `ACC_Accounts_Receivable` to `UNKNOWN_LEAK` (or `ACC_Cash` to `UNKNOWN_LEAK`), causing a temporary bump in the spatial flow dispersion (entropy) of `ACC_Cash` and surrounding nodes.
  * **Local Temperature ($T_i$):** Indicates temporal balance volatility (standard deviation). During months when cash is unilaterally siphoned and lost (Feb, Mar, Aug, Sep, Nov), the balances of `ACC_Cash`, `ACC_Accounts_Receivable`, and `UNKNOWN_LEAK` fluctuate wildly, proving that thermal loss (friction) is localized and generated at these nodes.
* **② 3D Micro Information Geometry Plot:**
    ![3D Micro KL Drift](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_2_1__3d_micro_kl_drift.png)
    ![3D Micro Z-Score](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/002_2_2_2__3d_micro_z_score_X.png)

    In the spatiotemporal information geometry plot (3D Micro KL Drift), a **"giant spire (wall of KL Drift spikes) piercing the sky"** appears on the node space of `ACC_Cash` and `ACC_Accounts_Receivable` during the first leakage steps in 2020-02 to 03. This provides paramount evidence that directly points out "which node and what month the leak occurred" during forensic audits, even when statistical anomaly detection (Z-scores) remains silent (evaluating it as normal) due to new, previously unrecorded connections (division-by-zero).

---

## 5. LQR Control Treatment

* **Treatment Plan:** **Immediate Hemostasis of the Outflow & Blockage of the Flow Path**
* **LQR Sensitivity Intervention (Acupoint Identification):**
    In the flow control sensitivity analysis (Sensitivity Matrix) calculated by LQR, the node with the maximum intervention effect (improvement sensitivity) is identified as the `ACC_Accounts_Receivable` (Accounts Receivable) node.
    ![LQR Control](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/004_1_3__control_lqr_performance_space.png)
* **Practical Treatment Plan:**
    1. **Implementation of Hemostasis (Mass Block):**
       Force-configure the accounting software at the schema definition level to "reject entries / trigger validation errors" for unbalanced entries (one-sided entries) where accounts receivable decreases (credit) but cash (debit cash) does not increase.
    2. **Physical Freezing of the Hub Account:**
       Identify the specific transaction IDs (e.g., `E_000213`) forming the bypass to `UNKNOWN_LEAK`, and force-freeze the operator account and approval process that executed those entries. This physically closes the "wound" of the leak.

---

## 6. 🚨 Forensic Alert & Falsification Analytics

### 6.1. False Negative Assessment

* **Observation:** During the mass deficit phase in 2020-02 to 03, the Z-Score (probabilistic statistics of liquidity change) did not exceed the threshold of `3.0`, failing to trigger an alert (false negative).
* **Physical Judgment:**
    This is a false negative of the statistical model due to its "zero-to-one blind spot." Because connections with `UNKNOWN_LEAK` were never defined in the past transaction history, the learned covariance matrix could not correctly evaluate the probabilistic anomaly of the new connection, letting the alert slide.
    During triage, we reject the normal judgment of the statistical model and prioritize the "non-zero spikes in the Kirchhoff conservation residual (max `364.53`)" as the absolute truth, confirming the diagnosis of a major hemorrhage pathology.

### 6.2. Falsifiability

To prove that this system represents "legitimate transactions" and "not embezzlement/outflow," the auditor must be presented with the following **"original documents or third-party evidence from outside the database"**:

1. **Original Bank Passbook / API Invoices:**
    Original bank statement passbooks (paper) or online banking API raw logs (uneditable transmission records) showing that the target amounts (representing the `$1,353.48` cumulative loss) were actually deposited into the legal bank accounts of the corporate entity on the dates the mass deficit was detected (2020-02, 03, 08, 09, 11).
2. **Presentation of Immediate Reconciliation Entries:**
    Reconciliation agreements and account certificates showing that the balances determined as lost between the systems were actually remitted to other legitimate nodes (such as affiliates) as "funds in transit" by the next step, and that offset write-offs were completed.
