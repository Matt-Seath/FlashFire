import backtrader as bt
import math


class GoldenCrossStrategy(bt.Strategy):

    def __init__(self):
        self.fast = 5
        self.slow = 20
        self.order_percentage = 0.95
        self.ticker = "A2M"

        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period=self.fast, plotname="50 day moving average")

        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.slow, plotname="200 day moving average")

        self.crossover = bt.indicators.CrossOver(
            self.fast_moving_average, self.slow_moving_average)

    def next(self):
        pass
