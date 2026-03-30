"""Get composite trade signals for any ticker."""
from veroq import VeroqClient

client = VeroqClient()
for ticker in ["NVDA", "AAPL", "TSLA", "MSFT", "AMZN"]:
    result = client.ask(f"Trade signal for {ticker}")
    ts = result.get("trade_signal", {})
    if ts:
        print(f"{ticker}: {ts['action'].upper()} ({ts['score']}/100)")
        for f in ts.get("factors", [])[:2]:
            print(f"  - {f}")
