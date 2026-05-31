#!/usr/bin/env python3
import sys
import json
import os
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    import japanize_matplotlib
except ImportError:
    plt.rcParams['font.family'] = ['AppleGothic', 'Hiragino Sans', 'Hiragino Maru Gothic Pro', 'Noto Sans CJK JP', 'YuGothic', 'sans-serif']


def draw_bs_block_chart(report, out_path, max_y=None, fixed_assets_order=None, fixed_liabs_order=None, t_idx=None, top_k=8, time_labels=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Use fixed order if provided, otherwise calculate dynamically
    if fixed_assets_order and fixed_liabs_order:
        assets_dict = {item[0]: item[2] for item in report['bs_items'] if 'Asset' in item[1]}
        liabs_dict = {item[0]: item[2] for item in report['bs_items'] if 'Liability' in item[1] or 'Equity' in item[1]}
        
        assets = []
        for acc in fixed_assets_order:
            if acc == "ACC_Others":
                other_val = sum([v for k, v in assets_dict.items() if k not in fixed_assets_order])
                assets.append((acc, "Asset", other_val))
            else:
                assets.append((acc, "Asset", assets_dict.get(acc, 0)))
                
        liabs = []
        for acc in fixed_liabs_order:
            if acc == "ACC_Others":
                other_val = sum([v for k, v in liabs_dict.items() if k not in fixed_liabs_order])
                liabs.append((acc, "Liability", other_val))
            else:
                liabs.append((acc, "Liability", liabs_dict.get(acc, 0)))
    else:
        assets = [item for item in report['bs_items'] if 'Asset' in item[1]]
        liabs = [item for item in report['bs_items'] if 'Liability' in item[1] or 'Equity' in item[1]]
        MAX_ITEMS = top_k
        if MAX_ITEMS > 0:
            assets.sort(key=lambda x: x[2], reverse=True)
            if len(assets) > MAX_ITEMS:
                assets = assets[:MAX_ITEMS] + [("ACC_Others", "Asset", sum([x[2] for x in assets[MAX_ITEMS:]]))]
            liabs.sort(key=lambda x: x[2], reverse=True)
            if len(liabs) > MAX_ITEMS:
                liabs = liabs[:MAX_ITEMS] + [("ACC_Others", "Liability", sum([x[2] for x in liabs[MAX_ITEMS:]]))]
        else:
            assets.sort(key=lambda x: x[2], reverse=True)
            liabs.sort(key=lambda x: x[2], reverse=True)
            
    bottom_left = 0
    for acc, cat, bal in assets:
        val = max(0, bal)
        if val > 0:
            ax.bar('Assets', val, bottom=bottom_left, label=acc.replace('ACC_', ''))
            ax.text(0, bottom_left + val/2, f"{val:,.0f}", ha='center', va='center', color='white', fontweight='bold', fontsize=9)
            bottom_left += val
        
    bottom_right = 0
    for acc, cat, bal in liabs:
        val = max(0, bal)
        if val > 0:
            ax.bar('Liabilities & Equity', val, bottom=bottom_right, label=acc.replace('ACC_', ''))
            ax.text(1, bottom_right + val/2, f"{val:,.0f}", ha='center', va='center', color='white', fontweight='bold', fontsize=9)
            bottom_right += val
        
    net_inc = report['net_income']
    if net_inc > 0:
        label = 'Net Income (Retained Earnings)'
        ax.bar('Liabilities & Equity', net_inc, bottom=bottom_right, label=label)
        ax.text(1, bottom_right + net_inc/2, f"{net_inc:,.0f}", ha='center', va='center', color='white', fontweight='bold', fontsize=9)
        bottom_right += net_inc
    elif net_inc < 0:
        label = 'Net Loss (Deficit)'
        loss_val = -net_inc
        ax.bar('Assets', loss_val, bottom=bottom_left, label=label, color='tab:red', alpha=0.7, hatch='//')
        ax.text(0, bottom_left + loss_val/2, f"{loss_val:,.0f}", ha='center', va='center', color='white', fontweight='bold', fontsize=9)
        bottom_left += loss_val
        
    if max_y is not None:
        ax.set_ylim(0, max(max_y, 1) * 1.1)

    ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5), fontsize=8)
    title_str = f"Balance Sheet (Block Chart): {report['week']}"
    if t_idx is not None:
        current_time_label = time_labels.get(t_idx, report['week']) if (time_labels and t_idx in time_labels) else report['week']
        title_str = f"Balance Sheet (Block Chart)\nTimeline: {current_time_label} (t_idx={t_idx})"
    ax.set_title(title_str)
    plt.subplots_adjust(left=0.1, right=0.7, top=0.9, bottom=0.1)
    plt.savefig(out_path, dpi=150)

    print("✅ " + out_path)

    plt.close()

