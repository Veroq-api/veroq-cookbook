// Check insider trades for any ticker
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const ticker = process.argv[2] || 'AAPL';
const result = await client.ask(`Show me recent insider trades for ${ticker}`);

console.log(result.summary);

if (result.trade_signal) {
  const { action, score } = result.trade_signal;
  console.log(`\nSignal: ${action} (${score}/100)`);
}
