import pandas as pd 

def momentum_strategy(df, window=14):

    momentum = df['Close'].diff(window)

    signals = pd.Series(0, index=df.index)

    signals[momentum > 0] = 1   # Buy 
    signals[momentum < 0] = -1  # sell

    return signals