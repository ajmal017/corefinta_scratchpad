import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

# https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946

# https://newbedev.com/plotting-graph-using-python-and-dispaying-it-using-html

# https://blog.heptanalytics.com/flask-plotly-dashboard/

ticker = 'NQ=F'

df = yf.download(tickers=ticker, period='2y', interval='1d')

df = df.reset_index()


# print(df)

fig1 = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])]

                 )



fig1.show()
