import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# plt.axis([0, 50, 0, 1]) # limits for x and y

ticker = "NQ=F"

# data = yf.download(tickers = ticker, start='2019-01-04', end='2021-06-09')
data = yf.download(tickers = ticker, period = "1mo", interval = '1d')

# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

df1 = pd.DataFrame(data)
df = df1.reset_index()
j = 0
k = 0
# print(df)
for i in range(len(df)):
    y = df.loc[j, 'Close']
    date = df.loc[k, 'Date']
    plt.scatter(date, y)
    j += 1
    k += 1
    plt.pause(1)

plt.show()

