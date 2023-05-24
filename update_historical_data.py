from core.scraping import TickerListScraper, StockDataScraper
import requests

def main():
    # get all tickers from nasdaq
    scraper = TickerListScraper()
    tickers = scraper.scrape_tickers("ALL")

    # scrape historical data for all tickers
    stock_scraper = StockDataScraper(tickers)

    # only get the last week of data since it's an update
    stock_scraper.update_tickers_data(period="1wk", interval="1d")
    stock_scraper.update_tickers_data(period="1wk", interval="1h")
    stock_scraper.update_tickers_data(period="1wk", interval="1m")


if __name__ == "__main__":
    main()
