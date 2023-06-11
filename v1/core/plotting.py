from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_ticker(df, ticker, last_n_days):

    fig = make_subplots(rows=3, cols=1)

    # Candlestick
    fig.append_trace(
            go.Candlestick(
                x=df["Date"],
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
                increasing_line_color="green",
                decreasing_line_color="red",
            ),
            row=1, col=1
    )
    # plot signal as histogram (green for buy > 0, red for sell < 0)
    fig.append_trace(
            go.Bar(
                x=df["Date"],
                y=df["signal_sum"] * max(df["Close"]) / 10,
                marker=dict(color=df["signal_sum"].apply(lambda x: "green" if x > 0 else "red")),
            ),
            row=1, col=1
    )

    # MACD
    fig.append_trace(
            go.Scatter(x=df["Date"], y=df["macd"], line=dict(color="blue", width=1)),
            row=2, col=1
    )

    fig.append_trace(
            go.Scatter(x=df["Date"], y=df["macd_signal"], line=dict(color="orange", width=1)),
            row=2, col=1
    )
    fig.append_trace(
            go.Bar(x=df["Date"], y=df["macd_histogram"], marker=dict(color="gray")),
            row=2, col=1
    )
    # highlight MACD crossover events
    fig.append_trace(
            go.Scatter(
                x=df["Date"],
                y=df["macd"].where(df["macd_crossover"]),
                mode="markers",
                marker=dict(color="green", size=10),
            ),
            row=2, col=1
    )
    fig.append_trace(
            go.Scatter(
                x=df["Date"],
                y=df["macd"].where(df["macd_crossunder"]),
                mode="markers",
                marker=dict(color="red", size=10),
            ),
            row=2, col=1
    )

    # MFI
    fig.append_trace(
                go.Scatter(
                x=df["Date"],
                y=df["mfi"],
                line=dict(color="purple", width=1),
                yaxis="y2",
            ),
            row=3, col=1
    )
    # 80/20 lines
    fig.append_trace(
            go.Scatter(
                x=df["Date"],
                y=[80] * len(df["Date"]),
                line=dict(color="gray", width=1, dash="dash"),
                yaxis="y2",
            ),
            row=3, col=1
    )
    fig.append_trace(
            go.Scatter(
                x=df["Date"],
                y=[20] * len(df["Date"]),
                line=dict(color="gray", width=1, dash="dash"),
                yaxis="y2",
            ),
            row=3, col=1
    )

    # highlight MFI > 80 red and MFI < 20 green
    fig.append_trace(

            go.Scatter(
                x=df["Date"],
                y=[None if mfi < 80 else df["mfi"][i] for i, mfi in enumerate(df["mfi"])],
                mode="markers",
                marker=dict(color="red", size=10),
                yaxis="y2",
            ),
            row=3, col=1
    )
    fig.append_trace(

            go.Scatter(
                x=df["Date"],
                y=[None if mfi > 20 else df["mfi"][i] for i, mfi in enumerate(df["mfi"])],
                mode="markers",
                marker=dict(color="green", size=10),
                yaxis="y2",
            ),
            row=3, col=1
    )


    # Update xaxis properties
    fig.update_layout(
            title=f"{ticker} - {last_n_days} days",
            xaxis_rangeslider_visible=False,
            showlegend=False,
            height=1200,
            width=700,
    )

    # Update yaxis properties
    fig.update_yaxes(title_text="Price", row=1, col=1)
    fig.update_yaxes(title_text="MACD", row=2, col=1)
    fig.update_yaxes(title_text="MFI", row=3, col=1)

    # 2 y axes for row 1 (price and SIGNAL)
    fig.update_yaxes(title_text="SIGNAL", row=1, col=1, secondary_y=True)

    fig.show()