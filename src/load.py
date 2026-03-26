import pandas as pd
from pathlib import Path
import json

"""
Load EV market analysis data.
"""
def load_json(filepath: str) -> dict:
    """
    Load data from a JSON file.
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        Dictionary containing the loaded JSON data
    """
    with open(filepath, 'r') as f:
        return json.load(f)


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load data from a CSV file.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        DataFrame containing the loaded data
    """
    return pd.read_csv(filepath)


def load_multiple_files(directory: str) -> pd.DataFrame:
    """
    Load and concatenate multiple CSV files from a directory.
    
    Args:
        directory: Path to directory containing CSV files
        
    Returns:
        Combined DataFrame from all CSV files
    """
    path = Path(directory)
    dfs = [pd.read_csv(f) for f in path.glob("*.csv")]
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

