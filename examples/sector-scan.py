"""Scan an entire sector for opportunities."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Find undervalued tech stocks with strong momentum")

screener = result.get("data", {}).get("screener", {})
matches = screener.get("results", [])

if matches:
    print(f"Found {len(matches)} matches:\n")
    print(f"  {'Ticker':<8} {'Price':>8} {'RSI':>6} {'Change':>8} {'Signal':>8}")
    print(f"  {'-'*42}")
    for m in matches[:10]:
        ticker = m.get("ticker", "?")
        price = m.get("price", "?")
        rsi = m.get("rsi", "?")
        change = m.get("change_pct", "?")
        signal = m.get("signal", "?")
        print(f"  {ticker:<8} ${price:>7} {rsi:>6} {change:>7}% {signal:>8}")
    reasons = screener.get("match_reasons", {})
    if reasons:
        print("\nWhy these matched:")
        for ticker, reason in list(reasons.items())[:3]:
            print(f"  {ticker}: {reason}")
else:
    print(result.get("summary", "No sector scan results."))
