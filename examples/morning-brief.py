"""Generate a morning market briefing."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Give me a morning market briefing with indices, sectors, and key news")

data = result.get("data", {})
summary = result.get("summary", "")

print("=" * 60)
print("  MORNING MARKET BRIEFING")
print("=" * 60)

indices = data.get("market", {}).get("indices", [])
if indices:
    print("\n  Market Indices:")
    for idx in indices:
        name = idx.get("name", "?")
        value = idx.get("value", 0)
        change = idx.get("change_pct", 0)
        sign = "+" if change >= 0 else ""
        print(f"    {name:<16} {value:>10,.2f}  {sign}{change:.2f}%")

news = data.get("news", {}).get("articles", [])
if news:
    print("\n  Top Headlines:")
    for n in news[:5]:
        print(f"    - {n.get('title', '?')[:70]}")

if summary:
    print(f"\n  Summary:\n  {summary[:400]}")

print("\n" + "=" * 60)
