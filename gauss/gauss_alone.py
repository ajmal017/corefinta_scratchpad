import math
import numpy as np
from finta import TA
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px

import pandas as pd

from datetime import datetime

ticker = "NQ=F"
#data = yf.download(tickers = ticker, start='2010-01-04', end='2018-12-31')
data = yf.download(tickers = ticker, period = "2y", interval = '1wk')

# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# https://pypi.org/project/yfinance/
# data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

df2 = pd.DataFrame(data)

df2 = df2.reset_index()

# Gauss
num_periods_gauss = 15.5
df2['symbol'] = 2 * math.pi / num_periods_gauss
df2['beta'] = (1 - np.cos(df2['symbol']) ) / ((1.414)**(0.5) - 1)
df2['alpha'] = - df2['beta'] + (df2['beta']**2 + df2['beta'] * 2)**2

# Gauss equation
# initialize
df2.loc[0, 'gauss'] = df2.loc[0, 'Close']
df2.loc[1, 'gauss'] = df2.loc[1, 'Close']
df2.loc[2, 'gauss'] = df2.loc[2, 'Close']
df2.loc[3, 'gauss'] = df2.loc[3, 'Close']
df2.loc[4, 'gauss'] = df2.loc[4, 'Close']

for i in range (4, len(df2)):
    df2.loc[i, 'gauss'] = df2.loc[i, 'Close'] * df2.loc[i, 'alpha']**4 + (4 * (1 - df2.loc[i, 'alpha']))*df2.loc[i-1, 'gauss'] \
                          - (6 * ((1 - df2.loc[i, 'alpha']) ** 2) * df2.loc[i - 2, 'gauss']) \
                          + (4 * (1 - df2.loc[i, 'alpha']) ** 3) * df2.loc[i - 3, 'gauss'] \
                          - ((1 - df2.loc[i, 'alpha']) ** 4) * df2.loc[i - 4, 'gauss']

# ATR

# https://www.statology.org/exponential-moving-average-pandas/
num_periods_ATR = 21
multiplier = 1

df2['ATR_diff'] = df2['High'] - df2['Low']
df2['ATR'] = df2['ATR_diff'].ewm(span=num_periods_ATR, adjust=False).mean()
# df2['ATR'] = df2['ATR_diff'].rolling(window=num_periods_ATR).mean()
df2['Line'] = df2['gauss']
df2['upper_band'] = df2['Line'] + multiplier * df2['ATR']
df2['lower_band'] = df2['Line'] - multiplier * df2['ATR']

multiplier_1 = 1.6
multiplier_2 = 1.4

df2['upper_band_1'] = df2['Line'] + multiplier_1 * df2['ATR']
df2['lower_band_1'] = df2['Line'] - multiplier_1 * df2['ATR']

df2['upper_band_2'] = df2['Line'] + multiplier_2 * df2['ATR']
df2['lower_band_2'] = df2['Line'] - multiplier_2 * df2['ATR']


print(df2)

df2.to_csv("gauss.csv")

# https://community.plotly.com/t/how-to-plot-multiple-lines-on-the-same-y-axis-using-plotly-express/29219/9

# https://plotly.com/python/legend/#legend-item-names

# fig1 = px.scatter(df2, x='date', y=['close', 'open', 'high', 'low'], title='SPY Daily Chart')

fig1 = go.Figure(data=[go.Candlestick(x=df2['Date'],
                open=df2['Open'],
                high=df2['High'],
                low=df2['Low'],
                close=df2['Close'])]

)

fig1.add_trace(
    go.Scatter(
        x=df2['Date'],
        y=df2['upper_band'],
        name='upper band',
        mode="lines",
        line=go.scatter.Line(color="gray"),
        showlegend=True)
)

fig1.add_trace(
    go.Scatter(
        x=df2['Date'],
        y=df2['lower_band'],
        name='lower band',
        mode="lines",
        line=go.scatter.Line(color="gray"),
        showlegend=True)
)

fig1.add_trace(
    go.Scatter(
        x=df2['Date'],
        y=df2['upper_band_1'],
        name='upper band_1',
        mode="lines",
        line=go.scatter.Line(color="gray"),
        showlegend=True)
)

fig1.add_trace(
    go.Scatter(
        x=df2['Date'],
        y=df2['lower_band_1'],
        name='lower band_1',
        mode="lines",
        line=go.scatter.Line(color="gray"),
        showlegend=True)
)


fig1.add_trace(
    go.Scatter(
        x=df2['Date'],
        y=df2['Line'],
        name="Gauss",
        mode="lines",
        line=go.scatter.Line(color="blue"),
        showlegend=True)
)

fig1.show()

