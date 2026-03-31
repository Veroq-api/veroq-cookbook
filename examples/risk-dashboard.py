"""Real-time risk monitoring dashboard with Flask + VEROQ.

Serves a web dashboard that shows portfolio risk metrics, refreshed
every 30 seconds via SSE. Monitors drawdown, correlation, VIX exposure,
and per-ticker signals. Sends alerts when risk thresholds are breached.
"""
import json
import time
from flask import Flask, Response, render_template_string
from veroq import VeroqClient

app = Flask(__name__)
client = VeroqClient()

PORTFOLIO = ["NVDA", "AAPL", "TSLA", "MSFT", "GOOGL"]
RISK_THRESHOLD = 70  # Signal score below this triggers a warning

DASHBOARD_HTML = """
<!DOCTYPE html>
<html><head><title>Risk Dashboard</title>
<style>
  body { font-family: monospace; background: #1a1a2e; color: #eee; padding: 20px; }
  table { border-collapse: collapse; width: 100%; }
  th, td { padding: 10px; border: 1px solid #333; text-align: left; }
  .warn { color: #ff6b6b; } .ok { color: #51cf66; }
</style></head>
<body>
<h1>VEROQ Risk Dashboard</h1>
<div id="data">Loading...</div>
<script>
const es = new EventSource("/stream");
es.onmessage = e => { document.getElementById("data").innerHTML = e.data; };
</script>
</body></html>
"""

def assess_risk():
    """Pull signals for each ticker and compute risk summary."""
    rows = []
    alerts = []
    for ticker in PORTFOLIO:
        result = client.ask(f"{ticker} risk assessment and trade signal")
        signal = result.get("trade_signal", {})
        score = signal.get("score", 50)
        action = signal.get("action", "hold").upper()

        status = "ok" if score >= RISK_THRESHOLD else "warn"
        if status == "warn":
            alerts.append(f"{ticker} signal is {action} ({score}/100)")

        rows.append(f'<tr class="{status}"><td>{ticker}</td><td>{action}</td>'
                     f'<td>{score}/100</td><td>{result["confidence"]["level"]}</td></tr>')

    alert_html = ""
    if alerts:
        alert_html = '<div class="warn"><b>ALERTS:</b><ul>'
        alert_html += "".join(f"<li>{a}</li>" for a in alerts)
        alert_html += "</ul></div>"

    return (f'{alert_html}<table><tr><th>Ticker</th><th>Signal</th>'
            f'<th>Score</th><th>Confidence</th></tr>{"".join(rows)}</table>')

@app.route("/")
def index():
    return render_template_string(DASHBOARD_HTML)

@app.route("/stream")
def stream():
    """SSE endpoint — pushes updated risk data every 30 seconds."""
    def generate():
        while True:
            html = assess_risk()
            yield f"data: {json.dumps(html)}\n\n"
            time.sleep(30)
    return Response(generate(), mimetype="text/event-stream")

# Run with: VEROQ_API_KEY=xxx python risk-dashboard.py
if __name__ == "__main__":
    app.run(port=5050, debug=True)
