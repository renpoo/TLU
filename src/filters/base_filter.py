#!/usr/bin/env python3
# ==========================================
# src/filters/base_filter.py
# TLU Base Pipeline Filter Framework
# ==========================================
"""!
@file base_filter.py
@brief Standard Base Framework for TLU Stream Pipeline Filters.
@details Implements Template Method pattern, History Window Management,
         Design by Contract (DbC) assertions, and decoupled I/O formatting.
"""

import sys
import csv
import argparse
import os
import numpy as np
from typing import List, Dict, Tuple, Any, Optional

from src.filters.cli_parser import get_base_parser
from src.filters.stream_processor import setup_pipeline, yield_time_slices, load_initial_state

# ==========================================
# 1. Design by Contract (DbC) Assertions
# ==========================================

def assert_valid_matrix(T_slice: np.ndarray, N: int):
    """!
    @brief DbC Invariant: Assert matrix dimensions and numerical validity.
    """
    if not isinstance(T_slice, np.ndarray):
        raise TypeError(f"DbC Violation: T_slice must be a numpy.ndarray, got {type(T_slice)}")
    if T_slice.shape != (N, N):
        raise ValueError(f"DbC Violation: T_slice shape must be ({N}, {N}), got {T_slice.shape}")
    if np.isnan(T_slice).any() or np.isinf(T_slice).any():
        raise ValueError("DbC Violation: T_slice contains NaN or Inf values")

def assert_mass_conservation(T_slice: np.ndarray, tol: float = 1e-5):
    """!
    @brief DbC Invariant: Assert Conservation of Mass in closed system flux.
    """
    inflow = np.sum(T_slice, axis=0)
    outflow = np.sum(T_slice, axis=1)
    net_total = np.sum(inflow - outflow)
    if abs(net_total) > tol:
        raise ValueError(f"DbC Violation: Conservation of Mass violated. Net total flux delta = {net_total:.6f}")

# ==========================================
# 2. History Window Buffer
# ==========================================

class HistoryBuffer:
    """!
    @brief Encapsulated sliding window buffer for node/system state histories.
    """
    def __init__(self, windows_config: Optional[Dict[str, int]] = None):
        self._config = windows_config or {}
        self._buffers: Dict[str, List[np.ndarray]] = {key: [] for key in self._config}

    def append(self, key: str, value: np.ndarray):
        if key not in self._buffers:
            self._buffers[key] = []
        self._buffers[key].append(value)
        max_size = self._config.get(key, 100)
        if len(self._buffers[key]) > max_size:
            self._buffers[key].pop(0)

    def get(self, key: str) -> List[np.ndarray]:
        return self._buffers.get(key, [])

    def __getitem__(self, key: str) -> List[np.ndarray]:
        return self.get(key)

# ==========================================
# 3. Abstract Base Filter Framework
# ==========================================

class BaseFilter:
    """!
    @brief Abstract Base Class for all TLU Pipeline Filters (Template Method Pattern).
    """
    cli_description: str = "TLU Base Pipeline Filter"
    output_header: List[str] = []
    history_config: Dict[str, int] = {}
    validate_mass_conservation: bool = False

    def __init__(self):
        self.parser = get_base_parser(self.cli_description)
        self.add_arguments(self.parser)

    def add_arguments(self, parser: argparse.ArgumentParser):
        """Override in subclass to register filter-specific CLI arguments."""
        pass

    def process_slice(
        self, 
        t_idx: int, 
        T_slice: np.ndarray, 
        history: HistoryBuffer,
        X_initial: np.ndarray,
        args: argparse.Namespace
    ) -> Tuple[List[List[Any]], Dict[str, np.ndarray]]:
        """!
        @brief Process a single time slice. Must be overridden by subclasses.
        @param t_idx Current time index.
        @param T_slice N x N flux matrix for this time slice.
        @param history HistoryBuffer instance containing past state vectors.
        @param X_initial Initial state vector (Day 0).
        @param args Parsed CLI argument namespace.
        @return Tuple of (records list, dictionary of new state arrays to update in history).
        """
        raise NotImplementedError("Subclasses must implement process_slice()")

    def format_records(self, raw_records: List[List[Any]]) -> List[List[str]]:
        """!
        @brief Decoupled presentation formatting. Converts numeric records into string tokens for CSV writing.
        """
        formatted = []
        for row in raw_records:
            formatted_row = []
            for item in row:
                if isinstance(item, (float, np.floating)):
                    formatted_row.append(f"{float(item):.4f}")
                elif isinstance(item, (int, np.integer)):
                    formatted_row.append(str(item))
                else:
                    formatted_row.append(str(item))
            formatted.append(formatted_row)
        return formatted

    def run(self):
        """!
        @brief Standard Template Method execution pipeline.
        """
        env_dir = os.environ.get("TARGET_ENV", "workspace")

        # 1. Pipeline Setup (reads sys.stdin, writes header to sys.stdout)
        args, N, reader, writer = setup_pipeline(self.parser, self.output_header)

        # 2. Update dynamic history window limits from args if present
        updated_history_config = dict(self.history_config)
        if hasattr(args, "history_window") and args.history_window:
            for k in updated_history_config:
                updated_history_config[k] = args.history_window
        elif hasattr(args, "temp_window") and args.temp_window:
            for k in updated_history_config:
                updated_history_config[k] = args.temp_window
        elif hasattr(args, "baseline_window") and args.baseline_window:
            for k in updated_history_config:
                updated_history_config[k] = args.baseline_window

        # 3. Load Initial State & Initialize History
        X_initial = load_initial_state(env_dir, N)
        history = HistoryBuffer(updated_history_config)

        # 4. Main Stream Loop
        for t_idx, T_slice in yield_time_slices(reader, N):
            # DbC Invariant Verification
            assert_valid_matrix(T_slice, N)
            if self.validate_mass_conservation:
                assert_mass_conservation(T_slice)

            # Subclass Pure Compute Logic
            records, state_updates = self.process_slice(t_idx, T_slice, history, X_initial, args)

            # History Buffer Update
            for key, val in state_updates.items():
                history.append(key, val)

            # Format and Output Stream
            formatted_records = self.format_records(records)
            for rec in formatted_records:
                writer.writerow(rec)

        sys.stdout.flush()
