import pandas as pd


def sort_by_sales_volume(df: pd.DataFrame, ascending: bool = False) -> pd.DataFrame:
    """Sort DataFrame by sales_volume.

    Args:
        df: Input data frame.
        ascending: If True, sort ascending; otherwise descending.

    Returns:
        Sorted DataFrame.
    """
    if 'sales_volume' not in df.columns:
        raise KeyError("Column 'sales_volume' not found in dataframe")
    return df.sort_values('sales_volume', ascending=ascending).reset_index(drop=True)
