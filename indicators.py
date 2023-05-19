from pyti.money_flow_index import money_flow_index as mfi
from pyti.moving_average_convergence_divergence import moving_average_convergence_divergence as macd
from pyti.simple_moving_average import simple_moving_average as sma

def compute_indicators(df):
    # MFI
    MFI_PERIOD = 14
    df["mfi"] = mfi(df["Close"], df["High"], df["Low"], df["Volume"], MFI_PERIOD)

    # MACD
    SHORT_PERIOD = 12
    LONG_PERIOD = 26
    SIGNAL_PERIOD = 9
    df["macd"] = macd(df["Close"].to_numpy(), SHORT_PERIOD, LONG_PERIOD)
    df["macd_signal"] = sma(df["macd"], SIGNAL_PERIOD)
    df["macd_histogram"] = df["macd"] - df["macd_signal"]
    return df

# todo make this probabalistic, not binary
# fix a bug here where the signal_sum is not being calculated correctly
def identify_events(df, SENSITIVITY=3):
    # MFI > 80 or MFI < 20
    df["mfi_overbought"] = (df["mfi"] > 80).astype(int)
    df["mfi_oversold"] = (df["mfi"] < 20).astype(int)

    # MACD crossover
    df["macd_above"] = (df["macd"] > df["macd_signal"]).astype(int)
    # crossover is when macd_above changes from 0 to 1
    df["macd_crossover"] = (df["macd_above"] - df["macd_above"].shift(1)) == 1
    df["macd_crossunder"] = (df["macd_above"] - df["macd_above"].shift(1)) == -1

    df["signal"] = df["mfi_oversold"] - df["mfi_overbought"] + df["macd_crossover"] - df["macd_crossunder"]
    df['signal_sum'] = df['signal'].rolling(SENSITIVITY).sum()
    df['signal_sum'] = df['signal_sum'].fillna(0)
    df['signal_sum'] = df['signal_sum'].astype(int)

    return df