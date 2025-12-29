"""
✅ EXTENDED pywhatkit - WAITS FULL CYCLE
"""

import pywhatkit as pwk
import time

GROUP_ID = "HcNhbsRbTfX0w3LSbxhPYw"
MESSAGE = "✅ EXTENDED WAIT - Now Sends!"

print("🦁 1. Brave → web.whatsapp.com → KEEP OPEN & FOCUSED")
input("✅ Press Enter when ready...")

print("📱 Sending... (wait 45s FULL CYCLE)")
pwk.sendwhatmsg_to_group_instantly(GROUP_ID, MESSAGE)
print("⏳ Waiting FULL 45 seconds for send... DO NOT TOUCH")
time.sleep(45)  # FULL pywhatkit cycle
print("✅ Check group NOW!")

