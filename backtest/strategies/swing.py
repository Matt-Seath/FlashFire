import backtrader as bt
import math

from backtest.base_strategy import FFBaseStrategy


class GoldenCrossStrategy(FFBaseStrategy):

    def __init__(self):
        self.fast = 5
        self.slow = 20
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period=self.fast, plotname="50 day moving average")
        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.slow, plotname="200 day moving average")
        self.crossover = bt.indicators.CrossOver(
            self.fast_moving_average, self.slow_moving_average)

        FFBaseStrategy.__init__(self)

    def next(self):
        data_date = self.get_date()
        if self.position.size == 0:
            if self.crossover > 0:

                if data_date >= self.alert_range:
                    self.buy_alerts.append(data_date)

                amount_to_invest = (self.order_percentage * self.broker.cash)
                self.size = math.floor(amount_to_invest / self.data.close)
                self.log_buy_order()
                self.order = self.buy(size=self.size)
                self.total_buys += 1

        if self.position.size > 0:
            if self.crossover < 0:

                if data_date >= self.alert_range:
                    self.sell_alerts.append(data_date)
                self.log_sell_order()
                self.order = self.close()
                self.total_sells += 1
