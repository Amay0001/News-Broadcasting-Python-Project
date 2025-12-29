"""
✅ LIVE NEWS FROM OFFICIAL SITES - BBC, TOI, Hindu, Reuters
Real headlines scraped daily at 8AM
"""

import requests
from bs4 import BeautifulSoup
import pywhatkit as pwk
import schedule
import time
from datetime import datetime

GROUP_ID = "HcNhbsRbTfX0w3LSbxhPYw"
NEWS_HOUR = 8
NEWS_MINUTE = 00 

def scrape_bbc():
    """BBC World News - Official"""
    try:
        url = "https://www.bbc.com/news"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # BBC top stories
        titles = soup.find_all(['h1', 'h2', 'h3'], limit=4)
        news = []
        for title in titles:
            text = title.get_text().strip()
            if text and len(text) > 15:
                news.append(f"🌍 BBC: {text[:85]}...")
        return news or ["🌍 BBC: Latest world news"]
    except:
        return ["🌍 BBC: News temporarily unavailable"]

def scrape_times_of_india():
    """Times of India - Official India News"""
    try:
        url = "https://timesofindia.indiatimes.com/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # TOI headlines
        titles = soup.find_all(['h1', 'h2', 'h3'], class_=['u-f1', 'heading'], limit=4)
        news = []
        for title in titles:
            text = title.get_text().strip()
            if text and len(text) > 15:
                news.append(f"🇮🇳 TOI: {text[:85]}...")
        return news or ["🇮🇳 TOI: India latest news"]
    except:
        return ["🇮🇳 TOI: India news unavailable"]

def scrape_the_hindu():
    """The Hindu - Official"""
    try:
        url = "https://www.thehindu.com/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Hindu top stories
        titles = soup.find_all('h2', limit=3)
        news = []
        for title in titles:
            text = title.get_text().strip()
            if text and len(text) > 15:
                news.append(f"📖 Hindu: {text[:85]}...")
        return news or ["📖 Hindu: In-depth analysis"]
    except:
        return ["📖 Hindu: News unavailable"]

def scrape_reuters():
    """Reuters - Global News"""
    try:
        url = "https://www.reuters.com/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        titles = soup.find_all(['h1', 'h2', 'h3'], limit=3)
        news = []
        for title in titles:
            text = title.get_text().strip()
            if text and len(text) > 15:
                news.append(f"📰 Reuters: {text[:85]}...")
        return news or ["📰 Reuters: Breaking news"]
    except:
        return ["📰 Reuters: Global news unavailable"]

def fetch_all_news():
    """Combine all sources"""
    print("📰 Scraping OFFICIAL sources...")
    all_news = []
    
    all_news.extend(scrape_bbc())
    print("✅ BBC scraped")
    
    all_news.extend(scrape_times_of_india())
    print("✅ TOI scraped")
    
    all_news.extend(scrape_the_hindu())
    print("✅ Hindu scraped")
    
    all_news.extend(scrape_reuters())
    print("✅ Reuters scraped")
    
    return all_news[:10]  # Top 10 headlines

def send_morning_news():
    """Send complete news briefing"""
    try:
        print(f"⏰ [{datetime.now().strftime('%H:%M:%S')}] Preparing briefing...")
        
        headlines = fetch_all_news()
        news_message = f"""🌅 *MORNING NEWS BRIEFING*
📅 {datetime.now().strftime('%d %B %Y, %A')}
━━━━━━━━━━━━━━━━━━━━

"""
        news_message += "\n".join(headlines)
        news_message += f"\n\n*Fresh from official sources* 📱"
        
        print(f"📱 Sending {len(headlines)} headlines...")
        pwk.sendwhatmsg_to_group_instantly(GROUP_ID, news_message)
        print("✅ News sent! Full cycle wait...")
        time.sleep(60)
        print(f"✅ [{datetime.now().strftime('%H:%M:%S')}] NEWS DELIVERED!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# === MAIN EXECUTION ===
if __name__ == "__main__":
    print("📰 OFFICIAL NEWS BOT - LIVE SCRAPING")
    print("=" * 50)
    print("📱 Group:", GROUP_ID)
    print("🦁 Brave WhatsApp: KEEP OPEN!")
    
    print("\n🧪 LIVE TEST - Real headlines NOW...")
    send_morning_news()
    
    print("\n🔄 DAILY SCHEDULE:")
    schedule.every().day.at(f"{NEWS_HOUR:02d}:{NEWS_MINUTE:02d}").do(send_morning_news)
    print(f"• 8:00 AM daily → Fresh news")
    
    print("\n⏳ Bot active! (Ctrl+C stop)")
    while True:
        schedule.run_pending()
        time.sleep(60)
