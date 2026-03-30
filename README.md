# VEROQ Cookbook

[![License](https://img.shields.io/badge/license-MIT-2EE89A)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-2EE89A)](https://python.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-2EE89A)](https://typescriptlang.org)
[![VEROQ](https://img.shields.io/badge/powered%20by-VEROQ-2EE89A)](https://veroq.ai)

Code examples and recipes for building with [VEROQ](https://veroq.ai) — the trust protocol for agentic AI.

## Quick Start

```python
from veroq import VeroqClient
client = VeroqClient()  # uses VEROQ_API_KEY env var

answer = client.ask("How is NVDA doing?")
print(answer["summary"])
```

## Examples

| Example | Description | Language |
|---------|-------------|----------|
| [ask-anything.py](examples/ask-anything.py) | Ask any financial question | Python |
| [verify-claim.py](examples/verify-claim.py) | Fact-check with evidence chain | Python |
| [stream-sse.py](examples/stream-sse.py) | Real-time SSE streaming | Python |
| [trading-signals.py](examples/trading-signals.py) | Composite trade signals | Python |
| [ask-anything.ts](examples/ask-anything.ts) | Ask any financial question | TypeScript |
| [verify-claim.ts](examples/verify-claim.ts) | Fact-check with evidence chain | TypeScript |
| [stream-sse.ts](examples/stream-sse.ts) | Real-time SSE streaming | TypeScript |
| [portfolio-monitor.py](examples/portfolio-monitor.py) | Monitor a portfolio | Python |
| [screener.py](examples/screener.py) | NLP stock screener | Python |
| [multi-ticker.py](examples/multi-ticker.py) | Compare multiple tickers | Python |

## Get Started

1. Get a free API key at [veroq.ai/pricing](https://veroq.ai/pricing)
2. `export VEROQ_API_KEY=vq_live_xxx`
3. `pip install veroq` or `npm install @veroq/sdk`

## Links

- [API Documentation](https://veroq.ai/docs)
- [API Reference](https://veroq.ai/api-reference)
- [Python SDK](https://github.com/Veroq-api/veroq-python)
- [TypeScript SDK](https://github.com/Veroq-api/veroq-js)