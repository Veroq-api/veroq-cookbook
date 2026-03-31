// Find companies reporting earnings this week
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const result = await client.ask("Who is reporting earnings this week?");

console.log(result.summary);

if (result.endpoints_called?.length) {
  console.log(`\nSources checked: ${result.endpoints_called.join(', ')}`);
}
