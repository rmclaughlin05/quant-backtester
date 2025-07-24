Quant Backtester

A Python-based engine for backtesting quantitative trading strategies on historical stock data.

Overview

This project provides a modular and extensible framework to:

Download historical market data using yfinance
Generate trading signals using strategies such as:
SMA/EMA crossover
Bollinger Bands
Momentum-based strategies
Simulate portfolio performance, including:
Cash and position tracking
Commission and slippage assumptions
Dynamic position sizing
Calculate performance metrics:
Total Return
CAGR
Volatility
Sharpe Ratio
Maximum Drawdown
Visualize results:
Portfolio value over time
Buy/sell signals
Drawdowns
Benchmark comparisons (e.g., S&P 500)
Features

Strategy module designed for easy extension with new algorithms
Portfolio simulator with realistic trading assumptions
Comprehensive performance evaluation and risk metrics
Benchmarking tools to compare strategy performance
Visualization utilities for intuitive result interpretation
Included Strategies

Strategy	Description
SMA/EMA Crossover	Buys when a short-term moving average crosses above a long-term average; sells when it crosses below.
Bollinger Bands	Buys when the price dips below the lower Bollinger Band; sells when the price exceeds the upper band.
Momentum	Buys when recent returns exceed a defined threshold; exits on momentum reversal or stop conditions.
