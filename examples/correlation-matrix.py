"""Compare how tickers move together."""
from veroq import VeroqClient

client = VeroqClient()
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]
result = client.ask(f"Show correlation matrix for {', '.join(tickers)}")

data = result.get("data", {})
matrix = data.get("correlation", {}).get("matrix", {})

if matrix:
    print("Correlation Matrix (90-day)\n")
    header = "          " + "  ".join(f"{t:>6}" for t in tickers)
    print(header)
    print("  " + "-" * (len(header) - 2))
    for t1 in tickers:
        row = matrix.get(t1, {})
        vals = "  ".join(f"{row.get(t2, 0):>6.2f}" for t2 in tickers)
        print(f"  {t1:<6}  {vals}")
    print("\n  1.00 = perfect correlation, -1.00 = inverse")
else:
    print(result.get("summary", "No correlation data available."))
