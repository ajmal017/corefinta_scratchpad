import yfinance as yf
import pandas as pd

ticker = "NQ=F"
data = yf.download(tickers = ticker, start='2000-01-04', end='2021-06-01')
# data = yf.download(tickers = ticker, period = "1y", interval = '5m')

# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# https://pypi.org/project/yfinance/
# data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

df = pd.DataFrame(data)
print(df)
df.to_csv('yahoo_download_09182000')
