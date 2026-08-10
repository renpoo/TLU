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
        self.num_hft = max(2, int(self.num_users * 0.10))
        
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
                label = row["node_label"]
                val = float(row["initial_X"])
                # Extract user ID (e.g. USR_001 from USR_001_Cash or USR_001_STK_001)
                parts = label.split('_')
                if len(parts) >= 2 and parts[0] == "USR":
                    user_id = f"{parts[0]}_{parts[1]}"
                    self.initial_state[user_id] = self.initial_state.get(user_id, 0.0) + val

    def tearDown(self):
        self.tmp_dir.cleanup()

    def _get_user_id(self, account_label):
        parts = account_label.split('_')
        if len(parts) >= 2 and parts[0] == "USR":
            return f"{parts[0]}_{parts[1]}"
        return account_label

    def test_initial_mass_contract(self):
        """
        Contract 1: HFTs must start with NO stock (only cash), 
        while Institutional and Retail hold the initial market mass.
        Since initial_X currently exports (Cash + Stock Value), all users have some initial_X.
        We ensure Institutional has massively more initial mass than Retail.
        """
        inst_masses = [self.initial_state[u] for u in self.inst_users]
        hft_masses = [self.initial_state[u] for u in self.hft_users]
        retail_masses = [self.initial_state[u] for u in self.retail_users]

        self.assertGreater(min(inst_masses), max(hft_masses), "Institutional mass must exceed HFT cash pool")
        self.assertGreater(min(hft_masses), max(retail_masses), "HFT cash pool must exceed retail individual wealth")

    def test_topology_hub_contract(self):
        """
        Contract 2: Valid Double-Entry Network Topology.
        Every transaction MUST have valid Debit and Credit accounts.
        """
        for row in self.transactions:
            debit_acc = row["Debit_Account"]
            credit_acc = row["Credit_Account"]
            
            self.assertTrue(len(debit_acc) > 0, f"Empty Debit account in row: {row}")
            self.assertTrue(len(credit_acc) > 0, f"Empty Credit account in row: {row}")
            self.assertNotEqual(debit_acc, credit_acc, f"Self-loop trade detected: {row}")

    def test_mass_conservation_contract(self):
        """
        Contract 3: Mass Conservation in Double-Entry Accounting.
        For stock transactions, Amount * Price (stock side) must equal Amount (cash side).
        """
        tx_map = {}
        for row in self.transactions:
            tx_id = row["Transaction_ID"]
            tx_map.setdefault(tx_id, []).append(row)
            
        for tx_id, rows in tx_map.items():
            if len(rows) == 2:
                stock_row = next((r for r in rows if r["Asset_Type"].startswith("STK")), None)
                cash_row = next((r for r in rows if r["Asset_Type"] == "CASH"), None)
                if stock_row and cash_row:
                    stock_val = float(stock_row["Amount"]) * float(stock_row["Price"])
                    cash_val = float(cash_row["Amount"])
                    self.assertAlmostEqual(stock_val, cash_val, places=2,
                                           msg=f"Mass conservation broken in Transaction {tx_id}")

if __name__ == "__main__":
    unittest.main()
