import os
import pandas as pd
import wallstreet as ws
from tqdm import tqdm

def scrape_all():
    toc = []
    for ticker in tqdm(open('./tickers.txt', 'r').read().splitlines()):
        stock = scrape_ticker(ticker)
        if stock:
            toc.append({
                    'ticker': ticker,
                    'name': stock.name,
                })
        else:
            print(f"failed to get '{ticker}'")
    pd.DataFrame(toc).to_csv('./toc.csv')


def scrape_ticker(ticker, duration='d'):
    if not os.path.exists('./data'):
        os.makedirs('./data')
    try:
        stock = ws.Stock(ticker)
    except Exception as e:
        print(f"failed to get '{ticker}', {e}")
        return None
    df = stock.historical(days_back=9999, frequency=duration)
    df.to_csv(f'./data/{ticker}.csv')
    return df