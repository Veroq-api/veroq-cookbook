// See today's biggest gainers and losers
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const result = await client.ask("What are today's biggest market movers? Top gainers and losers");

console.log(result.summary);

if (result.intent) {
  console.log(`\nDetected intent: ${result.intent}`);
}
