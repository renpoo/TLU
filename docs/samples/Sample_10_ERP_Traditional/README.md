# Sample 10: ERP Traditional Cost Allocation

## Overview
This sample environment models the classical **"Direct Labor Hours Allocation"** commonly used in enterprise ERP systems.
Total factory overhead is allocated to products in direct proportion to their labor hours, ignoring differences in actual activity effort (such as setups and inspections).

---

## Physical & Mathematical Signatures
* **Fixed Allocation Distortion & Over-concentration**:
  Mass-produced Product A (`DPT_Prod_A`) absorbs **89.0%** of total overhead due to long labor hours, while specialty Product B (`DPT_Prod_B`) receives only **11.0%**, under-costing Product B.
* **PCA Eigenvector Locking**:
  The principal component (PC1) eigenvector loadings are locked with a correlation > 0.95 to `ACC_Direct_Labor_Exp`.
* **Reduced Thermodynamic Entropy ($S = 2.6568$)**:
  Constrained by a single linear rule, the system's degree of freedom (entropy) drops, exhibiting structural stiffness (Thrombosis).

---

## Eastern Medicine Diagnosis
* **Pathology:** **Congestion & Blood Stasis (気滞・血瘀)**
* **Interpretation:** Excessive cost burden is concentrated in Product A's meridian, leaving Product B in a false state of low cost (hidden deficit).

---

## Acupuncture Points & Interventions
* 🎯 **Tsubo:** `ACC_COGS_DPT_Prod_A` ── Releasing the unfair cost burden on Product A.
* 🤝 **Symbiotic Intervention:** Correct the allocation algorithm itself rather than pressuring Product A's shop-floor workers.
