#!/usr/bin/env python3
# ==========================================
# src/core/core_temporal_binning.py
# TLU Core: Unified Temporal Binning Engine
# ==========================================
"""!
@file core_temporal_binning.py
@brief Unified Temporal Binning Engine for TLU time series and COO stream aggregation.
@details Standardizes temporal resolution mapping across day, week, month, quarter, year, and sub-day intervals.
"""

import re
import pandas as pd
from typing import Tuple

def parse_interval_spec(interval_str: str) -> Tuple[str, int]:
    """!
    @brief Parse interval string (e.g., 'week', '3d', 'month 2') into (unit, coefficient).
    """
    clean = interval_str.strip().lower()
    
    # 1. Unit then number (e.g. "day 3", "week 2")
    match_unit_num = re.match(r'^([a-zA-Z]+)\s*(\d+)$', clean)
    if match_unit_num:
        unit, num_str = match_unit_num.groups()
        return unit, int(num_str)
        
    # 2. Number then unit (e.g. "3 day", "3s", "12h")
    match_num_unit = re.match(r'^(\d+)\s*([a-zA-Z]+)$', clean)
    if match_num_unit:
        num_str, unit = match_num_unit.groups()
        return unit, int(num_str)
        
    # 3. Unit only (default coefficient = 1)
    return clean, 1

def apply_temporal_binning(series: pd.Series, interval: str) -> pd.Series:
    """!
    @brief Convert datetime pd.Series into aggregated string group keys based on interval.
    """
    if not isinstance(series, pd.Series):
        series = pd.Series(series)

    if interval == "none":
        return series.astype(str)
        
    if not pd.api.types.is_datetime64_any_dtype(series):
        series = pd.to_datetime(series, errors='coerce')

    unit, num = parse_interval_spec(interval)

    # Day
    if unit in ['day', 'd', 'days']:
        if num == 1:
            return series.dt.strftime('%Y-%m-%d')
        else:
            return series.dt.floor(f"{num}D").dt.strftime('%Y-%m-%d')

    # Week
    elif unit in ['week', 'w', 'weeks']:
        if num == 1:
            return series.dt.strftime('%G-W%V')
        else:
            return series.dt.floor(f"{num}W").dt.strftime('%Y-%m-%d')

    # Month
    elif unit in ['month', 'm', 'months']:
        if num == 1:
            return series.dt.strftime('%Y-%m')
        else:
            rounded_month = ((series.dt.month - 1) // num) * num + 1
            return series.dt.year.astype(str) + '-' + rounded_month.astype(str).str.zfill(2)

    # Quarter
    elif unit in ['quarter', 'q', 'quarters']:
        q = (series.dt.month - 1) // 3 + 1
        if num == 1:
            return series.dt.year.astype(str) + '-Q' + q.astype(str)
        else:
            rounded_q = ((q - 1) // num) * num + 1
            return series.dt.year.astype(str) + '-Q' + rounded_q.astype(str)

    # Year
    elif unit in ['year', 'y', 'years']:
        if num == 1:
            return series.dt.strftime('%Y')
        else:
            rounded_year = (series.dt.year // num) * num
            return rounded_year.astype(str)

    # Sub-day units (s, min, h)
    pd_unit = None
    if unit in ['s', 'sec', 'second', 'seconds']:
        pd_unit = 's'
    elif unit in ['min', 'minute', 'minutes']:
        pd_unit = 'min'
    elif unit in ['h', 'hr', 'hour', 'hours']:
        pd_unit = 'h'

    if pd_unit:
        freq = f"{num}{pd_unit}"
        try:
            return series.dt.floor(freq).dt.strftime('%Y-%m-%d %H:%M:%S')
        except Exception:
            pass

    # Fallback directly
    try:
        freq = f"{num}{unit}" if num > 1 else unit
        return series.dt.floor(freq).dt.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return series.dt.strftime('%Y-%m-%d')
