import pandas as pd
import numpy as np
from typing import Dict
from datetime import datetime

class PortfolioManager:
    """Manages investment portfolio allocation and performance tracking"""
    
    def __init__(self, initial_investment: float = 100000):
        self.initial_investment = initial_investment
    
    def calculate_allocation_values(self, allocations, stock_prices):
        """Calculate shares and dollar amounts for each allocation"""
        # [Implementation for allocation calculations]
    
    def calculate_portfolio_performance(self, allocations, stock_data, start_date=None):
        """Calculate historical portfolio performance with metrics"""
        # [Implementation with timezone-aware date handling]
    
    def calculate_individual_performance(self, allocations, stock_data, start_date=None):
        """Calculate individual stock performance within portfolio"""
        # [Implementation for per-stock analytics]