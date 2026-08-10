# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_9_fMRI_Seizure`
**Date Analyzed:** 2026-08-11 06:38:49

## 1. Final Diagnosis

### 🟠 Topological Feedback Loop (Wash Trade / Resonance)
- **Severity:** HIGH
- **Evidence:** Max Spectral Radius: 1.0000.
- **Interpretation:** An artificial loop of funds or extreme resonance has formed in the network.

---
## 2. Comprehensive Descriptive Statistics Table

The table below details the descriptive statistics computed individually for all active analytical scales across the TLU mathematical modules:

| Measure / Scale | Mean | Median | Mode (count / total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis | Z-Exceed |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Dynamics: acceleration_a | 0.0000 | 0.0000 | 0.0000 (35/300, 11.7%) | -160.7900 | 147.7600 | 308.5500 | 58.1625 | 49.7131 | -0.1130 | 0.4380 | 1 |
| Dynamics: jerk_j | -0.0000 | 0.0000 | 0.0000 (38/300, 12.7%) | -245.4300 | 252.9100 | 498.3400 | 101.1325 | 85.3246 | 0.0506 | 0.5289 | 0 |
| Dynamics: snap_s | -0.0000 | 0.0000 | 0.0000 (42/300, 14.0%) | -465.6200 | 452.1800 | 917.8000 | 173.2775 | 153.2127 | 0.0564 | 0.7537 | 1 |
| Dynamics: state_X | 100000.0000 | 99985.1350 | 100119.8000 (31/300, 10.3%) | 99732.9400 | 100417.0300 | 684.0900 | 244.4750 | 159.0480 | 0.3191 | -0.8413 | 0 |
| Dynamics: velocity_v | 0.0000 | 0.0000 | 0.0000 (30/300, 10.0%) | -99.6700 | 80.2300 | 179.9000 | 40.7275 | 34.5568 | -0.1127 | 0.0682 | 0 |
| Dynamics: viscosity_C | 10000.0000 | 9997.6568 | 9988.5900 (3/300, 1.0%) | 9985.1177 | 10022.9123 | 37.7946 | 15.5462 | 10.7705 | 0.6542 | -0.4832 | 0 |
| Forensics: conservation_residual | 0.0000 | 0.0000 | 0.0000 (60/60, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Forensics: kl_divergence_drift | 0.4489 | 0.0579 | 0.0010 (12/60, 20.0%) | 0.0000 | 1.7696 | 1.7696 | 0.9153 | 0.5655 | 0.8616 | -0.6997 | 0 |
| Stability: spectral_radius | 1.0000 | 1.0000 | 1.0000 (60/60, 100.0%) | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Stiffness: partial_corr | 0.3810 | 0.3109 | 1.0000 (300/1500, 20.0%) | -1.0000 | 1.0000 | 2.0000 | 0.4307 | 0.3878 | 0.0913 | 0.2888 | 12 |
| Stiffness: stiffness_k | -0.0000 | -0.0000 | 0.0000 (1500/1500, 100.0%) | -0.0030 | 0.0037 | 0.0067 | 0.0001 | 0.0003 | 0.7433 | 49.9935 | 23 |
| Thermo: entropy_S | 9.0983 | 9.5233 | 10.0000 (30/60, 50.0%) | 7.3110 | 9.9994 | 2.6884 | 1.7391 | 0.9965 | -0.4792 | -1.3308 | 0 |
| Thermo: free_energy_F | 496949.4 | 496711.2 | 496655.0 (2/60, 3.3%) | 496087.8 | 500000.0 | 3912.2 | 652.9 | 779.1 | 1.9441 | 3.9121 | 1 |
| Thermo: gross_activity_U | 500000.0 | 500000.0 | 500000.0 (60/60, 100.0%) | 500000.0 | 500000.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0 |
| Thermo: temperature_T | 340.2913 | 382.3385 | 390.8000 (2/60, 3.3%) | 0.0000 | 399.2638 | 399.2638 | 37.4535 | 90.4312 | -2.0541 | 3.5112 | 1 |
| Topology: stress | 1.2822 | 1.1054 | 0.0000 (40/1200, 3.3%) | 0.0000 | 15.7809 | 15.7809 | 1.1550 | 1.5018 | 5.7864 | 49.7108 | 8 |
| Topology: weight | 915.8751 | 564.1500 | 2332.4000 (8/1200, 0.7%) | 226.4700 | 2667.4600 | 2440.9900 | 236.4125 | 803.7185 | 1.4418 | 0.2297 | 0 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `50000.00 ~ 50000.00`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `10002.2033`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `02_Prefrontal_Cortex` | 10015.9306 | `2024-01-01 10:08:30` | 10022.9123 |
| `03_Temporal_Lobe` | 10002.2033 | `2024-01-01 10:09:50` | 10007.5630 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `0.4411`)
| Node | Average Strain Energy |
| :--- | :---: |
| `02_Prefrontal_Cortex` | 0.4399 |
| `04_Visual_Cortex` | 0.4411 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `0.4616` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `03_Temporal_Lobe` | 0.4753 |
| `01_Parietal_Lobe` | 0.4616 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

