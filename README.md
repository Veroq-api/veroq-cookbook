# VEROQ Cookbook

[![License](https://img.shields.io/badge/license-MIT-2EE89A)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-2EE89A)](https://python.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-2EE89A)](https://typescriptlang.org)
[![VEROQ](https://img.shields.io/badge/powered%20by-VEROQ-2EE89A)](https://veroq.ai)

**60 ready-to-run examples** for building with [VEROQ](https://veroq.ai) — the trust protocol for agentic AI.

## Quick Start

```bash
pip install veroq                    # Python
npm install @veroq/sdk               # TypeScript
export VEROQ_API_KEY=vq_live_xxx     # free at veroq.ai/pricing

python examples/ask-anything.py
```

## Examples

### Ask & Verify

| Example | Description | |
|---------|-------------|--|
| [ask-anything](examples/ask-anything.py) | Ask any financial question | [py](examples/ask-anything.py) · [ts](examples/ask-anything.ts) |
| [verify-claim](examples/verify-claim.py) | Fact-check with evidence chain | [py](examples/verify-claim.py) · [ts](examples/verify-claim.ts) |
| [stream-sse](examples/stream-sse.py) | Real-time SSE streaming | [py](examples/stream-sse.py) · [ts](examples/stream-sse.ts) |
| [evidence-chain](examples/evidence-chain.py) | Full source provenance | [py](examples/evidence-chain.py) · [ts](examples/evidence-chain.ts) |
| [confidence-breakdown](examples/confidence-breakdown.py) | Decomposed confidence scores | [py](examples/confidence-breakdown.py) · [ts](examples/confidence-breakdown.ts) |
| [batch-verify](examples/batch-verify.py) | Verify multiple claims | [py](examples/batch-verify.py) · [ts](examples/batch-verify.ts) |

### Trading & Signals

| Example | Description | |
|---------|-------------|--|
| [trading-signals](examples/trading-signals.py) | Composite trade signals (0-100) | [py](examples/trading-signals.py) · [ts](examples/trade-signal.ts) |
| [watchlist-scanner](examples/watchlist-scanner.py) | Scan a watchlist | [py](examples/watchlist-scanner.py) · [ts](examples/watchlist-scanner.ts) |
| [screener](examples/screener.py) | NLP stock screener | [py](examples/screener.py) |
| [backtest-strategy](examples/backtest-strategy.py) | Backtest RSI strategy | [py](examples/backtest-strategy.py) · [ts](examples/backtest-strategy.ts) |
| [correlation-matrix](examples/correlation-matrix.py) | How tickers move together | [py](examples/correlation-matrix.py) · [ts](examples/correlation-matrix.ts) |
| [bull-bear-debate](examples/bull-bear-debate.py) | Bull vs bear for any stock | [py](examples/bull-bear-debate.py) |

### Market Data

| Example | Description | |
|---------|-------------|--|
| [market-movers](examples/market-movers.py) | Biggest gainers and losers | [py](examples/market-movers.py) · [ts](examples/market-movers.ts) |
| [earnings-calendar](examples/earnings-calendar.py) | Who reports this week | [py](examples/earnings-calendar.py) · [ts](examples/earnings-calendar.ts) |
| [insider-trades](examples/insider-trades.py) | SEC Form 4 insider activity | [py](examples/insider-trades.py) · [ts](examples/insider-trades.ts) |
| [analyst-ratings](examples/analyst-ratings.py) | Consensus + price targets | [py](examples/analyst-ratings.py) · [ts](examples/analyst-ratings.ts) |
| [competitors](examples/competitors.py) | Company competitors | [py](examples/competitors.py) · [ts](examples/competitors.ts) |
| [financials](examples/financials.py) | Revenue, margins, P/E | [py](examples/financials.py) · [ts](examples/financials.ts) |
| [sector-scan](examples/sector-scan.py) | Scan an entire sector | [py](examples/sector-scan.py) · [ts](examples/sector-scan.ts) |

### Crypto, Forex & Economy

| Example | Description | |
|---------|-------------|--|
| [crypto-prices](examples/crypto-prices.py) | Top crypto + 24h changes | [py](examples/crypto-prices.py) · [ts](examples/crypto-prices.ts) |
| [defi-overview](examples/defi-overview.py) | DeFi TVL and protocols | [py](examples/defi-overview.py) |
| [forex-rates](examples/forex-rates.py) | Major forex pairs | [py](examples/forex-rates.py) · [ts](examples/forex-rates.ts) |
| [commodity-prices](examples/commodity-prices.py) | Gold, oil, silver | [py](examples/commodity-prices.py) |
| [treasury-yields](examples/treasury-yields.py) | US yield curve | [py](examples/treasury-yields.py) |

### Portfolio & Monitoring

| Example | Description | |
|---------|-------------|--|
| [portfolio-monitor](examples/portfolio-monitor.py) | Monitor portfolio tickers | [py](examples/portfolio-monitor.py) |
| [multi-ticker](examples/multi-ticker.py) | Compare multiple tickers | [py](examples/multi-ticker.py) |
| [morning-brief](examples/morning-brief.py) | Daily market briefing | [py](examples/morning-brief.py) · [ts](examples/morning-brief.ts) |
| [stream-portfolio](examples/stream-portfolio.ts) | SSE streaming for portfolio | [ts](examples/stream-portfolio.ts) |
| [full-analysis](examples/full-analysis.ts) | Cross-reference streamed | [ts](examples/full-analysis.ts) |
| [news-search](examples/news-search.ts) | Search financial news | [ts](examples/news-search.ts) |

### Integrations

| Example | What it does |
|---------|-------------|
| [langchain-agent](examples/langchain-agent.py) | LangChain agent with VEROQ tools |
| [crewai-team](examples/crewai-team.py) | CrewAI multi-agent team |
| [discord-bot](examples/discord-bot.py) | Discord bot (!ask, !verify) |
| [slack-bot](examples/slack-bot.py) | Slack bot (/ask, /verify) |
| [telegram-webhook](examples/telegram-webhook.py) | Telegram bot |
| [csv-export](examples/csv-export.py) | Export screener to CSV |
| [scheduled-report](examples/scheduled-report.py) | Daily email reports |
| [risk-dashboard](examples/risk-dashboard.py) | Real-time risk monitoring |
| [news-digest](examples/news-digest.py) | Daily news digest by topic |
| [alert-system](examples/alert-system.py) | Price alerts with webhooks |

## Links

- [VEROQ](https://veroq.ai) — Interactive demos
- [API Reference](https://veroq.ai/api-reference) — 300+ endpoints
- [Python SDK](https://github.com/Veroq-api/veroq-python)
- [TypeScript SDK](https://github.com/Veroq-api/veroq-js)
- [MCP Server](https://github.com/Veroq-api/veroq-mcp)

Free tier: 1,000 credits/month. No credit card.
