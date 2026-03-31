"""Export screener results to CSV for spreadsheet analysis.

Runs a natural language screen, enriches each match with trade signals,
and writes a clean CSV with ticker, price, RSI, sentiment, and signal.
Useful for importing into Excel, Google Sheets, or a backtest pipeline.
"""
import csv
import sys
from datetime import datetime
from veroq import VeroqClient

client = VeroqClient()

# Accept a screen query from the command line, or use a default
query = " ".join(sys.argv[1:]) or "oversold large cap tech stocks with high volume"
print(f"Screening: {query}")

# Run the NLP screener through /ask
result = client.ask(f"Screen for {query}")
matches = result.get("data", {}).get("screener", {}).get("results", [])

if not matches:
    print("No matches found. Try a different screen.")
    sys.exit(0)

# Enrich each match with a trade signal
rows = []
for match in matches:
    ticker = match["ticker"]
    signal_result = client.ask(f"Trade signal for {ticker}")
    ts = signal_result.get("trade_signal", {})

    rows.append({
        "ticker": ticker,
        "price": match.get("price", ""),
        "change_pct": match.get("change_pct", ""),
        "rsi": match.get("rsi", ""),
        "volume": match.get("volume", ""),
        "sector": match.get("sector", ""),
        "signal_action": ts.get("action", ""),
        "signal_score": ts.get("score", ""),
        "top_factor": ts.get("factors", [""])[0] if ts.get("factors") else "",
    })
    print(f"  {ticker}: {ts.get('action', '?')} ({ts.get('score', '?')}/100)")

# Write to CSV with timestamp in filename
filename = f"screen_{datetime.now():%Y%m%d_%H%M%S}.csv"
with open(filename, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"\nExported {len(rows)} results to {filename}")
