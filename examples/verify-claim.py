"""Verify any claim with evidence chain and confidence breakdown."""
from veroq import VeroqClient

client = VeroqClient()
result = client.verify("The Federal Reserve held rates steady in March 2026")

print(f"Verdict: {result['verdict']} ({result['confidence']*100:.0f}%)")
print(f"\nConfidence breakdown:")
for k, v in result["confidence_breakdown"].items():
    print(f"  {k}: {v*100:.0f}%")
print(f"\nEvidence chain ({len(result['evidence_chain'])} sources):")
for e in result["evidence_chain"]:
    print(f"  [{e['position']}] {e['source']}: \"{e['snippet'][:80]}...\"")
