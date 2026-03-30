import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const result = await client.verify("NVIDIA beat Q4 earnings expectations");

console.log(`Verdict: ${result.verdict} (${Math.round(result.confidence * 100)}%)`);
for (const e of result.evidence_chain || []) {
  console.log(`  [${e.position}] ${e.source}: "${e.snippet.slice(0, 80)}..."`);
}
