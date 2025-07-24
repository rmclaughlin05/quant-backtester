import pandas as pd 

def bollinger_bands_strategy(df, window=20, num_std=2):

    close = df['Close']
    rolling_mean = close.rolling(window=window).mean()
    rolling_std = close.rolling(window=window).std()

    upper_band = rolling_mean + (rolling_std * num_std)
    lower_band = rolling_mean - (rolling_std * num_std)

    signals = pd.Series(0, index=df.index)\
    
    signals[close< lower_band] = 1  
    signals[close> upper_band] = -1

    return signals