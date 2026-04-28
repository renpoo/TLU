import unittest
import io
import sys
from contextlib import redirect_stdout
import argparse
from src.filters._0_0_generate_dummy_market import generate_stream

class TestGenerateDummyMarket(unittest.TestCase):
    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--months", type=int, default=1)
        self.parser.add_argument("--seed", type=int, default=42)
        self.parser.add_argument("--num-users", type=int, default=10)
        self.parser.add_argument("--num-stocks", type=int, default=5)
        self.parser.add_argument("--wash-trade-prob", type=float, default=0.0)
        self.parser.add_argument("--pump-dump-prob", type=float, default=0.0)

    def test_basic_invariants(self):
        """Test that basic market rules are upheld (no self-trading, positive values)."""
        args = self.parser.parse_args(["--months", "1"])
        
        f = io.StringIO()
        with redirect_stdout(f):
            import random, numpy as np
            random.seed(args.seed)
            np.random.seed(args.seed)
            generate_stream(args)
            
        output = f.getvalue().strip().split('\n')
        header = output[0].strip()
        data = [line.strip() for line in output[1:]]
        
        self.assertEqual(header, "Transaction_ID,Timestamp,Stock_ID,Buyer_ID,Seller_ID,Price,Volume,Memo")
        self.assertGreater(len(data), 0, "No transactions were generated.")
        
        for line in data:
            parts = line.split(',')
            buyer = parts[3]
            seller = parts[4]
            price = float(parts[5])
            volume = int(parts[6])
            
            self.assertNotEqual(buyer, seller, f"Self-trading detected in transaction: {line}")
            self.assertGreater(price, 0.0, f"Non-positive price detected: {line}")
            self.assertGreater(volume, 0, f"Non-positive volume detected: {line}")

    def test_determinism_with_seed(self):
        """Test that the exact same output is generated given the same seed."""
        args1 = self.parser.parse_args(["--months", "1", "--seed", "123"])
        f1 = io.StringIO()
        with redirect_stdout(f1):
            import random, numpy as np
            random.seed(args1.seed)
            np.random.seed(args1.seed)
            generate_stream(args1)
            
        args2 = self.parser.parse_args(["--months", "1", "--seed", "123"])
        f2 = io.StringIO()
        with redirect_stdout(f2):
            random.seed(args2.seed)
            np.random.seed(args2.seed)
            generate_stream(args2)
            
        self.assertEqual(f1.getvalue(), f2.getvalue(), "Outputs differed despite identical seeds.")

    def test_wash_trade_injection(self):
        """Test that wash trades are successfully injected with high probability."""
        args = self.parser.parse_args(["--months", "1", "--wash-trade-prob", "1.0"])
        
        f = io.StringIO()
        with redirect_stdout(f):
            import random, numpy as np
            random.seed(args.seed)
            np.random.seed(args.seed)
            generate_stream(args)
            
        output = f.getvalue().strip().split('\n')
        
        wash_trades = [line for line in output if "Wash_Trade" in line]
        self.assertGreater(len(wash_trades), 0, "No Wash_Trade generated despite prob=1.0")

if __name__ == '__main__':
    unittest.main()
