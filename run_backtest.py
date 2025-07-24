from QuantBacktester.data.loader import load_stock_data
from QuantBacktester.strategy.sma_ema_crossover import sma_ema_crossover
from QuantBacktester.portfolio.simulator import PortfolioSimulator
from QuantBacktester.metrics import calculate_metrics
from QuantBacktester.visual import plot_portfolio_value, plot_drawdown, plot_benchmark_comparison
from QuantBacktester.strategy.bollinger_bands import bollinger_bands_strategy
from QuantBacktester.strategy.momentum import momentum_strategy


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

    
    strategies = {
        "SMA/EMA Crossover": sma_ema_crossover,
        "Bollinger Bands": bollinger_bands_strategy,
        "Momentum": momentum_strategy
    }
    results_dict = {}
    metrics_dict = {}

    # Run portfolio simulation
    portfolio = PortfolioSimulator(initial_cash=initial_cash, commission=commission, position_size=position_size)
   
    for name, strategy_func in strategies.items():
        print(f"\nRunning strategy: {name}")
        signals = strategy_func(df)
        results = portfolio.run_backtest(df, signals)
        results_dict[name] = results
        metrics = calculate_metrics(results)
        metrics_dict[name] = metrics

        print(f"Preformance metrics for {name}:")
        for key, value in metrics.items():
            print(f"{key}: {value:.4f}")

    best_strategy = max(metrics_dict.items(), key=lambda x: x[1].get('Sharpe Ratio', -float('inf')))
    best_name, best_metrics = best_strategy

    print(f"\nBest strategy: {best_name} with Sharpe Ratio: {best_metrics.get('Sharpe Ratio', 'N/A'):.4f}")

    print(f"\nPlotting results for best strategy: {best_name}...")
    best_results = results_dict[best_name]
    plot_portfolio_value(best_results)
    plot_drawdown(best_results)
    plot_benchmark_comparison(best_results, benchmark_symbol)
    
run_backtest("AAPL")