"""Offline, deterministic, no-wallet/no-exchange trading simulator."""
from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True)
class Candle:
    close: float

def simulate(prices: Iterable[float], starting_cash: float = 1000.0,
             fee_rate: float = 0.001, allocation: float = 0.10) -> dict:
    """SMA(5/20) crossover, spot-only, no borrowing; marks open position to market."""
    prices = list(prices)
    if len(prices) < 21 or any(p <= 0 for p in prices):
        raise ValueError("Need at least 21 positive closing prices")
    if starting_cash <= 0 or not (0 <= fee_rate < 1) or not (0 < allocation <= 1):
        raise ValueError("Invalid simulation parameters")
    cash, units, trades, peak, max_drawdown = starting_cash, 0.0, [], starting_cash, 0.0
    equity_curve = []
    previous_signal = None
    for i, price in enumerate(prices):
        if i >= 19:
            fast = sum(prices[i-4:i+1]) / 5
            slow = sum(prices[i-19:i+1]) / 20
            signal = fast > slow
            if previous_signal is not None and signal and not previous_signal and units == 0:
                budget = cash * allocation
                units = budget * (1 - fee_rate) / price
                cash -= budget
                trades.append({"index": i, "side": "buy", "price": price, "notional": budget})
            elif previous_signal is not None and not signal and previous_signal and units > 0:
                proceeds = units * price * (1 - fee_rate)
                cash += proceeds
                trades.append({"index": i, "side": "sell", "price": price, "net_proceeds": proceeds})
                units = 0.0
            previous_signal = signal
        equity = cash + units * price
        peak = max(peak, equity)
        max_drawdown = max(max_drawdown, (peak - equity) / peak)
        equity_curve.append(round(equity, 6))
    final_equity = cash + units * prices[-1]
    return {"mode": "offline_simulation", "starting_cash": starting_cash,
            "final_equity": round(final_equity, 2),
            "net_pnl": round(final_equity - starting_cash, 2),
            "return_pct": round((final_equity / starting_cash - 1) * 100, 2),
            "max_drawdown_pct": round(max_drawdown * 100, 2),
            "open_units": round(units, 8), "trades": trades,
            "equity_curve": equity_curve}
