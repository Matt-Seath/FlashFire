import backtrader as bt
import datetime
import time

from backtest.strategies import TestStrategy


PATH = "assets/trader/datafeed.csv"
FROMDATE = datetime.datetime(2000, 1, 1)
TODATE = datetime.datetime(2001, 12, 31)


def countdown(text, dots=4, speed=1):
    print(text, end="")
    for i in range(dots):
        print(".kjkl", end="")
        time.sleep(speed)
    return


def main():
    cerebro = bt.Cerebro()

    cerebro.broker.set_cash(100000)

    data = bt.feeds.YahooFinanceCSVData(
        dataname=PATH,
        fromdate=FROMDATE,
        todate=TODATE,
        reverse=False
    )

    cerebro.adddata(data)

    cerebro.addstrategy(TestStrategy)

    print('Starting portfolio value: %.2f' % cerebro.broker.getvalue())

    countdown("\nStarting Cerebro")
    cerebro.run()

    print('Final portfolio value: %.2f' % cerebro.broker.getvalue())
