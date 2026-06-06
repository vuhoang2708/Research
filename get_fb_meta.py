import urllib.request
import re
import sys

def get_meta(url):
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            # trích xuất og:title
            title_match = re.search(r'<meta\s+property=["\']og:title["\']\s+content=["\'](.*?)["\']', html)
            if not title_match:
                title_match = re.search(r'<meta\s+content=["\'](.*?)["\']\s+property=["\']og:title["\']', html)
            
            # trích xuất og:description
            desc_match = re.search(r'<meta\s+property=["\']og:description["\']\s+content=["\'](.*?)["\']', html)
            if not desc_match:
                desc_match = re.search(r'<meta\s+content=["\'](.*?)["\']\s+property=["\']og:description["\']', html)
                
            title = title_match.group(1) if title_match else "None"
            desc = desc_match.group(1) if desc_match else "None"
            
            # In tiêu đề HTML
            html_title_match = re.search(r'<title>(.*?)</title>', html)
            html_title = html_title_match.group(1) if html_title_match else "None"
            
            print(f"URL: {url}")
            print(f"HTML Title: {html_title}")
            print(f"og:title: {title}")
            print(f"og:description: {desc}")
            print("-" * 50)
    except Exception as e:
        print(f"Error reading {url}: {e}")

urls = [
    "https://www.facebook.com/share/v/1CrxXpDmkh/",
    "https://www.facebook.com/share/v/1Y3vjTos84/"
]
for url in urls:
    get_meta(url)
