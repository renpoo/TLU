#!/usr/bin/env python3
import sys
import json
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

def draw_bs_block_chart(report, out_path, max_y=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # report['bs_items'] is a dict: { Custom_Label: [[acc, cat, bal], ...] }
    assets = []
    liabs = []
    for label, items in report['bs_items'].items():
        for acc, cat, bal in items:
            if 'Asset' in cat:
                assets.append((f"{label}-{acc}", bal))
            elif 'Liability' in cat or 'Equity' in cat:
                liabs.append((f"{label}-{acc}", bal))
    
    bottom_left = 0
    for name, bal in assets:
        val = max(0, bal)
        if val > 0:
            ax.bar('Assets', val, bottom=bottom_left, label=name)
            bottom_left += val
            
    bottom_right = 0
    for name, bal in liabs:
        val = max(0, bal)
        if val > 0:
            ax.bar('Liabilities & Equity', val, bottom=bottom_right, label=name)
            bottom_right += val
            
    eq_val = max(0, report['equity'] + report['net_income'])
    if eq_val > 0:
        ax.bar('Liabilities & Equity', eq_val, bottom=bottom_right, label='Equity (Retained Earnings)')
        
    if max_y is not None:
        ax.set_ylim(0, max_y * 1.1)

    # Put legend outside
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize='small')
    ax.set_title(f"Hybrid B/S (State): {report['week']}")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()

def draw_pl_waterfall(report, out_path, min_y=None, max_y=None):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    labels = ['Revenue']
    values = [report['revenue']]
    
    for label, items in report['pl_items'].items():
        for acc, cat, bal in items:
            if 'Expense' in cat:
                labels.append(f"{label}-{acc}")
                values.append(-bal)
                
    labels.append('Net Income')
    values.append(report['net_income'])
    
    labels.append('UNKNOWN_LEAK')
    values.append(report['unknown_leak'])
    
    cumulative = np.cumsum([values[0]] + values[1:-2]) # Exclude Net Income and Leak from cumsum
    bottoms = [0] + list(cumulative[:-1]) + [0, 0] # Net Income and Leak start from 0
    
    colors = ['#2ecc71'] + ['#e74c3c']*(len(values)-3) + ['#3498db', '#f39c12']
    
    ax.bar(labels, values, bottom=bottoms, color=colors)
    ax.axhline(0, color='black', linewidth=1)
    
    if min_y is not None and max_y is not None:
        range_y = max_y - min_y
        if range_y == 0: range_y = max(abs(max_y), 1)
        ax.set_ylim(min_y - range_y*0.1, max_y + range_y*0.1)

    ax.set_title(f"Hybrid P/L (Flux & Leak): {report['week']}")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()

def draw_trend(reports, out_path):
    fig, ax = plt.subplots(figsize=(12, 6))
    weeks = [r['week'] for r in reports]
    revenues = [r['revenue'] for r in reports]
    expenses = [-r['expense'] for r in reports]
    net_incomes = [r['net_income'] for r in reports]
    leaks = [r['unknown_leak'] for r in reports]
    
    ax.bar(weeks, revenues, label='Revenue', color='#2ecc71', alpha=0.5)
    ax.bar(weeks, expenses, label='Expense', color='#e74c3c', alpha=0.5)
    ax.plot(weeks, net_incomes, label='Net Income', color='#3498db', marker='o', linewidth=2)
    ax.plot(weeks, leaks, label='UNKNOWN_LEAK', color='#f39c12', linestyle='--', linewidth=2)
    
    ax.axhline(0, color='black', linewidth=1)
    ax.set_title("P/L and Leak Trend Over Time")
    ax.legend()
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
    with open(args.json, 'r') as f: reports = json.load(f)
    if not reports: sys.exit(0)
        
    final_report = reports[-1]
    draw_bs_block_chart(final_report, os.path.join(args.out_dir, "000_0_1__BS_Block_Total.png"))
    draw_pl_waterfall(final_report, os.path.join(args.out_dir, "000_0_1__PL_Waterfall_Total.png"))
    draw_trend(reports, os.path.join(args.out_dir, "000_0_1__PL_Trend.png"))

if __name__ == "__main__":
    main()
