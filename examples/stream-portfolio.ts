// Stream updates for a portfolio
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const portfolio = 'AAPL, NVDA, GOOGL, TSLA, BTC';

console.log(`Streaming analysis for: ${portfolio}\n`);

for await (const event of client.askStream(`Full portfolio review: ${portfolio}`)) {
  if (event.type === 'data') {
    console.log(`  [loaded] ${event.data.key}`);
  }
  if (event.type === 'summary_token') {
    process.stdout.write(event.data.token);
  }
  if (event.type === 'done') {
    console.log(`\n\nDone in ${event.data.response_time_ms}ms — ${event.data.credits_used} credits`);
  }
}
