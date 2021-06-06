import yfinance as yf
import pandas as pd

tickers = ['TSLA', 'MSFT']

class Yahoo:
    def historical(self):
        # tickers = ['TSLA', 'MSFT']
        for i in tickers:
            data = yf.download(i, period='1y')
            df = pd.DataFrame(data)
            print(df)
            df.to_csv(i + '.csv')


def main():
    app = Yahoo()
    app.historical()


if __name__ == "__main__":
    main()