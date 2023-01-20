from datetime import date, timedelta


class BaseStrategy:

    alert_range = date.today() - timedelta(days=100)
    buy_alerts = None
    sell_alerts = None
    total_buys = 0
    total_sells = 0

    def __init__(self):
        self.buy_alerts = []
        self.sell_alerts = []
        self.strategy_name = self.__class__.__name__
