// Major forex pairs
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const result = await client.ask("What are the current major forex rates? EUR/USD, GBP/USD, USD/JPY");

console.log(result.summary);
console.log(`\nResponse time: ${result.response_time_ms}ms`);
