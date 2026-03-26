#!/usr/bin/env python3
# tests/unit/test_cli_parser.py
import unittest
from src.filters.cli_parser import get_base_parser, parse_projector_args

class TestCLIParser(unittest.TestCase):
    def test_get_base_parser_defaults(self):
        parser = get_base_parser("Test Description")
        args = parser.parse_args([])
        self.assertEqual(args.node_map, "workspace/ephemeral/_node_map.csv")
        self.assertEqual(args.time_map, "workspace/ephemeral/_time_map.csv")
        self.assertEqual(args.sys_params, "workspace/config/_sys_params.csv")
        self.assertEqual(args.domain_tags, "workspace/config/_domain_tags.csv")

    def test_extend_parser_for_specific_filter(self):
        parser = get_base_parser("Extended Parser")
        parser.add_argument("--custom_threshold", type=float, default=0.5)
        args = parser.parse_args([])
        self.assertEqual(args.custom_threshold, 0.5)

        args = parser.parse_args(["--custom_threshold", "0.9"])
        self.assertEqual(args.custom_threshold, 0.9)

    def test_parse_projector_args_as_integers(self):
        args = ["--col_time=0", "--col_src=1", "--col_tgt=2", "--col_val=3"]
        result = parse_projector_args(args)
        
        self.assertEqual(result.get('col_time'), 0)
        self.assertEqual(result.get('col_src'), 1)
        self.assertEqual(result.get('col_tgt'), 2)
        self.assertEqual(result.get('col_val'), 3)

    def test_parse_projector_args_as_strings_and_time_format(self):
        args = [
            "--col_time=date_str",
            "--col_src=sender",
            "--col_tgt=receiver",
            "--col_val=amount",
            "--time_format=%Y/%m/%d"
        ]
        result = parse_projector_args(args)
        
        self.assertEqual(result.get('col_time'), "date_str")
        self.assertEqual(result.get('col_src'), "sender")
        self.assertEqual(result.get('col_tgt'), "receiver")
        self.assertEqual(result.get('col_val'), "amount")
        self.assertEqual(result.get('time_format'), "%Y/%m/%d")

if __name__ == '__main__':
    unittest.main()
