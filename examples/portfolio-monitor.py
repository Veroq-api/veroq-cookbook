"""Monitor a portfolio of tickers."""
from veroq import VeroqClient

client = VeroqClient()
portfolio = ["NVDA", "AAPL", "MSFT", "GOOGL", "TSLA"]

for ticker in portfolio:
    result = client.ask(f"{ticker} price and sentiment")
    data = result.get("data", {}).get("ticker", {})
    price = data.get("price", {})
    print(f"{ticker}: ${price.get('current', '?')} ({price.get('change_pct', '?')}%)")
