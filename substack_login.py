import time
import pickle
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIGURATION ---
SUBSTACK_LOGIN_URL = "https://substack.com/sign-in?redirect=%2F&for_pub=mypminterview"

# Hardcoded Credentials
EMAIL = "farzeenjawidkhan@gmail.com"
PASSWORD = "Farzeen@2112"
COOKIES_FILE = "substack_cookies.pkl"

def delete_old_cookies():
    """Delete old cookies file to ensure a fresh login session."""
    if os.path.exists(COOKIES_FILE):
        os.remove(COOKIES_FILE)
        print(f"[INFO] Old cookies file '{COOKIES_FILE}' deleted.")

def login_to_substack():
    """Automate Substack login and extract session cookies."""
    
    # Setup Selenium WebDriver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # 🔹 Uncomment to run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("[INFO] Opening Substack login page...")
        driver.get(SUBSTACK_LOGIN_URL)

        # Click "Sign in with password"
        wait = WebDriverWait(driver, 15)
        sign_in_with_password = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'login-option substack-login__login-option')]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", sign_in_with_password)
        time.sleep(1)
        sign_in_with_password.click()
        print("[INFO] Clicked 'Sign in with password'.")

        # Enter email
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']")))
        email_input.send_keys(EMAIL)
        print("[INFO] Entered email.")

        # Enter password
        password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
        password_input.send_keys(PASSWORD)
        print("[INFO] Entered password.")

        # Click the continue button
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]")))
        login_button.click()
        print("[INFO] Submitted login. Waiting for CAPTCHA...")

        # Pause script for user to solve CAPTCHA manually
        print("\n[INFO] CAPTCHA detected. Please solve it manually in the browser.")
        input("[INFO] After solving the CAPTCHA, press Enter to continue...")

        # Click "Continue" after CAPTCHA
        try:
            continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue')]")))
            continue_button.click()
            print("[INFO] Clicked 'Continue' after CAPTCHA verification.")
        except:
            print("[WARNING] No 'Continue' button found after CAPTCHA. Login may have succeeded.")

        # Wait for authentication to complete
        time.sleep(5)

        print("[INFO] Login successful! Extracting cookies...")

        # --- Extract all cookies ---
        cookies = driver.get_cookies()
        with open(COOKIES_FILE, "wb") as f:
            pickle.dump(cookies, f)

        print(f"[SUCCESS] New cookies saved to {COOKIES_FILE}")

    except Exception as e:
        print(f"[ERROR] Failed to login: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    delete_old_cookies()  # Ensure old cookies are removed before login
    login_to_substack()