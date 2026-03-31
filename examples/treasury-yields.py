"""US treasury yield curve."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Show me the current US treasury yield curve")

data = result.get("data", {})
yields_data = data.get("yields", {}).get("curve", [])

if yields_data:
    print("US Treasury Yield Curve\n")
    print(f"  {'Maturity':<12} {'Yield':>8} {'Change':>8}")
    print(f"  {'-'*30}")
    for y in yields_data:
        maturity = y.get("maturity", "?")
        rate = y.get("yield", 0)
        change = y.get("change", 0)
        sign = "+" if change >= 0 else ""
        print(f"  {maturity:<12} {rate:>7.3f}% {sign}{change:.3f}%")
    spread = data.get("yields", {}).get("ten_two_spread")
    if spread is not None:
        status = "NORMAL" if spread > 0 else "INVERTED"
        print(f"\n  10Y-2Y Spread: {spread:.3f}% ({status})")
else:
    print(result.get("summary", "No yield data available."))
