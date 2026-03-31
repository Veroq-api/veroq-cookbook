"""Gold, oil, silver and other commodities."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("What are current commodity prices for gold, oil, and silver?")

data = result.get("data", {})
commodities = data.get("commodities", {}).get("prices", [])

if commodities:
    print("Commodity Prices\n")
    print(f"  {'Commodity':<16} {'Price':>10} {'Change':>8}")
    print(f"  {'-'*36}")
    for c in commodities:
        name = c.get("name", "?")
        price = c.get("price", 0)
        change = c.get("change_pct", 0)
        sign = "+" if change >= 0 else ""
        print(f"  {name:<16} ${price:>9,.2f} {sign}{change:.2f}%")
else:
    print(result.get("summary", "No commodity data available."))
