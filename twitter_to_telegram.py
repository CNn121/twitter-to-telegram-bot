import time
import feedparser
import requests

# === Configuration ===
RSS_FEED = 'https://nitter.poast.org/DegenCapitalLLC/rss'  # You can replace this with another working Nitter instance
TELEGRAM_TOKEN = '8197633731:AAFY6e8h_9ITemvwOmWZt1Io3J2RnyntVZA'  # From @BotFather
CHAT_ID = '637263381','637263381'  # From @userinfobot
CHECK_INTERVAL = 60  # In seconds (set to 120 for every 2 min)

last_tweet = None

def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': text}
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print("❌ Failed to send message:", response.text)
    else:
        print("✅ Message sent")

while True:
    try:
        feed = feedparser.parse(RSS_FEED)
        if not feed.entries:
            print("⚠️ No tweets found.")
        else:
            latest = feed.entries[0]
            if latest.link != last_tweet:
                last_tweet = latest.link
                message = f"🕊 New tweet from {latest.author}:\n{latest.title}\n{latest.link}"
                send_telegram_message(message)
        time.sleep(CHECK_INTERVAL)
    except Exception as e:
        print("🔥 Error:", e)
        time.sleep(CHECK_INTERVAL)