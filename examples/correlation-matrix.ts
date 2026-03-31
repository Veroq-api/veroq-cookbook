// Ticker correlation analysis
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const result = await client.ask(
  "Show me the correlation between AAPL, MSFT, GOOGL, and AMZN over the past 90 days"
);

console.log(result.summary);

if (result.intent) {
  console.log(`\nIntent: ${result.intent}`);
  console.log(`Credits: ${result.credits_used}`);
}
