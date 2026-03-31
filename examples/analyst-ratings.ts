// Get analyst consensus and price targets
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const ticker = process.argv[2] || 'MSFT';
const result = await client.ask(`What do analysts say about ${ticker}? Price targets?`);

console.log(result.summary);
console.log(`\nResponse time: ${result.response_time_ms}ms`);
console.log(`Credits used: ${result.credits_used}`);
