import feedparser
import ssl
import json
from datetime import datetime

# choose one topic, like the national games
topic = "the 15th national games of china"
#fronm the google news
rss_url = f"https://news.google.com/rss/search?q={topic.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# analyze the data
feed = feedparser.parse(rss_url)

print(f"Successfully find {len(feed.entries)} news!")

news_list = []
for entry in feed.entries[:20]: 
    news_item = {
        "title": entry.title,
        "link": entry.link,
        "published": entry.published,
        "source": entry.source.title if 'source' in entry else "Unknown",
        "summary_snippet": entry.summary if 'summary' in entry else "" 
    }
    news_list.append(news_item)

with open('national_games.json', 'w', encoding='utf-8') as f:
    json.dump(news_list, f, ensure_ascii=False, indent=4)

print("Data has been save as 'national_games.json' ")
