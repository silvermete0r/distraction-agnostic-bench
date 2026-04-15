import os
import argparse
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

NEWSAPI_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = os.environ.get("NEWS_API_KEY")

def fetch_articles(query: str = "AI", page_size: int = 100) -> list[dict]:
    """Fetch up to page_size articles sorted by popularity from NewsAPI."""
    if not API_KEY:
        raise ValueError("NEWS_API_KEY is missing. Check your .env file.")

    from_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

    params = {
        "q": query,
        "from": from_date,
        "sortBy": "popularity",
        "language": "en",      
        "apiKey": API_KEY,
        "pageSize": min(page_size, 100),
        "page": 1
    }

    try:
        response = requests.get(NEWSAPI_ENDPOINT, params=params, timeout=15)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Network error while reaching NewsAPI: {e}")

    data = response.json()

    if data.get("status") != "ok":
        raise RuntimeError(f"NewsAPI error: {data.get('message', 'unknown error')}")

    articles = data.get("articles", [])
    print(f"Fetched {len(articles)} articles (total available: {data.get('totalResults', '?')})")
    return articles


def format_article(idx: int, article: dict) -> str:
    """Format a single article into the required <message> XML line."""
    source  = (article.get("source") or {}).get("name") or "Unknown Source"
    author  = article.get("author") or "Unknown Author"
    pub_at  = article.get("publishedAt") or ""
    title   = (article.get("title") or "").replace("\n", " ").strip()
    desc    = (article.get("description") or "").replace("\n", " ").strip()
 
    def attr(value: str) -> str:
        return value.replace("&", "&amp;").replace('"', "&quot;")
 
    body = f"{title} | {desc}"
 
    return (
        f'<message source="{attr(source)}" author="{attr(author)}" publishedAt="{attr(pub_at)}">'
        f"{body}"
        f"</message>"
    )


def write_output(articles: list[dict], output_path: str) -> None:
    lines = []
    for idx, article in enumerate(articles):
        lines.append(format_article(idx, article))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Wrote {len(lines)} articles to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Fetch 100 popular news articles via NewsAPI")

    parser.add_argument(
        "--output",
        default="data/news_output.txt",
        help="Path for the output .txt file (default: news_output.txt)",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=100,
        help="Number of articles to fetch, max 100 (default: 100)",
    )

    parser.add_argument(
        "--query",
        type=str,
        default="AI",
        help="Keyword to search for (default: 'AI')",
    )

    args = parser.parse_args()
    
    articles = fetch_articles(query=args.query, page_size=args.count)
    write_output(articles, args.output)

if __name__ == "__main__":
    main()