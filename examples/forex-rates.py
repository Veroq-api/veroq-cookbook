"""Current forex rates for major pairs."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Show me major forex rates")

data = result.get("data", {})
forex = data.get("forex", {}).get("rates", [])

if forex:
    print("Major Forex Rates\n")
    print(f"  {'Pair':<10} {'Rate':>10} {'Change':>8}")
    print(f"  {'-'*30}")
    for pair in forex[:10]:
        symbol = pair.get("pair", "?")
        rate = pair.get("rate", 0)
        change = pair.get("change_pct", 0)
        sign = "+" if change >= 0 else ""
        print(f"  {symbol:<10} {rate:>10.4f} {sign}{change:.2f}%")
else:
    print(result.get("summary", "No forex data available."))
