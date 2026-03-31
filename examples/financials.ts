// Financial statements overview
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const ticker = process.argv[2] || 'AMZN';
const result = await client.ask(
  `Show me ${ticker}'s latest financials — revenue, margins, and cash flow`
);

console.log(result.summary);
console.log(`\nEndpoints used: ${result.endpoints_called?.join(', ') || 'N/A'}`);
