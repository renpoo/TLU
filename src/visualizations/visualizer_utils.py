import os, sys, argparse
import pandas as pd
import japanize_matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import json

def get_base_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--out_dir", type=str, default="workspace/output_plots/")
    parser.add_argument("--filename", type=str, default=None)
    # デフォルトのテーマは 'dark'（ユーザー合意に基づく唯一の起点）
    parser.add_argument("--theme", type=str, default='dark')
    parser.add_argument("--node_map", type=str, default="_node_map.csv")
    parser.add_argument("--time_map", type=str, default="_time_map.csv")
    parser.add_argument("--max_legend", type=int, default=25)
    return parser

def apply_theme(theme_name="dark"):
    """
    指定されたテーマ名のJSONを読み込み、Matplotlibのグローバル設定を適用しつつ、
    セマンティックカラーの辞書を返す。
    ※フェイルファスト思想に基づき、ファイル欠損やパースエラー時は容赦なくクラッシュさせる。
    """
    # 配布パッケージとしての絶対パス（コンテナ内の絶対法則）
    json_path = f"src/visualizations/themes/theme_{theme_name}.json"
    
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"❌ Theme configuration file not found: {json_path}")
        
    with open(json_path, 'r', encoding='utf-8') as f:
        theme_cfg = json.load(f)

    # デフォルト値を駆逐: JSON内に 'mode' が無ければ KeyError でクラッシュさせる
    mode = theme_cfg["mode"]
    plt.style.use('dark_background' if mode == 'dark' else 'default')
    plt.rcParams['savefig.format'] = 'png'
        
    return theme_cfg

def load_node_labels(node_map_path: str, max_n: int) -> dict:
    """
    CSVからノードラベルを読み込む。
    デフォルト値（ダミーラベル）の生成を駆逐。ファイル不在や列名不一致は即座にクラッシュさせる。
    """
    if not os.path.exists(node_map_path):
        raise FileNotFoundError(f"❌ Node map file not found: {node_map_path}")
        
    idx_to_label = {i: f"Node_{i:02d}" for i in range(max_n)}
    try:
        df = pd.read_csv(node_map_path)
        for _, row in df.iterrows():
            idx = int(row['node_idx'])
            if idx < max_n: idx_to_label[idx] = str(row['node_label'])
    except Exception: 
        raise FileNotFoundError(f"❌ Node map file not found: {node_map_path}")

    return idx_to_label

def load_time_labels(time_map_path: str, max_n: int) -> dict:
    """
    CSVから時間ラベルを読み込む。
    こちらも同様にデフォルト値を駆逐し、完全なフェイルファストを適用。
    """
    if not os.path.exists(time_map_path):
        raise FileNotFoundError(f"❌ Time map file not found: {time_map_path}")
        
    idx_to_label = {i: f"Time_{i:02d}" for i in range(max_n)}
    try:
        df = pd.read_csv(time_map_path)
        for _, row in df.iterrows():
            idx = int(row['t_idx'])
            if idx < max_n: idx_to_label[idx] = str(row['time_label'])
    except Exception: 
        raise FileNotFoundError(f"❌ Time map file not found: {time_map_path}")

    return idx_to_label

def save_plot(fig, out_dir: str, filename: str):
    os.makedirs(out_dir, exist_ok=True)
    base_name = os.path.splitext(filename)[0]
    out_path = os.path.join(out_dir, f"{base_name}.png")
    fig.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f"✅ Saved: {out_path}", file=sys.stderr)


def _draw_single_heatmap(ax, pivot_df, cmap, cbar_label, title_text, x_labels, y_labels, top_k_idx, text_col, outlier_col):
    """ [Pure Drawing Logic] 単一のヒートマップを描画し、装飾を施す """
    sns.heatmap(pivot_df, ax=ax, cmap=cmap, robust=True, 
                cbar_kws={'label': cbar_label}, 
                xticklabels=x_labels) # 修正: X軸ラベルを必ず渡す

    ax.set_title(title_text, fontsize=15, color=text_col, loc='left', fontweight='bold')
    ax.set_ylabel("Node (Dept/Account)", color=text_col, fontsize=12)
    ax.set_xlabel("Timeline", color=text_col, fontsize=12)

    # 軸目盛りの調整
    ax.tick_params(axis='x', rotation=45, colors=text_col, labelsize=10)
    ax.set_yticklabels(y_labels, fontsize=10, rotation=0)

    # Y軸ラベルのハイライト処理
    for i, label in enumerate(ax.get_yticklabels()):
        if i in top_k_idx:
            label.set_color(outlier_col)
            label.set_fontweight('bold')
        else:
            label.set_color(text_col)
            label.set_alpha(0.8)

def _draw_matrix_heatmap(ax, pivot_df, cmap, cbar_label, title_text, axis_labels, text_col, bg_col=None, mask=None, vmin=None, vmax=None):
    """ [Pure Drawing Logic] N x N の相関・ラグ行列ヒートマップを描画する """
    import seaborn as sns
    sns.heatmap(pivot_df, ax=ax, cmap=cmap, mask=mask, vmin=vmin, vmax=vmax,
                xticklabels=axis_labels, yticklabels=axis_labels, 
                cbar_kws={'label': cbar_label})
                
    ax.set_title(title_text, fontsize=16, color=text_col, pad=20, fontweight='bold')
    ax.set_xlabel("Target Node (Effect)", color=text_col, fontsize=12)
    ax.set_ylabel("Source Node (Cause)", color=text_col, fontsize=12)

    ax.tick_params(axis='x', rotation=45, colors=text_col)
    ax.tick_params(axis='y', rotation=0, colors=text_col)
    
    if bg_col:
        ax.set_facecolor(bg_col)
