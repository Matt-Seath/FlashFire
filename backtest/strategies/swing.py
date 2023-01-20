import backtrader as bt
import math
from datetime import date, timedelta


class GoldenCrossStrategy(bt.Strategy):

    def __init__(self):
        self.alert_range = date.today() - timedelta(days=7)
        self.buy_alerts = []
        self.sell_alerts = []
        self.key = "gcs"
        self.fast = 5
        self.slow = 20
        self.total_buys = 0
        self.total_sells = 0
        self.order_percentage = 0.95

        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period=self.fast, plotname="50 day moving average")

        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.slow, plotname="200 day moving average")

        self.crossover = bt.indicators.CrossOver(
            self.fast_moving_average, self.slow_moving_average)

    def next(self):
        data_date = self.data.datetime.date()
        if self.position.size == 0:
            if self.crossover > 0:

                if data_date >= self.alert_range:
                    self.buy_alerts.append(data_date)

                amount_to_invest = (self.order_percentage * self.broker.cash)
                self.size = math.floor(amount_to_invest / self.data.close)

                print(
                    f"\033[0m{data_date} \033[96mBuy \033[0m{self.size} shares at {self.data.close[0]:.2f}")
                self.buy(size=self.size)
                self.total_buys += 1

        if self.position.size > 0:
            if self.crossover < 0:

                if data_date >= self.alert_range:
                    self.sell_alerts.append(data_date)

                print(
                    f"\033[0m{data_date} \033[95mSell \033[0m{self.size} shares at {self.data.close[0]:.2f}")
                self.close()
                self.total_sells += 1
