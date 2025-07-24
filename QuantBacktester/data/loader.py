import pandas as pd 
import yfinance as yf

def load_stock_data(symbol: str, start: str = '2000-01-01', end: str = '2024-12-31') -> pd.DataFrame: 

    df = yf.download(symbol, start=start, end=end)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    df.dropna(inplace=True)
    return df
