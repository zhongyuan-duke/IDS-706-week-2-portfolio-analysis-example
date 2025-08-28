import numpy as np
import pandas as pd
import pytest
from portfolio import portfolio_stats


def test_portfolio_stats_basic():
    data = {"AAPL": [0.01, 0.02, -0.01], "MSFT": [0.00, 0.01, 0.02]}
    returns = pd.DataFrame(data)
    weights = np.array([0.5, 0.5])
    stats = portfolio_stats(returns, weights)
    assert "return" in stats
    assert "volatility" in stats
    assert "sharpe_ratio" in stats
    assert stats["volatility"] > 0


def test_portfolio_stats_all_negative_returns():
    data = {"AAPL": [-0.01, -0.02, -0.01], "MSFT": [-0.01, -0.01, -0.02]}
    returns = pd.DataFrame(data)
    weights = np.array([0.5, 0.5])
    stats = portfolio_stats(returns, weights)
    assert stats["return"] < 0
    assert stats["volatility"] > 0


def test_portfolio_stats_invalid_weights():
    data = {"AAPL": [0.01, 0.02, 0.03], "MSFT": [0.01, 0.01, 0.01]}
    returns = pd.DataFrame(data)
    weights = np.array([0.7, 0.2])  # Does not sum to 1
    stats = portfolio_stats(returns, weights)
    # Should still compute, but return will be scaled by weights
    assert isinstance(stats["return"], float)


def test_portfolio_stats_single_asset():
    data = {"AAPL": [0.01, 0.02, 0.03]}
    returns = pd.DataFrame(data)
    weights = np.array([1.0])
    stats = portfolio_stats(returns, weights)
    assert stats["return"] == round(returns.mean().iloc[0], 3)
    assert stats["volatility"] == round(returns.std().iloc[0], 3)
