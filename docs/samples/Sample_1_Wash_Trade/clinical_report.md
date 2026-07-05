# Mathematical Diagnostics Report: Sample_1_Wash_Trade

## (Target: Independent Case 1 / Financial Accounting Wash Trade Diagnosis)

---

## 0. Executive Summary

* **Overall Diagnosis (Conclusion First):** HIGH (Severe Convective Obstruction / Circular Wash Trading). A closed self-circulation loop of cash flows has been detected between specific accounts (Cash and Accounts Receivable), indicating fictitious transactions conducted to artificially inflate revenue.
* **Root Cause (Stability Evaluation):** The maximum spectral radius ($\rho$) of the transition probability matrix spikes up to **`0.7488`** during wash-trading months (January, February, May), showing that the accounting flow is locked into an abnormal circular synchronization loop.
* **Overall Constitution (Health State):**
  The system's mass (capital scale) is stable (mean `200000.00`). Free energy, which reflects capacity to absorb shock, is superficially high (mean `3140312.23`) due to the fictitious trades. However, entropy is elevated (mean `1.5791`), and cash balances exhibit abnormal local overheating (mean temperature `245382.12`). Maximum coupling stiffness reaches **`7.33e-09`**, indicating severe structural rigidity ("stiffness lock" or "arteriosclerosis") during trading months.
* **Areas for Improvement and Advice:**
  * **Stagnation (Viscosity) Identification:** Sales Revenue (**`07_ACC_Sales_Revenue`**) shows extreme latency (mean viscosity `56302.40`, peaking at **`101329.39`** in **`2020-12`**), indicating abnormal year-end delays.
  * **Treatment Points & Contraindications:** The optimal point to restore system flexibility is Cost of Goods Sold (**`02_ACC_COGS`** / minimum strain energy `4.34`). Forced adjustment of Rent Expense (**`06_ACC_Rent_Exp`** / maximum strain energy `8.46`) is strictly contraindicated.

---

## 1. Overall Constitution Diagnosis and Judgment

### ① HIGH: Topological Circulation Failure (Circular Wash Trading Loop)

Static cumulative metrics (cumulative sales of `$1,094,143.89`, net profit of `$201,321.16`) appear healthy. However, step-wise analysis reveals abnormal transaction spikes in January ($t=0$), February ($t=1$), and May ($t=4$) between Cash and Accounts Receivable. This indicates structured circular trades designed to inflate revenue.

### ② Overall Health and Constitution Evaluation (Mathematical Bridge)

* **Physique & Weight (Mass `state_X`):** Mean `200000.00`, Max `1000000.00`.
  * *Mathematical Interpretation:* Stock volumes are inflated by wash trades and do not represent genuine business scale.
* **Immunity & Basic Stamina (Free Energy `free_energy_F`):** Mean `3140312.23`.
  * *Mathematical Interpretation:* The cumulative free energy is artificially boosted by circular transactions; real shock-absorbing capacity is depleted.
* **Autonomic Nervous System & Metabolic Efficiency (Entropy `entropy_S`):** Mean `1.5791`.
  * *Mathematical Interpretation:* Circular flows induce administrative overhead, causing abnormal entropy spikes.
* **Body Temperature (Temperature `temperature_T`):** Mean `245382.12`.
  * *Mathematical Interpretation:* Local accounts show severe inflation (overheating) during circular trade phases.
* **Arteriosclerosis (Coupling Stiffness `stiffness_k`):** Max `7.33e-09`.
  * *Mathematical Interpretation:* PCA PC1 explainability spikes during wash-trading months, locking Cash and Accounts Receivable into rigid synchronization.
* **Stiff Shoulder (Viscosity `viscosity_C`):** Sales Revenue (`07_ACC_Sales_Revenue`) exhibits high viscosity (mean `56302.40`), indicating chronic settlement friction.

---

## 2. Physical and Mathematical Detailed Analysis

### ① 3D Dynamics Descriptive Statistics (Kinematics)

The descriptive statistics of the convective data (state `state_X`, velocity `velocity_v`, acceleration `acceleration_a`, local viscosity `viscosity_C`) are shown below. The data source is [result.000_1_1_filter_dynamics.analysis.csv](../../../samples/Sample_1_Wash_Trade/output_data/result.000_1_1_filter_dynamics.analysis.csv).

