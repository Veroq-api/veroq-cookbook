"""Get bull and bear case for any stock."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Give me the bull and bear case for TSLA")

data = result.get("data", {})
trade_signal = result.get("trade_signal", {})

print("TSLA Bull vs Bear Analysis\n")

if trade_signal:
    score = trade_signal.get("score", "?")
    action = trade_signal.get("action", "?").upper()
    print(f"  Overall Signal: {action} ({score}/100)\n")
    factors = trade_signal.get("factors", [])
    if factors:
        print("  Key Factors:")
        for f in factors:
            print(f"    - {f}")

summary = result.get("summary", "")
if summary:
    print(f"\n  Analysis:\n  {summary[:500]}")
