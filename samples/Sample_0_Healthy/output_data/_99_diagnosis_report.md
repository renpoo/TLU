# TLU Meta-Diagnosis Report (Attending Physician's Summary)

**Target Environment:** `samples/Sample_0_Healthy`
**Date Analyzed:** 2026-05-03 10:44:51

## 1. Final Diagnosis

### 🟢 Healthy System (No Structural Pathologies Detected)
- **Severity:** NORMAL
- **Evidence:** All physical parameters remained within stable thresholds.
- **Interpretation:** The system is functioning efficiently without any detectable structural anomalies, leaks, or loops.

---
## 2. Scale-Invariant Diagnostic Metrics

| Physical Domain | Extracted Metric | Value | Threshold |
|-----------------|------------------|-------|-----------|
| Macro Forensics | Relative Mass Leak Ratio | 0.0000 | > 1e-06 |
| Control Theory  | Max Spectral Radius      | 0.0000 | >= 0.6 |
| Thermodynamics  | Relative Free Energy Ratio| 0.4061 | < -0.1 |
| Micro Forensics | Max Local Z-Score        | 0.00 | > 3.0 |

> *Generated automatically by the TLU Meta-Diagnosis Engine.*

<!--
<LLM_DIAGNOSTIC_CONTEXT>
{
  "timestamp": "2026-05-03T10:44:51.943812",
  "environment": "samples/Sample_0_Healthy",
  "physics_metrics": {
    "max_abs_residual": 0.0,
    "mean_gross_activity": 1302063.825769231,
    "relative_leak_ratio": 0.0,
    "max_spectral": 0.0,
    "min_free_energy": 93251.36,
    "min_relative_free_energy": 0.406125999313399,
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
    "assets": 216622.47999999998,
    "liabilities": 169191.21000000084,
    "equity": 0.0,
    "net_income": 47431.269999999786,
    "total_liab_eq": 216622.48000000062,
    "revenue": 955157.5599999998,
    "expense": 907726.29,
    "is_balanced": true,
    "bs_items": [
      [
        "ACC_Accounts_Payable",
        "Liability",
        111101.96000000014
      ],
      [
        "ACC_Accounts_Receivable",
        "Asset",
        115309.2699999999
      ],
      [
        "ACC_Cash",
        "Liability (Short/Overdraft)",
        58089.2500000007
      ],
      [
        "ACC_Inventory",
        "Asset",
        101313.21000000008
      ]
    ],
    "pl_items": [
      [
        "ACC_COGS",
        "Expense",
        525436.7600000001
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
        955157.5599999998
      ],
      [
        "ACC_Travel_Exp",
        "Expense",
        99308.44999999998
      ]
    ],
    "tb_items": [
      [
        "ACC_Accounts_Payable",
        "Liability",
        515648.01000000007,
        626749.9700000002,
        111101.96000000014
      ],
      [
        "ACC_Accounts_Receivable",
        "Asset",
        955157.5599999998,
        839848.2899999999,
        115309.2699999999
      ],
      [
        "ACC_COGS",
        "Expense",
        525436.7600000001,
        0.0,
        525436.7600000001
      ],
      [
        "ACC_Cash",
        "Asset",
        839848.2899999999,
        897937.5400000006,
        -58089.2500000007
      ],
      [
        "ACC_Inventory",
        "Asset",
        626749.9700000002,
        525436.7600000001,
        101313.21000000008
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
        955157.5599999998,
        955157.5599999998
      ],
      [
        "ACC_Travel_Exp",
        "Expense",
        99308.44999999998,
        0.0,
        99308.44999999998
      ]
    ]
  }
}
</LLM_DIAGNOSTIC_CONTEXT>
-->
