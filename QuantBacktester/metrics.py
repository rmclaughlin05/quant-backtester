import pandas as pd 
import numpy as np 

def calculate_metrics(portfolio):
    returns = portfolio['Portfolio Value'].pct_change().dropna()
    start_value = portfolio['Portfolio Value'].iloc[0]
    end_value = portfolio['Portfolio Value'].iloc[-1]

    total_return = (end_value/start_value) - 1

    days = (portfolio.index[-1] - portfolio.index[0]).days
    cgar = (end_value/start_value) ** (365/days) - 1 

    volatility = returns.std() * np.sqrt(252)  

    sharpe_ratio = returns.mean() / returns.std() * np.sqrt(252) if returns.std() != 0 else np.nan

    cumulative_returns = portfolio['Portfolio Value']/ start_value
    running_max = cumulative_returns.cummax()
    drawdown = cumulative_returns - running_max -1
    max_drawdown = drawdown.min()

    return{
        'Total Return': total_return,
        'CAGR': cgar,
        'Volatility': volatility,
        'Sharpe Ratio': sharpe_ratio,
        'Max Drawdown': max_drawdown
    }