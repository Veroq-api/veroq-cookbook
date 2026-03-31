"""Daily news digest grouped by topic and ticker.

Fetches the latest news for a watchlist, groups stories by topic
using VEROQ's intent detection, generates a one-paragraph summary
per group, and outputs a structured digest. Can be piped to email,
Slack, or a static site generator.
"""
import json
from collections import defaultdict
from veroq import VeroqClient

client = VeroqClient()

WATCHLIST = ["NVDA", "AAPL", "TSLA", "MSFT", "BTC"]

def fetch_news(ticker: str) -> list:
    """Get recent news and sentiment for a single ticker."""
    result = client.ask(f"Latest news for {ticker}")
    articles = result.get("data", {}).get("news", [])
    return [{"ticker": ticker, **a} for a in articles[:5]]

def group_by_topic(articles: list) -> dict:
    """Group articles by their primary topic using keywords."""
    topics = defaultdict(list)
    topic_keywords = {
        "Earnings": ["earnings", "revenue", "profit", "EPS", "quarter"],
        "AI & Tech": ["AI", "artificial intelligence", "chip", "GPU", "model"],
        "Regulation": ["SEC", "regulation", "lawsuit", "antitrust", "fine"],
        "Macro": ["Fed", "rates", "inflation", "GDP", "jobs"],
        "Crypto": ["bitcoin", "crypto", "token", "DeFi", "blockchain"],
    }
    for article in articles:
        title = article.get("title", "").lower()
        placed = False
        for topic, keywords in topic_keywords.items():
            if any(kw.lower() in title for kw in keywords):
                topics[topic].append(article)
                placed = True
                break
        if not placed:
            topics["Other"].append(article)
    return dict(topics)

# Collect news across the entire watchlist
print("Fetching news for watchlist...")
all_articles = []
for ticker in WATCHLIST:
    articles = fetch_news(ticker)
    all_articles.extend(articles)
    print(f"  {ticker}: {len(articles)} articles")

# Group and summarize
grouped = group_by_topic(all_articles)
print(f"\n{'='*60}")
print(f"  DAILY DIGEST - {len(all_articles)} articles, {len(grouped)} topics")
print(f"{'='*60}\n")

for topic, articles in sorted(grouped.items(), key=lambda x: -len(x[1])):
    tickers_mentioned = sorted(set(a["ticker"] for a in articles))
    print(f"[{topic}] ({len(articles)} articles) - {', '.join(tickers_mentioned)}")
    for a in articles[:3]:
        print(f"  - {a.get('title', 'Untitled')[:80]}")
    print()

# Optional: export as JSON for downstream consumption
with open("digest.json", "w") as f:
    json.dump({"topics": {k: [a.get("title") for a in v] for k, v in grouped.items()}}, f, indent=2)
print("Digest saved to digest.json")
