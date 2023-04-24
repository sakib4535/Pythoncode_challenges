# Multiple Inheritance

# Base calss 1
class Investment:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

    def investment_info(self):
        print("Inside Investment class")
        print("Symbol:", self.symbol, "Price: ", self.price)

# Base class 2
class Portfolio:
    def __init__(self, investments):
        self.investments = investments

    def portfolio_info(self):
        print(" Inside the Portfolio")
        for investment in self.investments:
            print("Symbol: ", investment.symbol, "Price: ", investment.price)

# Derived Class
class Trader(Investment, Portfolio):
    def __init__(self, symbol, price, investments):
        Investment.__init__(self, symbol, price)
        Portfolio.__init__(self, investments)

    def trader_info(self, name, strategy):
        print("Inside Trader Class")
        print("Name: ", name, "Strategy", strategy)

# Create object of Investment and Trader

inv1 = Investment("AAPL", 170.49)
inv2 = Investment("GOOG", 2890.78)
inv3 = Investment("TSLA", 2000.34)

trader1 = Trader("MSFT", 2130, [inv1,inv2])
trader2 = Trader("AMZN", 3400, [inv2, inv3])


# Access data
trader1.investment_info()
trader1.portfolio_info()
trader1.trader_info('Sakib', 'Long-term')

trader2.investment_info()
trader2.portfolio_info()
trader2.trader_info('Robin', 'Short-term')