"""Natural language stock screener."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Find oversold semiconductor stocks with high sentiment")

for match in result.get("data", {}).get("screener", {}).get("results", []):
    print(f"{match['ticker']}: ${match.get('price', '?')} | RSI: {match.get('rsi', '?')}")
