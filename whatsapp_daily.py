from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# ====== EDIT THESE ======
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
PHONE_NUMBER = "919480288346"      # no +, no spaces
MESSAGE = "Good Evening"
# ========================

# XPath for the message box, built from your DevTools screenshot
MESSAGE_BOX_XPATH = (
    '//div[@contenteditable="true" and @role="textbox" '
    'and @data-tab="10" and @data-lexical-editor="true"]'
)

def get_driver():
    options = Options()
    options.binary_location = BRAVE_PATH
    options.add_argument("--no-first-run")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_experimental_option("detach", True)  # keep Brave window open
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver

def send_to_unsaved_number():
    driver = get_driver()
    wait = WebDriverWait(driver, 40)

    # 1) Login to WhatsApp Web in this Brave window
    driver.get("https://web.whatsapp.com/")
    print("📱 Scan QR in this Brave window if asked, wait till chats load...")
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, '//div[@role="textbox" and @contenteditable="true"]')
        )
    )
    print("✅ Logged in.")

    # 2) Open chat with UNSAVED number using wa.me
    chat_url = f"https://wa.me/{PHONE_NUMBER}"
    driver.get(chat_url)
    print(f"🔗 Opening chat with {PHONE_NUMBER} ...")

    # Click “Continue to Chat” / redirect to WhatsApp Web
    try:
        continue_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[contains(@href,"/send")]')
            )
        )
        continue_btn.click()
    except Exception:
        pass  # sometimes auto-redirect happens

    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])

    # 3) Find the message input box using the precise XPath and send message
    msg_box = wait.until(
        EC.visibility_of_element_located((By.XPATH, MESSAGE_BOX_XPATH))
    )
    msg_box.click()
    time.sleep(1)
    msg_box.send_keys(MESSAGE + Keys.ENTER)
    print("✅ MESSAGE SENT SUCCESSFULLY!")

    # Optional: leave Brave open; comment next line if you want to close it
    # driver.quit()

if __name__ == "__main__":
    input("👉 Close other Brave windows started by Selenium, then press Enter to start... ")
    send_to_unsaved_number()
