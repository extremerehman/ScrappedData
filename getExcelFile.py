import requests
from bs4 import BeautifulSoup
import csv
import os
from urllib.parse import urljoin

# 🔹 Login Credentials
LOGIN_URL = "https://substack.com/api/v1/login"
USER_EMAIL = "farzeenjawidkhan@gmail.com"  # Replace with your email
USER_PASSWORD = "Farzeen@2112"   # Change to your password
TARGET_PUB = "mypminterview"
TARGET_URL = "https://www.mypminterview.com/about"

# 🔹 Headers to simulate a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}

# 🔹 Login Function
def login_to_site(session):
    """Login to Substack and return an authenticated session."""
    login_data = {
        "email": USER_EMAIL,
        "password": USER_PASSWORD,
        "for_pub": TARGET_PUB
    }
    try:
        session.get("https://substack.com/sign-in", headers=HEADERS)  # Get CSRF token if needed
        response = session.post(LOGIN_URL, json=login_data, headers=HEADERS)
        
        if response.status_code == 200:
            print("✅ Login successful!")
            session.get("https://www.mypminterview.com/", headers=HEADERS)  # Authenticate cookies
            return True
        else:
            print(f"❌ Login failed! Status code: {response.status_code}\nResponse: {response.text}")
            return False
    except Exception as e:
        print(f"⚠️ Login error: {str(e)}")
        return False

# 🔹 Extract all links from the page
def scrape_all_links(session):
    """Extracts all links and titles from the page and saves them in a CSV file."""
    response = session.get(TARGET_URL, headers=HEADERS)
    if response.status_code != 200:
        print(f"⚠️ Failed to fetch the page: {TARGET_URL}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # 🔹 Extract all <a> tags
    all_links = []
    for a_tag in soup.find_all("a", href=True):
        title = a_tag.text.strip()
        link = a_tag["href"].strip()

        # 🔹 **Skip invalid links**
        if link.startswith(("mailto:", "javascript:", "#")):
            continue  # Skip email links, JavaScript links, and empty links

        if not link.startswith("http"):  # Handle relative URLs
            link = urljoin("https://www.mypminterview.com", link)

        # Check if link is valid
        try:
            link_response = session.get(link, headers=HEADERS, timeout=5)
            if link_response.status_code == 200:
                all_links.append([title, link])
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Skipping broken link: {link} - {e}")

    # Save to CSV
    with open("all_links.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link"])
        writer.writerows(all_links)

    print(f"✅ Scraped {len(all_links)} valid links. Saved to 'all_links.csv'.")
    return all_links

# 🔹 Main Function
def main():
    session = requests.Session()

    # **Step 1: Login First**
    if not login_to_site(session):
        print("❌ Login failed! Exiting...")
        return

    # **Step 2: Scrape all links**
    all_links = scrape_all_links(session)
    if not all_links:
        print("❌ No valid links found. Exiting...")
        return

    print("\n🎉 Scraping Complete! All links saved successfully.")

# 🔹 Run the script
if __name__ == "__main__":
    main()