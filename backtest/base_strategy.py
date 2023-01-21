from datetime import date, timedelta
import backtrader as bt


class FFBaseStrategy(bt.Strategy):

    alert_range = date.today() - timedelta(days=100)
    buy_alerts = None
    sell_alerts = None
    total_buys = 0
    total_sells = 0

    def __init__(self):
        self.key = "btds"
        self.dataclose = self.datas[0].close
        self.sell_created = 0
        self.sell_executed = 0
        self.buy_created = 0
        self.buy_executed = 0
        self.order_percentage = 0.95
        self.order = None
        self.buy_alerts = []
        self.sell_alerts = []
        self.strategy_name = self.__class__.__name__

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def log_buy_order(self):
        print(
            f"\033[0m{self.get_date()} - Buy Order Placed - {self.size} shares at {self.data.close[0]:.2f}")

    def log_sell_order(self):
        print(
            f"\033[0m{self.get_date()} - Sell Order Placed - {self.size} shares at {self.data.close[0]:.2f}")

    def log_buy_exec(self):
        print(
            f"\033[0m{self.get_date()} - \033[96mBuy Executed\033[0m - {self.size} shares at {self.order.executed.price:.2f}")

    def log_sell_exec(self):
        print(
            f"\033[0m{self.get_date()} - \033[95mSell Executed\033[0m - {self.size} shares at {self.order.executed.price:.2f}")

    def get_date(self):
        return self.data.datetime.date()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log_buy_exec()
                self.buy_executed += 1
            elif order.issell():
                self.log_sell_exec()
                self.sell_executed += 1
            self.bar_executed = len(self)

        self.order = None
