import math

from backtest.base_strategy import FFBaseStrategy


class BuyTheDipStrategy(FFBaseStrategy):
    key = "btd"

    def __init__(self):
        FFBaseStrategy.__init__(self)

    def next(self):
        if self.order:
            return

        if not self.position:
            if self.dataclose[0] < self.dataclose[-1]:

                if self.dataclose[-1] < self.dataclose[-2]:

                    amount_to_invest = (
                        self.order_percentage * self.broker.cash)
                    self.size = math.floor(amount_to_invest / self.data.close)
                    self.log_buy_order()
                    self.order = self.buy(size=self.size)
                    self.buy_created += 1
        else:
            if len(self) >= (self.bar_executed + 5):
                self.order = self.close()
                self.sell_created += 1
                self.log_sell_order()
