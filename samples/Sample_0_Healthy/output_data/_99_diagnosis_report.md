# TLU Meta-Diagnosis Report (Attending Physician's Summary)

**Target Environment:** `samples/Sample_0_Healthy`
**Date Analyzed:** 2026-05-02 10:05:50

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
| Control Theory  | Max Spectral Radius      | 0.0000 | >= 0.9 |
| Thermodynamics  | Relative Free Energy Ratio| 0.8288 | < -0.1 |
| Micro Forensics | Max Local Z-Score        | 0.00 | > 3.0 |

> *Generated automatically by the TLU Meta-Diagnosis Engine.*

<!--
<LLM_DIAGNOSTIC_CONTEXT>
{
  "timestamp": "2026-05-02T10:05:50.387554",
  "environment": "samples/Sample_0_Healthy",
  "physics_metrics": {
    "max_abs_residual": 0.0,
    "mean_gross_activity": 1337387.234230769,
    "relative_leak_ratio": 0.0,
    "max_spectral": 0.0,
    "min_free_energy": 85485.52,
    "min_relative_free_energy": 0.8288111469064383,
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
    "assets": 229102.63999999908,
    "liabilities": 181671.3700000001,
    "equity": 0.0,
    "net_income": 47431.269999999786,
    "total_liab_eq": 229102.6399999999,
    "revenue": 955157.5599999998,
    "expense": 907726.29,
    "is_balanced": true,
    "bs_items": [
      [
        "ACC_Accounts_Payable",
        "Liability",
        74067.95000000007
      ],
      [
        "ACC_Accounts_Receivable",
        "Asset",
        115309.2699999999
      ],
      [
        "ACC_Cash",
        "Asset",
        113793.36999999918
      ],
      [
        "ACC_Inventory",
        "Liability (Short/Overdraft)",
        107603.42000000004
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
        343765.39,
        417833.3400000001,
        74067.95000000007
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
        726054.9200000007,
        113793.36999999918
      ],
      [
        "ACC_Inventory",
        "Asset",
        417833.3400000001,
        525436.7600000001,
        -107603.42000000004
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
