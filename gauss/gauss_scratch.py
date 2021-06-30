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
data = yf.download(tickers = ticker, period = "1y")

# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
# https://pypi.org/project/yfinance/
# data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")

df2 = pd.DataFrame(data)

# Gauss
num_periods_gauss = 16.5
df2['symbol'] = 2 * math.pi / num_periods_gauss
df2['beta'] = (1 - np.cos(df2['symbol']) ) / ((1.414)**(0.5) - 1)
df2['alpha'] = - df2['beta'] + (df2['beta']**2 + df2['beta'] * 2)**2

print(df2)
df2.to_csv('scratch.csv')
