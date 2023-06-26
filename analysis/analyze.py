import os
import requests
import json

FMP_KEY = os.environ.get("FMP_KEY")
BASE_URL = "https://financialmodelingprep.com/api/v4"


class News:
    """Scan for news articles"""

    def __init__(self, pages=10):
        self.pages = pages
        self.curr_page = 0
        self.general_url = f"{BASE_URL}/general_news?page={self.curr_page}&apikey={FMP_KEY}"

        self.sentiment_url = f"{BASE_URL}/stock-news-sentiments-rss-feed?page={self.curr_page}&apikey={FMP_KEY}"

    @staticmethod
    def screen_ticker(ticker):
        url = f"https://financialmodelingprep.com/api/v3/stock_news?ticker={ticker}&limit=10&apikey={FMP_KEY}"
        response = requests.get(url)
        return response.json()

    def screen_sentiment(self):
        self.curr_page = 1
        data = []

        for i in range(self.pages):
            response = requests.get(self.sentiment_url)
            self.curr_page += 1

            if response.status_code == 200:
                data.extend(response.json())
            else:
                raise requests.exceptions.RequestException(
                    'API request failed with status code: ' + str(response.status_code))

        return data

    def screen_general(self):
        self.curr_page = 1
        data = []
        for i in range(self.pages):
            response = requests.get(self.general_url)
            self.curr_page += 1

            if response.status_code == 200:
                data.extend(response.json())
            else:
                raise requests.exceptions.RequestException(
                    'API request failed with status code: ' + str(response.status_code))

        return data


class Screener:
    """Refresh stocks in db"""

    def __init__(self, scrape_limit=20000):
        self.scrape_limit = scrape_limit
        self.scrape_url = f'https://financialmodelingprep.com/api/v3/stock-screener?marketCapMoreThan=10000000&limit={scrape_limit}&apikey={FMP_KEY}'
        self.tickers = []

    def screen_stocks(self):
        response = requests.get(self.scrape_url)

        if response.status_code == 200:
            data = response.json()
        else:
            raise requests.exceptions.RequestException(
                'API request failed with status code: ' + str(response.status_code))

        return data


if __name__ == "__main__":
    s = Screener(scrape_limit=1000)
    s.screen_stocks()
