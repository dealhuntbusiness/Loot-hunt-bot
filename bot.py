import os, requests, time, feedparser
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_ID", "@LootHuntDeals")
bot = Bot(token=TOKEN)

FEEDS = [
    "https://www.desidime.com/api/feed",
    "https://www.grabon.in/indulge/feed/",
]

sent = set()

def get_deals():
    deals = []
    for url in FEEDS:
        try:
            f = feedparser.parse(url)
            for e in f.entries[:5]:
                deals.append((e.title, e.link))
        except:
            pass
    return deals

def main():
    while True:
        for title, link in get_deals():
            if link not in sent:
                sent.add(link)
                msg = f"🔥 *LOOT ALERT* 🔥\n\n{title}\n\n👉 {link}\n\n#Loot #Deal"
                try:
                    bot.send_message(chat_id=CHANNEL, text=msg, parse_mode="Markdown")
                except Exception as e:
                    print(e)
        time.sleep(600)

if __name__ == "__main__":
    main()
