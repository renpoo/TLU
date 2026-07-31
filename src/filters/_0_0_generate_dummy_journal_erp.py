#!/usr/bin/env python3
# ==========================================
# generate_dummy_journal_erp.py
# TLU System: Utility & Simulation Layer (Scratch Extension)
# Category: Clean ERP-Level Journal Generator with Dynamic Data-Driven T-ABC
# Version: 3.0 (Dynamic Volatility-Driven Entropy Dissipation Model)
# ==========================================

import sys
import csv
import argparse
import random
import datetime
import numpy as np
from collections import defaultdict

def setup_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="TLU Clean ERP Journal Generator with Dynamic Data-Driven T-ABC Allocation"
    )
    parser.add_argument("--months", type=int, default=12, help="Period to generate (in months)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument(
        "--allocation-mode",
        type=str,
        choices=["none", "traditional", "abc", "tabc"],
        default="tabc",
        help="Cost allocation mode: 'none', 'traditional' (labor-hours), 'abc' (activity-driven), or 'tabc' (dynamic entropy-driven T-ABC)"
    )
    parser.add_argument("--out-initial-state", type=str, default="", help="Path to write the initial state (Day 0) CSV")
    return parser

def create_entry(entry_id: str, date_str: str, amount: float, debit_acc: str, debit_dept: str, credit_acc: str, credit_dept: str, memo: str) -> list:
    """Generate one double-entry bookkeeping transaction (2 rows)."""
    amount = round(amount, 2)
    entry = []
    # Credit (Source of funds/resource outflow)
    entry.append([entry_id, date_str, credit_acc, credit_dept, "0.0", str(amount), f"{memo}_CR"])
    # Debit (Destination of funds/resource inflow)
    entry.append([entry_id, date_str, debit_acc, debit_dept, str(amount), "0.0", f"{memo}_DR"])
    return entry

