import time
import random
from finta import TA
import pandas as pd

# creates a stock simulator, generates an indicator and buy/sell signals
# can be ported to any market data API, for prices and FIX engine to send trades to the market

class StockSimulator:

    def __init__(self):
        self.counter = 0
        self.buy_msg = "Buy today"
        self.stock_price = 0
        self.stock_list = []
        self.indicator = 0
        self.signal = "NONE"

    # This is the simulator that executes all the methods
    def simulator(self):
        num_candles_in_test_period = 10
        # length_of_indicator = 4
        sleep_seconds = 2
        while self.counter < num_candles_in_test_period:
            self.generate_stock_price()
            self.stock_list_mgr()
            self.update_signal()
            time.sleep(sleep_seconds)
            self.counter += 1

    # Generate the stock price
    def generate_stock_price(self):
        lowest_stock_px = 1
        highest_stock_px = 10
        self.stock_price = "{:.2f}".format(random.randint(lowest_stock_px, highest_stock_px))
        stock_price_msg = f'latest stock price: {self.stock_price}'
        print(stock_price_msg)

    # Create a list that collects most recent indicator length of stock prices
    def stock_list_mgr(self):
        length_of_indicator = 4
        self.stock_list.append(self.stock_price)
        if len(self.stock_list) > length_of_indicator:
            self.stock_list.pop(0)
        stock_list_msg = f'list of stock prices: {self.stock_list}'
        print(stock_list_msg)

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
        self.indicator = "{:.2f}".format(recent_indicator_value)
        wma_msg = f'WMA: {self.indicator}'
        print(wma_msg)

    # Generate buy/sell signal based on trend pointing up or down on indicator
    def update_signal(self):
        prev_indicator = self.indicator
        self.finta_indicator()
        if prev_indicator != 0:
            if self.indicator > prev_indicator:
                self.signal = "LONG"
            elif self.indicator < prev_indicator:
                self.signal = "SHORT"
        print(self.signal)

def main():
    app = StockSimulator()
    app.simulator()

if __name__ == "__main__":
    main()