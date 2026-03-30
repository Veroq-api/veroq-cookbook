"""Compare multiple tickers side by side."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Compare AAPL vs MSFT vs GOOGL")
print(result["summary"])
