#!/usr/bin/env python3
# ==========================================
# _90_visualize_TEMPLATE.py
# TLU System: [Domain Name] Visualization
# ==========================================
import sys
import pandas as pd
import matplotlib.pyplot as plt

# 1. 共通可視化基盤のインポート (配管とテーマエンジンの再利用)
from src.visualization.___visualizer_utils import (
    get_visualizer_parser,
    apply_theme,
    load_node_labels,
    load_time_labels,
    setup_plot,
    save_plot
)

def generate_your_plot(df: pd.DataFrame, theme_cfg: dict, idx_to_node_label: dict, idx_to_time_label: dict):
    """
    [Pure Plotting Function]
    データフレームとテーマ設定を受け取り、MatplotlibのFigureオブジェクトを生成して返す純粋関数。
    
    ※この関数内に、旧版の可視化ロジック（ax.plot や ax.scatter など）をそのまま移植してください。
    """
    # キャンバスと軸のセットアップ (サイズは必要に応じて変更)
    fig, ax = setup_plot(figsize=(12, 8))
    
    # === ここに真の可視化ロジック（旧版コードの呼び出し）を実装 ===
    # 【例: テーマエンジンからの高度な色取得】
    # domain_colors = theme_cfg.get('your_domain', {}).get('colors', ['#00FF00', '#FF00FF'])
    
    # 【例: データのプロット】
    # if 'node_idx' in df.columns and 'metric_value' in df.columns:
    #     for node_idx, group in df.groupby('node_idx'):
    #         label = idx_to_node_label.get(int(node_idx), f"Node_{node_idx}")
    #         ax.plot(group['t_idx'], group['metric_value'], label=label)
    
    # 【例: グラフの装飾】
    # ax.set_title("Your Domain Analysis", fontsize=16)
    # ax.set_xlabel("Time Step")
    # ax.set_ylabel("Metric Value")
    # ax.legend(loc='best')
    # ax.grid(True, alpha=0.3)
    
    # 必ず完成した Figure オブジェクト (fig) を返すこと
    return fig

def main():
    # 1. 共通パーサーのセットアップと引数取得
    # (--out_dir, --filename, --theme, --node_map 等はここで自動処理されます)
    parser = get_visualizer_parser("TLU [Domain Name] Visualization")
    
    # 必要に応じてこのスクリプト特有の引数を追加
    # parser.add_argument("--threshold", type=float, default=0.5, help="Plot threshold")
    
    args = parser.parse_args()

    # 2. データの堅牢な読み込み (標準入力からのCSVパイプラインを想定)
    try:
        df = pd.read_csv(sys.stdin)
        if df.empty:
            print("[WARN] No data received from stdin. Exiting.", file=sys.stderr)
            sys.exit(0)
    except Exception as e:
        print(f"Error reading input data: {e}", file=sys.stderr)
        sys.exit(1)

    # 3. メタデータの読み込み (Nodeラベル, Timeラベルの解決)
    # df内に存在する最大インデックスを基準に辞書を構築
    max_n = int(df['node_idx'].max()) + 1 if 'node_idx' in df.columns else 50
    max_t = int(df['t_idx'].max()) + 1 if 't_idx' in df.columns else 100
    
    idx_to_node_label = load_node_labels(args.node_map, max_n)
    idx_to_time_label = load_time_labels(args.time_map, max_t)

    # 4. テーマエンジンの適用 (JSONからのセマンティックカラーのロードと背景色設定)
    try:
        theme_cfg = apply_theme(args.theme)
    except Exception as e:
        print(f"[WARN] Theme application failed: {e}. Falling back to default styles.", file=sys.stderr)
        theme_cfg = {}

    # 5. プロット生成関数の呼び出し (配管から隔離された描画処理)
    fig = generate_your_plot(df, theme_cfg, idx_to_node_label, idx_to_time_label)

    # 6. 画像の保存または画面表示 (I/Oの共通化)
    save_plot(fig, args.out_dir, args.filename)

if __name__ == "__main__":
    main()
