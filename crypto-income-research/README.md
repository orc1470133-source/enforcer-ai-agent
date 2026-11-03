# Crypto Income Research Agent (Paper Trading)

This starter provides a **deterministic trend strategy, not a trained AI agent**. Freqtrade can backtest and dry-run it. Add FreqAI as a separate, reviewed phase once a non-ML baseline is established.

Default mode: dry-run; spot only; no credentials; no guarantee of income.

## Install and test
1. Install Docker and follow https://www.freqtrade.io/en/stable/docker_quickstart/ to initialize the official docker-compose environment and user_data.
2. Copy ConservativeTrend.py to user_data/strategies and config.example.json to user_data/config.json.
3. Check that your chosen exchange supports the configured BTC/USDT and ETH/USDT pairs in your jurisdiction. No keys are required for dry-run public data.
4. Download candles: docker compose run --rm freqtrade download-data --config user_data/config.json --timeframes 1h --days 365
5. Backtest: docker compose run --rm freqtrade backtesting --config user_data/config.json --strategy ConservativeTrend --enable-protections
6. Paper run: docker compose run --rm freqtrade trade --config user_data/config.json --strategy ConservativeTrend

Review the Freqtrade documentation for version-specific command details. Observe out-of-sample performance, net P&L, fees, max drawdown and simulated-versus-actual slippage. Paper trade for at least 30 days. No strategy is production-validated. Stop-loss orders can execute worse than requested. Live execution is not configured or approved.

FreqAI reference: https://docs.freqtrade.io/en/stable/freqai/ . The bundled FreqAI demonstration strategy is not for production.
