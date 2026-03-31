// Scan an entire sector for opportunities
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const sector = process.argv[2] || 'semiconductors';
const result = await client.ask(`Scan the ${sector} sector — oversold stocks with strong fundamentals`);

console.log(result.summary);

if (result.endpoints_called?.length) {
  console.log(`\nEndpoints called: ${result.endpoints_called.length}`);
  console.log(`Credits used: ${result.credits_used}`);
}
