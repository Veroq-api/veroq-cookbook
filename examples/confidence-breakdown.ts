// Confidence decomposition from verify
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const result = await client.verify("Apple will release a foldable iPhone in 2026");

console.log(`Verdict: ${result.verdict}`);
console.log(`Overall confidence: ${Math.round(result.confidence * 100)}%\n`);

if (result.confidence_breakdown) {
  for (const [factor, score] of Object.entries(result.confidence_breakdown)) {
    const bar = '█'.repeat(Math.round((score as number) * 20));
    console.log(`  ${factor.padEnd(20)} ${bar} ${Math.round((score as number) * 100)}%`);
  }
}

console.log(`\nSources checked: ${result.evidence_chain?.length || 0}`);
