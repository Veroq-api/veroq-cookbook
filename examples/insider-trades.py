"""Check insider trades for any ticker."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Show me insider trades for AAPL")

trades = result.get("data", {}).get("insider", {}).get("trades", [])
if trades:
    print("Recent insider trades for AAPL:\n")
    for t in trades[:8]:
        direction = "BUY" if t.get("transaction_type", "").lower() == "purchase" else "SELL"
        name = t.get("insider_name", "Unknown")
        shares = t.get("shares", "?")
        value = t.get("value", 0)
        date = t.get("date", "?")
        print(f"  {date} | {name:25s} | {direction:4s} | {shares:>10s} shares | ${value:>12,.0f}")
else:
    print(result.get("summary", "No insider trade data found."))
