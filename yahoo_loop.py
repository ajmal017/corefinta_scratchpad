import yfinance as yf
import pandas as pd
import time

# data = yf.download(tickers = ticker, start='2019-01-04', end='2021-06-09')
# data = yf.download(tickers = ticker, period = "2y", interval = '1wk')
# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# https://pypi.org/project/yfinance/
# data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

# https://www.geeksforgeeks.org/python-how-to-get-the-last-element-of-list/

counter = 0

while counter < 40:
    ticker = "ES=F"
    interval = '1d'
    data = yf.download(tickers = ticker, period = "30m", interval = '1m')

    df = pd.DataFrame(data)
    close_lst = []

    close_lst.extend(df['Close'].tolist())
    # time.sleep(2)
    print(close_lst)
    highest_price = max(close_lst)
    print(highest_price)
    # latest_price = (close_lst[-1])
    # print(latest_price)
    time.sleep(10)
    counter += 1
