"""Get top crypto prices with 24h changes."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Show me top crypto prices")

data = result.get("data", {})
crypto = data.get("crypto", {}).get("prices", [])

if crypto:
    print(f"{'Token':<10} {'Price':>12} {'24h':>8} {'Market Cap':>14}")
    print("-" * 48)
    for c in crypto[:10]:
        symbol = c.get("symbol", "?")
        price = c.get("price", 0)
        change = c.get("change_24h", 0)
        mcap = c.get("market_cap", 0)
        sign = "+" if change >= 0 else ""
        print(f"  {symbol:<8} ${price:>11,.2f} {sign}{change:>6.1f}% ${mcap:>12,.0f}")
else:
    print(result.get("summary", "No crypto price data available."))
