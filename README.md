# IEMT302_Repo_AvelaNkanini
# JSE Indices Scraper

This Python script scrapes the top 5 stock indices data from the Johannesburg Stock Exchange (JSE) website.

## Features

- Uses Playwright for headless browser automation to load dynamic content.
- Parses the stock data table with BeautifulSoup.
- Prints the Symbol, Company Name, Volume, and Change for the top 5 entries.

## Requirements

- Python 3.7+
- `playwright`
- `beautifulsoup4`

## Install dependencies with:

- pip install -r requirements.txt
- playwright install
- python scraper.py