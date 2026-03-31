// Backtest an RSI strategy on any ticker
import { VeroqClient } from '@veroq/sdk';

const client = new VeroqClient();
const ticker = process.argv[2] || 'SPY';
const result = await client.ask(
  `Backtest an RSI strategy on ${ticker} — buy when RSI < 30, sell when RSI > 70`
);

console.log(result.summary);

if (result.endpoints_called?.includes('/backtest')) {
  console.log('\nBacktest engine was used for this analysis');
}
console.log(`Credits used: ${result.credits_used}`);
