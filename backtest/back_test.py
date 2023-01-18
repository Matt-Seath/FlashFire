import backtrader as bt
from datetime import date

from backtest.strategies.all import *
from backtest.pipelines.django_pls import DjangoDataFeed
from core.models import StockHistory


STRATEGY = GoldenCrossStrategy

FROMDATE = [2022, 8, 13]
TODATE__ = [2023, 1, 13]


def main(symbol):

    FILTERS = {
        "stock_id": symbol + ".AX",
        "date__gte": date(*FROMDATE),
        "date__lt": date(*TODATE__)
    }

    cerebro = bt.Cerebro()

    cerebro.broker.set_cash(10000)
    queryset = StockHistory.objects.filter(**FILTERS)

    data = DjangoDataFeed(queryset)

    cerebro.adddata(data)

    cerebro.addstrategy(STRATEGY)

    cerebro.addsizer(bt.sizers.SizerFix, stake=1)

    print('\033[92mStarting portfolio value:\033[95m %.2f' %
          cerebro.broker.getvalue())

    cerebro.run()

    print('\033[92mFinal portfolio value:\033[95m %.2f' %
          cerebro.broker.getvalue())

    cerebro.plot()
