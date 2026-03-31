"""Scan a watchlist of tickers for signals."""
from veroq import VeroqClient

client = VeroqClient()
watchlist = ["AAPL", "NVDA", "TSLA", "AMD", "META", "AMZN", "GOOGL", "NFLX"]

print("Watchlist Scanner\n")
print(f"  {'Ticker':<7} {'Price':>9} {'Change':>8} {'RSI':>6} {'Signal':>8} {'Score':>6}")
print(f"  {'-'*50}")

alerts = []
for ticker in watchlist:
    result = client.ask(f"{ticker} price and trade signal")
    data = result.get("data", {}).get("ticker", {})
    price_info = data.get("price", {})
    ts = result.get("trade_signal", {})
    price = price_info.get("current", "?")
    change = price_info.get("change_pct", "?")
    rsi = data.get("technicals", {}).get("rsi", "?")
    action = ts.get("action", "?").upper()
    score = ts.get("score", "?")
    print(f"  {ticker:<7} ${price:>8} {change:>7}% {rsi:>6} {action:>8} {score:>5}")
    if isinstance(score, (int, float)) and (score >= 75 or score <= 25):
        alerts.append((ticker, action, score))

if alerts:
    print(f"\nAlerts:")
    for t, a, s in alerts:
        print(f"  {t}: {a} signal (score: {s}/100)")
