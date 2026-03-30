"""Stream financial intelligence in real-time via SSE."""
from veroq import VeroqClient

client = VeroqClient()
for event in client.ask_stream("What is AAPL stock price and technicals?"):
    if event["type"] == "thinking":
        print(f"Analyzing: {event['data'].get('intents', [])}")
    elif event["type"] == "data":
        print(f"[{event['data']['key']}] loaded")
    elif event["type"] == "summary_token":
        print(event["data"]["token"], end="", flush=True)
    elif event["type"] == "done":
        print(f"\n\nDone in {event['data']['response_time_ms']}ms")
