import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Portfolio:
    def __init__(self, tickers, weights, start="2020-01-01", end="2024-12-31"):
        self.tickers = tickers
        self.weights = np.array(weights)
        self.start = start
        self.end = end
        self.price_data = None
        self.returns = None

    def load_data(self):
        all_data = {}
        for ticker in self.tickers:
            ticker_obj = yf.Ticker(ticker)
            hist = ticker_obj.history(start=self.start, end=self.end)
            if "Adj Close" in hist.columns:
                all_data[ticker] = hist["Adj Close"]
            else:
                all_data[ticker] = hist["Close"]
        self.price_data = pd.DataFrame(all_data)

    def compute_returns(self):
        if self.price_data is None:
            raise ValueError("Price data not loaded.")
        self.returns = self.price_data.pct_change().dropna()

    def calculate_stats(self):
        if self.returns is None:
            raise ValueError("Returns not computed.")
        mean_returns = self.returns.mean()
        cov_matrix = self.returns.cov()
        port_return = np.dot(self.weights, mean_returns)
        port_volatility = np.sqrt(
            np.dot(self.weights.T, np.dot(cov_matrix, self.weights))
        )
        sharpe_ratio = port_return / port_volatility
        return {
            "return": round(port_return, 3),
            "volatility": round(port_volatility, 3),
            "sharpe_ratio": round(sharpe_ratio, 3),
        }

    def plot_prices(self, filename="portfolio_returns(oop).png"):
        if self.price_data is None:
            raise ValueError("Price data not loaded.")
        plt.style.use("ggplot")
        fig, ax = plt.subplots(figsize=(10, 5))
        fig.patch.set_facecolor("white")
        ax.set_facecolor("white")

        self.price_data.plot(ax=ax, title="Stock Prices")
        ax.set_ylabel("Price")
        ax.grid(True, color="lightgray", linestyle="--", linewidth=0.7)

        plt.tight_layout()
        plt.savefig(filename)
        plt.close(fig)


if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    weights = [0.25, 0.25, 0.25, 0.25]

    portfolio = Portfolio(tickers, weights)
    portfolio.load_data()
    portfolio.compute_returns()
    stats = portfolio.calculate_stats()

    print("Portfolio Stats:", stats)
    portfolio.plot_prices()
    print("Portfolio returns plot saved as 'portfolio_returns(oop).png'.")
