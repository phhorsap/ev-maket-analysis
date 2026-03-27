#!/usr/bin/env python3
"""
EV Market Analysis - Main Module
"""
import pandas as pd
from load import load_json, load_data_csv   
from processing import sort_by_sales_volume
from visualization import create_bar_chart

def main():
    """Main entry point for the application."""
    print("EV Market Analysis")
    print("=" * 50)
    # Add your analysis code here
    pass

data_json = pd.DataFrame(load_json('data/data.json')['market_data'])

csv_data = load_data_csv('data/ev-analysis-data.csv')
csv_data = sort_by_sales_volume(csv_data, ascending=False)
create_bar_chart(csv_data, x_col='model', y_col='sales_volume', title='EV Sales Models (sorted by sales_volume)')


if __name__ == "__main__":
    main()