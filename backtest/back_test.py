import backtrader as bt
import datetime

from backtest.strategies.all import *
from backtest.pipelines.django_pls import DjangoDataFeed
from core.models import StockHistory

STOCK = "A2M"
STRATEGY = BuyTheDipStrategy()

FROMDATE = datetime.datetime(2000, 12, 31)
TODATE = datetime.datetime(2001, 12, 31)


def main():
    cerebro = bt.Cerebro()

    cerebro.broker.set_cash(10000)
    queryset = StockHistory.objects.filter(stock_id=STOCK + ".AX")
    data = DjangoDataFeed(queryset)

    cerebro.adddata(data)

    cerebro.addstrategy(STRATEGY)

    print('Starting portfolio value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final portfolio value: %.2f' % cerebro.broker.getvalue())

    cerebro.plot()
