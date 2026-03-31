"""Verified Swarm — 5 agents analyze a ticker with confidence scoring and verification receipts.

Demonstrates: POST /api/v1/swarm/run
Agents: planner -> researcher -> verifier -> critic -> synthesizer
Each step is verified before passing to the next. Budget caps prevent runaway costs.
"""
import os, sys, json, urllib.request, urllib.error

API_KEY = os.environ.get("VEROQ_API_KEY", "")
BASE = os.environ.get("VEROQ_BASE_URL", "https://api.veroq.ai")
TICKER = sys.argv[1] if len(sys.argv) > 1 else "NVDA"

if not API_KEY:
    print("Set VEROQ_API_KEY to run this example.")
    sys.exit(1)

# Step 1: Launch a verified swarm with all 5 agents
payload = json.dumps({
    "query": f"Analyze {TICKER} for a position",
    "roles": ["planner", "researcher", "verifier", "critic", "synthesizer"],
    "credit_budget": 25,
    "escalation_threshold": 70,
}).encode()

req = urllib.request.Request(
    f"{BASE}/api/v1/swarm/run",
    data=payload,
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
)

try:
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read())
except urllib.error.HTTPError as e:
    print(f"API error {e.code}: {e.read().decode()}")
    sys.exit(1)

# Step 2: Print each agent's step
print(f"Swarm session: {data.get('session_id', 'n/a')}\n")
for step in data.get("steps", []):
    role = step["role"].upper()
    conf = step.get("confidence", {})
    score = conf.get("score", conf.get("level", "?"))
    flag = " [ESCALATED]" if step.get("escalated") else ""
    print(f"  [{role}] confidence={score}{flag}")
    summary = step.get("summary", "")[:120]
    print(f"    {summary}{'...' if len(step.get('summary', '')) > 120 else ''}")
    print()

# Step 3: Show the final synthesis
synthesis = data.get("synthesis", {})
text = synthesis.get("summary", synthesis) if isinstance(synthesis, dict) else synthesis
print(f"SYNTHESIS:\n  {str(text)[:300]}\n")

# Step 4: Verification summary and budget
vs = data.get("verification_summary", {})
print(f"Verification: {vs.get('avg_confidence', '?')}% avg confidence, "
      f"{vs.get('flagged_steps', 0)} flagged / {vs.get('steps_total', vs.get('steps_verified', '?'))} steps")
print(f"Budget used: {data.get('total_credits_used', '?')} credits")
if data.get("escalated"):
    print("** Analysis was escalated for human review **")
