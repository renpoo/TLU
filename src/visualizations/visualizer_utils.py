import os, sys, argparse
import pandas as pd
import japanize_matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import json

plt.rcParams['font.family'] = 'Noto Sans CJK JP'
plt.rcParams['font.monospace'] = ['Noto Sans CJK JP'] + plt.rcParams['font.monospace']

def get_base_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--out_dir", type=str, default="workspace/output_plots/")
    parser.add_argument("--filename", type=str, default=None)
    # Default theme is 'dark' (only starting point based on user agreement)
    parser.add_argument("--theme", type=str, default='dark')
    parser.add_argument("--node_map", type=str, default="_node_map.csv")
    parser.add_argument("--time_map", type=str, default="_time_map.csv")
    parser.add_argument("--max_legend", type=int, default=25)
    return parser

def apply_theme(theme_name="dark"):
    """
    Loads the JSON of the specified theme name, applies Matplotlib's global settings,
    and returns a dictionary of semantic colors.
    * Based on the fail-fast philosophy, it crashes without mercy if files are missing or parsing errors occur.
    """
    # Absolute path as a distribution package (absolute rule in container)
    json_path = f"src/visualizations/themes/theme_{theme_name}.json"
    
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"❌ Theme configuration file not found: {json_path}")
        
    with open(json_path, 'r', encoding='utf-8') as f:
        theme_cfg = json.load(f)

    # Eliminate default values: crash with KeyError if 'mode' is not in JSON
    mode = theme_cfg["mode"]
    plt.style.use('dark_background' if mode == 'dark' else 'default')
    plt.rcParams['savefig.format'] = 'png'
        
    return theme_cfg

def load_node_labels(node_map_path: str, max_n: int) -> dict:
    """
    Load node labels from CSV.
    Eliminate the generation of default values (dummy labels). File absence or column name mismatch immediately crashes.
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
    Load time labels from CSV.
    Similarly eliminate default values and completely apply fail-fast.
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

def draw_single_heatmap(ax, pivot_df, cmap, cbar_label, title_text, x_labels, y_labels, top_k_idx, text_col, outlier_col):
    """ [Pure Drawing Logic] Draws a single heatmap and applies decoration. """
    sns.heatmap(pivot_df, ax=ax, cmap=cmap, robust=True, 
                cbar_kws={'label': cbar_label}, 
                xticklabels=x_labels) # Fix: Always pass X-axis labels

    ax.set_title(title_text, fontsize=15, color=text_col, loc='left', fontweight='bold')
    ax.set_ylabel("Node (Dept/Account)", color=text_col, fontsize=12)
    ax.set_xlabel("Timeline", color=text_col, fontsize=12)

    # Adjust axis tick marks
    ax.tick_params(axis='x', rotation=45, colors=text_col, labelsize=10)
    ax.set_yticklabels(y_labels, fontsize=10, rotation=0)

    # Y-axis label highlight processing
    for i, label in enumerate(ax.get_yticklabels()):
        if i in top_k_idx:
            label.set_color(outlier_col)
            label.set_fontweight('bold')
        else:
            label.set_color(text_col)
            label.set_alpha(0.8)

    return

def draw_matrix_heatmap(ax, pivot_df, cmap, cbar_label, title_text, axis_labels, text_col, bg_col=None, mask=None, vmin=None, vmax=None):
    """ [Pure Drawing Logic] Draws an N x N correlation/lag matrix heatmap. """
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

    return

def save_plot(fig, out_dir: str, filename: str):
    os.makedirs(out_dir, exist_ok=True)
    base_name = os.path.splitext(filename)[0]
    out_path = os.path.join(out_dir, f"{base_name}.png")
    fig.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f"✅ Saved: {out_path}", file=sys.stderr)

