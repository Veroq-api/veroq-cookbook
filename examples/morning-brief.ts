// Morning market briefing
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const result = await client.ask(
  "Give me a morning market briefing — indices, key movers, and any major news"
);

console.log('=== Morning Brief ===\n');
console.log(result.summary);

if (result.endpoints_called?.length) {
  console.log(`\n--- ${result.endpoints_called.length} sources checked in ${result.response_time_ms}ms ---`);
}
