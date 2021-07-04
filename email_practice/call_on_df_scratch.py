import yfinance as yf
import pandas as pd

# https://stackoverflow.com/questions/21800169/python-pandas-get-index-of-rows-which-column-matches-certain-value
# https://stackoverflow.com/questions/51571121/how-to-select-rows-which-values-start-and-end-with-a-specific-value-in-pandas
# https://davidhamann.de/2017/06/26/pandas-select-elements-by-string/
# https://www.interviewqs.com/ddi-code-snippets/rows-cols-python
# https://stackoverflow.com/questions/41217310/get-index-of-a-row-of-a-pandas-dataframe-as-an-integer

# data = yf.download(tickers = ticker, start='2019-01-04', end='2021-06-09')
ticker = 'NQ=F'
data = yf.download(tickers=ticker, period="3mo", interval='1wk')
df = pd.DataFrame(data)
df = df.reset_index()
selected_date = df['Date'] == '2021-06-21'
selected_row = df.loc[selected_date]
# selected_index = df.index[selected_date]
selected_index = int(df[selected_date].index[0])

print(selected_row)
print(selected_index)
select_to_end = df[selected_index:len(df)]
print(select_to_end)
# print(df)

# print(df[['Date', 'Close']].tail(3))
