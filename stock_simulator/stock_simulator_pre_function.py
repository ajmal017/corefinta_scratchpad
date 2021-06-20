import time
import random
from finta import TA
import pandas as pd

# use outlook app and put it in favorites by selecting the sender email address and clicking star in upper-right
# then set notifications for favorites

class StockSimulator:

    def __init__(self):
        self.counter = 0
        self.buy_msg = "Buy today"
        self.stock_price = 0
        self.stock_list = []
        self.wma = 0
        self.signal = "NONE"

    def simulator(self):
        while self.counter < 10:
            self.stock_price = random.randint(0, 10)
            print(self.stock_price)
            self.stock_list.append(self.stock_price)
            if len(self.stock_list) > 3:
                self.stock_list.pop(0)
            print(self.stock_list)
            # self.simple_trigger()
            self.sma()
            prev_wma = self.wma
            self.finta_sma()
            if prev_wma != 0:
                if self.wma > prev_wma:
                    self.signal = "LONG"
                elif self.wma < prev_wma:
                    self.signal = "SHORT"
            print(self.signal)

            time.sleep(5)
            self.counter += 1

    def simple_trigger(self):
        if self.stock_price > 4:
            print('you hit it!')

    def sma(self):
        simple_ma = sum(self.stock_list) / len(self.stock_list)
        formatted_simplema = "{:.2f}".format(simple_ma)
        print(formatted_simplema)

    def finta_sma(self):
        df = pd.DataFrame()
        df['open'] = self.stock_list
        df['high'] = self.stock_list
        df['low'] = self.stock_list
        df['close'] = self. stock_list
        df['sma'] = TA.WMA(df, len(self.stock_list))
        self.wma = df['sma'].iloc[-1]
        print(self.wma)

    def trigger(self):
        x = 0
        while self.counter < 10:
            x = x + 1
            print(x)
            if x == 4:
                self.buy_msg = f"Short that {x} mutha!"
                print(self.buy_msg)
                break
            else:
                time.sleep(2)
                self.counter += 1

def main():
    app = StockSimulator()
    app.simulator()

if __name__ == "__main__":
    main()