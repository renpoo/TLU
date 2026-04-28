#!/usr/bin/env python3
import sys
import json
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

def draw_bs_block_chart(report, out_path, max_y=None):
    fig, ax = plt.subplots(figsize=(8, 6))
    
    assets = [item for item in report['bs_items'] if 'Asset' in item[1]]
    liabs = [item for item in report['bs_items'] if 'Liability' in item[1] or 'Equity' in item[1]]
    
    bottom_left = 0
    for acc, cat, bal in assets:
        val = max(0, bal) # Clip negative for stacked bar
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
        
    eq_val = max(0, report['equity'] + report['net_income'])
    if eq_val > 0:
        ax.bar('Liabilities & Equity', eq_val, bottom=bottom_right, label='Equity (Retained Earnings)')
        ax.text(1, bottom_right + eq_val/2, f"{eq_val:,.0f}", ha='center', va='center', color='white', fontweight='bold', fontsize=9)
    
    if max_y is not None:
        ax.set_ylim(0, max_y * 1.1)

    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    ax.set_title(f"Balance Sheet (Block Chart): {report['week']}")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()

def draw_pl_waterfall(report, out_path, min_y=None, max_y=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    labels = ['Revenue']
    values = [report['revenue']]
    
    expenses = [item for item in report['pl_items'] if item[1] == 'Expense']
    for acc, cat, bal in expenses:
        labels.append(acc.replace('ACC_', ''))
        values.append(-bal)
        
    labels.append('Net Income')
    values.append(report['net_income'])
    
    cumulative = np.cumsum([values[0]] + values[1:-1])
    bottoms = [0] + list(cumulative[:-1]) + [0]
    
    colors = ['#2ecc71'] + ['#e74c3c']*(len(expenses)) + ['#3498db']
    
    ax.bar(labels, values, bottom=bottoms, color=colors)
    ax.axhline(0, color='black', linewidth=1)
    
    for i, v in enumerate(values):
        ax.text(i, bottoms[i] + v/2, f"{v:,.0f}", ha='center', va='center', color='white', fontweight='bold', fontsize=8)
        
    if min_y is not None and max_y is not None:
        # Give 10% padding
        range_y = max_y - min_y
        if range_y == 0:
            range_y = max(abs(max_y), 1)
        ax.set_ylim(min_y - range_y * 0.1, max_y + range_y * 0.1)

    ax.set_title(f"Profit & Loss (Waterfall): {report['week']}")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()

def draw_pl_trend(reports, out_path):
    fig, ax = plt.subplots(figsize=(12, 6))
    weeks = [r['week'] for r in reports]
    revenues = [r['revenue'] for r in reports]
    expenses = [-r['expense'] for r in reports]
    net_incomes = [r['net_income'] for r in reports]
    
    ax.bar(weeks, revenues, label='Revenue', color='#2ecc71', alpha=0.7)
    ax.bar(weeks, expenses, label='Expense', color='#e74c3c', alpha=0.7)
    ax.plot(weeks, net_incomes, label='Net Income', color='#3498db', marker='o', linewidth=2)
    
    ax.axhline(0, color='black', linewidth=1)
    ax.set_title("Profit & Loss Trend Over Time")
    ax.legend()
    
    if len(weeks) > 20:
        step = len(weeks) // 20
        ax.set_xticks(np.arange(0, len(weeks), step))
        ax.set_xticklabels(weeks[::step], rotation=90)
    else:
        plt.xticks(rotation=90)
        
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", required=True)
    parser.add_argument("--out_dir", required=True)
    parser.add_argument("--seq_dir", required=True)
    args = parser.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)
    
    with open(args.json, 'r') as f:
        reports = json.load(f)
        
    if not reports:
        sys.exit(0)
        
    # 1. Total Summary Images
    final_report = reports[-1]
    draw_bs_block_chart(final_report, os.path.join(args.out_dir, "000_0_1__BS_Block_Total.png"))
    draw_pl_waterfall(final_report, os.path.join(args.out_dir, "000_0_1__PL_Waterfall_Total.png"))
    draw_pl_trend(reports, os.path.join(args.out_dir, "000_0_1__PL_Trend.png"))
    
    # Pre-calculate Global Max/Min for Animation Sequences
    global_max_assets = max([r['assets'] for r in reports])
    global_max_pl = 0
    global_min_pl = 0
    
    for r in reports:
        # P/L peak heights can be measured by looking at cumsums of the waterfall
        values = [r['revenue']]
        expenses = [item for item in r['pl_items'] if item[1] == 'Expense']
        for acc, cat, bal in expenses:
            values.append(-bal)
        values.append(r['net_income'])
        
        cumulative = np.cumsum([values[0]] + values[1:-1])
        bottoms = [0] + list(cumulative[:-1]) + [0]
        peaks = [b + v for b, v in zip(bottoms, values)]
        
        global_max_pl = max(global_max_pl, max(peaks))
        global_min_pl = min(global_min_pl, min(peaks), min(bottoms))

    # 2. Individual Sequence Images (for every time step)
    seq_dir = args.seq_dir
    
    for i, r in enumerate(reports):
        # Format index to have leading zeros for sorting
        idx_str = f"{i:03d}"
        draw_bs_block_chart(r, os.path.join(seq_dir, f"BS_Block_{idx_str}_{r['week']}.png"), max_y=global_max_assets)
        draw_pl_waterfall(r, os.path.join(seq_dir, f"PL_Waterfall_{idx_str}_{r['week']}.png"), min_y=global_min_pl, max_y=global_max_pl)

if __name__ == "__main__":
    main()
