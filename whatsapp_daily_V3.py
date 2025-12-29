"""
✅ FIXED DAILY SCHEDULER - 15:50 TODAY + Daily Forever
"""

import pywhatkit as pwk
import schedule
import time
from datetime import datetime

# === CONFIG - 15:50 TODAY ===
GROUP_ID = "HcNhbsRbTfX0w3LSbxhPYw"
DAILY_MESSAGE = "Good Morning Team! 📅 Automated Daily Update"
SEND_HOUR = 15    # 3 PM
SEND_MINUTE = 50  # 50 minutes (15:50)

def send_group_message():
    """Your WORKING method"""
    try:
        print(f"⏰ [{datetime.now().strftime('%H:%M:%S')}] Sending...")
        pwk.sendwhatmsg_to_group_instantly(GROUP_ID, DAILY_MESSAGE)
        print("✅ Scheduled! Waiting 45s...")
        time.sleep(45)
        print(f"✅ [{datetime.now().strftime('%H:%M:%S')}] SENT!")
    except Exception as e:
        print(f"❌ Error: {e}")

print("🤖 WHATSAPP DAILY SCHEDULER v4 - 15:50")
print("=" * 50)
print(f"📱 Group: {GROUP_ID}")
print(f"⏰ NEXT: {SEND_HOUR}:{SEND_MINUTE:02d} TODAY")
print("🦁 KEEP Brave WhatsApp OPEN & FOCUSED!")

# === NO TEST - DIRECT SCHEDULE ===
schedule.every().day.at(f"{SEND_HOUR:02d}:{SEND_MINUTE:02d}").do(send_group_message)
print(f"\n🔄 SCHEDULED: {SEND_HOUR:02d}:{SEND_MINUTE:02d} (2 mins from now!)")
print("⏳ Waiting for 15:50...")

print("\n📊 SCHEDULE:")
print(f"• TODAY 15:50 → Message 1")
print(f"• TOMORROW 15:50 → Message 2")
print(f"• EVERY DAY 15:50 → Forever")

print("\n🚀 Press Ctrl+C to stop")
while True:
    schedule.run_pending()
    time.sleep(60)
