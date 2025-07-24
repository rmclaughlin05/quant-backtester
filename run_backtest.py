from QuantBacktester.data.loader import load_stock_data
from QuantBacktester.strategy.sma_ema_crossover import sma_ema_crossover
from QuantBacktester.portfolio.simulator import PortfolioSimulator
from QuantBacktester.metrics import calculate_metrics
from QuantBacktester.visual import plot_portfolio_value, plot_drawdown, plot_benchmark_comparison

def run_backtest(
    symbol: str,
    initial_cash: float = 100000,
    commission: float = 0.001,
    position_size: float = 0.1,
    short_window: int = 20,
    long_window: int = 50,
    use_ema: bool = True,
    benchmark_symbol: str = "SPY"
):
    # Load data
    df = load_stock_data(symbol)

    # Generate signals
    signals = sma_ema_crossover(df, short_window=short_window, long_window=long_window, use_ema=use_ema)

    # Run portfolio simulation
    portfolio = PortfolioSimulator(initial_cash=initial_cash, commission=commission, position_size=position_size)
    results = portfolio.run_backtest(df, signals)

    # Print last 10 portfolio states
    print(results.tail(10))

    # Calculate and print metrics
    metrics = calculate_metrics(results)
    print("\nPerformance Metrics:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

    # Plot results
    plot_portfolio_value(results)
    plot_drawdown(results)
    plot_benchmark_comparison(results, symbol=benchmark_symbol)

run_backtest("MSFT")