import plotly.express as px
import pandas as pd

def create_bar_chart(df, x_col: str, y_col: str, title: str):
    """
    Create a bar chart using Plotly Express.
    
    Args:
        df: DataFrame containing the data to plot
        x_col: Column name for the x-axis
        y_col: Column name for the y-axis
        title: Title of the chart
        save_path: Path to save the HTML file of the chart
    """
    fig = px.bar(df, x=x_col, y=y_col, title=title)
    fig.show()
   
