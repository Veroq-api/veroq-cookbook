// Top crypto prices
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const result = await client.ask("Show me the top 10 crypto prices — BTC, ETH, SOL, and others");

console.log(result.summary);

if (result.trade_signal) {
  console.log(`\nBTC signal: ${result.trade_signal.action} (${result.trade_signal.score}/100)`);
}