def draw_pl_waterfall(report, out_path, min_y=None, max_y=None, fixed_expenses_order=None, t_idx=None, top_k=8, time_labels=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    labels = ['Revenue']
    values = [report['revenue']]
    
    if fixed_expenses_order:
        exp_dict = {item[0]: item[2] for item in report['pl_items'] if item[1] == 'Expense'}
        expenses = []
        for acc in fixed_expenses_order:
            if acc == "ACC_Others":
                other_val = sum([v for k, v in exp_dict.items() if k not in fixed_expenses_order])
                expenses.append((acc, "Expense", other_val))
            else:
                expenses.append((acc, "Expense", exp_dict.get(acc, 0)))
    else:
        expenses = [item for item in report['pl_items'] if item[1] == 'Expense']
        expenses.sort(key=lambda x: x[2], reverse=True)
        MAX_EXP = top_k
        if MAX_EXP > 0:
            if len(expenses) > MAX_EXP:
                expenses = expenses[:MAX_EXP] + [("ACC_Others", "Expense", sum([x[2] for x in expenses[MAX_EXP:]]))]

    for acc, cat, bal in expenses:
        labels.append(str(acc).replace('ACC_', ''))
        values.append(-bal)
        
    labels.append('Net Income')
    values.append(report['net_income'])
    
    cumulative = np.cumsum([values[0]] + values[1:-1])
    bottoms = [0] + list(cumulative[:-1]) + [0]
    
    # Dynamic coloring for each distinct expense category
    cmap = plt.get_cmap('tab10')
    colors = ['#2ecc71']
    for idx, (acc, _, _) in enumerate(expenses):
        if fixed_expenses_order:
            color_idx = fixed_expenses_order.index(acc) if acc in fixed_expenses_order else idx
        else:
            color_idx = idx
        colors.append(cmap(color_idx % 10))
    colors.append('#3498db')
    
    ax.bar(labels, values, bottom=bottoms, color=colors)
    ax.axhline(0, color='black', linewidth=1)
    
    for i, v in enumerate(values):
        ax.text(i, bottoms[i] + v/2, f"{v:,.0f}", ha='center', va='center', color='white', fontweight='bold', fontsize=8)
        
    if min_y is not None and max_y is not None:
        range_y = max_y - min_y
        range_y = max(abs(max_y), 1) if range_y == 0 else range_y
        ax.set_ylim(min_y - range_y * 0.1, max_y + range_y * 0.1)

    title_str = f"Monthly Profit and Loss Flow (Waterfall): {report['week']}"
    if t_idx is not None:
        current_time_label = time_labels.get(t_idx, report['week']) if (time_labels and t_idx in time_labels) else report['week']
        title_str = f"Monthly Profit and Loss Flow (Waterfall)\nTimeline: {current_time_label} (t_idx={t_idx})"
    ax.set_title(title_str)
    ax.set_ylabel("Monthly Profit and Loss (Amount)")
    plt.xticks(rotation=90, ha='center', fontsize=8)
    plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.3) # Reserve more bottom space for vertical labels
    plt.savefig(out_path, dpi=150) # Removed bbox_inches='tight'

    print("✅ " + out_path)

    plt.close()

