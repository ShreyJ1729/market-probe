# SMP-500: Daily insights for swing traders on the top 500 large-cap US stocks

## Misc Notes

- SMP-500, daily insights for swing traders on the top 500 large cap US stocks.
- mailing or text messaging list
- browser automation and screenshot in mail for top 5 decisions
- running top x (1000?) large cap us stocks
- add more indicators (all from pandas ta library)
- backtesting w different aggressiveness levels and granularity (ranging from 1m to 1d)
- genetic algorithm for backtesting, pick random x indicators, for each have different buy/sell parameters and evolve over time to find best combinations for different levels of granularity and diff market conditions (diff years)
- make a game to help people learn about the stock market - show a random stock price (at different granularities), and allow people to choose indicators of their choice to show in the graph too (up to x indicators max). Then ask them to guess bullish/bearish in the timespan of a certain amount (say, 10-20 ticks after the last data point). reveal stock ticker, granulairty, and date/time after guess. keep score and show leaderboard.

- to programmatically do MACD predictions on crossover/crossunder, take the last k datapoints from each line, compute line of best fit on them, then see if they cross in the next k datapoints. if they do, then predict the direction of the crossover/crossunder. if they don't, then predict no change. (this is a very simple model, but it's a start).

another good strategy for confirmation

- https://www.youtube.com/watch?v=fgtfI5eAS_Y
- support and resistance with breaks
- squeeze momentum indicator
- 200 day MA to see general market trend so we only trade in same direction as market

combining the above strat with MACD produces great results, not very often but when it does it's a big win since we're combining momentum compression with confirmation of trend reversal pointing towards the overall market trend.

for swing trading, target HIGH VOLUME, HIGH VOLATILITY stocks
top swing trading stocks
tech:

- AAPL
- META
- MSFT
- AMZN
- GOOG
- NFLX
- AMD
- PYPL
- SBUX
- CRM

- CAT
- K
- KSS

others

- HTCR
-

- so during backtesting, will first run on everything, then will classify stocks by volatility and volume, and then run on top k% of those stocks, where k is a parameter that can be tuned
- then to prevent data drift, will retune model every so often depending on the granularity of the data (if 1m, then every day, if 1d, then every week, etc) --> these numbers are just guesses, will have to do some research on how often market conditions change

would also be interesting to do sentiment analysis on recent finance related news articles. see what stocks are mentioend in the news and practice extra caution when trading those stocks.

try a strategy only using squeeze momentum where you for red

- buy when bars turn black
- sell when bars turn red or reach middle
  and vice versa for green

Task list

- []

to get around rate limiting on yahoo finance, deploy multiple proxy servers on modal labs included in this code base, and then use a proxy rotation library to rotate through them. this will allow us to get around the rate limiting and get more data faster.

places to get intraday data

- https://www.thetadata.net/subscribe --> options data going back 4 years, $40 per month
- rapid api unlimited https://rapidapi.com/dubois4and/api/quotient --> 130/mo unlimited requests so just mass scrape everything with a month. covers Market data API for intraday (1-minutes) data, end-of-day data, options data, crypto, forex, live prices, fundamental data, trading signal, and much more, on various assets (Stocks, ETFs, Funds, Indices, Forex, Cryptocurrencies, etc), on worldwide stock exchanges (us, canada, australia, uk and europe).

after buying just query yahoo finance every day for eod minute data and then store it in a database updating the above data.

polygon.io

- free tier --> You can get two years history with up to 5/calls per minute on free plan. My script for their API pulls 6 weeks of 1 minute data per call, so you only need 9 calls pet calendar year per ticker. Two minutes per ticker => 720 tickers per day.

combining the above with personal scraper is sufficient for current purposes, combined with daily data for the last 10 years for all other stocks.

steps from here

1. get data for all stock tickers on the nasdaq api
   a. 10 years at 1d granularity
   b. 730 days at 1h granularity
   c. 7 days at 1m granularity
2. work on backtesting framework

https://pypi.org/project/yfinance/ --> info on using requests with headers to get around rate limiting

stock2vec --> cluster stocks by true correlation in price changes, rather than industry and semantics.
