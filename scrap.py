import requests
from bs4 import BeautifulSoup
import csv
import os
import time
from urllib.parse import urlparse

def login_to_site(session):
    """Login to Substack and return the authenticated session"""
    # Initial login URL
    login_url = "https://substack.com/api/v1/login"
    
    # Login credentials
    login_data = {
        "email": "farzeenjawidkhan@gmail.com",
        "password": "Farzeen@2112",
        "for_pub": "mypminterview"
    }
    
    # Additional headers needed for Substack
    login_headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Origin": "https://substack.com",
        "Referer": "https://substack.com/sign-in"
    }
    
    try:
        # First, get the CSRF token if needed
        session.get("https://substack.com/sign-in", headers=login_headers)
        
        # Perform login
        response = session.post(
            login_url, 
            json=login_data,
            headers=login_headers
        )
        
        if response.status_code == 200:
            print("Login successful!")
            # After successful login, get the mypminterview page to set necessary cookies
            session.get("https://www.mypminterview.com/", headers=headers)
            return True
        else:
            print(f"Login failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"Login error: {str(e)}")
        return False

def clean_filename(title):
    # Remove or replace invalid characters for filenames
    invalid_chars = '<>:"/\\|?*'
    filename = ''.join(char if char not in invalid_chars else '_' for char in title)
    return filename[:150] + '.md'  # Changed extension to .md for markdown files

def create_output_directory():
    # Create a directory to store all markdown files
    output_dir = "scraped_content"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def convert_to_markdown(element):
    """Convert HTML elements to markdown format"""
    if element.name == 'h1':
        return f"# {element.get_text().strip()}\n\n"
    elif element.name == 'h2':
        return f"## {element.get_text().strip()}\n\n"
    elif element.name == 'h3':
        return f"### {element.get_text().strip()}\n\n"
    elif element.name == 'h4':
        return f"#### {element.get_text().strip()}\n\n"
    elif element.name == 'h5':
        return f"##### {element.get_text().strip()}\n\n"
    elif element.name == 'h6':
        return f"###### {element.get_text().strip()}\n\n"
    elif element.name == 'p':
        text = element.get_text().strip()
        # Handle links within paragraphs
        for link in element.find_all('a'):
            href = link.get('href', '')
            text = text.replace(link.get_text(), f"[{link.get_text()}]({href})")
        return f"{text}\n\n"
    elif element.name == 'ul':
        return ''.join(f"* {li.get_text().strip()}\n" for li in element.find_all('li')) + '\n'
    elif element.name == 'ol':
        return ''.join(f"{i+1}. {li.get_text().strip()}\n" for i, li in enumerate(element.find_all('li'))) + '\n'
    elif element.name == 'blockquote':
        return f"> {element.get_text().strip()}\n\n"
    elif element.name == 'pre' or element.name == 'code':
        return f"```\n{element.get_text().strip()}\n```\n\n"
    elif element.name == 'strong' or element.name == 'b':
        return f"**{element.get_text().strip()}**"
    elif element.name == 'em' or element.name == 'i':
        return f"*{element.get_text().strip()}*"
    return element.get_text().strip() + "\n\n"

def scrape_article_content(session, url):
    try:
        response = session.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Find the main article content
            article = soup.find('article') or soup.find('div', class_='post-content')
            
            if article:
                # Convert content to markdown
                markdown_content = ""
                for element in article.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'blockquote', 'pre', 'code']):
                    markdown_content += convert_to_markdown(element)
                return markdown_content
            return "No content found"
    except Exception as e:
        return f"Error scraping content: {str(e)}"
    
    return "Failed to fetch content"

# Headers to mimic a browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}

def main():
    # Create a session to maintain login cookies
    session = requests.Session()
    
    # Login first
    if not login_to_site(session):
        print("Failed to login. Exiting...")
        return
    
    # Create output directory
    output_dir = create_output_directory()
    
    # Read URLs from CSV
    with open("scraped_blog_links.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        total_links = sum(1 for row in reader)  # Count total links
        file.seek(0)  # Reset file pointer
        next(reader)  # Skip header row
        
        for index, row in enumerate(reader, 1):
            title = row['Title']
            url = row['Link']
            
            # Skip non-article URLs
            if 'mailto:' in url or '/subscribe' in url:
                continue
                
            # Create filename from title
            filename = clean_filename(title)
            filepath = os.path.join(output_dir, filename)
            
            # Skip if file already exists
            if os.path.exists(filepath):
                print(f"Skipping {index}/{total_links}: {title} (already exists)")
                continue
            
            print(f"Scraping {index}/{total_links}: {title}")
            
            # Scrape content using authenticated session
            content = scrape_article_content(session, url)
            
            # Save content to file
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n")
                f.write(f"*Source: {url}*\n\n")
                f.write("---\n\n")  # Horizontal rule for better separation
                f.write(content)
            
            # Add a delay to be respectful to the server
            time.sleep(2)
    
    print("\nScraping complete. Content saved in 'scraped_content' directory.")

if __name__ == "__main__":
    main()