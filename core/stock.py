from typing import Literal, List, Tuple, LiteralString
import pandas as pd
import wallstreet as ws
import pandas_ta as ta

VALID_INTERVALS = Literal[
    "1m", "2m", "5m", "15m", "30m", "1h", "90m", "1d", "1wk", "1mo", "3mo"
]
PERIOD_LIMITS_IN_MINS = {
    "1m": 7 * 24 * 60,
    "2m": 7 * 24 * 60,
    "5m": 7 * 24 * 60,
    "15m": 7 * 24 * 60,
    "30m": 7 * 24 * 60,
    "90m": 7 * 24 * 60,
    "1h": 730 * 24 * 60,
    "1d": None,
    "5d": None,
    "1wk": None,
    "1mo": None,
    "3mo": None,
}


class Stock:
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker

    def get_historical_data(
        self, period: str, interval: Literal["1m", "1h", "1d", "1wk", "1mo", "3mo"]
    ) -> None:
        if interval not in VALID_INTERVALS:
            raise Exception(
                f"Invalid interval '{interval}', must be one of {VALID_INTERVALS}"
            )

        period_limit = PERIOD_LIMITS_IN_MINS[interval]

        # convert period to minutes
        period_in_mins = None
        if period[-1] == "d":
            period_in_mins = int(period[:-1]) * 24 * 60
        elif period[-2:] == "wk":
            period_in_mins = int(period[:-2]) * 24 * 60 * 7
        elif period[-2:] == "mo":
            period_in_mins = int(period[:-2]) * 24 * 60 * 30
        elif period[-1] == "y":
            period_in_mins = int(period[:-1]) * 24 * 60 * 365
        else:
            raise Exception(f"Invalid period '{period}'")

        if period_in_mins <= period_limit:
            # start date is 1 year ago
            self.df = pd.DataFrame().ta.ticker(
                self.ticker, period=period, interval=interval
            )
        else:
            raise Exception(f"Period of {period} is too long for interval {interval}")

    def compute_technical_indicators(self) -> None:
        pass

    def get_todays_data(self) -> None:
        pass

    def to_csv(self, filepath: str) -> None:
        self.df.to_csv(filepath)
