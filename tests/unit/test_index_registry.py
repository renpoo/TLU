#!/usr/bin/env python3
# test_index_registry.py
import unittest
from src.filters.stream_processor import IndexRegistry

class TestIndexRegistry(unittest.TestCase):
    def test_assign_new_id_starts_from_zero(self):
        """
        [Red] SDL_05: 未知のラベルが渡されたとき、0から順番にIDを発番することを確認する。
        """
        registry = IndexRegistry()
        
        # 初めて見るラベルには 0 が割り当てられる
        self.assertEqual(registry.assign_new_id("Cash"), 0)
        # 次の新しいラベルには 1 が割り当てられる
        self.assertEqual(registry.assign_new_id("Sales"), 1)
        # 既に知っているラベルが来たら、同じIDを返す
        self.assertEqual(registry.assign_new_id("Cash"), 0)

    def test_assign_new_id_returns_correct_existing_id(self):
        """
        [Red] すでに登録済みのラベルが複数ある場合、それぞれの正しいIDを返すこと。
        """
        registry = IndexRegistry()
        registry.assign_new_id("Cash")   # ID: 0
        registry.assign_new_id("Sales")  # ID: 1
        registry.assign_new_id("Tax")    # ID: 2
        
        # 既に知っているラベルなら、それぞれの正しいIDを返すはず
        self.assertEqual(registry.assign_new_id("Sales"), 1)
        self.assertEqual(registry.assign_new_id("Tax"), 2)

if __name__ == '__main__':
    unittest.main()
