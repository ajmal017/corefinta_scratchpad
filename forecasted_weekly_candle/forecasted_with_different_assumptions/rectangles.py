import numpy as np
from finta import TA
import yfinance as yf
import plotly.graph_objects as go


import pandas as pd

from datetime import timedelta


""" do WMA 9 (all ATR w/i 1 band) 21 or 34 (smooth trend) for daily or 9 for weekly n = 5 ATR = 21"""
""" do change period 45 or 15 or 6 on weeklies - go back to the place of trend change"""
""" WMA9 for 2 day bars with ATR 21 """

ticker = "TQQQ"

# data = yf.download(tickers = ticker, start='2019-01-04', end='2021-06-09')
data = yf.download(tickers = ticker, period = "1y", interval = '1d')

# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

df1 = pd.DataFrame(data)

df2 = df1.reset_index()

fig1 = go.Figure(data=[go.Candlestick(x=df2['Date'],
                open=df2['Open'],
                high=df2['High'],
                low=df2['Low'],
                close=df2['Close'])]

)

fig1.add_shape(type="rect",
    x0='2021-08-30', y0=146, x1='2021-09-10', y1=152,
    line=dict(
        color="LightSeaGreen",
        width=2,
    ),
   fillcolor="RoyalBlue", opacity=0.4,

)

fig1.add_shape(type="rect",
    x0='2021-12-03', y0=144, x1='2021-12-22', y1=168,
    line=dict(
        color="LightSeaGreen",
        width=2,
    ),
   fillcolor="RoyalBlue", opacity=0.4,

)

fig1.add_shape(type="line",
    x0='2021-08-31', y0=145, x1='2021-12-21', y1=145,
    line=dict(
        color="LightSeaGreen",
        width=4,
        dash='dashdot',

    ),
               )

fig1.add_shape(type="line",
    x0='2021-12-07', y0=168, x1='2021-12-21', y1=168,
    line=dict(
        color="LightSeaGreen",
        width=4,
        dash='dashdot',

    ),
               )

fig1.add_shape(type="line",
    x0='2021-11-23', y0=183, x1='2021-12-21', y1=183,
    line=dict(
        color="LightSeaGreen",
        width=4,
        dash='dashdot',

    ),
               )

fig1.add_annotation(x='2021-12-14', y=168,
            text="1st Target",
            showarrow=True,
            arrowhead=1)

fig1.add_annotation(x='2021-12-09', y=183,
            text="2nd Target",
            showarrow=True,
            arrowhead=1)


fig1.update_shapes(dict(xref='x', yref='y'))

fig1.update_layout(hovermode='x', spikedistance = -1, width=1800, height=1200)

# fig1.update_xaxes(showspikes=True, spikemode='across', spikesnap='cursor', showline=True, showgrid=True)

fig1.update_yaxes(showspikes=True, spikemode='across', spikesnap='cursor', showline=True, showgrid=True, ticks='inside', nticks=40)

fig1.show()