def draw_pl_trend(reports, out_path, fixed_expenses_order, time_labels=None):
    fig, ax = plt.subplots(figsize=(12, 6))
    weeks = [time_labels.get(i, r['week']) if (time_labels and i in time_labels) else r['week'] for i, r in enumerate(reports)]
    revenues = [r['revenue'] for r in reports]
    net_incomes = [r['net_income'] for r in reports]
    
    # Collect timeseries data for each expense category
    exp_data = {acc: [] for acc in fixed_expenses_order}
    for r in reports:
        exp_dict = {item[0]: item[2] for item in r['pl_items'] if item[1] == 'Expense'}
        for acc in fixed_expenses_order:
            if acc == "ACC_Others":
                val = sum([v for k, v in exp_dict.items() if k not in fixed_expenses_order])
            else:
                val = exp_dict.get(acc, 0)
            exp_data[acc].append(val)
            
    # Plot Revenue on positive side
    ax.bar(weeks, revenues, label='Revenue', color='#2ecc71', alpha=0.7)
    
    # Plot stacked Expenses on negative side
    bottom_neg = np.zeros(len(reports))
    cmap = plt.get_cmap('tab10')
    for idx, acc in enumerate(fixed_expenses_order):
        vals = np.array(exp_data[acc])
        if np.any(vals > 0):
            ax.bar(weeks, -vals, bottom=bottom_neg, label=acc.replace('ACC_', ''), color=cmap(idx % 10), alpha=0.85)
            bottom_neg -= vals
            
    # Overlay Net Income as line chart
    ax.plot(weeks, net_incomes, label='Net Income', color='#3498db', marker='o', linewidth=2)
    
    ax.axhline(0, color='black', linewidth=1)
    ax.set_title("Monthly Profit and Loss Trend Over Time (Revenue vs Expenses)")
    ax.set_ylabel("Monthly Profit and Loss (Amount)")
    ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5), fontsize=8)
    
    if len(weeks) > 20:
        step = len(weeks) // 20
        ax.set_xticks(np.arange(0, len(weeks), step))
        ax.set_xticklabels(weeks[::step], rotation=90, fontsize=8)
    else:
        plt.xticks(rotation=90, fontsize=8)
        
    plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.2)
    plt.savefig(out_path, dpi=150)
    print("✅ " + out_path)
    plt.close()

