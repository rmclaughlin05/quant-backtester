import pandas as pd 

def sma_ema_crossover(df,short_window=50, long_window=200, use_ema=False):
    

    price_col = 'Close'
    signals = pd.DataFrame(index=df.index)
    signals['Signal'] = df[price_col]

    if use_ema:
        signals['short'] = df[price_col].ewm(span=short_window, adjust=False).mean()
        signals['long'] = df[price_col].ewm(span=long_window, adjust=False).mean()
    else:
        signals['short'] = df[price_col].rolling(window=short_window).mean()
        signals['long'] = df[price_col].rolling(window=long_window).mean()
    
    signals['Signal'] = 0
    signals.loc[signals['short'] > signals['long'], 'Signal'] = 1
    signals.loc[signals['short'] < signals['long'], 'Signal'] = -1
    signals['Signal'] = signals['Signal'].shift(1).fillna(0)

    return signals['Signal']
    