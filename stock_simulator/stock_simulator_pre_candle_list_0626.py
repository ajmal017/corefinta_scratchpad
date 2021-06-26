import time
import random
from finta import TA
import pandas as pd
import yfinance as yf

# creates a stock simulator, generates an indicator and buy/sell signals
# can be ported to any market data API, for prices and FIX engine to send trades to the market
NUM_PERIODS = 3
TICKS_PER_CANDLE = 4
TICKS_IN_TEST_PERIOD = 20

class StockSimulator:

    def __init__(self):
        self.tick_count = 0
        self.stock_price = 0
        self.stock_list = []
        self.indicator = 0
        self.wma_formatted = 0
        self.signal = "NONE"
        self.yahoo_counter = 0
        self.df = pd.DataFrame()
        self.wma_msg = None
        self.ticks_per_candle = TICKS_PER_CANDLE
        self.periods = NUM_PERIODS
        self.candle_count = 0
        self.ticks_in_test_period = TICKS_IN_TEST_PERIOD
        self.n = 0

    # This is the simulator that executes all the methods
    def simulator(self):
        sleep_seconds = 2
        self.generate_yahoo_stock_px()
        while self.tick_count < self.ticks_in_test_period:
            self.choose_yahoo_stock_px()
            self.stock_list_mgr()
            self.update_signal()
            self.print_statement()
            time.sleep(sleep_seconds)
            self.tick_count += 1

    # Generate the stock price
    def generate_stock_price(self):
        lowest_stock_px = 1
        highest_stock_px = 10
        self.stock_price = random.randint(lowest_stock_px, highest_stock_px)
        stock_px_formatted = "{:.2f}".format(self.stock_price)
        stock_price_msg = f'price: {stock_px_formatted}'
        print(stock_price_msg)

    def generate_yahoo_stock_px(self):
        # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        ticker = "NQ=F"
        # data = yf.download(tickers=ticker, start='2010-01-04', end='2018-12-31')
        data = yf.download(tickers = ticker, period = "1mo")
        self.df = data
        self.df.to_csv('stock_px_sample.csv')

    def choose_yahoo_stock_px(self):
        self.candle_count = str(self.tick_count // self.ticks_per_candle + 1).zfill(3)
        self.tick_number = str(self.tick_count % self.ticks_per_candle + 1).zfill(3)
        self.stock_price = self.df['Close'].iloc[self.yahoo_counter]
        stock_px_formatted = "{:.2f}".format(self.stock_price)
        stock_price_msg = f'price: {stock_px_formatted}'
        # print(stock_price_msg)
        self.yahoo_counter += 1

    # Create a list that collects most recent indicator length of stock prices
    def stock_list_mgr(self):
        self.stock_list.append(self.stock_price)
        if len(self.stock_list) > self.periods:
            self.stock_list.pop(0)
        # stock_list_msg = f'list of stock prices: {self.stock_list}'
        # print(stock_list_msg)

    def candle_list_mgr(self):
        if self.tick_number == self.ticks_per_candle - 1:
            self.stock_list.append(self.stock_price)
            self.n += 1
            if self.n < self.periods:
                return

    # Calculate indicator value by converting list to a dataframe and using Finta package
    def finta_indicator(self):
        df = pd.DataFrame()
        df['open'] = self.stock_list
        df['high'] = self.stock_list
        df['low'] = self.stock_list
        df['close'] = self. stock_list
        fin_ta_indicator = TA.WMA
        df['indicator'] = fin_ta_indicator(df, len(self.stock_list))
        recent_indicator_value = df['indicator'].iloc[-1]
        self.indicator = recent_indicator_value
        self.wma_formatted = "{:.2f}".format(self.indicator)
        fin_ta_formatted = fin_ta_indicator.__name__
        self.wma_msg = f'{fin_ta_formatted}: {self.wma_formatted}'
        # print(self.wma_msg)

    # Generate buy/sell signal based on trend pointing up or down on indicator
    def update_signal(self):
        prev_indicator = self.indicator
        self.finta_indicator()
        if prev_indicator != 0:
            if self.indicator > prev_indicator:
                self.signal = "LONG at " + str(self.wma_formatted) + ' or higher'
            elif self.indicator < prev_indicator:
                self.signal = "SHORT at " + str(self.wma_formatted) + ' or lower'
        # print(self.signal)

    def print_statement(self):
        print(f'Candle:{self.candle_count} Tick: {self.tick_number} price: {self.stock_price} list:{self.stock_list} {self.wma_msg} {self.signal}')


def main():
    app = StockSimulator()
    app.simulator()

if __name__ == "__main__":
    main()