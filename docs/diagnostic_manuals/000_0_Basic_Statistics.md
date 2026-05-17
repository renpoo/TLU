# 000_0: Basic Statistics & Foundation (基礎体力と基本統計量)

## 1. 対象モジュールとグラフ (Prefix: `000_0_X`)
* **財務・基礎状態:** `000_0_1__BS_Block_Total.png`, `000_0_1__PL_Waterfall_Total.png`, `000_0_1__PL_Trend_Revenue_vs_Expenses.png`
* **統計分布:** `000_0_2_3__histogram_kde.png`, `000_0_2_4__rolling_quantiles.png`, `000_0_2_5__kurtosis_vs_phase.png`

## 2. 東洋医学的メタファー (Epistemology)
* **基礎体力 (Foundation):** システムの絶対量（売上、資産、総トラフィック等）は「骨格・体格」と「基礎代謝」を表します。
* **脈の乱れ・発作 (Statistics):** Z-Scoreの突出（Z > 3.0）や尖度（Kurtosis）の異常な高さ（ファットテール）は、システムが通常許容できない「突発的な発作（ショック）」に対する脆弱性（ブラックスワン体質）を示します。

## 3. 検査基準と導出する一次所見
1. **体格の推移:** 資産総額や取引量が物理的に成長しているか、あるいは縮小（萎縮）しているか。
2. **歪度 (Skewness) と尖度 (Kurtosis):** KDE分布やRolling Quantilesにおいて、極端に尾が長い（Fat-tail / 高Kurtosis）場合、「普段は平穏だが、突然致命的なショックが訪れる脆弱な体質（Fragility）」という所見を導き出します。
3. **日常の誤認 (Zero-to-One Anomaly):** ほかの指標で慢性的な病気（高い粘性や継続的な出血）が存在するにもかかわらず、Z-Scoreが常に平坦な場合、「統計モデルが病気を『日常（ニューノーマル）』として誤認してしまっている（統計的監視の敗北）」という所見を下します。
