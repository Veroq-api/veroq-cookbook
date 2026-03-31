// Search financial news
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const query = process.argv[2] || 'AI chip demand';
const result = await client.ask(`Latest news about ${query}`);

console.log(`=== News: ${query} ===\n`);
console.log(result.summary);

if (result.intent) {
  console.log(`\nIntent: ${result.intent}`);
}
console.log(`Response: ${result.response_time_ms}ms | Credits: ${result.credits_used}`);
