import numpy as np
from finta import TA
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px

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

df = df1.reset_index()

df7 = df.rename(columns = {'Date': 'date', 'Open':'open', 'High': 'high', 'Low':'low', 'Close':'close','Volume': 'volume'}, inplace = False)

df7.to_csv('daily.csv')

n = 5

df3 = df7.groupby(np.arange(len(df7))//n).max()
# print('df3 max:', df3)

df4 = df7.groupby(np.arange(len(df7))//n).min()
# print('df4 min:', df4)

df5 = df7.groupby(np.arange(len(df7))//n).first()
# print('df5 open:', df5)

df6 = df7.groupby(np.arange(len(df7))//n).last()
# print('df6 close:', df6)

agg_df = pd.DataFrame()

agg_df['date'] = df6['date']
agg_df['low'] = df4['low']
agg_df['high'] = df3['high']
agg_df['open'] = df5['open']
agg_df['close'] = df6['close']

# print(agg_df)

df2 = agg_df

# print(df2)
num_periods = 21
df2['SMA'] = TA.SMA(df2, 21)
df2['FRAMA'] = TA.FRAMA(df2, 10)
df2['WMA'] = TA.WMA(df2, 9)
df2['TEMA'] = TA.TEMA(df2, num_periods)
# df2['VWAP'] = TA.VWAP(df2)

# ATR

num_periods_ATR = 21
multiplier = 1

df2['ATR_diff'] = df2['high'] - df2['low']
df2['ATR'] = df2['ATR_diff'].ewm(span=num_periods_ATR, adjust=False).mean()
df2['Line'] = df2['WMA'].round(2)
df2['line_change'] = df2['Line'] / df2['Line'].shift(1)
df3 = pd.DataFrame()
df3['date'] = df2['date']
df3['close'] = df2['line_change']
df3['open'] = df2['line_change']
df3['high'] = df2['line_change']
df3['low'] = df2['line_change']

# calculate projection angle
periods_change = 5 # drives the projection

df3['change_SMA'] = TA.WMA(df3, periods_change) # drives the projection
df2['change_SMA'] = df3['change_SMA']

df2['upper_band'] = df2['Line'] + multiplier * df2['ATR']
df2['lower_band'] = df2['Line'] - multiplier * df2['ATR']

multiplier_1 = 1.6
multiplier_2 = 2.3

df2['upper_band_1'] = (df2['Line'] + multiplier_1 * df2['ATR']).round(2)
df2['lower_band_1'] = (df2['Line'] - multiplier_1 * df2['ATR']).round(2)

df2['upper_band_2'] = df2['Line'] + multiplier_2 * df2['ATR'].round(2)
df2['lower_band_2'] = df2['Line'] - multiplier_2 * df2['ATR'].round(2)

# try the loop again
bars_back = 10
date_diff = df2.loc[len(df2)-1, 'date'] - df2.loc[len(df2)-2, 'date']

line_diff = df2.loc[len(df2)-1, 'change_SMA']

def date_by_adding_business_days(from_date, add_days):
    business_days_to_add = add_days
    current_date = from_date
    while business_days_to_add > 0:
        current_date += timedelta(days=1)
        weekday = current_date.weekday()
        if weekday >= 5: # sunday = 6
            continue
        business_days_to_add -= 1
    return current_date

counter = 0
bars_out = 20
while counter < bars_out:

    df2.loc[len(df2), 'Line'] = df2.loc[len(df2) - 1, 'Line'] * line_diff
    df2.loc[len(df2) - 1, 'date'] = date_by_adding_business_days(df2.loc[len(df2) - 2, 'date'], n)
    counter += 1

multiplier_projection = multiplier
multiplier_1_projection = multiplier_1
multiplier_2_projection = multiplier_2

ATR = df2.loc[len(df2) - bars_out - 1, 'ATR'] * multiplier_projection
ATR_1 = df2.loc[len(df2) - bars_out - 1, 'ATR'] * multiplier_1_projection
ATR_2 = df2.loc[len(df2) - bars_out - 1, 'ATR'] * multiplier_2_projection

counter1 = 0
while counter1 < bars_out:
    df2.loc[len(df2) - bars_out + counter1-1, 'upper_band_1'] = df2.loc[len(df2) - bars_out - 1 + counter1, 'Line'] + ATR_1
    df2.loc[len(df2) - bars_out + counter1-1, 'lower_band_1'] = df2.loc[len(df2) - bars_out - 1 + counter1, 'Line'] - ATR_1
    df2.loc[len(df2) - bars_out + counter1-1, 'upper_band_2'] = df2.loc[len(df2) - bars_out - 1 + counter1, 'Line'] + ATR_2
    df2.loc[len(df2) - bars_out + counter1-1, 'lower_band_2'] = df2.loc[len(df2) - bars_out - 1 + counter1, 'Line'] - ATR_2
    df2.loc[len(df2) - bars_out + counter1-1, 'upper_band'] = df2.loc[len(df2) - bars_out - 1 + counter1, 'Line'] + ATR
    df2.loc[len(df2) - bars_out + counter1-1, 'lower_band'] = df2.loc[len(df2) - bars_out - 1 + counter1, 'Line'] - ATR

    counter1 += 1

recent_price = df2['close'].iloc[-bars_out-1]
# print(recent_price)
df2['recent_px'] = recent_price
df2['dist_to_upper'] = df2['upper_band'] / df2['recent_px'] - 1
df2['dist_to_lower'] = df2['lower_band'] / df2['recent_px'] - 1
df2['dist_to_line'] = df2['Line'] / df2['recent_px'] - 1

etf_data = yf.download(tickers = ticker, period = '5d', interval = '1d')
etf_df = pd.DataFrame(etf_data)
recent_etf = etf_df['Close'].iloc[-1]
# print(recent_etf)
df2['etf'] = recent_etf
df2['etf_upper'] = df2['etf']*(1 + df2['dist_to_upper']*3)
df2['etf_lower'] = df2['etf']*(1 + df2['dist_to_lower']*3)
df2['etf_line'] = df2['etf']*(1 + df2['dist_to_line']*3)

selected_range = df2[['date', 'etf', 'etf_line', 'etf_upper', 'etf_lower']].tail(21).round(2)
print(selected_range)
selected_range.to_csv('selected.csv')

df2.to_csv("gauss.csv")

# https://community.plotly.com/t/how-to-plot-multiple-lines-on-the-same-y-axis-using-plotly-express/29219/9

# https://plotly.com/python/legend/#legend-item-names

# fig1 = px.scatter(df2, x='date', y=['close', 'open', 'high', 'low'], title='SPY Daily Chart')

fig1 = go.Figure(data=[go.Candlestick(x=df2['date'],
                open=df2['open'],
                high=df2['high'],
                low=df2['low'],
                close=df2['close'])]

)

fig1.add_trace(
    go.Scatter(
        x=df2['date'],
        y=df2['upper_band'].round(2),
        name='upper band',
        mode="lines",
        line=go.scatter.Line(color="gray"),
        )
)

fig1.add_trace(
    go.Scatter(
        x=df2['date'],
        y=df2['lower_band'].round(2),
        name='lower band',
        mode="lines",
        line=go.scatter.Line(color="gray"),
        )
)

fig1.add_trace(
    go.Scatter(
        x=df2['date'],
        y=df2['upper_band_1'].round(2),
        name='upper band_1',
        mode="lines",
        line=go.scatter.Line(color="gray"),
        )
)

fig1.add_trace(
    go.Scatter(
        x=df2['date'],
        y=df2['lower_band_1'].round(2),
        name='lower band_1',
        mode="lines",
        line=go.scatter.Line(color="gray"))
)

fig1.add_trace(
    go.Scatter(
        x=df2['date'],
        y=df2['Line'],
        name="WMA",
        mode="lines",
        line=go.scatter.Line(color="blue"))
)

# fig1.add_vrect(x0='11-04-2021', x1='11-26-2021', fillcolor='LightSalmon', opacity=0.5, layer='below', line_width=0)

# fig1.update_layout(
#     title = f'{ticker} Chart', hovermode = 'x unified', width=2000, height=1200, showlegend=False
# )

fig1.add_shape(type='rect', xref='paper', yref='paper', x0='11-04-2021', y0=140, x1='11-26-2021', y1=160,
               line=dict(color='LightSeaGreen', width=3,), fillcolor='PaleTurquoise',)

fig1.show()
