import yt_dlp
import json

ydl_opts = {
    'skip_download': True,
    'quiet': True,
    'no_warnings': True,
    'socket_timeout': 10
}

urls = [
    "https://www.facebook.com/share/v/1CrxXpDmkh/",
    "https://www.facebook.com/share/v/1Y3vjTos84/"
]

for url in urls:
    print(f"Extracting {url}...")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"URL: {url}")
            print(f"Title: {info.get('title')}")
            print(f"Description: {info.get('description')}")
            print("=" * 50)
    except Exception as e:
        print(f"Error for {url}: {e}")
