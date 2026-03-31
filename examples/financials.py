"""Get revenue, margins, and financial statements."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Show me AAPL financials and margins")

data = result.get("data", {})
financials = data.get("financials", {})

if financials:
    print("AAPL Financial Overview\n")
    income = financials.get("income_statement", {})
    if income:
        print("  Income Statement (latest)")
        print(f"    Revenue:        ${income.get('revenue', 0):>14,.0f}")
        print(f"    Net Income:     ${income.get('net_income', 0):>14,.0f}")
        print(f"    EPS:            ${income.get('eps', '?')}")
    margins = financials.get("margins", {})
    if margins:
        print("\n  Margins")
        print(f"    Gross:          {margins.get('gross', '?')}%")
        print(f"    Operating:      {margins.get('operating', '?')}%")
        print(f"    Net:            {margins.get('net', '?')}%")
    ratios = financials.get("ratios", {})
    if ratios:
        print("\n  Valuation")
        print(f"    P/E:            {ratios.get('pe', '?')}")
        print(f"    P/S:            {ratios.get('ps', '?')}")
        print(f"    Debt/Equity:    {ratios.get('debt_equity', '?')}")
else:
    print(result.get("summary", "No financial data available."))
