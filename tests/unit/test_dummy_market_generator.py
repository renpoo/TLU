#!/usr/bin/env python3
import unittest
import subprocess
import csv
import io
import os
import tempfile

class TestDummyMarketGenerator(unittest.TestCase):
    """
    Physical & Topological Contract Tests for the Market Dummy Generator.
    Ensures that the universe generated respects mass conservation and the HFT Hub topology.
    """
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.initial_state_path = os.path.join(self.tmp_dir.name, "initial.csv")
        
        self.num_users = 20
        self.num_inst = max(1, int(self.num_users * 0.10))
        self.num_hft = max(1, int(self.num_users * 0.10))
        
        # Profiles based on the script's strict index assignment
        self.inst_users = set(f"USR_{i:03d}" for i in range(1, self.num_inst + 1))
        self.hft_users = set(f"USR_{i:03d}" for i in range(self.num_inst + 1, self.num_inst + self.num_hft + 1))
        self.retail_users = set(f"USR_{i:03d}" for i in range(self.num_inst + self.num_hft + 1, self.num_users + 1))

        # Run generator
        cmd = [
            "python3", "-m", "src.filters._0_0_generate_dummy_market",
            "--months", "1",
            "--num-users", str(self.num_users),
            "--num-stocks", "2",
            "--wash-trade-prob", "0.0",
            "--panic-dump-prob", "0.0",
            "--out-initial-state", self.initial_state_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        self.transactions = []
        reader = csv.DictReader(io.StringIO(result.stdout))
        for row in reader:
            self.transactions.append(row)
            
        self.initial_state = {}
        with open(self.initial_state_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.initial_state[row["node_label"]] = float(row["initial_X"])

    def tearDown(self):
        self.tmp_dir.cleanup()

    def test_initial_mass_contract(self):
        """
        Contract 1: HFTs must start with NO stock (only cash), 
        while Institutional and Retail hold the initial market mass.
        Since initial_X currently exports (Cash + Stock Value), all users have some initial_X.
        We ensure Institutional has massively more initial mass than Retail.
        """
        # Note: Because the current script outputs 'Total Asset' for initial_X, 
        # HFTs will have > 0 mass (due to cash). But Institutional should be vastly larger.
        inst_masses = [self.initial_state[u] for u in self.inst_users]
        hft_masses = [self.initial_state[u] for u in self.hft_users]
        retail_masses = [self.initial_state[u] for u in self.retail_users]

        self.assertGreater(min(inst_masses), max(hft_masses), "Institutional mass must exceed HFT cash pool")
        self.assertGreater(min(hft_masses), max(retail_masses), "HFT cash pool must exceed retail individual wealth")

    def test_topology_hub_contract(self):
        """
        Contract 2: Pure Hub Topology.
        Retail and Institutional MUST NEVER trade directly with each other.
        Every transaction MUST have at least one HFT as buyer or seller.
        """
        for row in self.transactions:
            buyer = row["Buyer_ID"]
            seller = row["Seller_ID"]
            
            # At least one side must be HFT
            buyer_is_hft = buyer in self.hft_users
            seller_is_hft = seller in self.hft_users
            
            self.assertTrue(buyer_is_hft or seller_is_hft, 
                            f"Topological violation! Direct trade detected: {buyer} -> {seller}")

    def test_mass_conservation_contract(self):
        """
        Contract 3: Mass Conservation.
        Transaction Amount = Volume * Price exactly.
        No money or shares disappear into the void.
        """
        for row in self.transactions:
            vol = float(row["Volume"])
            price = float(row["Price"])
            amount = float(row["Transaction_Amount"])
            
            # Accounting precision check
            self.assertAlmostEqual(vol * price, amount, places=2, 
                                   msg=f"Mass conservation broken in transaction: {row}")

if __name__ == "__main__":
    unittest.main()
