import requests
from bs4 import BeautifulSoup
import csv
import os
import time
import pickle

# Global Constants
COOKIES_FILE = "substack_cookies.pkl"
OUTPUT_DIR = "scraped_content"
INPUT_CSV = "incomplete.csv"

def load_cookies(session):
    """Load session cookies from the saved Selenium login session."""
    try:
        with open(COOKIES_FILE, "rb") as f:
            cookies = pickle.load(f)

        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'], domain=cookie.get('domain', ''))

        print("[INFO] Loaded session cookies. Skipping login.")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to load cookies: {str(e)}")
        return False

def clean_filename(title):
    """Sanitize filenames to remove invalid characters."""
    invalid_chars = '<>:"/\\|?*'
    filename = ''.join(char if char not in invalid_chars else '_' for char in title)
    return filename[:150] + ".md"  # Limit filename length and ensure markdown format

def create_output_directory():
    """Create a directory to store all markdown files."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def scrape_article_content(session, url):
    """Scrape article content and return as Markdown format."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Referer": "https://www.mypminterview.com/",
        "Connection": "keep-alive",
    }

    response = session.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        article = soup.find("article")
        if not article:
            return "No article found."

        content = "\n\n".join(tag.get_text() for tag in article.find_all(["h1", "h2", "h3", "p", "ul", "ol"]))

        return content if content else "No content found."

    return f"Failed to fetch article: {response.status_code}"

def main():
    """Main function to scrape and save content as Markdown files."""
    session = requests.Session()

    # Load session cookies
    if not load_cookies(session):
        print("[ERROR] Authentication failed. Please run `substack_login.py` again.")
        return

    # Create output directory
    create_output_directory()

    with open(INPUT_CSV, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row['Title']
            url = row['Link'].strip()

            print(f"[INFO] Scraping: {title}")
            content = scrape_article_content(session, url)

            if "Failed to fetch" not in content and "No article found" not in content:
                filename = clean_filename(title)
                filepath = os.path.join(OUTPUT_DIR, filename)

                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f"# {title}\n\n")
                    f.write(f"*Source: {url}*\n\n")
                    f.write("---\n\n")
                    f.write(content)

                print(f"[SUCCESS] Saved: {filepath}")
            else:
                print(f"[WARNING] Could not scrape: {title}")

    print("\n✅ Scraping complete. Markdown files saved in 'scraped_content' directory.")

if __name__ == "__main__":
    main()