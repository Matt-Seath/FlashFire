import backtrader as bt
import math

from backtest.base_strategy import FFBaseStrategy


class GoldenCrossStrategy(FFBaseStrategy):
    key = "gcs"

    def __init__(self):
        self.fast = 5
        self.slow = 20
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period=self.fast, plotname=f"{self.fast} day moving average")
        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.slow, plotname=f"{self.slow} day moving average")
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


class PreCrossStrategy(FFBaseStrategy):
    key = "pcs"

    def __init__(self):
        self.fast = 5
        self.slow = 20
        self.can_cross = False
        self.fast_moving_average = bt.indicators.SMA(
            self.data.close, period=self.fast, plotname=f"{self.fast} day moving average")
        self.slow_moving_average = bt.indicators.SMA(
            self.data.close, period=self.slow, plotname=f"{self.slow} day moving average")
        self.crossover = bt.indicators.CrossOver(
            self.fast_moving_average, self.slow_moving_average)

        FFBaseStrategy.__init__(self)

    def next(self):
        diff_multiplier = 1.5
        fma_diff = self.fast_moving_average.lines.sma[0] - \
            self.fast_moving_average.lines.sma[-1]
        sma_diff = self.slow_moving_average.lines.sma[0] - \
            self.slow_moving_average.lines.sma[-1]
        fma_forecast = self.fast_moving_average.lines.sma[0] + (
            fma_diff * diff_multiplier)
        sma_forecast = self.slow_moving_average.lines.sma[0] + (
            sma_diff * diff_multiplier)
        # print(f"Slow: {self.slow_moving_average.lines.sma[0]}\n")

        data_date = self.get_date()
        if self.position.size == 0:
            if (fma_forecast > sma_forecast) and self.can_cross:

                if data_date >= self.alert_range:
                    self.buy_alerts.append(data_date)

                amount_to_invest = (self.order_percentage * self.broker.cash)
                self.size = math.floor(amount_to_invest / self.data.close)
                self.log_buy_order()
                self.order = self.buy(size=self.size)
                self.total_buys += 1

        if fma_forecast < sma_forecast:
            self.can_cross = True
            if self.position.size > 0:
                if data_date >= self.alert_range:
                    self.sell_alerts.append(data_date)
                self.log_sell_order()
                self.order = self.close()
                self.total_sells += 1
