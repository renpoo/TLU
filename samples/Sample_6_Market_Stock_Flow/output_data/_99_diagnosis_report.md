# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_6_Market_Stock_Flow`
**Date Analyzed:** 2026-08-11 06:34:14

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
| Dynamics: acceleration_a | 0.0000 | 0.0000 | 0.0000 (135/360, 37.5%) | -75816540.8000 | 80100222.2300 | 155916763.0300 | 118659.2650 | 11475566.6868 | 0.1930 | 23.1516 | 14 |
| Dynamics: jerk_j | 0.0000 | 0.0000 | 0.0000 (140/360, 38.9%) | -124284537.3700 | 155916763.0300 | 280201300.4000 | 203101.2450 | 19498744.6205 | 0.5609 | 25.0636 | 11 |
| Dynamics: snap_s | -0.0000 | 0.0000 | 0.0000 (150/360, 41.7%) | -248289557.2100 | 239743140.6000 | 488032697.8100 | 601454.1075 | 35330379.0996 | -0.0698 | 22.8813 | 12 |
| Dynamics: state_X | 406126241.4533 | 93878458.0850 | 291423397.1000 (24/360, 6.7%) | -539123.3600 | 1493964049.2100 | 1494503172.5700 | 658383940.7550 | 509768341.9263 | 1.0489 | -0.3642 | 0 |
| Dynamics: velocity_v | 0.0000 | 0.0000 | 0.0000 (140/360, 38.9%) | -67827650.2800 | 65981464.0400 | 133809114.3200 | 7385.9700 | 8158320.5555 | -0.2821 | 40.3742 | 8 |
| Dynamics: viscosity_C | 40613162.2784 | 9076559.7268 | 29142339.7100 (24/360, 6.7%) | 13175.4788 | 149263929.9070 | 149250754.4282 | 65807145.2320 | 51093993.2140 | 1.0512 | -0.3597 | 0 |
| Forensics: conservation_residual | 0.0000 | 0.0000 | 0.0000 (24/24, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Forensics: kl_divergence_drift | 8.8674 | 7.0470 | 0.0000 (1/24, 4.2%) | 0.0000 | 23.6711 | 23.6711 | 5.1302 | 5.7702 | 0.8307 | 0.4045 | 0 |
| Stability: spectral_radius | 0.9816 | 0.9995 | 1.0000 (12/24, 50.0%) | 0.8744 | 1.0000 | 0.1256 | 0.0223 | 0.0354 | -2.1407 | 3.4591 | 1 |
| Stiffness: partial_corr | 0.0775 | 0.0000 | 0.0000 (3090/5400, 57.2%) | -1.0000 | 1.0000 | 2.0000 | 0.0684 | 0.5807 | -0.0198 | -0.3265 | 0 |
| Stiffness: stiffness_k | 0.0000 | 0.0000 | 0.0000 (5400/5400, 100.0%) | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 6.5548 | 1076.9202 | 5 |
| Thermo: entropy_S | 1.7394 | 1.5036 | 0.2000 (2/24, 8.3%) | 0.1665 | 4.7120 | 4.5455 | 1.8663 | 1.2941 | 0.7718 | -0.1918 | 0 |
| Thermo: free_energy_F | 6036402755.2 | 6066136997.8 | 5831684166.0 (1/24, 4.2%) | 5831684165.9 | 6091893621.8 | 260209455.9 | 100994055.8 | 69181026.0 | -1.4181 | 1.2746 | 0 |
| Thermo: gross_activity_U | 6091974341.8 | 6091893621.8 | 6091893622.0 (20/24, 83.3%) | 6091893621.8 | 6092971868.5 | 1078246.7 | 0.0 | 234335.1 | 3.5010 | 12.0270 | 1 |
| Thermo: temperature_T | 29651551.4172 | 20649616.6150 | 0.0000 (1/24, 4.2%) | 0.0000 | 78115115.7447 | 78115115.7447 | 41035095.1103 | 25660655.0365 | 0.6311 | -1.0167 | 0 |
| Topology: stress | 150.8043 | 0.7867 | 0.0000 (68/487, 14.0%) | 0.0000 | 13948.0940 | 13948.0940 | 1.7636 | 1033.4679 | 9.2945 | 99.4934 | 9 |
| Topology: weight | 13084780.6324 | 19920.3200 | 111.0000 (2/487, 0.4%) | 13.8600 | 441354259.5500 | 441354245.6900 | 1384238.8250 | 58985383.4172 | 5.7347 | 33.8886 | 12 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `609189362.18 ~ 609221357.63`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `58239516.0205`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `01_USR_002` | 143448843.0912 | `2020-02` | 149263929.9070 |
| `00_USR_001` | 143329389.4154 | `2020-04` | 144794366.9900 |
| `10_STK_001` | 112157075.0560 | `2020-01` | 112157075.0560 |
| `14_STK_005` | 66346897.1570 | `2020-01` | 66346897.1570 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `3.8238`)
| Node | Average Strain Energy |
| :--- | :---: |
| `03_USR_004` | 0.2530 |
| `02_USR_003` | 0.2892 |
| `09_USR_010` | 3.7814 |
| `04_USR_005` | 3.7889 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `4.1658` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `10_STK_001` | 4.1658 |
| `11_STK_002` | 4.1658 |
| `12_STK_003` | 4.1658 |
| `13_STK_004` | 4.1658 |
| `14_STK_005` | 4.1658 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

