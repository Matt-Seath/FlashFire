from datetime import date, timedelta
import backtrader as bt

from loggers.coloured_text import Colour


class FFBaseStrategy(bt.Strategy):

    alert_range = date.today() - timedelta(days=3)
    buy_alerts = None
    sell_alerts = None
    total_buys = 0
    total_sells = 0
    key = "ffb"

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.sell_created = 0
        self.sell_executed = 0
        self.buy_created = 0
        self.buy_executed = 0
        self.order_percentage = 0.95
        self.order = None
        self.buy_alerts = []
        self.sell_alerts = []
        self.counter = 0
        self.strategy_name = self.__class__.__name__

    def log_buy_order(self):
        print(
            f"{Colour.ENDC}{str(self.get_date()):<12}{'Buy Order':<15}{self.size} shares at {self.data.close[0]:.2f}")

    def log_sell_order(self):
        print(
            f"{Colour.ENDC}{str(self.get_date()):<12}{'Sell Order':<15}{self.size} shares at {self.data.close[0]:.2f}")

    def log_exec(self, txt, txt_colour):
        print(
            f"{Colour.ENDC}{str(self.get_date()):<12}{txt_colour}{txt:<15}{Colour.ENDC}{self.size} shares at {txt_colour}{self.order.executed.price:.2f}{Colour.ENDC}")

    def get_date(self):
        return self.data.datetime.date()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log_exec("BUY EXECUTED", Colour.OKBLUE)
                self.buy_executed += 1
            elif order.issell():
                self.log_exec("SELL EXECUTED", Colour.HEADER)
                self.sell_executed += 1
            self.bar_executed = len(self)

        self.order = None
