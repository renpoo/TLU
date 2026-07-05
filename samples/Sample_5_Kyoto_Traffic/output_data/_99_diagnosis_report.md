# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_5_Kyoto_Traffic`
**Date Analyzed:** 2026-07-06 07:17:08

## 1. Final Diagnosis

### ⚠️ COMPOSITE PATHOLOGY DETECTED
The system is suffering from multiple overlapping structural failures.

### 🟠 Chronic High Friction (Baseline Tearing)
- **Severity:** HIGH
- **Evidence:** Mean Entropy: 39.91.
- **Interpretation:** The system's baseline is inherently chaotic and highly viscous. Long-term structural integrity is doubtful due to constant energy dissipation.

### 🔴 Thermal Death (Absolute Energy Depletion)
- **Severity:** CRITICAL
- **Evidence:** Min Free Energy: -876907.64.
- **Interpretation:** The system has exhausted its resilience. External intervention is required.

### 🟠 Topological Feedback Loop (Wash Trade / Resonance)
- **Severity:** HIGH
- **Evidence:** Max Spectral Radius: 1.0000.
- **Interpretation:** An artificial loop of funds or extreme resonance has formed in the network.

---
## 2. Comprehensive Descriptive Statistics Table

The table below details the descriptive statistics computed individually for all active analytical scales across the TLU mathematical modules:

| Measure / Scale | Mean | Median | Mode (count / total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis | Z-Exceed |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Dynamics: acceleration_a | 0.0000 | 0.0000 | 0.0000 (28/600, 4.7%) | -3665.0000 | 3618.0000 | 7283.0000 | 125.5000 | 477.3676 | -0.5423 | 30.0186 | 14 |
| Dynamics: state_X | 10000.0000 | 10008.0000 | 10033.0000 (4/600, 0.7%) | 91.0000 | 19789.0000 | 19698.0000 | 372.2500 | 3571.5943 | -0.5041 | 3.4006 | 0 |
| Dynamics: velocity_v | 0.0000 | 1.0000 | 53.0000 (8/600, 1.3%) | -4323.0000 | 4333.0000 | 8656.0000 | 100.2500 | 616.0416 | -1.1071 | 28.2775 | 18 |
| Dynamics: viscosity_C | 1000.0000 | 999.9000 | 995.3000 (3/600, 0.5%) | 13.0250 | 1966.2500 | 1953.2250 | 33.1125 | 325.1747 | -0.5512 | 4.4484 | 28 |
| Forensics: conservation_residual | 0.0000 | 0.0000 | 0.0000 (24/24, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Forensics: kl_divergence_drift | 0.1505 | 0.0233 | 0.0090 (2/24, 8.3%) | 0.0000 | 1.7572 | 1.7572 | 0.0259 | 0.3984 | 3.2856 | 9.8580 | 1 |
| Stability: spectral_radius | 1.0000 | 1.0000 | 1.0000 (24/24, 100.0%) | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Stiffness: partial_corr | 0.0622 | 0.0000 | 1.0000 (1360/15000, 9.1%) | -1.0000 | 1.0000 | 2.0000 | 1.6211 | 0.7539 | -0.1279 | -1.5174 | 0 |
| Stiffness: stiffness_k | 0.0000 | 0.0000 | 0.0000 (15000/15000, 100.0%) | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.4418 | 17.3457 | 325 |
| Thermo: entropy_S | 39.9051 | 39.8676 | 40.8000 (6/24, 25.0%) | 39.0100 | 40.8309 | 1.8209 | 1.5712 | 0.8074 | 0.0231 | -1.9438 | 0 |
| Thermo: free_energy_F | 49744.2 | 186947.6 | -876908.0 (1/24, 4.2%) | -876907.6 | 250000.0 | 1126907.6 | 45832.7 | 325475.8 | -1.9895 | 2.4992 | 0 |
| Thermo: gross_activity_U | 250000.0 | 250000.0 | 250000.0 (24/24, 100.0%) | 250000.0 | 250000.0 | 0.0 | 0.0 | 0.0 | nan | nan | 0 |
| Thermo: temperature_T | 5095.5609 | 1610.9842 | 0.0000 (1/24, 4.2%) | 0.0000 | 28788.7614 | 28788.7614 | 1186.5157 | 8325.2500 | 1.9889 | 2.4962 | 0 |
| Topology: stress | 1.5093 | 1.2577 | 0.0000 (160/1920, 8.3%) | 0.0000 | 47.0080 | 47.0080 | 0.8221 | 1.8681 | 10.2518 | 200.2604 | 30 |
| Topology: weight | 3099.7188 | 3164.0000 | 2560.0000 (6/1920, 0.3%) | 121.0000 | 7296.0000 | 7175.0000 | 1665.2500 | 1273.9470 | -0.2634 | -0.0128 | 2 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `25000.00 ~ 25000.00`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `1026.6549`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `02_GojoKurumayacho` | 1387.5309 | `2021-06` | 1966.2500 |
| `03_GojoMuromachi` | 1369.8809 | `2021-12` | 1901.3500 |
| `17_SanjoKurumayacho` | 1339.3507 | `2021-12` | 1867.5500 |
| `18_SanjoMuromachi` | 1288.2649 | `2021-12` | 1771.2500 |
| `24_ShijoShinmachi` | 1119.8389 | `2021-12` | 1355.0000 |
| `11_NijoKarasuma` | 1118.8448 | `2021-12` | 1347.5750 |
| `15_SanjoHorikawa` | 1026.6549 | `2021-12` | 1037.5000 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `1.4564`)
| Node | Average Strain Energy |
| :--- | :---: |
| `21_ShijoKarasuma` | 1.2853 |
| `24_ShijoShinmachi` | 1.3054 |
| `11_NijoKarasuma` | 1.3883 |
| `06_IchijoKarasuma` | 1.4008 |
| `22_ShijoKurumayacho` | 1.4052 |
| `20_ShijoHorikawa` | 1.4128 |
| `01_GojoKarasuma` | 1.4564 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `1.8468` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `05_IchijoHorikawa` | 2.5929 |
| `07_IchijoKurumayacho` | 2.0524 |
| `00_GojoHorikawa` | 2.0095 |
| `09_IchijoShinmachi` | 1.9241 |
| `15_SanjoHorikawa` | 1.8855 |
| `18_SanjoMuromachi` | 1.8688 |
| `08_IchijoMuromachi` | 1.8468 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

