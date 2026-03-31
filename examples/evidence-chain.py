"""Verify a claim and show the full evidence chain."""
from veroq import VeroqClient

client = VeroqClient()
result = client.verify("NVIDIA revenue grew over 100% year-over-year in 2025")

verdict = result.get("verdict", "unknown")
confidence = result.get("confidence", 0)
chain = result.get("evidence_chain", [])

print(f"Claim: NVIDIA revenue grew over 100% YoY in 2025")
print(f"Verdict: {verdict.upper()} ({confidence*100:.0f}% confident)\n")

if chain:
    print(f"Evidence Chain ({len(chain)} sources):\n")
    for link in chain:
        pos = link.get("position", "?")
        source = link.get("source", "unknown")
        snippet = link.get("snippet", "")[:120]
        reliability = link.get("reliability", "?")
        print(f"  [{pos}] {source} (reliability: {reliability})")
        print(f"      \"{snippet}...\"\n")
else:
    print("No evidence chain available.")
    print(f"\nSummary: {result.get('summary', 'N/A')}")