| Metric (Scale) | Mean | Median | Mode: Value (Freq/Total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **State state_X** | 200000.0000 | 168745.8450 | 1000000.0000 (12/120, 10.0%) | -1094143.8900 | 1000000.0000 | 2094143.8900 | 451631.9050 | 413401.7651 | -0.1691 | 0.8123 |
| **Velocity velocity_v** | 0.0000 | 14859.1200 | 0.0000 (12/120, 10.0%) | -160439.4800 | 148590.1200 | 309029.6000 | 42876.3200 | 52123.8761 | -0.6512 | 1.8109 |
| **Acceleration acceleration_a** | 0.0000 | 0.0000 | 0.0000 (19/120, 15.8%) | -92138.4500 | 89123.1200 | 181261.5700 | 14321.0900 | 31209.4312 | -0.2109 | 2.5612 |
| **Local Viscosity viscosity_C** | 32952.9912 | 18120.4500 | 100000.0000 (12/120, 10.0%) | 789.1200 | 100000.0000 | 99210.8800 | 42310.4500 | 31890.3200 | 1.0112 | 0.0891 |

* **Statistical Interpretation:**
  Due to circular transactions, the standard deviation of `velocity_v` is elevated to `52123.88` (compared to Sample 0's `38733.67`), indicating that fictitious flows are shaking the system dynamically.

---

## 3. Thermodynamic and Topological Analysis

### ① Macro Thermodynamic Analysis (Energy Stack & T-S Diagram: Reverse Carnot Cycle)

![Thermodynamics Energy Stack](../../../samples/Sample_1_Wash_Trade/readme_plots/001_1_2__thermodynamics_energy_stack.png)

![T-S Diagram](../../../samples/Sample_1_Wash_Trade/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

* **Reverse Carnot Cycle & Entropy Dispersion:**
  In wash-trading months, circular flows drive up the system temperature ($T$), expanding entropy losses ($TS$) and depressing the net free energy ($F = U - TS$). The counter-clockwise, closed egg-shaped loop in the T-S diagram represents a "reverse Carnot cycle" where energy is wasted on friction without performing external work.

### ② 3D Local Thermodynamics (Entropy, Temperature, Internal Energy)

![3D Local Entropy](../../../samples/Sample_1_Wash_Trade/readme_plots/001_1_2_1__3d_local_entropy.png)

![3D Local Temperature](../../../samples/Sample_1_Wash_Trade/readme_plots/001_1_2_2__3d_local_temperature.png)

![3D Local Internal Energy](../../../samples/Sample_1_Wash_Trade/readme_plots/001_1_2_7__3d_local_internal_energy.png)

### ③ Network Topology Evolution (Temporal Sequence)

* **t=0 (2020-01: Commencement of circular loop)**:
  ![Topology t0](../../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00000.png)
* **2020-04 (t=3: Normal flow dispersion)**:
  ![Topology t3](../../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00003.png)
* **2020-05 (t=4: Re-linking and hardening of loop)**:
  ![Topology t4](../../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00004.png)
* **2020-12 (t=11: Return to default state)**:
  ![Topology t11](../../../samples/Sample_1_Wash_Trade/readme_plots/002_1_2__network_topology.t.00011.png)

### ④ Information Geometry & 3D Micro KL Drift

![Macro Forensics](../../../samples/Sample_1_Wash_Trade/readme_plots/002_2_1__macro_forensics_dashboard.png)

![3D Micro KL Drift](../../../samples/Sample_1_Wash_Trade/readme_plots/002_2_2_1__3d_micro_kl_drift.png)

---

## 4. Geometric and Structural Analysis

### ① Coupling Stiffness PCA & Eigenvector Evolution

![PCA Ratio](../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_2__principal_axes_ratio.png)

![PCA PC1 Evolution](../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_3__eigenvector_evolution.png)

* **PC1 Eigenvector Concentration:**
  During wash trading, the PC1 explanation ratio peaks at **`95.28%`** ($t=4$), indicating that the entire network variance is captured by the circular flow. The PC1 eigenvector weights concentrate on `01_ACC_Accounts_Receivable` (`-0.7162`) and `03_ACC_Cash` (`0.3524`), mathematically proving the stiffness lock between Cash and Accounts Receivable.

---

## 5. Audit and Anomaly Verification

### ① Conservation Residual Limits

* The mean, min, max, and range are all **0.0000**. Because the ledger balances perfectly, traditional static audit tools (which check B/S balance) cannot detect this fraud. It is only exposed through spectral stability analysis ($\rho \ge 0.75$).

### ② Verification of Specific Fraudulent Entries (Audit Trail)

Granular inspection of `Dummy_Journal_Stream.csv` isolates the circular transactions:

1. **2020-01-03 (t=0):** Amount **`$40,433.60`** (Journal IDs: `E_000020` to `E_000022` / round-trip between Cash and Accounts Receivable)
2. **2020-02-01 (t=1):** Amount **`$53,282.77`** (Journal IDs: `E_000257` to `E_000259`)
3. **2020-05-22 (t=4):** Amount **`$44,939.48`** (Journal IDs: `E_001327` to `E_001329`)

* **Total Wash Trade Volume:** **`$138,655.85`**

### ③ Model Contamination (Boiling Frog Effect)

In the 3D Micro KL Drift plot, the first (January) and second (February) wash trades trigger massive coordinate spikes. However, the third (May) trade triggers a much smaller spike, despite having a similar transaction volume. This occurs because the statistical model adapted to the earlier wash trades, integrating them into its normal baseline (**Model Contamination / Boiling Frog Effect**). Combining physical topology metrics ($\rho = 0.7488$) prevents this blind spot, ensuring continuous detection.

---

## 6. Control Stability & Intervention Analysis

### ① Maximum Spectral Radius (Stability)

![System Stability](../../../samples/Sample_1_Wash_Trade/readme_plots/004_1_2__system_stability.png)

### ② LQR Control & Intervention Sensitivity

![LQR Control Space](../../../samples/Sample_1_Wash_Trade/readme_plots/004_1_3__control_lqr_performance_space.png)

### ③ Sensitivity Matrix

![Sensitivity Matrix](../../../samples/Sample_1_Wash_Trade/readme_plots/004_2_1__sensitivity_matrix.png)

---

## 7. Diagnostics: Viscosity & Treatment Points

### ① Stagnation (Viscosity) Analysis & Peak Identification

Nodes exceeding the Q3 threshold (**`44861.6956`**) are listed below. Source: [result.000_1_1_filter_dynamics.analysis.csv](../../../samples/Sample_1_Wash_Trade/output_data/result.000_1_1_filter_dynamics.analysis.csv).

* **`07_ACC_Sales_Revenue`**:
  * Mean Viscosity: **`56302.3970`**
  * Peak Period: **`2020-12`** (Peak Value: **`101329.3915`**)
  * *Mathematical Interpretation:* The local viscosity trend heatmap ([000_1_7_1__viscosity_trend.png](../../../samples/Sample_1_Wash_Trade/readme_plots/000_1_7_1__viscosity_trend.png)) clearly illustrates the extreme viscosity peak on Sales Revenue at the year-end step.
* **`04_ACC_Inventory`**:
  * Mean Viscosity: **`52231.0350`**
  * Peak Period: **`2020-12`** (Peak Value: **`56957.7977`**)
* **`03_ACC_Cash`**:
  * Mean Viscosity: **`44861.6956`**
  * Peak Period: **`2020-01`** (Peak Value: **`46831.8290`**)

### ② Treatment Points ("Tsubo") & Contraindications

#### 🎯 Treatment Points (Strain Energy $\le$ Q1)

1. **`03_ACC_Cash`** (Mean Strain Energy: **`2.1413`**)
2. **`01_ACC_Accounts_Receivable`** (Mean Strain Energy: **`2.2150`**)
3. **`02_ACC_COGS`** (Mean Strain Energy: **`4.3436`**)

#### 🚫 Contraindications (Strain Energy $\ge$ Q3)

1. **`07_ACC_Sales_Revenue`** (Mean Strain Energy: **`8.7863`**)
2. **`06_ACC_Rent_Exp`** (Mean Strain Energy: **`8.4552`**)
3. **`09_ACC_Equity_Capital`** (Mean Strain Energy: **`8.3317`**)

---





#### Jing-Well (Boundary) Node Externalities & Symbiotic Control Points (Chapter 10 Application)
When prescribing interventions for boundary terminal nodes (Jing-Well points) interfacing with the external environment, such as `01_ACC_Accounts_Receivable` or `05_ACC_Accounts_Payable`, local optimization relying purely on internal liquidity enhancement is strictly prohibited. Forcing a rapid collection of Accounts Receivable (sedation/泻) squeezes the cash flow of clients (External Backlash), which loops back as negative feedback (customer churn and drop in sales revenue) to the primary entity. Therefore, any intervention at these Jing-Well nodes must be paired with symbiotic actions (Yin-Yang balancing), such as relaxing COGS/AP payment windows or offering shared digital invoice infrastructure to buffer the external friction, achieving a sustainable homeostasis across the system boundary.

## 8. Falsifiability & Limits

To falsify the circular wash trade diagnosis, the following external physical evidence must be presented:

1. **Physical Delivery Proof of Goods:**
   For the specific transaction dates and amounts (totaling `$138,655.85`), the presentation of original shipping waybills, courier receipts, or signed delivery logs proving that physical goods were actually moved.
2. **Legal Independence of Counterparts:**
   The presentation of share registers and corporate registration papers proving that the trading counterparties are completely independent third parties.
