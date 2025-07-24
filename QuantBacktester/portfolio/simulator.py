import pandas as pd 

class PortfolioSimulator:
    def __init__(self, initial_cash=100000, commission=0.001, position_size= 0.1):

        self.initial_cash = initial_cash
        self.commission = commission
        self.position_size = position_size
        self.cash = initial_cash

        self.position = 0
        self.position_price = 0

        self.portfolio_value_history = []
    
    def run_backtest(self, data: pd.DataFrame, signals: pd.Series):
        

        portfolio_history = []

        for date, signal in signals.items():
            price = data.loc[date, 'Close']

            if signal == 1:
                if self.position == 0:
                    amount_to_invest = self.cash * self.position_size
                    shares_to_buy = amount_to_invest // price
                    if shares_to_buy > 0:
                        cost = shares_to_buy * price
                        commission_cost = cost * self.commission
                        total_cost = cost + commission_cost
                        if total_cost <= self.cash:
                            self.cash -= total_cost
                            self.position += shares_to_buy
                            self.position_price = price
            
            elif signal == -1:

                if self.position > 0:
                    proceeds = self.position * price
                    commission_cost = proceeds * self.commission
                    net_proceeds = proceeds - commission_cost
                    self.cash += net_proceeds
                    self.position = 0
                    self.position_price = 0
            # Calculate portfolio value
            portfolio_value = self.position * price
            total_value = self.cash + portfolio_value

            portfolio_history.append({
                'Date': date,
                'Cash': self.cash,
                'Position': self.position,
                'Position Price': self.position_price,
                'Price': price,
                'Portfolio Value': total_value,
                'Signal': signal,
            })
        return pd.DataFrame(portfolio_history).set_index('Date')