"""Find companies reporting earnings this week."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Who is reporting earnings this week?")

cal = result.get("data", {}).get("earnings_calendar", {}).get("earnings", [])
if cal:
    print(f"{len(cal)} companies reporting:\n")
    for e in cal[:10]:
        print(f"  {e.get('ticker','?'):6s} | {e.get('date','?')} | EPS est: {e.get('eps_estimate','?')}")
else:
    print(result.get("summary", "No earnings data available."))
