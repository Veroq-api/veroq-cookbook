"""Slack bot with /ask and /verify slash commands.

Uses Slack's Bolt framework to handle slash commands. Responds
ephemerally first (so the user sees instant feedback), then posts
the full result to the channel with formatted blocks.
"""
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from veroq import VeroqClient

app = App(token=os.environ["SLACK_BOT_TOKEN"])
veroq = VeroqClient()

@app.command("/ask")
def handle_ask(ack, command, respond):
    """Handle /ask <financial question> slash command."""
    ack("Researching...")  # Immediate acknowledgment (Slack requires <3s)

    query = command["text"]
    result = veroq.ask(query)

    # Build Slack Block Kit message
    blocks = [
        {"type": "header", "text": {"type": "plain_text", "text": f"VEROQ: {query[:50]}"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": result["summary"][:2900]}},
    ]

    # Add trade signal as a context block
    signal = result.get("trade_signal", {})
    if signal:
        blocks.append({
            "type": "context",
            "elements": [{"type": "mrkdwn", "text": (
                f"*Signal:* {signal['action'].upper()} ({signal['score']}/100) | "
                f"*Confidence:* {result['confidence']['level']} | "
                f"*Time:* {result['response_time_ms']}ms"
            )}],
        })

    respond(blocks=blocks, response_type="in_channel")

@app.command("/verify")
def handle_verify(ack, command, respond):
    """Handle /verify <claim to fact-check> slash command."""
    ack("Verifying...")

    claim = command["text"]
    result = veroq.verify(claim)

    # Format evidence chain as bullet list
    evidence_lines = []
    for ev in result["evidence_chain"][:5]:
        evidence_lines.append(f"- *{ev['source']}*: {ev['snippet'][:150]}")

    verdict_icon = {"true": "Confirmed", "false": "Disputed", "unverified": "Unverified"}
    blocks = [
        {"type": "header", "text": {"type": "plain_text", "text": verdict_icon.get(result["verdict"], "?")}},
        {"type": "section", "text": {"type": "mrkdwn", "text": f"*Claim:* {claim}"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": f"*Confidence:* {result['confidence']*100:.0f}%"}},
        {"type": "section", "text": {"type": "mrkdwn", "text": "\n".join(evidence_lines)}},
    ]

    respond(blocks=blocks, response_type="in_channel")

# Run with: SLACK_BOT_TOKEN=xoxb-... SLACK_APP_TOKEN=xapp-... VEROQ_API_KEY=... python slack-bot.py
SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
