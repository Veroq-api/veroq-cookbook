"""See today's biggest gainers and losers."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("What are the biggest market movers today?")

data = result.get("data", {})
gainers = data.get("gainers", [])
losers = data.get("losers", [])

if gainers:
    print("TOP GAINERS")
    print("-" * 40)
    for g in gainers[:5]:
        print(f"  {g.get('ticker','?'):6s} | ${g.get('price','?'):>8} | +{g.get('change_pct','?')}%")

if losers:
    print("\nTOP LOSERS")
    print("-" * 40)
    for l in losers[:5]:
        print(f"  {l.get('ticker','?'):6s} | ${l.get('price','?'):>8} | {l.get('change_pct','?')}%")

if not gainers and not losers:
    print(result.get("summary", "No market mover data available."))
