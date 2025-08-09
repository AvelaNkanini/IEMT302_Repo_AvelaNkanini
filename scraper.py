import requests
from bs4 import BeautifulSoup

# Using wttr.in for easy weather info (no JavaScript, just HTML/text)
url = "https://wttr.in/Johannesburg?format=%C+%t"

response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch the page")
    exit()

# This site returns plain text, no need for complex HTML parsing
print("Current Johannesburg Weather:", response.text.strip())
