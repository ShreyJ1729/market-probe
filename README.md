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

todo

- iterate over top 100 most volatile, highest volume stocks (or some other list)
- - for each compute charts
- - - 1m
- - - 5m
- - - 15m
- - - 30m
- - - 1h
- - - 4h
- - - 1d
- for each chart compute indicators and run different strategied
- - SR Breaks + SQZM + SMA200 --> use this to find events
- - MACD + MFI + WT --> use this to confirm events

create a "game" where a random stocks is picked, a random timeframe is picked, and 60-100 tickers are shown, goal is to guess what the price movement will be 10-20 tickers down the line.

another way is to compute 100s of indicators, for lines put crossover booleans, and set the target for each day as up if the next 10 candlestick SMA is above the current price, and down if it's below. then train an RF to do this. yt video: https://www.youtube.com/watch?v=iJmteST6fP8

another idea is to monitor changes in stock prices post-earnings, see who's the most volatile, and run a strategy buynig straddles 2-3 weeks prior to earnings for those stocks. backtest and everything etc.
--> also make sure there's enough liquidity for this, and that the options are not too expensive
A YouTuber by the name Benjamin just released a study on this, in his latest video. His backtests show it’s better to sell strangles, and to focus on stocks whose implied move is greater than their historical move.

- could also be interesting to see if selling right before earnings is the move
- https://www.youtube.com/channel/UCkcnYVAVZQOB-nXHechtXDg

paper around earnings straddles: https://papers.ssrn.com/sol3/Papers.cfm?abstract_id=2204549

short strangle buy when IV is abnormally high, run some backtests on this
IT IS ALL PRICED IN. The option markets are efficient, if you buy the contracts well before earnings you have to deal with theta and IV crush. If you buy the contracts right before earnings you have IV crush, making them about the same. In order to get 20-40% moves in your straddle you must buy relatively short dated contracts and the underlying asset (a stock) must move more than anticipated. Contracts that are longer dated will not move as much on earnings and if the underlying asset does not move much the contracts will be IV crushed.

calculate hurst exponent for different stocks, then trade only those with exponents close to 0/1, since those follow mean reversion and trend following strategies respectively.
if hurst exponent in increasing in a sliding window.

also todo make a UI where you can pick a stock and it shows buy signals across granularities, and you have a sensitivity slider.
