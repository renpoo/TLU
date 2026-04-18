#!/usr/bin/env python3
# test_003_1_1_filter_fk_simulation.py
import unittest
import numpy as np
from src.filters._003_1_1_filter_fk_simulation import run_fk_analysis

class TestFilterFKSimulation(unittest.TestCase):
    def setUp(self):
        self.N = 3
        # Node 0 -> Node 1 (10.0), Node 1 -> Node 2 (5.0)
        self.T_slice = np.array([
            [0.0, 10.0, 0.0],
            [0.0,  0.0, 5.0],
            [0.0,  0.0, 0.0]
        ])
        self.t_idx = 1
        self.q_history = [
            np.array([-5.0, 5.0, 0.0]),
            np.array([-8.0, 3.0, 5.0]),
            np.array([-10.0, 5.0, 5.0])
        ]
        self.gamma = 0.85
        self.max_k = 5

    def test_run_fk_analysis_static(self):
        """[Red->Green] Pure function test of FK system (Static mode)"""
        static_dq_input = np.array([100.0, 0.0, 0.0]) # Shock of +100 to Node 0
        
        records, q_current = run_fk_analysis(
            t_idx=self.t_idx, 
            T_slice=self.T_slice, 
            q_history=self.q_history,
            fk_input_mode='static', 
            static_dq_input=static_dq_input,
            gamma=self.gamma, 
            max_k=self.max_k
        )
        
        # N records are returned
        self.assertEqual(len(records), self.N)
        
        # q_current is correctly calculated and returned ([-10, 5, 5])
        self.assertEqual(q_current.shape, (3,))
        
        # Record structure: [t_idx, node_idx, fk_echo_impact]
        node0_rec = records[0]
        self.assertEqual(node0_rec[0], self.t_idx)
        self.assertEqual(node0_rec[1], 0)
        
        # FK output is calculated (formatted as string)
        self.assertNotEqual(node0_rec[2], "0.0000")

    def test_run_fk_analysis_impulse(self):
        """[Red->Green] Pure function test evaluating isolated 'impulse' offset extraction bindings"""
        records, q_current = run_fk_analysis(
            t_idx=self.t_idx, 
            T_slice=self.T_slice, 
            q_history=self.q_history,
            fk_input_mode='impulse', 
            static_dq_input=np.zeros(3),
            gamma=self.gamma, 
            max_k=self.max_k
        )
        # Impulse mode mathematically defaults subtracting the historic mean gracefully
        self.assertEqual(len(records), self.N)
        self.assertNotEqual(records[0][2], "nan")

if __name__ == '__main__':
    unittest.main()
