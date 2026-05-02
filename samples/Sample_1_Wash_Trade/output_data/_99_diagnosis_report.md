# TLU Meta-Diagnosis Report (Attending Physician's Summary)

**Target Environment:** `samples/Sample_1_Wash_Trade`
**Date Analyzed:** 2026-05-02 10:06:15

## 1. Final Diagnosis

### 🟢 Healthy System (No Structural Pathologies Detected)
- **Severity:** NORMAL
- **Evidence:** All physical parameters remained within stable thresholds.
- **Interpretation:** The system is functioning efficiently without any detectable structural anomalies, leaks, or loops.

---
## 2. Scale-Invariant Diagnostic Metrics

| Physical Domain | Extracted Metric | Value | Threshold |
|-----------------|------------------|-------|-----------|
| Macro Forensics | Relative Mass Leak Ratio | 0.0000 | > 0.001 |
| Control Theory  | Max Spectral Radius      | 0.6857 | >= 0.9 |
| Thermodynamics  | Relative Free Energy Ratio| 0.8473 | < -0.1 |
| Micro Forensics | Max Local Z-Score        | 0.00 | > 3.0 |

> *Generated automatically by the TLU Meta-Diagnosis Engine.*

<!--
<LLM_DIAGNOSTIC_CONTEXT>
{
  "timestamp": "2026-05-02T10:06:15.220940",
  "environment": "samples/Sample_1_Wash_Trade",
  "physics_metrics": {
    "max_abs_residual": 0.0,
    "mean_gross_activity": 1356904.6784615382,
    "relative_leak_ratio": 0.0,
    "max_spectral": 0.685715,
    "min_free_energy": 85485.52,
    "min_relative_free_energy": 0.8472663000534815,
    "max_z_score": 0.0,
    "max_leak_location": "Time: 2020-W01"
  },
  "detected_pathologies": [
    {
      "pathology": "Healthy System (No Structural Pathologies Detected)",
      "severity": "NORMAL",
      "evidence": "All physical parameters remained within stable thresholds.",
      "interpretation": "The system is functioning efficiently without any detectable structural anomalies, leaks, or loops."
    }
  ],
  "financial_baseline": {
    "week": "2020-W52",
    "assets": 267085.2799999998,
    "liabilities": 184506.64000000013,
    "equity": 0.0,
    "net_income": 82578.63999999966,
    "total_liab_eq": 267085.2799999998,
    "revenue": 993131.2699999998,
    "expense": 910552.6300000001,
    "is_balanced": true,
    "bs_items": [
      [
        "ACC_Accounts_Payable",
        "Liability",
        67911.02000000008
      ],
      [
        "ACC_Accounts_Receivable",
        "Asset",
        153211.32999999973
      ],
      [
        "ACC_Cash",
        "Asset",
        113873.95000000007
      ],
      [
        "ACC_Inventory",
        "Liability (Short/Overdraft)",
        116595.62000000005
      ]
    ],
    "pl_items": [
      [
        "ACC_COGS",
        "Expense",
        530066.5200000001
      ],
      [
        "ACC_Payroll_Exp",
        "Expense",
        220971.34
      ],
      [
        "ACC_Rent_Exp",
        "Expense",
        62009.74
      ],
      [
        "ACC_Sales_Revenue",
        "Revenue",
        993131.2699999998
      ],
      [
        "ACC_Travel_Exp",
        "Expense",
        97505.03000000001
      ]
    ],
    "tb_items": [
      [
        "ACC_Accounts_Payable",
        "Liability",
        345559.88,
        413470.9000000001,
        67911.02000000008
      ],
      [
        "ACC_Accounts_Receivable",
        "Asset",
        1029521.7999999998,
        876310.4700000001,
        153211.32999999973
      ],
      [
        "ACC_COGS",
        "Expense",
        530066.5200000001,
        0.0,
        530066.5200000001
      ],
      [
        "ACC_Cash",
        "Asset",
        876310.4700000001,
        762436.52,
        113873.95000000007
      ],
      [
        "ACC_Inventory",
        "Asset",
        413470.9000000001,
        530066.5200000001,
        -116595.62000000005
      ],
      [
        "ACC_Payroll_Exp",
        "Expense",
        220971.34,
        0.0,
        220971.34
      ],
      [
        "ACC_Rent_Exp",
        "Expense",
        62009.74,
        0.0,
        62009.74
      ],
      [
        "ACC_Sales_Revenue",
        "Revenue",
        0.0,
        993131.2699999998,
        993131.2699999998
      ],
      [
        "ACC_Travel_Exp",
        "Expense",
        97505.03000000001,
        0.0,
        97505.03000000001
      ]
    ]
  }
}
</LLM_DIAGNOSTIC_CONTEXT>
-->
