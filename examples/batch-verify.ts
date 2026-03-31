// Verify multiple claims in parallel
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();

const claims = [
  "NVIDIA is the most valuable company in the world",
  "Bitcoin hit an all-time high in 2026",
  "The Fed raised rates in March 2026",
];

const results = await Promise.all(claims.map((c) => client.verify(c)));

for (let i = 0; i < claims.length; i++) {
  const r = results[i];
  const pct = Math.round(r.confidence * 100);
  console.log(`${r.verdict.padEnd(12)} (${pct}%) — "${claims[i]}"`);
}
