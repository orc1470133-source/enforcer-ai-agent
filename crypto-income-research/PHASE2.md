# Phase 2 — Offline prototypes (no financial transactions)

This phase adds a **standard-library-only** deterministic spot trading simulator and an ACP-compatible *service concept*, not an authenticated ACP implementation.

## Run locally

From the `crypto-income-research` directory:

```bash
python -m unittest discover -s tests -v
python marketplace.py
python -c "from simulator import simulate; print(simulate([100+(i%20)*2 for i in range(100)]))"
```

The simulator uses a simple 5/20-period moving-average crossover, 10% cash allocation per entry and a 0.1% fee assumption per fill. This is illustrative, not a predictive AI model. It does **not** model order book slippage, spreads, funding, taxes, data latency, liquidity, outages or live fills. Results are not indicative of real returns.

The marketplace module drafts a hypothetical $5 educational research offering and generates a report from **supplied demo prices**. It does not connect to ACP, list services, accept payments, or create a wallet.

## Next gated milestones

1. Add licensed historical data fixtures and walk-forward backtesting with realistic costs and no look-ahead.
2. Evaluate a FreqAI model against the deterministic baseline, avoiding leakage.
3. Add ACP CLI read-only discovery and validate service schema against the installed upstream CLI.
4. Build a dashboard separating simulated P&L from *actual settled* service revenue (currently zero).
5. Require separate approval before any wallet, exchange key, paid listing or live order is enabled.
