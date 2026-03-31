/**
 * Agent Runtime — Run the same query across finance, legal, and research verticals.
 *
 * Demonstrates: POST /api/v1/runtime/run
 * Each vertical applies domain-specific roles, safety rules, and escalation thresholds.
 * Compare how the same question produces different analysis through different lenses.
 */

const API_KEY = process.env.VEROQ_API_KEY ?? "";
const BASE = process.env.VEROQ_BASE_URL ?? "https://api.veroq.ai";

if (!API_KEY) {
  console.error("Set VEROQ_API_KEY to run this example.");
  process.exit(1);
}

const QUERY = process.argv[2] ?? "Analyze the risk of holding TSLA through earnings";
const VERTICALS = ["finance", "legal", "research"] as const;

interface RuntimeResult {
  vertical: string;
  runtime_info?: { cost_mode: string; credit_budget: number; escalation_threshold: number };
  synthesis?: { summary: string } | string;
  total_credits_used?: number;
  verification_summary?: { avg_confidence: number; flagged_steps: number };
  escalated?: boolean;
}

async function runVertical(vertical: string): Promise<RuntimeResult> {
  const res = await fetch(`${BASE}/api/v1/runtime/run`, {
    method: "POST",
    headers: { Authorization: `Bearer ${API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({ query: QUERY, vertical, credit_budget: 25 }),
    signal: AbortSignal.timeout(60_000),
  });
  if (!res.ok) throw new Error(`${vertical}: HTTP ${res.status}`);
  return res.json() as Promise<RuntimeResult>;
}

// Run all verticals in parallel, compare results
const results = await Promise.allSettled(VERTICALS.map(runVertical));

console.log(`Query: "${QUERY}"\n`);

for (let i = 0; i < VERTICALS.length; i++) {
  const vertical = VERTICALS[i].toUpperCase();
  const result = results[i];

  if (result.status === "rejected") {
    console.log(`[${vertical}] Error: ${result.reason}`);
    continue;
  }

  const d = result.value;
  const synthesis = typeof d.synthesis === "object" ? d.synthesis?.summary : d.synthesis;
  const snippet = (synthesis ?? "No synthesis").slice(0, 200);
  const vs = d.verification_summary;

  console.log(`[${vertical}]`);
  console.log(`  ${snippet}${(synthesis?.length ?? 0) > 200 ? "..." : ""}`);
  console.log(`  Confidence: ${vs?.avg_confidence ?? "?"}% | Credits: ${d.total_credits_used ?? "?"}` +
    `${vs?.flagged_steps ? ` | Flagged: ${vs.flagged_steps}` : ""}` +
    `${d.escalated ? " | ESCALATED" : ""}`);
  console.log();
}
