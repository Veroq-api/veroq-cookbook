// Company competitor analysis
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const ticker = process.argv[2] || 'TSLA';
const result = await client.ask(`Who are ${ticker}'s main competitors and how do they compare?`);

console.log(result.summary);

if (result.trade_signal) {
  const { action, score } = result.trade_signal;
  console.log(`\n${ticker} signal: ${action} (${score}/100)`);
}
