from typing import Literal, List, Tuple
import os
import pandas as pd
from tqdm import tqdm
import requests
import pandas_ta as ta

SUPPORTED_EXCHANGES = Literal["NASDAQ", "NYSE", "ALL"]

VALID_INTERVALS = Literal[
    "1m", "2m", "5m", "15m", "30m", "1h", "90m", "1d", "1wk", "1mo", "3mo"
]


class TickerListScraper:
    def __init__(self) -> None:
        self.base_api_url = (
            "https://api.nasdaq.com/api/screener/stocks?tableonly=true&download=true"
        )

    def scrape_tickers(self, exchange: SUPPORTED_EXCHANGES) -> List[str]:
        print(f"Scraping tickers from {exchange}")
        tickers = self.scrape_tickers_of_exchange(exchange)
        tickers = [ticker[0] for ticker in tickers]
        print(f"Scraped {len(tickers)} tickers from {exchange}")
        return tickers

    def scrape_tickers_of_exchange(
        self, exchange: SUPPORTED_EXCHANGES
    ) -> List[Tuple[str, str]]:
        if exchange != "ALL":
            self.base_api_url += f"&exchange={exchange}"

        res = requests.get(
            self.base_api_url,
            headers={
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            },
        )

        if res.status_code != 200:
            raise Exception(f"Failed to get tickers from {self.exchange}")

        tickers = [(row["symbol"], row["name"]) for row in res.json()["data"]["rows"]]
        tickers = [(row[0].replace("^", "-"), row[1]) for row in tickers]

        return tickers

    def read_tickers_from_file(self, filepath: str) -> List[str]:
        tickers = open(filepath, "r").read().splitlines()
        return tickers


class StockDataScraper:
    def __init__(self, tickers: List[str]) -> None:
        self.tickers = tickers

    def scrape_historical_data(
        self, ticker, period: str, interval: VALID_INTERVALS
    ) -> pd.DataFrame:
        df = pd.DataFrame().ta.ticker(ticker, period=period, interval=interval)
        if df is None or df.empty:
            return None
        return df

    def scrape_tickers(self, period: str, interval: VALID_INTERVALS):
        print(f"Scraping {interval} data for {len(self.tickers)} tickers")
        if not os.path.exists(f"./data/{interval}"):
            os.makedirs(f"./data/{interval}")
        
        for ticker in tqdm(self.tickers):
            if os.path.exists(f"./data/{interval}/{ticker}.csv"):
                print(f"Skipping {ticker} as it already exists")
                continue
            df = self.scrape_historical_data(ticker, period=period, interval=interval)
            if df is not None:
                df.to_csv(f"./data/{interval}/{ticker}.csv")

    def update_tickers_data(self, period: str, interval: VALID_INTERVALS):
        print(f"Updating {interval} data for {len(self.tickers)} tickers")

        # if interval folder doesn't exist, scrape all data
        if not os.path.exists(f"./data/{interval}"):
            os.makedirs(f"./data/{interval}")
            self.scrape_tickers(period, interval)
            return

        for ticker in tqdm(self.tickers):
            # if ticker not in folder, scrape all data
            if not os.path.exists(f"./data/{interval}/{ticker}.csv"):
                df = self.scrape_historical_data(
                    ticker, period=period, interval=interval
                )
                if df is not None:
                    df.to_csv(f"./data/{interval}/{ticker}.csv")
                    return

            # otherwise, scrape new data, find last date, and append
            df = pd.read_csv(f"./data/{interval}/{ticker}.csv")
            last_date = df.iloc[-1]["datetime"]
            df = df.ta.ticker(ticker, period=period, interval=interval)
            if df is not None:
                df = df[df["datetime"] > last_date]  # filter out old data
                if not df.empty:
                    df.to_csv(f"./data/{interval}/{ticker}.csv", mode="a", header=False)
