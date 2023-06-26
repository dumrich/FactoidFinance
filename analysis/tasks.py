from celery import shared_task
import requests
from .analyze import Screener  # , Analyze
from .models import Stock, StockAnalysis
from articles.models import Article
from requests.exceptions import RequestException
from math import ceil
from .analyze import Screener, News, BASE_URL, FMP_KEY
import time


def get_news():
    n = News(pages=40)
    data = []

    counter = 1

    try:
        data = n.screen_sentiment()
    except RequestException:
        print("Error Screening News")

    for article in data:
        ticker, date, title, image, site, text, url, sentiment, score = \
            article["symbol"], article["publishedDate"], article["title"],\
            article["image"], article["site"], article["text"],\
            article["url"], article["sentiment"], article["sentimentScore"]

        c = None
        try:
            c = Article.objects.get(title=title)
        except Article.DoesNotExist:
            c = Article()

        c.title = title
        c.serialized_date = date
        c.image_link = image
        c.content = text
        c.original_link = url
        c.sentiment = sentiment
        c.sentiment_score = score
        c.site = site

        try:
            # Check if stocks exist already
            c.stock = Stock.objects.get(ticker=ticker)
        except Stock.DoesNotExist:
            pass

        c.save()

        print(f"Article {counter} added")
        counter += 1

    # Stock News for top 500 stocks
    top_stocks = Stock.objects.order_by('-market_cap')[:100]
    for stock in top_stocks:
        response = News.screen_ticker(stock.ticker)
        for data in response:
            date, title, image, site, text, url = \
                article["publishedDate"], article["title"],\
                article["image"], article["site"], article["text"],\
                article["url"]

            c = None
            try:
                c = Article.objects.get(title=title)
            except Article.DoesNotExist:
                c = Article()

                c.title = title
                c.serialized_date = date
                c.image_link = image
                c.content = text
                c.original_link = url
                c.site = site
                c.stock = stock

            c.save()

            print(f"Article {counter} added")
            counter += 1


def raw_screen():
    # Your script logic here
    s = Screener(scrape_limit=20000)
    data = []

    try:
        data = s.screen_stocks()
    except RequestException:
        print("Error Screening stocks")

    counter = 1
    for stock in data:
        ticker, name, marketCap = stock["symbol"], \
            stock["companyName"], stock["marketCap"]

        sector, price = stock["sector"], float(stock["price"])
        isEtf = stock["isEtf"]

        sharesOutstanding = ceil(marketCap / price)

        if sector == "Consumer Cyclical":
            sector = "Consumer Discretionary"
        elif sector == "Technology":
            sector = "Information Technology"

        try:
            # Check if stocks exist already
            c = Stock.objects.get(ticker=ticker)

            c.price = float(stock["price"])
            c.shares_outstanding = sharesOutstanding
            c.market_cap = marketCap
            c.isEtfOrFund = isEtf

        except Stock.DoesNotExist:
            c = Stock(firm_name=name, ticker=ticker, price=price,
                      shares_outstanding=sharesOutstanding, sector=sector)
            c.isEtfOrFund = isEtf
            c.market_cap = marketCap

        c.save()

        print(f"Stock {counter} finished\n")
        counter += 1


def get_analysis():
    top_stocks = Stock.objects.order_by('-market_cap')[:400:-1]
    counter = 1
    for stock in top_stocks:
        analysis = None
        try:
            analysis = StockAnalysis.objects.get(stock=stock)
        except StockAnalysis.DoesNotExist:
            analysis = StockAnalysis(stock=stock)
        profile = f"https://financialmodelingprep.com/api/v3/quote/{stock.ticker}?apikey={FMP_KEY}"
        try:
            response = requests.get(profile).json()[0]
        except KeyError:
            continue
        print(response)
        exchange, price, change, market, vol, open, close = response["exchange"], response["price"], response["change"], response["marketCap"], response["volume"], response["open"], response["previousClose"]

        sharesOut, eps, pe = response["sharesOutstanding"], response["eps"], response["pe"]

        analysis.price = price
        analysis.exchange = exchange
        analysis.change = change
        analysis.marketCap = market/3
        analysis.volume = vol/3
        analysis.open = open
        analysis.previousclose = close

        analysis.sharesOutstanding = sharesOut/3
        analysis.eps = eps
        analysis.pe = pe

        try:
            analysis.save()
        except:
            print("could not continue")
            continue

        print(f"Stock {counter} finished\n")
        counter += 1


@ shared_task
def screen_stocks():
    raw_screen()
