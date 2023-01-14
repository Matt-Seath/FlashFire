import backtrader as bt
import datetime
import time
from backtrader.feeds.yahoo import YahooFinanceCSVData

from backtest.strategies import BuyTheDipStrategy
from backtest.pipelines.backtrader_pls import DjangoDataFeed


PATH = "assets/trader/datafeed.csv"
FROMDATE = datetime.datetime(2000, 12, 31)
TODATE = datetime.datetime(2001, 12, 31)


def countdown(text, dots=4, speed=1):
    print(text, end="")
    for i in range(dots):
        print(".kjkl", end="")
        time.sleep(speed)
    return


def main():
    cerebro = bt.Cerebro()

    cerebro.broker.set_cash(10000)

    # data = DjangoDataFeed()

    # data.todate = TODATE
    # data.fromdate = FROMDATE
    # data.ticker = "WES.AX"

    data = YahooFinanceCSVData(
        dataname=PATH,
        fromdate=FROMDATE,
        todate=TODATE,
        reverse=False
    )

    cerebro.adddata(data)

    cerebro.addstrategy(BuyTheDipStrategy)

    print('Starting portfolio value: %.2f' % cerebro.broker.getvalue())

    # countdown("\nStarting Cerebro")
    cerebro.run()

    print('Final portfolio value: %.2f' % cerebro.broker.getvalue())
