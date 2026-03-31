// Full evidence chain from /verify
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const claim = process.argv[2] || "Tesla deliveries dropped in Q1 2026";
const result = await client.verify(claim);

console.log(`Claim: "${claim}"`);
console.log(`Verdict: ${result.verdict} (${Math.round(result.confidence * 100)}% confidence)\n`);

for (const e of result.evidence_chain || []) {
  const snippet = e.snippet.length > 100 ? e.snippet.slice(0, 100) + '...' : e.snippet;
  console.log(`  [${e.position}] ${e.source}`);
  console.log(`       "${snippet}"`);
}
