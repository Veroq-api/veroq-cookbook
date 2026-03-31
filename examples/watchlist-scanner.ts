// Scan a watchlist for signals
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const watchlist = ['AAPL', 'NVDA', 'TSLA', 'MSFT', 'AMZN'];

console.log('Scanning watchlist...\n');

const results = await Promise.all(
  watchlist.map((t) => client.ask(`Quick signal for ${t} — price, RSI, and sentiment`))
);

for (let i = 0; i < watchlist.length; i++) {
  const r = results[i];
  const sig = r.trade_signal;
  const label = sig ? `${sig.action} (${sig.score}/100)` : 'N/A';
  console.log(`${watchlist[i].padEnd(6)} ${label}`);
}
