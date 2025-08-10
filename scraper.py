#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.jse.co.za/indices")

        # Wait for the table to load fully
        page.wait_for_selector("table")

        # Get full HTML of the first table on the page
        table_html = page.inner_html("table")

        # Parse the table HTML using BeautifulSoup
        soup = BeautifulSoup(table_html, 'html.parser')
        rows = soup.find_all('tr')

        print("Symbol | Company Name | Volume | Change")
        print("-" * 50)

        count = 0
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 4:
                symbol = cols[0].get_text(strip=True)
                company = cols[1].get_text(strip=True)
                volume = cols[2].get_text(strip=True)
                change = cols[3].get_text(strip=True)
                print(f"{symbol} | {company} | {volume} | {change}")
                count += 1
                if count == 5:
                    break

        browser.close()

if __name__ == "__main__":
    main()