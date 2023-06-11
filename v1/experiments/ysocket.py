import yliveticker

last_time = {}
time_diff = {}


# this function is called on each ticker update
def on_new_msg(ws, msg):
    time = msg["timestamp"]
    ticker = msg["id"]
    if ticker in last_time:
        time_diff[ticker] = time - last_time[ticker]
    last_time[ticker] = time
    print(f"Average time between updates: {sum(time_diff.values()) / len(time_diff)}")
    print(time_diff)


yliveticker.YLiveTicker(
    on_ticker=on_new_msg, ticker_names=["TQQQ", "AAPL", "AMZN", "MSFT", "GOOG", "FB"]
)
