import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


def load_data(tickers, start="2020-01-01", end="2024-12-31"):
    """
    Download Adjusted Close price data for each ticker individually,
    return combined DataFrame.
    """
    all_data = {}
    for ticker in tickers:
        ticker_obj = yf.Ticker(ticker)
        hist = ticker_obj.history(start=start, end=end)
        # Use 'Adj Close' if available, else 'Close'
        if "Adj Close" in hist.columns:
            all_data[ticker] = hist["Adj Close"]
        else:
            all_data[ticker] = hist["Close"]
    df = pd.DataFrame(all_data)
    return df


def compute_returns(df):
    """
    Compute daily returns as percentage change.
    """
    return df.pct_change().dropna()


def portfolio_stats(returns, weights):
    """
    Calculate portfolio return, volatility, and Sharpe ratio.
    """
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    port_return = np.dot(weights, mean_returns)
    port_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = port_return / port_volatility
    # Round stats to 3 decimal places
    return {
        "return": round(port_return, 3),
        "volatility": round(port_volatility, 3),
        "sharpe_ratio": round(sharpe_ratio, 3),
    }


def plot_returns(df, filename="portfolio_returns.png"):
    plt.style.use("ggplot")
    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    df.plot(ax=ax, title="Stock Prices")
    ax.set_ylabel("Price")

    ax.grid(True, color="lightgray", linestyle="--", linewidth=0.7)

    plt.tight_layout()
    plt.savefig(filename)
    plt.close(fig)


if __name__ == "__main__":
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    weights = np.array([0.25, 0.25, 0.25, 0.25])  # Equal weights

    price_data = load_data(tickers)
    returns = compute_returns(price_data)
    stats = portfolio_stats(returns, weights)

    print("Portfolio Stats:", stats)
    plot_returns(price_data)
    print("Portfolio returns plot saved as 'portfolio_returns.png'.")
# This code provides a simple portfolio analysis tool that downloads stock data,
# computes returns, calculates portfolio statistics, and plots the stock prices.
# It uses yfinance for data retrieval and matplotlib for plotting.
