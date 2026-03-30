import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
for await (const event of client.askStream("AAPL price and technicals")) {
  if (event.type === "data") console.log(`[${event.data.key}] loaded`);
  if (event.type === "summary_token") process.stdout.write(event.data.token);
  if (event.type === "done") console.log(`\nDone in ${event.data.response_time_ms}ms`);
}
