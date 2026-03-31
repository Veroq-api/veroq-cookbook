"""Verify multiple claims at once."""
from veroq import VeroqClient

client = VeroqClient()

claims = [
    "Tesla delivered over 1.8 million vehicles in 2025",
    "The S&P 500 hit an all-time high in March 2026",
    "Bitcoin crossed $100,000 in 2025",
    "Amazon's AWS revenue exceeds $100 billion annually",
]

print("Batch Claim Verification\n")
print(f"  {'#':<3} {'Verdict':<14} {'Conf':>5}  Claim")
print(f"  {'-'*70}")

for i, claim in enumerate(claims, 1):
    result = client.verify(claim)
    verdict = result.get("verdict", "unknown").upper()
    confidence = result.get("confidence", 0)
    sources = len(result.get("evidence_chain", []))
    short = claim[:50] + ("..." if len(claim) > 50 else "")
    print(f"  {i:<3} {verdict:<14} {confidence*100:>4.0f}%  {short}")
    print(f"      Sources: {sources}")

print(f"\n  Verified {len(claims)} claims.")
