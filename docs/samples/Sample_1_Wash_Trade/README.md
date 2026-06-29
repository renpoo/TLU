# Wash Trade Report (Case 1)

> [!NOTE]
> A more detailed analysis report is available in [clinical_report.md](clinical_report.md).

## Target Entity: Sample 1

---

## 0. Executive Summary

* **Overall Diagnosis:** 【Warning / Needs Improvement】 Fictitious capital circulation (**"circular wash trading"**) has been detected between specific accounts (Cash and Accounts Receivable), artificially inflating sales revenue.
* **Overall Constitution (Physical State):** 
  The organization appears to have a large **"physique"** (stock volume) and healthy **"immunity and basic stamina"** (cumulative profit on P/L). However, this is merely a **"fever"** (artificial temperature rise) caused by non-substantial circulation, and the actual cash recovery capability is depleted. Frictional loss in circulation has disrupted the system's balance (**"autonomic nervous system"**), and the settlement routes are completely locked during wash-trading months, resulting in structural rigidity (**"arteriosclerosis / stiffness lock"**).
* **Areas for Improvement (Viscosity & Treatment Points):**
  - **Stagnation (Viscosity / "Stiff Shoulder") Range:** Severe settlement lags are observed in **"07_ACC_Sales_Revenue"**, **"04_ACC_Inventory"**, and **"03_ACC_Cash"** (top 25% viscosity range), with a peak of year-end stagnation around **2020-12**.
  - **Treatment Points ("Tsubo") Range:** The minimum intervention stress range (bottom 25% strain energy range), comprising **"03_ACC_Cash"**, **"01_ACC_Accounts_Receivable"**, and **"02_ACC_COGS"**, represents the highest priority treatment points to restore the system.
  - **Contraindications (Avoid Intervention) Range:** Conversely, aggressive reductions or interventions in **"07_ACC_Sales_Revenue"**, **"06_ACC_Rent_Exp"**, and **"09_ACC_Equity_Capital"** (top 25% strain energy range) must be strictly avoided, as they will trigger intense system backlash and functional paralysis.

---

## 1. Overall Diagnosis (Warning / Needs Improvement)

### 【Diagnosis】: Needs Improvement (Prevalence of Circular Wash Trading)
![System Stability](../../../samples/Sample_1_Wash_Trade/readme_plots/004_1_2__system_stability.png)

At first glance, the organization appears to maintain profitable operations. However, analyzing dynamic stability (maximum spectral radius $\rho$) over time reveals that during wash-trading months (January, February, and May), stability metrics surge near the warning threshold (`0.75`), peaking at **`0.7488`**. This is caused by a closed circular loop where Cash and Accounts Receivable are bounced back and forth while balancing the books. This non-substantial trading damages cash flow and increases bankruptcy risk. Immediate termination of these circular trades is required.

---

## 2. Overall Constitution (Health State) Analysis

Mapping the organization's "financial stamina" to a medical checkup template reveals the following structural distortions:

### ① Physique & Weight (Cumulative Trend of Capital Scale)
![B/S Cumulative Trend](../../../samples/Sample_1_Wash_Trade/readme_plots/000_0_1__BS_Trend.png)

Due to the circular bounce between Cash and Accounts Receivable, the Balance Sheet (B/S) asset scale is artificially inflated and does not reflect actual operational size.

### ② Immunity & Basic Stamina (Resilience to External Shocks)
![P/L Cumulative Trend](../../../samples/Sample_1_Wash_Trade/readme_plots/000_0_1__PL_Trend.png)

Although the Profit and Loss Statement (P/L) reports cumulative sales of `$1,094,143.89` and a net profit of `$201,321.16`, this basic stamina is merely a "fever" inflated by wash trades. There is no real buffer to absorb external economic shocks.

### ③ Autonomic Nervous System & Metabolic Efficiency (Regularity of Frictional Loss)
![T-S Diagram](../../../samples/Sample_1_Wash_Trade/readme_plots/001_1_3__thermodynamics_ts_diagram.png)

