#!/usr/bin/env python3
# test_index_registry.py
import unittest
from src.filters.stream_processor import IndexRegistry

class TestIndexRegistry(unittest.TestCase):
    def test_assign_new_id_starts_from_zero(self):
        """
        [Red] SDL_05: Verify that when an unknown label is passed, IDs are assigned sequentially starting from 0.
        """
        registry = IndexRegistry()
        
        # The first label seen is assigned 0
        self.assertEqual(registry.assign_new_id("Cash"), 0)
        # The next new label is assigned 1
        self.assertEqual(registry.assign_new_id("Sales"), 1)
        # If an already known label comes, it returns the same ID
        self.assertEqual(registry.assign_new_id("Cash"), 0)

    def test_assign_new_id_returns_correct_existing_id(self):
        """
        [Red] If there are multiple already registered labels, return their respective correct IDs.
        """
        registry = IndexRegistry()
        registry.assign_new_id("Cash")   # ID: 0
        registry.assign_new_id("Sales")  # ID: 1
        registry.assign_new_id("Tax")    # ID: 2
        
        # If it is an already known label, it should return its respective correct ID
        self.assertEqual(registry.assign_new_id("Sales"), 1)
        self.assertEqual(registry.assign_new_id("Tax"), 2)

if __name__ == '__main__':
    unittest.main()
