#!/usr/bin/env python3
# test_filter_linear_algebra.py
import unittest
import numpy as np

# Import the orchestration functions to be tested
from src.filters._004_1_2_filter_system_stability import run_system_stability_analysis
from src.filters._000_2_2_filter_principal_axes import run_principal_axes_analysis
from src.filters._002_1_3_filter_manifold_dimensionality import run_manifold_dimensionality_analysis

class TestSystemStabilityFilter(unittest.TestCase):
    
    def test_run_system_stability_analysis_dag(self):
        """
        [Red] Test normal condition: a perfect DAG (Directed Acyclic Graph) transition matrix.
        Because money strictly flows downstream, spectral radius must be 0.0.
        """
        # Node 0 -> Node 1 -> Node 2
        T_slice_dag = np.array([
            [0.0, 100.0,   0.0],
            [0.0,   0.0,  50.0],
            [0.0,   0.0,   0.0]
        ])
        
        # Act
        records = run_system_stability_analysis(t_idx=1, T_slice=T_slice_dag)
        
        # Assert (Record format: [t_idx, "spectral_radius", is_stable])
        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual(record[0], 1)               # t_idx
        self.assertEqual(record[1], "0.000000")      # spectral_radius
        self.assertEqual(record[2], 1)               # is_stable

    def test_run_system_stability_analysis_cycle(self):
        """
        [Red] Test anomaly condition: a graph containing a cycle (e.g. Wash Trading).
        Node 0 <-> Node 1 creates an infinite loop, breaking the DAG property.
        Spectral radius should be > 0.0.
        """
        # Node 0 <-> Node 1 (Cycle)
        T_slice_cycle = np.array([
            [0.0, 100.0,   0.0],
            [50.0,  0.0,   0.0],
            [0.0,   0.0,   0.0]
        ])
        
        # Act
        records = run_system_stability_analysis(t_idx=2, T_slice=T_slice_cycle)
        
        record = records[0]
        spectral_radius = float(record[1])
        
        # Assert: A cycle exists, so eigenvalues must be non-zero
        self.assertGreater(spectral_radius, 0.0)
        self.assertEqual(record[2], 1)  # stable because SR <= 1.0 (stochastic matrix)


class TestPrincipalAxesFilter(unittest.TestCase):
    
    def test_run_principal_axes_analysis_sufficient_history(self):
        """
        [Red] Test normal condition: enough history to compute covariance.
        """
        N = 3
        T_slice = np.zeros((N, N)) # T_slice itself doesn't affect history much here except giving current flux
        # Let's make current flux non-zero
        T_slice[0, 1] = 100.0
        
        # q_history needs at least 2 prior items to have >2 items in temp_history
        q_history = [
            np.array([10.0, -10.0, 0.0]),
            np.array([20.0, -20.0, 0.0])
        ]
        
        records, q_current = run_principal_axes_analysis(
            t_idx=3, 
            T_slice=T_slice, 
            q_history=q_history,
            top_k=2
        )
        
        # Since top_k=2 and N=3, it should return 2 * N = 6 records
        self.assertEqual(len(records), 6)
        
        # First record check (component 0, node 0)
        rec = records[0]
        self.assertEqual(rec[0], 3) # t_idx
        self.assertEqual(rec[1], 0) # component_idx
        self.assertEqual(rec[2], 0) # node_idx
        
        # Eigenvalues shouldn't be exactly "0.000000" if there's real variance
        # Actually it's just a straight line so 1st PC variance > 0, 2nd PC variance = 0
        eigenvalue = float(rec[3])
        self.assertGreater(eigenvalue, 0.0)

    def test_run_principal_axes_analysis_insufficient_history(self):
        """
        [Red] Test edge case: Not enough history (Burn-in period).
        Should safely return 0.0.
        """
        N = 2
        T_slice = np.zeros((N, N))
        q_history = []  # Empty history
        
        records, q_current = run_principal_axes_analysis(
            t_idx=0, 
            T_slice=T_slice, 
            q_history=q_history,
            top_k=1
        )
        
        # top_k=1, N=2 -> 2 records
        self.assertEqual(len(records), 2)
        rec = records[0]
        self.assertEqual(rec[3], "0.000000") # eigenvalue
        self.assertEqual(rec[4], "0.000000") # ratio


class TestManifoldDimensionalityFilter(unittest.TestCase):
    
    def test_run_manifold_dimensionality_analysis_basic(self):
        """
        [Red] Test normal condition: calculating effective rank of T_slice.
        """
        # Rank 2 matrix
        T_slice = np.array([
            [10.0, 0.0,  0.0],
            [0.0,  5.0,  0.0],
            [0.0,  0.0,  0.0]
        ])
        
        records = run_manifold_dimensionality_analysis(
            t_idx=5, 
            T_slice=T_slice,
            top_k=2
        )
        
        self.assertEqual(len(records), 2)
        
        rec_0 = records[0]
        # s_val
        self.assertEqual(rec_0[2], "10.000000")
        # effective_rank should be 2
        self.assertEqual(rec_0[4], 2)

    def test_run_manifold_dimensionality_analysis_zero_matrix(self):
        """
        [Red] Test edge case: completely empty T_slice (rank 0).
        """
        T_slice = np.zeros((3, 3))
        
        records = run_manifold_dimensionality_analysis(
            t_idx=6, 
            T_slice=T_slice,
            top_k=1
        )
        
        self.assertEqual(len(records), 1)
        rec = records[0]
        self.assertEqual(rec[2], "0.000000") # s_val
        self.assertEqual(rec[3], "0.000000") # ratio
        self.assertEqual(rec[4], 0)          # effective_rank


if __name__ == '__main__':
    unittest.main()
