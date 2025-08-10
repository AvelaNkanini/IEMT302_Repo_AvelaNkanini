#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://techcrunch.com/2024/07/31/india-is-the-largest-market-for-meta-ai-usage/"

# Send GET request with a User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract headline
    headline_tag = soup.find('h1')
    if headline_tag:
        print("Headline:", headline_tag.get_text(strip=True))
    else:
        print("Headline not found.")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")

if __name__ == "__main__":
    # Whatever your main code is
    main()
