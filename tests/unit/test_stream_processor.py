#!/usr/bin/env python3
# tests/unit/test_stream_processor.py
import unittest
import io
import csv
import numpy as np

from src.filters.stream_processor import IndexRegistry, process_csv_stream, yield_time_slices
from src.filters.cli_parser import parse_projector_args

class TestStreamProcessor(unittest.TestCase):
    def test_process_csv_stream_basic(self):
        input_csv = (
            "date,sender,receiver,amount\n"
            "2023-01-01,Alice,Bob,100.5\n"
            "2023-01-02,Bob,Charlie,50.0\n"
            "2023-01-03,Alice,Charlie,33.3\n"
        )
        in_stream = io.StringIO(input_csv)
        out_stream = io.StringIO()
        
        node_registry = IndexRegistry()
        time_registry = IndexRegistry()
        
        args = [
            "--col_time=date", 
            "--col_src=sender", 
            "--col_tgt=receiver", 
            "--col_val=amount"
        ]
        mapping_config = parse_projector_args(args)

        process_csv_stream(in_stream, out_stream, mapping_config, node_registry, time_registry)
        
        output_csv = out_stream.getvalue()
        
        expected_csv = (
            "t_idx,src_idx,tgt_idx,value\n"
            "0,0,1,100.5\n"
            "1,1,2,50.0\n"
            "2,0,2,33.3\n"
        )
        self.assertEqual(output_csv, expected_csv)

    def test_export_registry_basic(self):
        from src.filters.stream_processor import export_registry
        registry = IndexRegistry()
        registry.assign_new_id("Cash")
        registry.assign_new_id("Sales")
        
        out_stream = io.StringIO()
        export_registry(registry, out_stream, "node_idx", "node_label")
        
        expected_csv = (
            "node_idx,node_label\n"
            "0,Cash\n"
            "1,Sales\n"
        )
        self.assertEqual(out_stream.getvalue(), expected_csv)

    def test_yield_time_slices_basic(self):
        mock_csv_stream = [
            ["t_idx", "src_idx", "tgt_idx", "value"],
            ["0", "0", "1", "10.0"],
            ["0", "1", "2", "5.0"],
            ["1", "2", "0", "8.0"],
        ]
        
        N = 3
        slices = list(yield_time_slices(mock_csv_stream, N))
        
        self.assertEqual(len(slices), 2)
        
        t0_idx, T0 = slices[0]
        self.assertEqual(t0_idx, 0)
        self.assertEqual(T0[0, 1], 10.0)
        self.assertEqual(T0[1, 2], 5.0)
        
        t1_idx, T1 = slices[1]
        self.assertEqual(t1_idx, 1)
        self.assertEqual(T1[2, 0], 8.0)

    def test_yield_time_slices_advanced(self):
        mock_csv_stream = [
            ["t_idx", "src_idx", "tgt_idx", "value"],
            ["0", "0", "1", "10.0"],
            ["0", "0", "1", "1.0"],
            ["0", "1", "2", "5.0"],
            ["1", "2", "0", "8.0"],
            ["1", "2", "0", "1.0"],
            ["1", "0", "2", "33.3"]
        ]
        
        N = 3
        slices = list(yield_time_slices(mock_csv_stream, N))
        
        self.assertEqual(len(slices), 2)
        
        t0_idx, T0 = slices[0]
        self.assertEqual(t0_idx, 0)
        self.assertEqual(T0[0, 1], 11.0)
        self.assertEqual(T0[1, 2], 5.0)
        
        t1_idx, T1 = slices[1]
        self.assertEqual(t1_idx, 1)
        self.assertEqual(T1[2, 0], 9.0)
        self.assertEqual(T1[0, 2], 33.3)

if __name__ == '__main__':
    unittest.main()
