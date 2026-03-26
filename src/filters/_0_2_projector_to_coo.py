#!/usr/bin/env python3
# _01_projector_to_coo.py
import sys
from src.filters.cli_parser import parse_projector_args
from src.filters.stream_processor import IndexRegistry, process_csv_stream, export_registry

def main():

    path = "workspace/ephemeral/"

    # 1. CLI引数のパース (sys.argv[1:] でスクリプト名以降の引数を渡す)
    mapping_config = parse_projector_args(sys.argv[1:])

    # 2. 辞書（レジストリ）の初期化 (毎回使い捨て: SDL_05準拠)
    node_registry = IndexRegistry()
    time_registry = IndexRegistry()

    # 3. メインストリーム処理 (標準入力 -> 標準出力)
    process_csv_stream(sys.stdin, sys.stdout, mapping_config, node_registry, time_registry)

    # 4. 証跡辞書の物理ファイル出力 (SDL_05準拠)
    # 実行ごとにゼロから生成され、上書きされる
    with open(path + "_node_map.csv", "w", encoding="utf-8") as f_node:
        export_registry(node_registry, f_node, "node_idx", "node_label")
        
    with open(path + "_time_map.csv", "w", encoding="utf-8") as f_time:
        export_registry(time_registry, f_time, "t_idx", "time_label")

if __name__ == "__main__":
    main()
