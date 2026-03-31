"""Backtest a simple RSI strategy."""
from veroq import VeroqClient

client = VeroqClient()
result = client.ask("Backtest RSI strategy on AAPL: buy when RSI < 30, sell when RSI > 70")

data = result.get("data", {})
backtest = data.get("backtest", {})

if backtest:
    perf = backtest.get("performance", {})
    print("Backtest Results: RSI Strategy on AAPL\n")
    print(f"  Total return:    {perf.get('total_return', '?')}%")
    print(f"  Sharpe ratio:    {perf.get('sharpe_ratio', '?')}")
    print(f"  Max drawdown:    {perf.get('max_drawdown', '?')}%")
    print(f"  Win rate:        {perf.get('win_rate', '?')}%")
    print(f"  Total trades:    {perf.get('total_trades', '?')}")
    print(f"  Period:          {backtest.get('period', '?')}")
    trades = backtest.get("trades", [])
    if trades:
        print(f"\nLast 5 trades:")
        for t in trades[-5:]:
            print(f"  {t.get('date','?')} | {t.get('action','?'):4s} @ ${t.get('price','?')}")
else:
    print(result.get("summary", "No backtest results available."))