def draw_bs_trend(reports, out_path, fixed_assets_order, fixed_liabs_order, time_labels=None):
    fig, ax = plt.subplots(figsize=(12, 6))
    weeks = [time_labels.get(i, r['week']) if (time_labels and i in time_labels) else r['week'] for i, r in enumerate(reports)]
    
    # Collect timeseries data for each category
    asset_data = {acc: [] for acc in fixed_assets_order}
    liab_data = {acc: [] for acc in fixed_liabs_order}
    net_income_pos = [] # Red ink (net loss) on assets side
    net_income_neg = [] # Blue ink (net profit) on liabilities side
    
    for r in reports:
        # assets
        assets_dict = {item[0]: item[2] for item in r['bs_items'] if 'Asset' in item[1]}
        for acc in fixed_assets_order:
            if acc == "ACC_Others":
                val = sum([v for k, v in assets_dict.items() if k not in fixed_assets_order])
            else:
                val = assets_dict.get(acc, 0)
            asset_data[acc].append(max(0, val))
            
        # liabilities & equity
        liabs_dict = {item[0]: item[2] for item in r['bs_items'] if 'Liability' in item[1] or 'Equity' in item[1]}
        for acc in fixed_liabs_order:
            if acc == "ACC_Others":
                val = sum([v for k, v in liabs_dict.items() if k not in fixed_liabs_order])
            else:
                val = liabs_dict.get(acc, 0)
            liab_data[acc].append(max(0, val))
            
        # net income / loss allocation
        net_inc = r['net_income']
        if net_inc >= 0:
            net_income_neg.append(net_inc)
            net_income_pos.append(0)
        else:
            net_income_neg.append(0)
            net_income_pos.append(-net_inc)
            
    # Plot positive side (Assets)
    bottom_pos = np.zeros(len(reports))
    for acc in fixed_assets_order:
        vals = np.array(asset_data[acc])
        if np.any(vals > 0):
            ax.bar(weeks, vals, bottom=bottom_pos, label=acc.replace('ACC_', ''), alpha=0.85)
            bottom_pos += vals
            
    # Add Net Loss as asset overlay if any
    loss_vals = np.array(net_income_pos)
    if np.any(loss_vals > 0):
        ax.bar(weeks, loss_vals, bottom=bottom_pos, label='Net Loss', color='tab:red', alpha=0.7, hatch='//')
        bottom_pos += loss_vals
        
    # Plot negative side (Liabilities & Equity)
    bottom_neg = np.zeros(len(reports))
    for acc in fixed_liabs_order:
        vals = np.array(liab_data[acc])
        if np.any(vals > 0):
            ax.bar(weeks, -vals, bottom=bottom_neg, label=acc.replace('ACC_', ''), alpha=0.85)
            bottom_neg -= vals
            
    # Add Net Income on Liabilities/Equity side if any
    gain_vals = np.array(net_income_neg)
    if np.any(gain_vals > 0):
        ax.bar(weeks, -gain_vals, bottom=bottom_neg, label='Net Income', color='tab:blue', alpha=0.7)
        bottom_neg -= gain_vals
        
    ax.axhline(0, color='black', linewidth=1)
    ax.set_title("Balance Sheet Trend Over Time (Assets vs Liabilities & Equity)")
    ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5), fontsize=8)
    
    if len(weeks) > 20:
        step = len(weeks) // 20
        ax.set_xticks(np.arange(0, len(weeks), step))
        ax.set_xticklabels(weeks[::step], rotation=90, fontsize=8)
    else:
        plt.xticks(rotation=90, fontsize=8)
        
    max_val = max(np.max(bottom_pos), np.max(np.abs(bottom_neg)))
    if max_val == 0: max_val = 1
    ax.set_ylim(-max_val * 1.1, max_val * 1.1)
    
    plt.subplots_adjust(left=0.1, right=0.8, top=0.9, bottom=0.2)
    plt.savefig(out_path, dpi=150)
    print("✅ " + out_path)
    plt.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", required=True)
    parser.add_argument("--out_dir", required=True)
    parser.add_argument("--seq_dir", required=True)
    parser.add_argument("--top_k", type=int, default=8, help="Number of top accounts to display individually (0 or negative for all)")
    parser.add_argument("--theme", default="dark")
    parser.add_argument("--node_map", default="")
    parser.add_argument("--time_map", default="")
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    
    with open(args.json, 'r') as f:
        reports = json.load(f)
        
    if not reports:
        sys.exit(0)
        
    # Load time labels from time_map if provided
    time_labels = {}
    if args.time_map and os.path.exists(args.time_map):
        try:
            df_time = pd.read_csv(args.time_map)
            time_labels = dict(zip(df_time['t_idx'], df_time['time_label']))
        except Exception as e:
            print(f"[WARN] Failed to load time map from {args.time_map}: {e}", file=sys.stderr)

    # 1. Total Summary Images
    final_report = reports[-1]
    final_t_idx = len(reports) - 1
    
    # Pre-calculate Global Max/Min and Global Account Ordering for Animation Sequences
    global_max_bs = max([max(r['assets'], r['total_liab_eq']) for r in reports])
    global_max_pl = 0
    global_min_pl = 0
    
    # Track global sums to determine fixed ordering
    global_assets = {}
    global_liabs = {}
    global_expenses = {}
    
    for r in reports:
        # P/L bounds
        values = [r['revenue']]
        expenses = [item for item in r['pl_items'] if item[1] == 'Expense']
        for acc, cat, bal in expenses:
            values.append(-bal)
            global_expenses[acc] = global_expenses.get(acc, 0) + bal
        values.append(r['net_income'])
        
        cumulative = np.cumsum([values[0]] + values[1:-1])
        bottoms = [0] + list(cumulative[:-1]) + [0]
        peaks = [b + v for b, v in zip(bottoms, values)]
        
        global_max_pl = max(global_max_pl, max(peaks))
        global_min_pl = min(global_min_pl, min(peaks), min(bottoms))
        
        # B/S sums
        for acc, cat, bal in r['bs_items']:
            if 'Asset' in cat:
                global_assets[acc] = global_assets.get(acc, 0) + bal
            elif 'Liability' in cat or 'Equity' in cat:
                global_liabs[acc] = global_liabs.get(acc, 0) + bal

    # Determine Top K or all accounts for fixed animation axes
    def get_top_k(acc_dict, k=8):
        sorted_acc = sorted(acc_dict.items(), key=lambda x: x[1], reverse=True)
        if k <= 0 or k >= len(sorted_acc):
            return [x[0] for x in sorted_acc]
        top = [x[0] for x in sorted_acc[:k]]
        if len(sorted_acc) > k: top.append("ACC_Others")
        return top

    fixed_assets = get_top_k(global_assets, args.top_k)
    fixed_liabs = get_top_k(global_liabs, args.top_k)
    fixed_expenses = get_top_k(global_expenses, args.top_k)

    draw_bs_block_chart(final_report, os.path.join(args.out_dir, "000_0_1__BS_Block_Total_Periodic.png"),
                        fixed_assets_order=fixed_assets, fixed_liabs_order=fixed_liabs, t_idx=final_t_idx, top_k=args.top_k, time_labels=time_labels)
    draw_pl_waterfall(final_report, os.path.join(args.out_dir, "000_0_1__PL_Waterfall_Total_Periodic.png"),
                      fixed_expenses_order=fixed_expenses, t_idx=final_t_idx, top_k=args.top_k, time_labels=time_labels)

    # Generate B/S Trend Image
    draw_bs_trend(reports, os.path.join(args.out_dir, "000_0_1__BS_Trend_Periodic.png"), fixed_assets, fixed_liabs, time_labels=time_labels)

    # Generate P/L Trend Image
    draw_pl_trend(reports, os.path.join(args.out_dir, "000_0_1__PL_Trend_Periodic.png"), fixed_expenses, time_labels=time_labels)

    # 2. Individual Sequence Images (for every time step)
    seq_dir = args.seq_dir
    
    for i, r in enumerate(reports):
        # Format index to have leading zeros for sorting
        idx_str = f"{i:03d}"
        week_str = str(r['week']).replace('/', '_')
        out_path = os.path.join(seq_dir, f"BS_Block_{idx_str}_{week_str}_Periodic.png")
        draw_bs_block_chart(r, out_path, 
                            max_y=global_max_bs, fixed_assets_order=fixed_assets, fixed_liabs_order=fixed_liabs, t_idx=i, time_labels=time_labels)

        print("✅ " + out_path)

    for i, r in enumerate(reports):
        # Format index to have leading zeros for sorting
        idx_str = f"{i:03d}"
        week_str = str(r['week']).replace('/', '_')
        out_path = os.path.join(seq_dir, f"PL_Waterfall_{idx_str}_{week_str}_Periodic.png")
        draw_pl_waterfall(r, out_path, 
                          min_y=global_min_pl, max_y=global_max_pl, fixed_expenses_order=fixed_expenses, t_idx=i, time_labels=time_labels)

        print("✅ " + out_path)
    
if __name__ == "__main__":
    main()
