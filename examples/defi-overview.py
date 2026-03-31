"""DeFi TVL and top protocols."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("What is the current DeFi TVL and top protocols?")

data = result.get("data", {})
defi = data.get("defi", {})

if defi:
    tvl = defi.get("total_tvl", 0)
    print(f"Total DeFi TVL: ${tvl:,.0f}\n")
    protocols = defi.get("protocols", [])
    if protocols:
        print(f"  {'Protocol':<20} {'TVL':>14} {'Change 24h':>12}")
        print(f"  {'-'*48}")
        for p in protocols[:10]:
            name = p.get("name", "?")
            p_tvl = p.get("tvl", 0)
            change = p.get("change_24h", 0)
            sign = "+" if change >= 0 else ""
            print(f"  {name:<20} ${p_tvl:>13,.0f} {sign}{change:.1f}%")
else:
    print(result.get("summary", "No DeFi data available."))
