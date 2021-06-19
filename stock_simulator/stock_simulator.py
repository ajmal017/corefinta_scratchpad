import time
import random

# use outlook app and put it in favorites by selecting the sender email address and clicking star in upper-right
# then set notifications for favorites

class StockSimulator:

    def __init__(self):
        self.counter = 0
        self.buy_msg = "Buy today"
        self.stock_price = 0
        self.stock_list = []

    def simulator(self):
        while self.counter < 10:
            self.stock_price = random.randint(0, 10)
            print(self.stock_price)
            self.stock_list.append(self.stock_price)
            if len(self.stock_list) > 3:
                self.stock_list.pop(0)
            print(self.stock_list)
            # self.simple_trigger()
            time.sleep(5)
            self.counter += 1

    def simple_trigger(self):
        if self.stock_price > 4:
            print('you hit it!')

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