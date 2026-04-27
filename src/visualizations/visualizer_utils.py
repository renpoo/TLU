import os, sys, argparse
import pandas as pd
import japanize_matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import json

try:
    import japanize_matplotlib
    # Ensure explicit 'family': 'monospace' properties also support Japanese characters
    plt.rcParams['font.monospace'] = ['IPAexGothic'] + plt.rcParams['font.monospace']
except ImportError:
    plt.rcParams['font.family'] = ['Noto Sans CJK JP', 'Hiragino Sans', 'YuGothic', 'sans-serif']
    plt.rcParams['font.monospace'] = ['Noto Sans CJK JP', 'Hiragino Sans'] + plt.rcParams['font.monospace']

def get_base_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--out_dir", type=str, default="workspace/output_plots/")
    parser.add_argument("--filename", type=str, default=None)
    # Default theme is 'dark' (only starting point based on user agreement)
    parser.add_argument("--theme", type=str, default='dark')
    parser.add_argument("--node_map", type=str, default="_node_map.csv")
    parser.add_argument("--time_map", type=str, default="_time_map.csv")
    parser.add_argument("--max_legend", type=int, default=25)
    parser.add_argument("--interactive", action="store_true", help="Keep the plot window open for interactive inspection")
    
    # Load thresholds from sys_params and inject them as parser arguments
    try:
        from src.filters.cli_parser import load_sys_params
        env_dir = os.environ.get("TARGET_ENV", "workspace")
        sys_params = load_sys_params(f"{env_dir}/config/_sys_params.csv")
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
    """!
    @brief Apply the UI visual theme JSON settings configuring Matplotlib globally.
    @details Implements Fail-Fast execution crashing immediately upon failure locating or parsing theme limits.

    @param theme_name Keyword identifier dictating the target base style bounds.

    @return Extracted parameter JSON dictionary configuring the target layout colors natively.

    @pre
        - Target `theme_name` JSON identically mapped on disk.
    @post
        - Implicitly transforms the Pyplot state system fully enforcing global attributes unconditionally.
    @invariant
        - Generates consistent graphical themes irrespective of previous rendering commands.
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
    
    # Expand graph margins globally so lines don't overlap with legends
    plt.rcParams['axes.xmargin'] = 0.05
    plt.rcParams['axes.ymargin'] = 0.20

        
    return theme_cfg

def load_node_labels(node_map_path: str, max_n: int) -> dict:
    """!
    @brief Extract formatted topological identifier string mappings safely.
    @details Implements strict logical boundaries enforcing fail-fast execution bypassing silently generated parameters explicitly.

    @param node_map_path Local relative file extraction map.
    @param max_n Strict dimensional limits structurally formatting iterations.

    @return Extracted parameter mapped ID structure dictionary.

    @pre
        - Bounded layout `max_n` explicitly matching dataset size safely.
    @post
        - Fail-fast strictly crashes eliminating runtime variable fallbacks unconditionally on data exceptions.
    @invariant
        - Preserves index integer representations aligned identically to sequential matrix indices.
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
    """!
    @brief Extract formatted sequential temporal target identifier map structures securely.
    @details Exerts tight parameter bounds enforcing early failure states overriding silent string derivations universally.

    @param time_map_path Sequence temporal bounds mapping parameter limits.
    @param max_n System configuration parameter upper time bound sequences.

    @return Dictionary sequence resolving mapping limits correctly.

    @pre
        - File map target securely existing structurally natively.
    @post
        - Fail-fast aborts runtime configurations preventing string generation anomalies dynamically.
    @invariant
        - Temporal integer configurations bounds accurately reflecting original pipeline logic layouts.
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
    """!
    @brief [Pure Drawing Logic] Draws a single heatmap and applies decoration safely.
    @details Applies visual structure maps bounding configuration metrics isolating aesthetic constraints cleanly.
    """
    sns.heatmap(pivot_df, ax=ax, cmap=cmap, robust=True, 
                cbar_kws={'label': cbar_label}, 
                xticklabels=x_labels) # Fix: Always pass X-axis labels

    ax.set_title(title_text, fontsize=15, color=text_col, loc='left', fontweight='bold')
    ax.set_ylabel("Node (Dept/Account)", color=text_col, fontsize=12)
    ax.set_xlabel("Timeline", color=text_col, fontsize=12)

    # Adjust axis tick marks
    ax.tick_params(axis='x', rotation=90, colors=text_col, labelsize=10)
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
    """!
    @brief [Pure Drawing Logic] Draws an N x N correlation/lag matrix heatmap mapping visual metrics strictly.
    @details Renders pure target geometry formatting isolating variables independently.
    """
    import seaborn as sns
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

def save_plot(fig, out_dir: str, filename: str):
    os.makedirs(out_dir, exist_ok=True)
    base_name = os.path.splitext(filename)[0]
    out_path = os.path.join(out_dir, f"{base_name}.png")
    fig.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f"✅ Saved: {out_path}", file=sys.stderr)
    
    # Intentionally freeze execution natively displaying GUI interactively
    if '--interactive' in sys.argv:
        plt.show()


def apply_smart_x_labels(ax, x_values, x_labels, text_col, max_labels=15):
    if len(x_values) == 0: return
    step = max(1, len(x_values) // max_labels)
    ax.set_xticks(x_values[::step])
    ax.set_xticklabels(x_labels[::step], rotation=90, color=text_col, ha='center', fontsize=10)
