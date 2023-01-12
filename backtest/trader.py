import backtrader
import datetime


def main():
    cerebro = backtrader.cerebro()

    cerebro.broker.set_cash(100000)

    print('Starting portfolio value: %.2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final portfolio value: %.2f' % cerebro.broker.getvalue())
