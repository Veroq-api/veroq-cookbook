"""Enterprise Governance — audit trails, decision lineage, and escalation detection.

Demonstrates: /swarm/run with enterprise_id, /feedback for flagging issues.
Shows how high-stakes decisions trigger escalation and how every step in the
pipeline produces a verifiable audit trail with confidence decomposition.
"""
import os, sys, json, urllib.request, urllib.error

API_KEY = os.environ.get("VEROQ_API_KEY", "")
BASE = os.environ.get("VEROQ_BASE_URL", "https://api.veroq.ai")
ENTERPRISE_ID = os.environ.get("VEROQ_ENTERPRISE_ID", "demo-enterprise")

if not API_KEY:
    print("Set VEROQ_API_KEY to run this example.")
    sys.exit(1)

def api_post(path: str, body: dict) -> dict:
    req = urllib.request.Request(
        f"{BASE}{path}",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())

# Step 1: Run a high-stakes analysis with enterprise audit trail
# Low escalation threshold (90%) means anything below 90% confidence gets flagged
print("Running swarm with enterprise governance...\n")
try:
    result = api_post("/api/v1/swarm/run", {
        "query": "Should we increase our AAPL position by $5M given current macro conditions?",
        "enterprise_id": ENTERPRISE_ID,
        "escalation_threshold": 90,
        "credit_budget": 25,
    })
except urllib.error.HTTPError as e:
    print(f"API error {e.code}: {e.read().decode()}")
    sys.exit(1)

session_id = result.get("session_id", "unknown")
print(f"Session: {session_id}")
print(f"Escalated: {'YES — requires human review' if result.get('escalated') else 'No'}\n")

# Step 2: Decision lineage — trace every agent's contribution
print("Decision lineage:")
for step in result.get("steps", []):
    conf = step.get("confidence", {})
    score = conf.get("score", conf.get("level", "?"))
    credits = step.get("credits_used", 0)
    escalated = step.get("escalated", False)
    marker = " ** BELOW THRESHOLD **" if escalated else ""
    print(f"  {step['role']:>12s}  confidence={score:<6s} credits={credits}{marker}")

# Step 3: Verification summary — the audit record
vs = result.get("verification_summary", {})
print(f"\nAudit summary:")
print(f"  Avg confidence:  {vs.get('avg_confidence', '?')}%")
print(f"  Steps verified:  {vs.get('steps_verified', vs.get('steps_total', '?'))}")
print(f"  Flagged steps:   {vs.get('flagged_steps', 0)}")
print(f"  Total credits:   {result.get('total_credits_used', '?')}")
print(f"  Enterprise ID:   {ENTERPRISE_ID}")

# Step 4: Submit feedback if escalated — feeds the self-improvement loop
if result.get("escalated") or vs.get("flagged_steps", 0) > 0:
    print("\nSubmitting governance feedback...")
    try:
        fb = api_post("/api/v1/feedback", {
            "session_id": session_id,
            "query": "AAPL $5M position increase",
            "reason": "low_confidence",
            "detail": "High-stakes decision flagged below 90% threshold",
            "enterprise_id": ENTERPRISE_ID,
        })
        print(f"  Feedback logged: {fb.get('feedback_id', 'ok')}")
    except Exception as e:
        print(f"  Feedback submission failed: {e}")