In the T-S diagram mapping volatility ($T$) to frictional entropy ($S$), the system exhibits extreme overheating (thermal stress) and entropy surges during wash-trading months. The diagram plots a counter-clockwise, closed egg-shaped loop (representing a "reverse Carnot idle cycle"), proving that energy is wasted on internal friction without producing external work.

### ④ Arteriosclerosis (PCA Principal Axes Evaluation)
![PCA Ratio](../../../samples/Sample_1_Wash_Trade/readme_plots/000_2_2__principal_axes_ratio.png)

Principal Component Analysis (PCA) of the coupling stiffness matrix reveals that during wash-trading periods, the dominant axes between Cash and Accounts Receivable become completely frozen. The first principal component (PC1) explainability ratio spikes, demonstrating a "stiffness lock" (structural hardening) equivalent to rigid arteries.

---

## 3. Key Areas for Improvement (Viscosity & Treatment Points)

Specific areas for improvement identified by the system and recommended action plans are detailed below:

### ⚠️ Stagnation (Viscosity) Identification (Local Viscosity Temporal Heatmap Analysis)
![Local Viscosity Trend](../../../samples/Sample_1_Wash_Trade/readme_plots/000_1_7_1__viscosity_trend.png)

* **Stagnation Range:** 
  The temporal heatmap mapping log local viscosity ($viscosity\_C$) shows that the sales revenue node (**`07_ACC_Sales_Revenue`**) maintains high frictional resistance throughout, peaking sharply in December.
  This viscosity surge (damping/delay) causes state trajectories to lock into localized regions of phase space (attractor confinement). Refer to the 3D Phase Portrait ([000_1_8__phase_portrait_3d.png](../../../samples/Sample_1_Wash_Trade/readme_plots/000_1_8__phase_portrait_3d.png)) for trajectory clustering.
  The top 25% viscosity group—**"07_ACC_Sales_Revenue"**, **"04_ACC_Inventory"**, and **"03_ACC_Cash"**—contains severe settlement delays.
  - **`07_ACC_Sales_Revenue`**: Mean viscosity `56302.40`, peaking at **`2020-12`** (peak value `101329.39`).
  - **`04_ACC_Inventory`**: Mean viscosity `52112.45`, peaking at **`2020-12`**.
  - **`03_ACC_Cash`**: Mean viscosity `30953.51`, peaking in **`2020-01`**.

### 🎯 Treatment Points ("Tsubo") & Contraindications
![Sensitivity Matrix](../../../samples/Sample_1_Wash_Trade/readme_plots/004_2_1__sensitivity_matrix.png)

* **Treatment Points Range:** Accounts in the bottom 25% of intervention strain energy—**"03_ACC_Cash"**, **"01_ACC_Accounts_Receivable"**, and **"02_ACC_COGS"**—can be adjusted with minimal frictional resistance.
  - **Advice:** These nodes represent the most effective points to restore natural flow and liquidity with the lowest structural backlash.
* **Contraindications Range:** Conversely, the top 25% strain energy group—**"07_ACC_Sales_Revenue"**, **"06_ACC_Rent_Exp"**, and **"09_ACC_Equity_Capital"**—must be avoided.
  - **Advice:** Forcing adjustments on these nodes will disrupt core connections and trigger massive system backlash.

---

## 4. Diagnostic Limitations and Falsifiability

To overturn (falsify) the diagnosis of "Circular Wash Trading," the following external, primary physical evidence must be presented:

1. **Physical Delivery Proof of Goods:**
   For the specific transaction dates and amounts (totaling `$138,655.85`), the presentation of original shipping waybills, courier receipts, or signed delivery logs proving that physical goods were actually moved.
2. **Legal Independence of Counterparts:**
   The presentation of share registers and corporate registration papers proving that the trading counterparties are completely independent third parties, with no capital, management, or beneficial ownership ties.

---
*Published by: TLU Financial Mathematical Diagnostics Engine (General Reader Edition)*
