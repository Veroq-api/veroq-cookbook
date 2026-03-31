// Complete cross-reference analysis (9 sources in parallel)
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const ticker = process.argv[2] || 'AAPL';

console.log(`Running full cross-reference analysis for ${ticker}...\n`);

for await (const event of client.askStream(`Full analysis of ${ticker} — everything you have`)) {
  if (event.type === 'data') {
    console.log(`  [${event.data.key}] loaded`);
  }
  if (event.type === 'summary_token') {
    process.stdout.write(event.data.token);
  }
  if (event.type === 'done') {
    const { response_time_ms, credits_used, endpoints_called } = event.data;
    console.log(`\n\n--- ${endpoints_called?.length || '?'} endpoints | ${response_time_ms}ms | ${credits_used} credits ---`);
  }
}
