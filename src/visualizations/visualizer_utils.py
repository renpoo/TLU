import os, sys, argparse
import pandas as pd
import japanize_matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import json

try:
    import japanize_matplotlib
    plt.rcParams['font.monospace'] = ['IPAexGothic'] + plt.rcParams['font.monospace']
except ImportError:
    plt.rcParams['font.family'] = ['AppleGothic', 'Hiragino Sans', 'Hiragino Maru Gothic Pro', 'Noto Sans CJK JP', 'YuGothic', 'sans-serif']
    plt.rcParams['font.monospace'] = ['AppleGothic', 'Hiragino Sans', 'Noto Sans CJK JP'] + plt.rcParams['font.monospace']

def get_base_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--out_dir", type=str, default="workspace/readme_plots/")
    parser.add_argument("--filename", type=str, default=None)
    parser.add_argument("--theme", type=str, default='dark')
    parser.add_argument("--node_map", type=str, default="_node_map.csv")
    parser.add_argument("--time_map", type=str, default="_time_map.csv")
    parser.add_argument("--max_legend", type=int, default=25)
    parser.add_argument("--interactive", action="store_true", help="Keep the plot window open for interactive inspection")
    
    try:
        from src.filters.cli_parser import load_sys_params
        env_dir = os.environ.get("TARGET_ENV", "workspace")
        sys_params_path = os.environ.get("TLU_SYS_PARAMS", f"{env_dir}/config/_sys_params.csv")
        sys_params = load_sys_params(sys_params_path)
        parser.add_argument("--thresh_z_score", type=float, default=sys_params.get("thresh_z_score", 3.0))
        parser.add_argument("--thresh_spectral_radius", type=float, default=sys_params.get("thresh_spectral_radius", 0.95))
        parser.add_argument("--thresh_fractal_lower", type=float, default=sys_params.get("thresh_fractal_lower", 0.5))
        parser.add_argument("--thresh_fractal_upper", type=float, default=sys_params.get("thresh_fractal_upper", 1.5))
    except ImportError:
        parser.add_argument("--thresh_z_score", type=float, default=3.0)
        parser.add_argument("--thresh_spectral_radius", type=float, default=0.95)
        parser.add_argument("--thresh_fractal_lower", type=float, default=0.5)
        parser.add_argument("--thresh_fractal_upper", type=float, default=1.5)

    return parser

def apply_theme(theme_name="dark"):
    json_path = f"src/visualizations/themes/theme_{theme_name}.json"
    
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"❌ Theme configuration file not found: {json_path}")
        
    with open(json_path, 'r', encoding='utf-8') as f:
        theme_cfg = json.load(f)

    mode = theme_cfg["mode"]
    plt.style.use('dark_background' if mode == 'dark' else 'default')
    plt.rcParams['savefig.format'] = 'png'
    
    plt.rcParams['axes.xmargin'] = 0.05
    plt.rcParams['axes.ymargin'] = 0.20

    return theme_cfg

def load_node_labels(node_map_path: str, max_n: int) -> dict:
    if not os.path.exists(node_map_path):
        raise FileNotFoundError(f"❌ Node map file not found: {node_map_path}")
        
    idx_to_label = {i: f"Node_{i:02d}" for i in range(max_n)}
    try:
        df = pd.read_csv(node_map_path)
        for _, row in df.iterrows():
            idx = int(row['node_idx'])
            if idx < max_n: 
                idx_to_label[idx] = f"{idx:02d}_{row['node_label']}"
    except Exception: 
        raise FileNotFoundError(f"❌ Node map file not found: {node_map_path}")

    return idx_to_label

def load_time_labels(time_map_path: str, max_n: int) -> dict:
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
    sns.heatmap(pivot_df, ax=ax, cmap=cmap, robust=True, 
                cbar_kws={'label': cbar_label}, 
                xticklabels=x_labels)

    ax.set_title(title_text, fontsize=15, color=text_col, loc='left', fontweight='bold')
    ax.set_ylabel("Node (Dept/Account)", color=text_col, fontsize=12)
    ax.set_xlabel("Timeline", color=text_col, fontsize=12)

    ax.tick_params(axis='x', rotation=90, colors=text_col, labelsize=10)
    ax.set_yticklabels(y_labels, fontsize=10, rotation=0)

    for i, label in enumerate(ax.get_yticklabels()):
        if i in top_k_idx:
            label.set_color(outlier_col)
            label.set_fontweight('bold')
        else:
            label.set_color(text_col)
            label.set_alpha(0.8)

    return

