# TLU Meta-Diagnosis Report (Attending Physician's Summary)

**Target Environment:** `samples/Sample_2_Embezzlement_Leak`
**Date Analyzed:** 2026-05-03 11:59:43

## 1. Final Diagnosis

### 🔴 Unbalanced Journal Mistake (Conservation Violation)
- **Severity:** CRITICAL
- **Evidence:** Relative Leak Ratio reached 0.0003 (Threshold: 1e-06). Raw residual: 407.89. Peak Location: Time: 2020-W05.
- **Interpretation:** The fundamental law of mass conservation is broken. A statistically significant percentage of systemic flux is disappearing or materializing from nowhere.

---
## 2. Scale-Invariant Diagnostic Metrics

| Physical Domain | Extracted Metric | Value | Threshold |
|-----------------|------------------|-------|-----------|
| Macro Forensics | Relative Mass Leak Ratio | 0.0003 | > 1e-06 |
| Control Theory  | Max Spectral Radius      | 0.0000 | >= 0.6 |
| Thermodynamics  | Relative Free Energy Ratio| 0.3957 | < -0.1 |
| Micro Forensics | Max Local Z-Score        | 0.00 | > 3.0 |

> *Generated automatically by the TLU Meta-Diagnosis Engine.*

<!--
<LLM_DIAGNOSTIC_CONTEXT>
{
  "timestamp": "2026-05-03T11:59:43.900582",
  "environment": "samples/Sample_2_Embezzlement_Leak",
  "physics_metrics": {
    "max_abs_residual": 407.89,
    "mean_gross_activity": 1287736.935769231,
    "relative_leak_ratio": 0.0003167494762867437,
    "max_spectral": 0.0,
    "min_free_energy": 93251.36,
    "min_relative_free_energy": 0.39568575835698977,
    "max_z_score": 0.0,
    "max_leak_location": "Time: 2020-W05"
  },
  "detected_pathologies": [
    {
      "pathology": "Unbalanced Journal Mistake (Conservation Violation)",
      "severity": "CRITICAL",
      "evidence": "Relative Leak Ratio reached 0.0003 (Threshold: 1e-06). Raw residual: 407.89. Peak Location: Time: 2020-W05.",
      "interpretation": "The fundamental law of mass conservation is broken. A statistically significant percentage of systemic flux is disappearing or materializing from nowhere."
    }
  ],
  "financial_baseline": {
    "week": "2020-W52",
    "assets": 211258.12000000023,
    "liabilities": 148394.59000000055,
    "equity": 0.0,
    "net_income": 62863.52999999991,
    "total_liab_eq": 211258.12000000046,
    "revenue": 955157.5599999998,
    "expense": 892294.0299999999,
    "is_balanced": true,
    "bs_items": [
      [
        "ACC_Accounts_Payable",
        "Liability",
        88381.15000000026
      ],
      [
        "ACC_Accounts_Receivable",
        "Asset",
        112493.81999999995
      ],
      [
        "ACC_Cash",
        "Liability (Short/Overdraft)",
        60013.44000000029
      ],
      [
        "ACC_Inventory",
        "Asset",
        98764.30000000028
      ]
    ],
    "pl_items": [
      [
        "ACC_COGS",
        "Expense",
        527985.6699999999
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
        79499.51999999997
      ],
      [
        "UNKNOWN_LEAK",
        "Expense",
        1827.76
      ]
    ],
    "tb_items": [
      [
        "ACC_Accounts_Payable",
        "Liability",
        538368.82,
        626749.9700000002,
        88381.15000000026
      ],
      [
        "ACC_Accounts_Receivable",
        "Asset",
        955157.5599999998,
        842663.7399999999,
        112493.81999999995
      ],
      [
        "ACC_COGS",
        "Expense",
        527985.6699999999,
        0.0,
        527985.6699999999
      ],
      [
        "ACC_Cash",
        "Asset",
        840835.9799999997,
        900849.42,
        -60013.44000000029
      ],
      [
        "ACC_Inventory",
        "Asset",
        626749.9700000002,
        527985.6699999999,
        98764.30000000028
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
        79499.51999999997,
        0.0,
        79499.51999999997
      ],
      [
        "UNKNOWN_LEAK",
        "Expense",
        1827.76,
        0.0,
        1827.76
      ]
    ]
  }
}
</LLM_DIAGNOSTIC_CONTEXT>
-->
