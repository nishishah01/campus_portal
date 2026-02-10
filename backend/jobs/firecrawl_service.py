import os
from firecrawl import FirecrawlApp

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

if not FIRECRAWL_API_KEY:
    raise ValueError("FIRECRAWL_API_KEY not found")

app = FirecrawlApp(FIRECRAWL_API_KEY)

def scrape_career_page(url):
    result = app.scrape(url)

    # Firecrawl returns a dict with multiple formats
    # We safely extract markdown if present
    if isinstance(result, dict):
        return result.get("markdown", "")

    return ""
