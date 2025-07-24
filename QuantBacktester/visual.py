import matplotlib.pyplot as plt
import pandas as pd 
import yfinance as yf

def plot_portfolio_value(results: pd.DataFrame):
    plt.figure(figsize=(12,6))
    plt.plot(results.index, results['Portfolio Value'], label='Strategy', linewidth=2)
    plt.title('Portfolio Value Over Time')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value ($)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
def plot_drawdown(results: pd.DataFrame):
    peak = results['Portfolio Value'].cummax()
    drawdown = (results['Portfolio Value'] - peak) / peak

    plt.figure(figsize=(12,4))
    plt.plot(drawdown.index, drawdown, label='Drawdown', color='red')
    plt.title('Portfolio Drawdown Over Time')
    plt.xlabel('Date')
    plt.ylabel('Drawdown (%)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_benchmark_comparison(results: pd.DataFrame, symbol="SPY"):
    start = results.index.min()
    end = results.index.max()
    benchmark_data = yf.download(symbol, start=start, end=end ,group_by='ticker', auto_adjust=False)
    if 'Adj Close' in benchmark_data.columns:
        benchmark = benchmark_data['Adj Close']
    elif (symbol, 'Adj Close') in benchmark_data.columns:
        benchmark = benchmark_data[(symbol, 'Adj Close')]
    else:
        raise KeyError("Adjusted Close not found in downloaded benchmark data.")

    benchmark = benchmark.reindex(results.index).ffill()

    strat = results['Portfolio Value']/ results['Portfolio Value'].iloc[0] * 100
    bench = benchmark / benchmark.iloc[0] * 100

    plt.figure(figsize=(12,6))
    plt.plot(strat.index, strat, label='Strategy', linewidth=2)
    plt.plot(bench.index, bench, label=f"{symbol} Benchmark", linewidth=2)
    plt.title('Strategy vs Benchmark Performance')
    plt.xlabel('Date')
    plt.ylabel('Normalized Value(100 = starting value)')
    plt.legend()
    plt.tight_layout()
    plt.show()