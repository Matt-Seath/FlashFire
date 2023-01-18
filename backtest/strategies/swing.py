import backtrader as bt
import math


class GoldenCrossStrategy(bt.Strategy):

    def __init__(self):
        self.key = "gcs"
        self.fast = 5
        self.slow = 20
        self.order_percentage = 0.95

        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period=self.fast, plotname="50 day moving average")

        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.slow, plotname="200 day moving average")

        self.crossover = bt.indicators.CrossOver(
            self.fast_moving_average, self.slow_moving_average)

    def next(self):
        if self.position.size == 0:
            if self.crossover > 0:
                amount_to_invest = (self.order_percentage * self.broker.cash)
                self.size = math.floor(amount_to_invest / self.data.close)

                print(
                    f"\033[96mBuy \033[0m{self.size} shares at {self.data.close[0]:.2f}")
                self.buy(size=self.size)

        if self.position.size > 0:
            if self.crossover < 0:

                print(
                    f"\033[93mSell \033[0m{self.size} shares at {self.data.close[0]:.2f}")
                self.close()
