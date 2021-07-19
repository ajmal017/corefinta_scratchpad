import pandas as pd
import mplfinance as mpf
import yfinance as yf

# https://stackoverflow.com/questions/41821916/charting-candlestick-ohlc-one-minute-bars-with-pandas-and-matplotlib

ticker = "NQ=F"
data = yf.download(tickers = ticker, period = "1mo", interval = '1d')

# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

df1 = pd.DataFrame(data)
df = df1.reset_index()

daily = df1
daily.index.name = 'Date'

mpf.plot(daily, type='candle')
