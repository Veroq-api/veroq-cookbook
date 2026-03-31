"""Get analyst consensus and price targets."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("What do analysts say about MSFT?")

analysts = result.get("data", {}).get("analysts", {})
if analysts:
    consensus = analysts.get("consensus", "N/A")
    target = analysts.get("price_target", {})
    print(f"MSFT Analyst Consensus: {consensus}\n")
    print(f"  Average target:  ${target.get('average', '?')}")
    print(f"  High target:     ${target.get('high', '?')}")
    print(f"  Low target:      ${target.get('low', '?')}")
    print(f"  Number of analysts: {analysts.get('count', '?')}\n")
    for r in analysts.get("recent_ratings", [])[:5]:
        print(f"  {r.get('date','?')} | {r.get('firm','?'):20s} | {r.get('rating','?')}")
else:
    print(result.get("summary", "No analyst data available."))
