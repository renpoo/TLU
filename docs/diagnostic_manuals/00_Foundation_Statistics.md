# Sub-Manual 00: Foundation & Statistical Baseline (基礎体力と基本統計量)

## 1. 対象データとグラフ
* **Foundation:** `000_0_1__BS_Block_Total.png`, `000_0_1__PL_Waterfall_Total.png`, `000_0_1__PL_Trend_Revenue_vs_Expenses.png`
* **Statistics:** `000_0_2_3__histogram_kde.png`, `000_0_2_4__rolling_quantiles.png`

## 2. 東洋医学的メタファー
* **基礎体力 (Foundation):** B/SやP/Lの総和は「骨格・体格」と「基礎代謝」を表します。
* **脈の乱れ・発作 (Statistics):** Z-Scoreの突出（Z > 3.0）やFat-tail（ファットテール）は、システムが通常許容できない「突発的な発作」や「ショック」に対する脆弱性を示します。

## 3. 検査すべき事項と導出する所見
1. **体格の推移:** 売上や資産総額が成長しているか、縮小しているか。
2. **歪度 (Skewness) と尖度 (Kurtosis):** KDE分布において、極端に尾が長い（Fat-tail）場合、「普段は平穏だが、突然致命的なショックが訪れるブラックスワン体質」という所見を導き出します。
3. **日常の誤認:** 慢性的な病気（高い粘性や漏洩）が存在するにもかかわらず、Z-Scoreが平坦な場合、「統計モデルが病気を『日常』として誤認している（統計的監視の敗北）」という所見を下します。
