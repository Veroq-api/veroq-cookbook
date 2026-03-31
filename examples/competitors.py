"""Find a company's main competitors."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Who are NVDA's main competitors?")

data = result.get("data", {})
competitors = data.get("competitors", {}).get("companies", [])

if competitors:
    print("NVDA Competitors\n")
    print(f"  {'Company':<20} {'Ticker':>6} {'Price':>10} {'Mkt Cap':>14}")
    print(f"  {'-'*54}")
    for c in competitors:
        name = c.get("name", "?")
        ticker = c.get("ticker", "?")
        price = c.get("price", 0)
        mcap = c.get("market_cap", 0)
        print(f"  {name:<20} {ticker:>6} ${price:>9,.2f} ${mcap:>13,.0f}")
else:
    print(result.get("summary", "No competitor data available."))
