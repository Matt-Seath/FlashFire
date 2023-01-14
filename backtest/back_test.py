import backtrader as bt
from datetime import datetime

from backtest.strategies.all import *
from backtest.pipelines.django_pls import DjangoDataFeed
from core.models import StockHistory


STOCK = "A2M"

STRATEGY = BuyTheDipStrategy

FROMDATE = [2002, 11, 1]
TODATE__ = [2023, 1, 1]

FILTERS = {
    "stock_id": STOCK + ".AX",
    "datetime__gte": datetime(*FROMDATE),
    "datetime__lte": datetime(*TODATE__)
}


def main():
    cerebro = bt.Cerebro()

    cerebro.broker.set_cash(10000)
    queryset = StockHistory.objects.filter(**FILTERS)
    data = DjangoDataFeed(queryset)

    cerebro.adddata(data)

    cerebro.addstrategy(STRATEGY)

    print('Starting portfolio value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final portfolio value: %.2f' % cerebro.broker.getvalue())

    cerebro.plot()
