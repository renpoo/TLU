#!/usr/bin/env python3
# ==========================================
# tests/unit/test_core_accounting_taxonomy.py
# Unit tests for AccountTaxonomy in core_accounting_taxonomy.py
# ==========================================
import unittest

from src.core.core_accounting_taxonomy import AccountTaxonomy, AccountCategory

class TestAccountTaxonomy(unittest.TestCase):
    def setUp(self):
        self.taxonomy = AccountTaxonomy()

    def test_classify_standard_accounts(self):
        self.assertEqual(self.taxonomy.classify_account("ACC_Cash"), AccountCategory.ASSET)
        self.assertEqual(self.taxonomy.classify_account("ACC_Accounts_Payable"), AccountCategory.LIABILITY)
        self.assertEqual(self.taxonomy.classify_account("ACC_Equity_Capital"), AccountCategory.EQUITY)
        self.assertEqual(self.taxonomy.classify_account("ACC_Sales_Revenue"), AccountCategory.REVENUE)
        self.assertEqual(self.taxonomy.classify_account("ACC_COGS"), AccountCategory.EXPENSE)

    def test_heuristic_classification(self):
        self.assertEqual(self.taxonomy.classify_account("Custom_Cash_Account"), AccountCategory.ASSET)
        self.assertEqual(self.taxonomy.classify_account("Vendor_Payable_Dept"), AccountCategory.LIABILITY)
        self.assertEqual(self.taxonomy.classify_account("Software_License_Exp"), AccountCategory.EXPENSE)

    def test_bs_pl_checks(self):
        self.assertTrue(self.taxonomy.is_balance_sheet(AccountCategory.ASSET))
        self.assertFalse(self.taxonomy.is_balance_sheet(AccountCategory.REVENUE))
        self.assertTrue(self.taxonomy.is_profit_loss(AccountCategory.EXPENSE))

if __name__ == '__main__':
    unittest.main()
