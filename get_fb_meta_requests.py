import requests
import re

def get_meta(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"'
    }
    
    try:
        session = requests.Session()
        # Gửi request để lấy các redirect nếu có
        response = session.get(url, headers=headers, timeout=15, allow_redirects=True)
        print(f"Status Code: {response.status_code}")
        print(f"Final URL: {response.url}")
        
        html = response.text
        
        # Tìm tiêu đề og:title
        title = "None"
        title_match = re.search(r'<meta[^>]*property=["\']og:title["\'][^>]*content=["\'](.*?)["\']', html)
        if not title_match:
            title_match = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*property=["\']og:title["\']', html)
        if title_match:
            title = title_match.group(1)
            
        # Tìm og:description
        desc = "None"
        desc_match = re.search(r'<meta[^>]*property=["\']og:description["\'][^>]*content=["\'](.*?)["\']', html)
        if not desc_match:
            desc_match = re.search(r'<meta[^>]*content=["\'](.*?)["\'][^>]*property=["\']og:description["\']', html)
        if desc_match:
            desc = desc_match.group(1)
            
        # Tìm tiêu đề html
        html_title = "None"
        html_title_match = re.search(r'<title>(.*?)</title>', html)
        if html_title_match:
            html_title = html_title_match.group(1)
            
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
