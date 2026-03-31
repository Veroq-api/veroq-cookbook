"""Price alert system with webhook delivery.

Monitors a list of tickers against user-defined conditions (price
thresholds, RSI levels, signal changes). When a condition triggers,
fires a webhook to Slack, Discord, or any HTTP endpoint. Designed
to run as a long-lived process or scheduled cron job.
"""
import os
import json
import time
import requests
from dataclasses import dataclass
from veroq import VeroqClient

client = VeroqClient()

# Webhook URL — set to your Slack incoming webhook, Discord webhook, or custom endpoint
WEBHOOK_URL = os.environ.get("ALERT_WEBHOOK_URL", "https://hooks.slack.com/services/xxx")

@dataclass
class Alert:
    ticker: str
    condition: str   # "price_above", "price_below", "rsi_below", "signal_change"
    threshold: float
    label: str

# Define your alerts — add as many as needed
alerts = [
    Alert("NVDA", "price_above", 950.0, "NVDA breakout above $950"),
    Alert("NVDA", "price_below", 800.0, "NVDA drops below $800"),
    Alert("AAPL", "rsi_below", 30.0, "AAPL oversold (RSI < 30)"),
    Alert("TSLA", "price_above", 300.0, "TSLA above $300"),
    Alert("BTC", "price_above", 100000.0, "Bitcoin above $100K"),
]

def fire_webhook(alert: Alert, current_value: float):
    """Send alert notification to the configured webhook."""
    payload = {
        "text": (
            f"VEROQ ALERT: {alert.label}\n"
            f"Ticker: {alert.ticker} | Condition: {alert.condition} | "
            f"Threshold: {alert.threshold} | Current: {current_value}"
        ),
    }
    try:
        resp = requests.post(WEBHOOK_URL, json=payload, timeout=10)
        print(f"  Webhook fired ({resp.status_code}): {alert.label}")
    except requests.RequestException as e:
        print(f"  Webhook failed: {e}")

def check_alerts():
    """Evaluate all alerts against current market data."""
    triggered = 0
    for alert in alerts:
        result = client.ask(f"{alert.ticker} price and RSI")
        data = result.get("data", {}).get("ticker", {})
        price = data.get("price", {}).get("current")
        rsi = data.get("technicals", {}).get("rsi")

        # Evaluate condition
        fired = False
        current = None
        if alert.condition == "price_above" and price and float(price) > alert.threshold:
            fired, current = True, price
        elif alert.condition == "price_below" and price and float(price) < alert.threshold:
            fired, current = True, price
        elif alert.condition == "rsi_below" and rsi and float(rsi) < alert.threshold:
            fired, current = True, rsi

        if fired:
            fire_webhook(alert, current)
            triggered += 1
        else:
            print(f"  {alert.ticker} {alert.condition}: OK (current={current or price})")

    return triggered

# Run once (for cron), or loop for continuous monitoring
print(f"Checking {len(alerts)} alerts...")
count = check_alerts()
print(f"\n{count} alert(s) triggered out of {len(alerts)}")