def draw_matrix_heatmap(ax, pivot_df, cmap, cbar_label, title_text, axis_labels, text_col, bg_col=None, mask=None, vmin=None, vmax=None):
    sns.heatmap(pivot_df, ax=ax, cmap=cmap, mask=mask, vmin=vmin, vmax=vmax,
                xticklabels=axis_labels, yticklabels=axis_labels, 
                cbar_kws={'label': cbar_label})
                
    ax.set_title(title_text, fontsize=16, color=text_col, pad=20, fontweight='bold')
    ax.set_xlabel("Target Node (Effect)", color=text_col, fontsize=12)
    ax.set_ylabel("Source Node (Cause)", color=text_col, fontsize=12)

    ax.tick_params(axis='x', rotation=90, colors=text_col)
    ax.tick_params(axis='y', rotation=0, colors=text_col)
    
    if bg_col:
        ax.set_facecolor(bg_col)

    return

def render_node_map_legend(
    ax, 
    idx_to_label: dict, 
    highlight_indices: list = None, 
    max_legend: int = 25, 
    theme_cfg: dict = None
):
    """!
    @brief Render a standardized right-side legend table mapping Node Index to Node Name.
    """
    import matplotlib.patches as mpatches
    
    if highlight_indices is None:
        highlight_indices = []
        
    text_col = theme_cfg['ui_canvas']['text_primary'] if theme_cfg else '#FFFFFF'
    legend_bg_col = theme_cfg['ui_canvas']['legend_bg'] if theme_cfg else '#1E1E1E'
    legend_edge_col = theme_cfg['ui_canvas']['legend_edge'] if theme_cfg else '#333333'
    c_outlier_text = theme_cfg['forensics']['colors']['anomaly_outlier'] if theme_cfg else '#FF4444'

    N = len(idx_to_label)
    handles = []
    labels = []
    display_count = min(N, max_legend)
    
    for i in range(display_count):
        label_str = idx_to_label.get(i, f"Node_{i}")
        handles.append(mpatches.Patch(color='none'))
        labels.append(f"{i:02d} : {label_str}")
        
    if N > max_legend:
        handles.append(mpatches.Patch(color='none'))
        labels.append(f"... and {N - max_legend} more nodes")

    leg = ax.legend(
        handles, labels, 
        title="Node Map (Index -> Name):\n" + "-"*28,
        loc='center left', bbox_to_anchor=(1.02, 0.5),
        facecolor=legend_bg_col, edgecolor=legend_edge_col,
        handlelength=0, handletextpad=0, 
        prop={'family': 'monospace', 'size': 10}
    )
                    
    plt.setp(leg.get_title(), color=text_col, family='monospace')

    for text_obj in leg.get_texts():
        text_str = text_obj.get_text()
        if ":" in text_str:
            idx_str = text_str.split(":")[0].strip()
            if idx_str.isdigit() and int(idx_str) in highlight_indices:
                text_obj.set_color(c_outlier_text)
                text_obj.set_fontweight('bold')
            else:
                text_obj.set_color(text_col)
        else:
            text_obj.set_color(text_col)
            
    return leg

def save_plot(fig, out_dir: str, filename: str):
    import time
    os.makedirs(out_dir, exist_ok=True)
    base_name = os.path.splitext(filename)[0]
    out_path = os.path.join(out_dir, f"{base_name}.png")
    fig.tight_layout()
    
    max_retries = 5
    for attempt in range(max_retries):
        try:
            fig.savefig(out_path, dpi=150)
            print(f"✅ Saved: {out_path}", file=sys.stderr)
            break
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"[WARN] Failed to save {out_path}. Retrying in 0.5s... (Attempt {attempt+1}/{max_retries}): {e}", file=sys.stderr)
                time.sleep(0.5)
                os.makedirs(out_dir, exist_ok=True)
            else:
                print(f"[ERROR] Hard failure saving {out_path}: {e}", file=sys.stderr)
                raise e
    
    if '--interactive' in sys.argv:
        plt.show()

def apply_smart_x_labels(ax, x_values, x_labels, text_col, max_labels=15):
    if len(x_values) == 0: return
    step = max(1, len(x_values) // max_labels)
    ax.set_xticks(x_values[::step])
    ax.set_xticklabels(x_labels[::step], rotation=90, color=text_col, ha='center', fontsize=10)
