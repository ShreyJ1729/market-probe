from core.scraping import TickerListScraper, StockDataScraper
import requests

def main():
    # get all tickers from nasdaq
    # scraper = TickerListScraper()
    # tickers = scraper.scrape_tickers("ALL")

    # # scrape historical data for all tickers
    # stock_scraper = StockDataScraper(tickers)
    
    # # 1d granularity for 10y period
    # stock_scraper.scrape_tickers(period="10y", interval="1d")

    # # 1h granularity for 730d period (limit)
    # stock_scraper.scrape_tickers(period="600d", interval="1h")

    # # 1m granularity for 7d period (limit)
    # stock_scraper.scrape_tickers(period="7d", interval="1m")



if __name__ == "__main__":
    main()
