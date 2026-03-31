// Get composite trade signal (0-100, 5 components)
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const ticker = process.argv[2] || 'NVDA';
const result = await client.ask(`What's the trade signal for ${ticker}?`);

console.log(result.summary);

if (result.trade_signal) {
  const { action, score, components } = result.trade_signal;
  console.log(`\n=== ${ticker} Trade Signal ===`);
  console.log(`Action: ${action}  Score: ${score}/100\n`);

  if (components) {
    for (const [name, value] of Object.entries(components)) {
      console.log(`  ${name.padEnd(16)} ${value}`);
    }
  }
}
