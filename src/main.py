#!/usr/bin/env python3
"""
EV Market Analysis - Main Module
"""
import pandas as pd
from load import load_json

def main():
    """Main entry point for the application."""
    print("EV Market Analysis")
    print("=" * 50)
    # Add your analysis code here
    pass

data = pd.DataFrame(load_json('data/data.json')['market_data'])
print(data.head())

if __name__ == "__main__":
    main()