import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const result = await client.ask("How is NVDA doing?");

console.log(result.summary);
console.log(`Trade signal: ${result.trade_signal?.action} (${result.trade_signal?.score}/100)`);
