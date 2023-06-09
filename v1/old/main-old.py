from .scraping import get_ticker_data, scrape_ticker_list
from ..indicators import compute_indicators, identify_events
from core.plotting import plot_ticker
from core.stock import Stock
import pandas as pd
from tqdm import tqdm
import json

# ideas
# - turn discrete events into continuous signals (probabilistic)
# - use ML on technical indicators to predict bullish/bearish (regression) --> try diff time frames for targets
# - - 1D CNN w each indicator as a channel --> output is a single value (bullish/bearish) with target from x days out comparison
# - backtesting and forwardtesting by deploying on modal and running on historical data and on a schedule
# once have system flow working, create UI for it with top stocks of interest displayed and link to chart and tradingview interface (ask for trading view chart embed)


def run_analysis(ticker_list_filepath):
    scrape_ticker_list(ticker_list_filepath)
    tickers = open(ticker_list_filepath, "r").read().splitlines()
    stocks = {}
    print("Running analysis...")
    for ticker in tqdm(tickers):
        try:
            df = pd.read_csv(f"./data/{ticker}.csv")
        except Exception as e:
            print(f"failed to get '{ticker}', {e}")
            continue

        df = compute_indicators(df)
        df = identify_events(df, SENSITIVITY=4)
        stocks[ticker] = df["signal_sum"].iloc[-1]
    return stocks


def user_input_analysis():
    ticker = input("Enter ticker: ").upper()
    last_n_days = int(input("Enter last n days: "))

    df = get_ticker_data(ticker, "d")

    if df is None:
        print(f"failed to get '{ticker}'")
        exit(1)

    df = compute_indicators(df)
    df = identify_events(df, SENSITIVITY=7)

    df = df.tail(last_n_days).reset_index()
    plot_ticker(df, ticker, last_n_days)


def main():
    # stock = Stock("brk-a")
    # stock.get_historical_data(period="max", interval="1d")
    # stock.compute_technical_indicators()


    user_input_analysis()
#     stocks_of_interest = run_analysis("./tickers/sp500.txt")
#     output = json.dumps(stocks_of_interest, indent=4)
#     print(
#         output,
#         file=open("./stocks_of_interest.json", "w+"),
#     )


if __name__ == "__main__":
    main()
