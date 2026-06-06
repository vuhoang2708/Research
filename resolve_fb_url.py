import requests

def resolve(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:
        r = requests.get(url, headers=headers, allow_redirects=True, timeout=10)
        print(f"URL: {url}")
        print(f"Status Code: {r.status_code}")
        print(f"History: {[h.url for h in r.history]}")
        print(f"Final URL: {r.url}")
        print("-" * 50)
    except Exception as e:
        print(f"Error {url}: {e}")

urls = [
    "https://www.facebook.com/share/v/1CrxXpDmkh/",
    "https://www.facebook.com/share/v/1Y3vjTos84/"
]
for url in urls:
    resolve(url)
