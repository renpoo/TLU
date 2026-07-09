# 000_1. 運動学と動的状態空間 (Dynamics & State-Space)

本ガイドは、Tensor-Link Utility (TLU) における運動学について解説します。

---

## 000_1: 運動学と動的状態空間

### 5. 3次元動的軌道リボン・位相空間プロット (`000_1_8__phase_portrait_3d.png` 等)

位置 $X$、速度 $\dot{X}$、加速度 $\ddot{X}$ から構築される3次元の位相空間軌道、または外力影響下の3次元力学特性（`000_1_6__3d_dynamics_external_force.png`）を示すグラフです。システムの動的安定性とカオス性を判別します。

#### 🟢 Sample 0 (正常代謝)

**臨床解説:**
軌道リボンが特定の安定アトラクター（リミットサイクル）へ収束します。外部のショックを弾性的にいなします。定常軌道を維持します。位置、速度、加速度の時系列変化、および3次元の位相空間軌道は規則的です。

- ![Sample 0 Dynamics Position](../../../samples/Sample_0_Healthy/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 0 Dynamics Velocity](../../../samples/Sample_0_Healthy/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 0 Dynamics Acceleration](../../../samples/Sample_0_Healthy/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 0 Phase Portrait](../../../samples/Sample_0_Healthy/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 0 Dynamics External Force](../../../samples/Sample_0_Healthy/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟡 Sample 1 (循環取引)

**臨床解説:**
軌道リボンが多次元的な広がりを失います。完全に平坦な二次元平面に押し潰されます。往復運動を繰り返します。自由度の大幅な喪失（還流ロック）を示します。

- ![Sample 1 Dynamics Position](../../../samples/Sample_1_Wash_Trade/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 1 Dynamics Velocity](../../../samples/Sample_1_Wash_Trade/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 1 Dynamics Acceleration](../../../samples/Sample_1_Wash_Trade/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 1 Phase Portrait](../../../samples/Sample_1_Wash_Trade/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 1 Dynamics External Force](../../../samples/Sample_1_Wash_Trade/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 2 (資金横領)

**臨床解説:**
資金が流出します。系内の活動質量が失われます。結合バネ剛性が破綻します。外部加振に対して病的共振を起こします。位相空間ではアトラクターの滑らかさが失われます。特異な軌跡として歪みます。

- ![Sample 2 Dynamics Position](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 2 Dynamics Velocity](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 2 Dynamics Acceleration](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 2 Phase Portrait](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 2 Dynamics External Force](../../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟡 Sample 3 (入力ミス)

**臨床解説:**
仕訳入力ミスが発生します。その瞬間に軌道が平衡点から弾き飛ばされます。病的構造はありません。翌期に正常アトラクターへ自律復元します。過渡応答は位置、速度、加速度のすべてに鋭い変動として現れます。位相空間では一時的なループとして記録されます。

- ![Sample 3 Dynamics Position](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 3 Dynamics Velocity](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 3 Dynamics Acceleration](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 3 Phase Portrait](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 3 Dynamics External Force](../../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 4 (複合アノマリー)

**臨床解説:**
循環取引の強制同期と横領による質量散逸が同時に発生します。アトラクターが崩壊します。軌道はカオス的無限発散へ突入します。位置・速度・加速度は期を追うごとに発散します。位相空間軌道は閉じない螺旋を描きます。

- ![Sample 4 Dynamics Position](../../../samples/Sample_4_Composite_Chaos/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 4 Dynamics Velocity](../../../samples/Sample_4_Composite_Chaos/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 4 Dynamics Acceleration](../../../samples/Sample_4_Composite_Chaos/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 4 Phase Portrait](../../../samples/Sample_4_Composite_Chaos/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 4 Dynamics External Force](../../../samples/Sample_4_Composite_Chaos/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 5 (京都交差点網)

**臨床解説:**
主要交差点の容量飽和（粘性ダンピングの無限大化）が発生します。状態の動的軌道が「特異平面」に固定化されます。渋滞デッドロックを示します。位置、速度、加速度は一定値（フリーズ）に収束します。位相空間でも単一の不働点へ吸い込まれるように停止します。

- ![Sample 5 Dynamics Position](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 5 Dynamics Velocity](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 5 Dynamics Acceleration](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 5 Phase Portrait](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 5 Dynamics External Force](../../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟢 Sample 6 (株券流体)

**臨床解説:**
株式市場における株券対流状態です。粘性と慣性が市場全体でバランスします。位置・速度・加速度は滑らかに連動します。位相空間では閉じられた3次元リミットサイクルが安定して維持されます。

- ![Sample 6 Dynamics Position](../../../samples/Sample_6_Market_Stock_Flow/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 6 Dynamics Velocity](../../../samples/Sample_6_Market_Stock_Flow/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 6 Dynamics Acceleration](../../../samples/Sample_6_Market_Stock_Flow/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 6 Phase Portrait](../../../samples/Sample_6_Market_Stock_Flow/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 6 Dynamics External Force](../../../samples/Sample_6_Market_Stock_Flow/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟢 Sample 7 (現金流体)

**臨床解説:**
市場ネットワーク内での現金対流状態です。定常的なキャッシュの往来が摩擦熱を抑えます。急激なショックに対してもしなやかに復元します。時系列変化は周期的です。位相空間上でも調和のとれたコンパクトなアトラクターを示します。

- ![Sample 7 Dynamics Position](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 7 Dynamics Velocity](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 7 Dynamics Acceleration](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 7 Phase Portrait](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 7 Dynamics External Force](../../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 8 (fMRI 脳梗塞)

**臨床解説:**
$t=30$ に梗塞が発生します。その瞬間、運動野の活動質量が消滅します。軌道は別の低機能状態アトラクターへと不連続にジャンプ（相転移）します。そこで固定化されます。位置、速度、加速度、および3次元位相空間プロットでアトラクターの縮退と形状変化が描かれています。

- ![Sample 8 Dynamics Position](../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 8 Dynamics Velocity](../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 8 Dynamics Acceleration](../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 8 Phase Portrait](../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 8 Dynamics External Force](../../../samples/Sample_8_fMRI_Stroke/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 9 (fMRI てんかん発作)

**臨床解説:**
全脳領域が異常周波数にハックされます。3次元軌道リボンは複雑性をすべて失います。単一サイン波の単調な円軌道へと完全にフリーズ（過同期）します。位置、速度、加速度、および3次元位相空間プロットで異常な規則性と複雑性の欠如が確認できます。

- ![Sample 9 Dynamics Position](../../../samples/Sample_9_fMRI_Seizure/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 9 Dynamics Velocity](../../../samples/Sample_9_fMRI_Seizure/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 9 Dynamics Acceleration](../../../samples/Sample_9_fMRI_Seizure/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 9 Phase Portrait](../../../samples/Sample_9_fMRI_Seizure/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 9 Dynamics External Force](../../../samples/Sample_9_fMRI_Seizure/readme_plots/000_1_6__3d_dynamics_external_force.png)

---

### 6. 加加速度 (Jerk) および 加加加速度 (Snap) の時系列変化 (`000_1_9__3d_dynamics_jerk.png` / `000_1_10__3d_dynamics_snap.png`)

加加速度（Jerk: 加速度の時間変化率 $\dddot{X}$）および加加加速度（Snap: Jerk の時間変化率 $\ddddot{X}$）は、システムの急激な状態変化（ショック）や、過渡的な高周波ノッキング発振を捉えるための高階微分メトリクスです。

#### 🟢 Sample 0 (正常代謝: Healthy)
* **臨床解説:** 時系列を通じて Jerk および Snap はほぼ完全に平坦（ゼロ平均定常）であり、不連続な取引ショックや急激な物理的加減速は存在しない健康状態を示します。

#### 🟡 Sample 1 (循環取引: Wash Trade)
* **臨床解説:** 架空取引の往復運動の切り替えしポイント（同期時点）において、Jerk と Snap が局所的な細いスパイクを形成します。流体の無理な方向転換ショックを検出しています。

#### 🔴 Sample 2 (資金横領: Embezzlement Leak)
* **臨床解説:** 資金の流出開始時（t=4）、およびシステム全体のキャッシュが底をつき始める後半のステップにおいて、流動性が不連続に破綻するため、巨大な Jerk / Snap のインパルス（急減速ショック波）が発生します。

#### 🟡 Sample 3 (入力ミス: Unbalanced Mistake)
* **臨床解説:** 片面入力ミスが発生したステップ（t=1）と、それが自己修正されたステップ（t=2）のピンポイントにおいてのみ、巨大な鋭いインパルス（Jerk / Snap の極値）が立ち上がります。

#### 🔴 Sample 4 (複合アノマリー: Composite Chaos)
* **臨床解説:** 循環取引の還流と横領の漏洩が重なるため、中盤から後半にかけて Jerk / Snap が激しく発振（ノッキング共振）します。システム崩壊前の末期的な自励振動を示します。

#### 🔴 Sample 5 (京都交差点網: Kyoto Traffic)
* **臨床解説:** 主要交差点の容量規制が始まった t=12 以降、車両の急ブレーキ・急発進（Jerk）およびそれに連鎖する渋滞の伝播伝達（Snap）が周辺交差点へ異常高騰・発振し、流れが完全にフリーズします。

#### 🟢 Sample 6 (株券流体: Market Stock Flow) & 🟢 Sample 7 (現金流体: Market Cash Flow)
* **臨床解説:** 正常な約定・決済流体運動であるため、Jerk / Snap ともに低位で安定して推移しており、突発的な市場パニックやシステムノッキングは発生していません。

#### 🔴 Sample 8 (fMRI 脳梗塞: fMRI Stroke)
* **臨床解説:** 脳血流の閉塞が発生した t=30 において、運動野の血流信号に急激な遮断（Jerk ショック）が発生。その後、周囲領域への伝達信号が不連続にのたうち回る Snap スパイクが観測されます。

#### 🔴 Sample 9 (fMRI てんかん発作: fMRI Seizure)
* **臨床解説:** 発作発症（t=30）以降、全脳がサイン波で異常同期するため、Jerk / Snap もサイン波の同期的な急変（自励的な機能的ノッキング振動）として高頻度かつ規則的なパターンで固定化されます。

