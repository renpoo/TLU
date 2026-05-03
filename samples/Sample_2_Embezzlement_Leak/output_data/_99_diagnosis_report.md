# TLU Meta-Diagnosis Report (Attending Physician's Summary)

**Target Environment:** `samples/Sample_2_Embezzlement_Leak`
**Date Analyzed:** 2026-05-03 10:01:01

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
| Thermodynamics  | Relative Free Energy Ratio| 0.5993 | < -0.1 |
| Micro Forensics | Max Local Z-Score        | 0.00 | > 3.0 |

> *Generated automatically by the TLU Meta-Diagnosis Engine.*

<!--
<LLM_DIAGNOSTIC_CONTEXT>
{
  "timestamp": "2026-05-03T10:01:01.414001",
  "environment": "samples/Sample_2_Embezzlement_Leak",
  "physics_metrics": {
    "max_abs_residual": 0.0,
    "mean_gross_activity": 1302095.4826923076,
    "relative_leak_ratio": 0.0,
    "max_spectral": 0.0,
    "min_free_energy": 93251.36,
    "min_relative_free_energy": 0.5992711356337151,
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
    "assets": 210740.62000000005,
    "liabilities": 177105.2599999999,
    "equity": 0.0,
    "net_income": 33635.3600000001,
    "total_liab_eq": 210740.62,
    "revenue": 949944.35,
    "expense": 916308.9899999999,
    "is_balanced": true,
    "bs_items": [
      [
        "ACC_Accounts_Payable",
        "Liability",
        121149.74999999988
      ],
      [
        "ACC_Accounts_Receivable",
        "Asset",
        112901.66000000003
      ],
      [
        "ACC_Cash",
        "Liability (Short/Overdraft)",
        55955.51000000001
      ],
      [
        "ACC_Inventory",
        "Asset",
        97838.96000000002
      ]
    ],
    "pl_items": [
      [
        "ACC_COGS",
        "Expense",
        522589.5899999999
      ],
      [
        "ACC_Payroll_Exp",
        "Expense",
        216416.59
      ],
      [
        "ACC_Rent_Exp",
        "Expense",
        71989.61
      ],
      [
        "ACC_Sales_Revenue",
        "Revenue",
        949944.35
      ],
      [
        "ACC_Travel_Exp",
        "Expense",
        105313.2
      ]
    ],
    "tb_items": [
      [
        "ACC_Accounts_Payable",
        "Liability",
        499278.80000000005,
        620428.5499999999,
        121149.74999999988
      ],
      [
        "ACC_Accounts_Receivable",
        "Asset",
        949944.35,
        837042.69,
        112901.66000000003
      ],
      [
        "ACC_COGS",
        "Expense",
        522589.5899999999,
        0.0,
        522589.5899999999
      ],
      [
        "ACC_Cash",
        "Asset",
        837042.69,
        892998.2,
        -55955.51000000001
      ],
      [
        "ACC_Inventory",
        "Asset",
        620428.5499999999,
        522589.5899999999,
        97838.96000000002
      ],
      [
        "ACC_Payroll_Exp",
        "Expense",
        216416.59,
        0.0,
        216416.59
      ],
      [
        "ACC_Rent_Exp",
        "Expense",
        71989.61,
        0.0,
        71989.61
      ],
      [
        "ACC_Sales_Revenue",
        "Revenue",
        0.0,
        949944.35,
        949944.35
      ],
      [
        "ACC_Travel_Exp",
        "Expense",
        105313.2,
        0.0,
        105313.2
      ]
    ]
  }
}
</LLM_DIAGNOSTIC_CONTEXT>
-->