def generate_stream(args):
    start_date = datetime.date(2020, 1, 1)
    total_days = args.months * 30 
    
    global_entry_count = 1
    event_queue = defaultdict(list)
    
    writer = csv.writer(sys.stdout)
    writer.writerow(["Entry_ID", "Trans_Date", "Account_Name", "Dept_Name", "Debit", "Credit", "Memo"])

    # Define initial opening balances
    balances = {
        "Cash": 1000000.00,
        "Raw_Materials": 500000.00,
        "Work_In_Process": 0.0,
        "Finished_Goods": 500000.00,
        "Equity_Capital": 2000000.00,
        "Accounts_Receivable": 0.0,
        "Accounts_Payable": 0.0,
        "Sales_Revenue": 0.0,
        "COGS": 0.0,
        "Direct_Labor_Exp": 0.0,
        "Mfg_Overhead_Exp": 0.0,
        "Mfg_Overhead_Allocated": 0.0,
        "Travel_Exp": 0.0,
        "Payroll_Exp": 0.0,
        "Rent_Exp": 0.0
    }

    if args.out_initial_state:
        with open(args.out_initial_state, "w", encoding="utf-8") as f:
            state_writer = csv.writer(f, lineterminator='\n')
            state_writer.writerow(["node_label", "initial_X"])
            for acc, val in balances.items():
                if val > 0:
                    state_writer.writerow([f"ACC_{acc}", f"{val:.2f}"])

    def attempt_entry(entry_id, date_str, amount, debit_acc, debit_dept, credit_acc, credit_dept, memo):
        nonlocal balances
        amount = round(amount, 2)
        
        # Enforce mass conservation on internal physical assets
        if credit_acc in ["Cash", "Accounts_Receivable", "Raw_Materials", "Work_In_Process", "Finished_Goods"]:
            if balances[credit_acc] < amount:
                amount = max(0.0, balances[credit_acc])
        
        if amount <= 0:
            return [], 0.0

        balances[credit_acc] -= amount
        balances[debit_acc] += amount

        entry = create_entry(entry_id, date_str, amount, debit_acc, debit_dept, credit_acc, credit_dept, memo)
        return entry, amount

    # Seasonal fluctuation wave for sales
    seasonal_wave = (np.sin(np.linspace(0, 4 * np.pi, total_days)) + 1) / 2

    # Monthly driver trackers for cost allocation & daily activity logs for dynamic volatility calculation
    monthly_drivers = {
        "DPT_Prod_A": {"labor_hours": 0.0, "machine_hours": 0.0, "setup_counts": 0, "inspection_counts": 0},
        "DPT_Prod_B": {"labor_hours": 0.0, "machine_hours": 0.0, "setup_counts": 0, "inspection_counts": 0}
    }
    daily_activity_series = [] # Stores daily total activity effort for dynamic CV calculation
    monthly_overhead_pool = 0.0

    for day in range(total_days):
        current_date = start_date + datetime.timedelta(days=day)
        date_str = current_date.strftime("%Y-%m-%d")
        daily_entries = []
        daily_total_activity_effort = 0.0

        # --------------------------------------------------
        # 1. Process event queue (future AR collections / AP payments)
        # --------------------------------------------------
        if day in event_queue:
            for task in event_queue[day]:
                entries, global_entry_count = task(date_str, global_entry_count)
                daily_entries.extend(entries)
            del event_queue[day]

        # --------------------------------------------------
        # 2. Manufacturing & ERP Production Cycle (Product A & Product B)
        # --------------------------------------------------
        # Product A: Mass-production (High volume, high labor-hours, low setups/inspections)
        # Product B: Custom/Specialty (Low volume, low labor-hours, high setups/inspections)
        
        # --- Production Batch Product A ---
        if random.random() < 0.7:
            mat_a = random.uniform(2000, 5000)
            labor_hrs_a = random.uniform(40, 80)
            machine_hrs_a = random.uniform(30, 60)
            setups_a = 1
            inspections_a = random.randint(1, 3)

            # Issue Raw Materials -> WIP Prod A
            entries, mat_exec = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, mat_a,
                "Work_In_Process", "DPT_Prod_A", "Raw_Materials", "DPT_Ops",
                f"Mat_Issue_Prod_A [Units:{mat_a/50:.1f}]"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1

            # Incur Direct Labor
            labor_cost_a = labor_hrs_a * 25.0 # $25/hr
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, labor_cost_a,
                "Work_In_Process", "DPT_Prod_A", "Cash", "DPT_Admin",
                f"Direct_Labor_Prod_A [Hours:{labor_hrs_a:.1f}]"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1

            # Track ERP drivers
            monthly_drivers["DPT_Prod_A"]["labor_hours"] += labor_hrs_a
            monthly_drivers["DPT_Prod_A"]["machine_hours"] += machine_hrs_a
            monthly_drivers["DPT_Prod_A"]["setup_counts"] += setups_a
            monthly_drivers["DPT_Prod_A"]["inspection_counts"] += inspections_a

            daily_total_activity_effort += (machine_hrs_a + setups_a * 10.0 + inspections_a * 5.0)

            # Completion of Goods -> Finished Goods A
            wip_to_fg_a = (mat_exec + labor_cost_a)
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, wip_to_fg_a,
                "Finished_Goods", "DPT_Prod_A", "Work_In_Process", "DPT_Prod_A",
                "FG_Completion_Prod_A"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1

        # --- Production Batch Product B ---
        if random.random() < 0.3:
            mat_b = random.uniform(800, 2000)
            labor_hrs_b = random.uniform(10, 25)
            machine_hrs_b = random.uniform(15, 35)
            setups_b = random.randint(4, 8)
            inspections_b = random.randint(8, 15)

            # Issue Raw Materials -> WIP Prod B
            entries, mat_exec_b = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, mat_b,
                "Work_In_Process", "DPT_Prod_B", "Raw_Materials", "DPT_Ops",
                f"Mat_Issue_Prod_B [Units:{mat_b/80:.1f}]"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1

            # Incur Direct Labor
            labor_cost_b = labor_hrs_b * 30.0 # $30/hr skilled
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, labor_cost_b,
                "Work_In_Process", "DPT_Prod_B", "Cash", "DPT_Admin",
                f"Direct_Labor_Prod_B [Hours:{labor_hrs_b:.1f}]"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1

            # Track ERP drivers
            monthly_drivers["DPT_Prod_B"]["labor_hours"] += labor_hrs_b
            monthly_drivers["DPT_Prod_B"]["machine_hours"] += machine_hrs_b
            monthly_drivers["DPT_Prod_B"]["setup_counts"] += setups_b
            monthly_drivers["DPT_Prod_B"]["inspection_counts"] += inspections_b

            daily_total_activity_effort += (machine_hrs_b + setups_b * 10.0 + inspections_b * 5.0)

            # Completion of Goods -> Finished Goods B
            wip_to_fg_b = (mat_exec_b + labor_cost_b)
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, wip_to_fg_b,
                "Finished_Goods", "DPT_Prod_B", "Work_In_Process", "DPT_Prod_B",
                "FG_Completion_Prod_B"
            )
            if entries: daily_entries.extend(entries); global_entry_count += 1

        daily_activity_series.append(daily_total_activity_effort)

        # --------------------------------------------------
        # 3. Daily Manufacturing Overhead Incurrence
        # --------------------------------------------------
        mfg_overhead_daily = random.uniform(500, 1500)
        entries, _ = attempt_entry(
            f"E_{global_entry_count:06d}", date_str, mfg_overhead_daily,
            "Mfg_Overhead_Exp", "DPT_Mfg_Support", "Cash", "DPT_Admin",
            "Factory_Overhead_Incurred"
        )
        if entries: 
            daily_entries.extend(entries)
            global_entry_count += 1
            monthly_overhead_pool += mfg_overhead_daily

        # --------------------------------------------------
        # 4. Sales and Collection Cycle
        # --------------------------------------------------
        base_sales = 2 + (seasonal_wave[day] * 3) + np.random.normal(0, 0.5)
        for _ in range(max(0, int(base_sales))):
            sales_amt = np.random.lognormal(mean=np.log(1200), sigma=0.4)
            sales_amt = max(200.0, sales_amt)

            # Sales record
            entries, exec_amt = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, sales_amt,
                "Accounts_Receivable", "DPT_Admin", "Sales_Revenue", "DPT_Sales", "Sales_Record"
            )
            if entries:
                daily_entries.extend(entries)
                global_entry_count += 1

            # COGS record
            cogs_amt = exec_amt * random.uniform(0.5, 0.75)
            prod_dept = "DPT_Prod_A" if random.random() < 0.7 else "DPT_Prod_B"
            entries, _ = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, cogs_amt,
                "COGS", prod_dept, "Finished_Goods", prod_dept, "COGS_Record"
            )
            if entries:
                daily_entries.extend(entries)
                global_entry_count += 1

            # Accounts Receivable Collection
            collection_day = day + random.randint(30, 90)

            def make_collection(amt):
                def task(d_str, e_count):
                    entries, _ = attempt_entry(
                        f"E_{e_count:06d}", d_str, amt,
                        "Cash", "DPT_Admin", "Accounts_Receivable", "DPT_Admin", "AR_Collection"
                    )
                    if entries:
                        return entries, e_count + 1
                    return [], e_count
                return task

            if sales_amt > 0:
                event_queue[collection_day].append(make_collection(sales_amt))

        # --------------------------------------------------
        # 5. Raw Material Purchase Cycle
        # --------------------------------------------------
        if day % 7 == 0:
            purch_amount = np.random.normal(15000, 2000)
            entries, exec_purch = attempt_entry(
                f"E_{global_entry_count:06d}", date_str, purch_amount,
                "Raw_Materials", "DPT_Ops", "Accounts_Payable", "DPT_Admin", "Raw_Material_Purchase"
            )
            if entries:
                daily_entries.extend(entries)
                global_entry_count += 1
            purch_amount = exec_purch

            pay_day = day + random.randint(30, 90)

            def make_payment(amt):
                def task(d_str, e_count):
                    entries, _ = attempt_entry(
                        f"E_{e_count:06d}", d_str, amt,
                        "Accounts_Payable", "DPT_Admin", "Cash", "DPT_Admin", "AP_Payment"
                    )
                    if entries:
                        return entries, e_count + 1
                    return [], e_count
                return task

            if purch_amount > 0:
                event_queue[pay_day].append(make_payment(purch_amount))

        # --------------------------------------------------
        # 6. Month-End Manufacturing Cost Allocation Execution
        # --------------------------------------------------
        if current_date.day == 28 and args.allocation_mode != "none":
            pool_to_allocate = monthly_overhead_pool
            if pool_to_allocate > 0:
                drv_a = monthly_drivers["DPT_Prod_A"]
                drv_b = monthly_drivers["DPT_Prod_B"]

                if args.allocation_mode == "traditional":
                    tot_hrs = drv_a["labor_hours"] + drv_b["labor_hours"]
                    ratio_a = (drv_a["labor_hours"] / tot_hrs) if tot_hrs > 0 else 0.5
                    ratio_b = 1.0 - ratio_a
                    
                    alloc_a = pool_to_allocate * ratio_a
                    alloc_b = pool_to_allocate * ratio_b

                    entries, _ = attempt_entry(
                        f"E_{global_entry_count:06d}", date_str, alloc_a,
                        "Finished_Goods", "DPT_Prod_A", "Mfg_Overhead_Exp", "DPT_Mfg_Support",
                        f"Cost_Alloc_Traditional [LaborRatio:{ratio_a*100:.1f}%]"
                    )
                    if entries: daily_entries.extend(entries); global_entry_count += 1

                    entries, _ = attempt_entry(
                        f"E_{global_entry_count:06d}", date_str, alloc_b,
                        "Finished_Goods", "DPT_Prod_B", "Mfg_Overhead_Exp", "DPT_Mfg_Support",
                        f"Cost_Alloc_Traditional [LaborRatio:{ratio_b*100:.1f}%]"
                    )
                    if entries: daily_entries.extend(entries); global_entry_count += 1

                elif args.allocation_mode == "abc":
                    pool_machine = pool_to_allocate * 0.40
                    pool_setup = pool_to_allocate * 0.35
                    pool_inspect = pool_to_allocate * 0.25

                    tot_m_hrs = drv_a["machine_hours"] + drv_b["machine_hours"]
                    r_m_a = (drv_a["machine_hours"] / tot_m_hrs) if tot_m_hrs > 0 else 0.5
                    
                    tot_setups = drv_a["setup_counts"] + drv_b["setup_counts"]
                    r_s_a = (drv_a["setup_counts"] / tot_setups) if tot_setups > 0 else 0.5
                    
                    tot_inspects = drv_a["inspection_counts"] + drv_b["inspection_counts"]
                    r_i_a = (drv_a["inspection_counts"] / tot_inspects) if tot_inspects > 0 else 0.5

                    alloc_abc_a = (pool_machine * r_m_a) + (pool_setup * r_s_a) + (pool_inspect * r_i_a)
                    alloc_abc_b = pool_to_allocate - alloc_abc_a

                    entries, _ = attempt_entry(
                        f"E_{global_entry_count:06d}", date_str, alloc_abc_a,
                        "Finished_Goods", "DPT_Prod_A", "Mfg_Overhead_Exp", "DPT_Mfg_Support",
                        f"Cost_Alloc_ABC [M_Hrs:{r_m_a*100:.0f}%, Setup:{r_s_a*100:.0f}%, Insp:{r_i_a*100:.0f}%]"
                    )
                    if entries: daily_entries.extend(entries); global_entry_count += 1

                    entries, _ = attempt_entry(
                        f"E_{global_entry_count:06d}", date_str, alloc_abc_b,
                        "Finished_Goods", "DPT_Prod_B", "Mfg_Overhead_Exp", "DPT_Mfg_Support",
                        f"Cost_Alloc_ABC [M_Hrs:{(1-r_m_a)*100:.0f}%, Setup:{(1-r_s_a)*100:.0f}%, Insp:{(1-r_i_a)*100:.0f}%]"
                    )
                    if entries: daily_entries.extend(entries); global_entry_count += 1

                elif args.allocation_mode == "tabc":
                    # DYNAMIC T-ABC MODEL (Data-driven entropy dissipation rate alpha(t))
                    # Calculate Coefficient of Variation (CV = std / mean) of daily activity effort
                    if len(daily_activity_series) >= 7:
                        arr = np.array(daily_activity_series[-30:]) # Last 30 days
                        mean_eff = np.mean(arr)
                        std_eff = np.std(arr)
                        cv_eff = (std_eff / mean_eff) if mean_eff > 0 else 0.2
                    else:
                        cv_eff = 0.2

                    # Dynamic Friction Dissipation Rate alpha(t):
                    # Higher daily volatility -> Higher physical friction loss isolated
                    alpha_t = np.clip(0.04 + 0.18 * cv_eff, 0.03, 0.25)
                    
                    friction_loss_amt = pool_to_allocate * alpha_t
                    effective_pool = pool_to_allocate - friction_loss_amt

                    tot_m_hrs = drv_a["machine_hours"] + drv_b["machine_hours"]
                    tot_setups = drv_a["setup_counts"] + drv_b["setup_counts"]
                    tot_inspects = drv_a["inspection_counts"] + drv_b["inspection_counts"]

                    r_m_a = (drv_a["machine_hours"] / tot_m_hrs) if tot_m_hrs > 0 else 0.5
                    r_s_a = (drv_a["setup_counts"] / tot_setups) if tot_setups > 0 else 0.5
                    r_i_a = (drv_a["inspection_counts"] / tot_inspects) if tot_inspects > 0 else 0.5

                    pool_m = effective_pool * 0.40
                    pool_s = effective_pool * 0.35
                    pool_i = effective_pool * 0.25

                    alloc_tabc_a = (pool_m * r_m_a) + (pool_s * r_s_a) + (pool_i * r_i_a)
                    alloc_tabc_b = effective_pool - alloc_tabc_a

                    entries, _ = attempt_entry(
                        f"E_{global_entry_count:06d}", date_str, alloc_tabc_a,
                        "Finished_Goods", "DPT_Prod_A", "Mfg_Overhead_Exp", "DPT_Mfg_Support",
                        f"Cost_Alloc_TABC [Eff:${effective_pool:.0f}, IsolatedLoss:${friction_loss_amt:.0f} (alpha:{alpha_t*100:.1f}%), VolatilityCV:{cv_eff:.2f}, M_Hrs:{r_m_a*100:.0f}%, Setup:{r_s_a*100:.0f}%, Insp:{r_i_a*100:.0f}%]"
                    )
                    if entries: daily_entries.extend(entries); global_entry_count += 1

                    entries, _ = attempt_entry(
                        f"E_{global_entry_count:06d}", date_str, alloc_tabc_b,
                        "Finished_Goods", "DPT_Prod_B", "Mfg_Overhead_Exp", "DPT_Mfg_Support",
                        f"Cost_Alloc_TABC [Eff:${effective_pool:.0f}, IsolatedLoss:${friction_loss_amt:.0f} (alpha:{alpha_t*100:.1f}%), VolatilityCV:{cv_eff:.2f}, M_Hrs:{(1-r_m_a)*100:.0f}%, Setup:{(1-r_s_a)*100:.0f}%, Insp:{(1-r_i_a)*100:.0f}%]"
                    )
                    if entries: daily_entries.extend(entries); global_entry_count += 1

            # Reset monthly trackers
            monthly_overhead_pool = 0.0
            daily_activity_series = []
            for d in monthly_drivers.values():
                d["labor_hours"] = 0.0
                d["machine_hours"] = 0.0
                d["setup_counts"] = 0
                d["inspection_counts"] = 0

        # Stream output
        for row in daily_entries:
            writer.writerow(row)

def main():
    parser = setup_argparser()
    args = parser.parse_args()
    random.seed(args.seed)
    np.random.seed(args.seed)
    generate_stream(args)

if __name__ == "__main__":
    main()
