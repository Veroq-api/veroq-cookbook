"""Break down why a verification is confident."""
from veroq import VeroqClient

client = VeroqClient()
result = client.verify("Apple is the most valuable company in the world by market cap")

verdict = result.get("verdict", "unknown")
confidence = result.get("confidence", 0)
breakdown = result.get("confidence_breakdown", {})

print(f"Claim: Apple is the most valuable company by market cap")
print(f"Verdict: {verdict.upper()}")
print(f"Overall Confidence: {confidence*100:.0f}%\n")

if breakdown:
    print("Confidence Breakdown:\n")
    max_key_len = max(len(k) for k in breakdown) if breakdown else 0
    for factor, score in sorted(breakdown.items(), key=lambda x: x[1], reverse=True):
        bar = "#" * int(score * 20)
        print(f"  {factor:<{max_key_len+2}} {score*100:>5.1f}%  {bar}")
else:
    print("No confidence breakdown available.")

reasoning = result.get("reasoning", "")
if reasoning:
    print(f"\nReasoning: {reasoning[:300]}")
