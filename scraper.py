#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def main():
    import requests
    from bs4 import BeautifulSoup

    url = "https://wttr.in/Johannesburg?format=%C+%t"
    response = requests.get(url)
    print("Current Johannesburg Weather:", response.text.strip())

if __name__ == "__main__":
    main()
