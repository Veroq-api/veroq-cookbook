"""Ask any financial question — get structured intelligence."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("How is NVDA doing?")

print(result["summary"])
print(f"Confidence: {result['confidence']['level']}")
print(f"Trade signal: {result['trade_signal']['action']} ({result['trade_signal']['score']}/100)")
print(f"Endpoints called: {result['endpoints_called']}")
