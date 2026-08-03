#!/usr/bin/env python3
# ==========================================
# src/core/core_accounting_taxonomy.py
# TLU Core: Financial Accounting Taxonomy Resolver
# ==========================================
"""!
@file core_accounting_taxonomy.py
@brief Financial accounting taxonomy definitions and classification helpers for TLU manifold projections.
@details Maps node labels and accounts to Balance Sheet (BS) and Profit & Loss (PL) financial categories.
"""

from enum import Enum
from typing import Dict, Any, Optional

class AccountCategory(Enum):
    ASSET = "Asset"
    LIABILITY = "Liability"
    EQUITY = "Equity"
    REVENUE = "Revenue"
    EXPENSE = "Expense"
    UNKNOWN = "Unknown"

# Default Standard Account Taxonomy Mapping
DEFAULT_ACCOUNT_TAXONOMY: Dict[str, AccountCategory] = {
    # Assets (BS Dr)
    "Cash": AccountCategory.ASSET,
    "Inventory": AccountCategory.ASSET,
    "Accounts_Receivable": AccountCategory.ASSET,
    "AR": AccountCategory.ASSET,
    "USR_Cash": AccountCategory.ASSET,
    "USR_Stock": AccountCategory.ASSET,
    
    # Liabilities (BS Cr)
    "Accounts_Payable": AccountCategory.LIABILITY,
    "AP": AccountCategory.LIABILITY,
    "STK_Issuer": AccountCategory.LIABILITY,
    
    # Equity (BS Cr)
    "Equity_Capital": AccountCategory.EQUITY,
    "Capital": AccountCategory.EQUITY,
    "Retained_Earnings": AccountCategory.EQUITY,
    "ACC_Input_From_Outside_Cash": AccountCategory.EQUITY,
    
    # Revenue (PL Cr)
    "Sales_Revenue": AccountCategory.REVENUE,
    "Revenue": AccountCategory.REVENUE,
    "Sales": AccountCategory.REVENUE,
    
    # Expense (PL Dr)
    "COGS": AccountCategory.EXPENSE,
    "Cost_of_Goods_Sold": AccountCategory.EXPENSE,
    "Travel_Exp": AccountCategory.EXPENSE,
    "Payroll_Exp": AccountCategory.EXPENSE,
    "Rent_Exp": AccountCategory.EXPENSE,
    "Operating_Exp": AccountCategory.EXPENSE,
    "ACC_Output_To_Outside_Cash": AccountCategory.EXPENSE,
}

class AccountTaxonomy:
    """!
    @brief Financial Taxonomy Resolver for TLU Nodes & Accounts.
    """
    def __init__(self, custom_mapping: Optional[Dict[str, str]] = None):
        self.mapping: Dict[str, AccountCategory] = DEFAULT_ACCOUNT_TAXONOMY.copy()
        if custom_mapping:
            for k, v in custom_mapping.items():
                try:
                    self.mapping[k] = AccountCategory(v)
                except ValueError:
                    pass

    def classify_account(self, name: str) -> AccountCategory:
        """!
        @brief Classify an account or node label into BS/PL category.
        """
        clean_name = name.replace("ACC_", "").strip()
        if clean_name in self.mapping:
            return self.mapping[clean_name]
        if name in self.mapping:
            return self.mapping[name]
        
        # Heuristic fallbacks
        lower = clean_name.lower()
        if "cash" in lower or "receivable" in lower or "stock" in lower or "inventory" in lower or "asset" in lower:
            return AccountCategory.ASSET
        if "payable" in lower or "liability" in lower or "issuer" in lower:
            return AccountCategory.LIABILITY
        if "capital" in lower or "equity" in lower or "retained" in lower:
            return AccountCategory.EQUITY
        if "revenue" in lower or "sale" in lower or "income" in lower:
            return AccountCategory.REVENUE
        if "exp" in lower or "cogs" in lower or "cost" in lower or "expense" in lower:
            return AccountCategory.EXPENSE
            
        return AccountCategory.UNKNOWN

    def is_balance_sheet(self, category: AccountCategory) -> bool:
        return category in (AccountCategory.ASSET, AccountCategory.LIABILITY, AccountCategory.EQUITY)

    def is_profit_loss(self, category: AccountCategory) -> bool:
        return category in (AccountCategory.REVENUE, AccountCategory.EXPENSE)
