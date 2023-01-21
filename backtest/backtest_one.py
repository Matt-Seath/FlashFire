import backtrader as bt
from datetime import date
from dateutil.relativedelta import relativedelta

from loggers.coloured_text import Colour
from core.models import StockHistory
from backtest.strategies.all import *
from backtest.pipelines.django_pls import DjangoDataFeed
from backtest.pipelines.yfinance_pls import get_dataframe


# STRATEGY = BuyTheDipStrategy
SQL_DATAFEED = True
STARTING_CASH = 10000

FROMDATE = [2022, 8, 13]
TODATE__ = [2023, 1, 13]
SPAN = relativedelta(date(*TODATE__), date(*FROMDATE))


def main(strategy, symbol):

    FILTERS = {
        "stock_id": symbol,
        "date__gte": date(*FROMDATE),
        "date__lt": date(*TODATE__)
    }

    valid_strategies = get_strategies()
    if strategy not in valid_strategies:
        raise Exception(
            f"Strategy key {strategy} is not associated with any valid strategy")

    cerebro = bt.Cerebro()

    cerebro.broker.set_cash(STARTING_CASH)

    if SQL_DATAFEED:
        queryset = StockHistory.objects.filter(**FILTERS)
        data = DjangoDataFeed(queryset)
    else:
        df = get_dataframe(**FILTERS)
        data = bt.feeds.PandasData(df)

    cerebro.adddata(data)
    cerebro.addstrategy(valid_strategies[strategy])
    cerebro.addsizer(bt.sizers.SizerFix, stake=1)

    print(
        f"\nStart: {date(*FROMDATE)}, End: {date(*TODATE__)}, Span: {SPAN.months} months")
    print(f'{Colour.BOLD}{date(*FROMDATE)} Starting portfolio value: {Colour.WARNING}{cerebro.broker.getvalue():.2f}{Colour.ENDC}\n')

    result = cerebro.run()

    net_change = (cerebro.broker.getvalue() - STARTING_CASH) / 100
    value_colour = Colour.OKGREEN if net_change >= 0 else Colour.FAIL
    print(
        f'\n{Colour.BOLD}{date(*FROMDATE)} Final portfolio value: {Colour.WARNING}{cerebro.broker.getvalue():.2f} {value_colour}({net_change:.2f}{Colour.ENDC}%)')

    print(f"\nBUY:  {result[0].buy_alerts}")
    print(f"SELL: {result[0].sell_alerts}")
    return result, cerebro, STARTING_CASH
