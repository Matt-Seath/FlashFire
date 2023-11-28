import backtrader as bt
from dateutil.relativedelta import relativedelta
from datetime import date
from flashfire.settings import ( 
    BTO_FROMDATE, 
    BTO_SQL_DATAFEED, 
    BTO_STARTING_CASH, 
    BTO_TODATE__, 
)
from loggers.coloured_text import Colour
from core.models import StockHistory
from backtest.strategies.all import *
from backtest.pipelines.django_pls import DjangoDataFeed
from backtest.pipelines.yfinance_pls import get_dataframe


SPAN = relativedelta(date(*BTO_TODATE__), date(*BTO_FROMDATE))

def main(strategy, symbol):

    FILTERS = {
        "stock_id": symbol,
        "date__gte": date(*BTO_FROMDATE),
        "date__lt": date(*BTO_TODATE__)
    }

    cerebro = bt.Cerebro()

    cerebro.broker.set_cash(BTO_STARTING_CASH)

    if BTO_SQL_DATAFEED:
        queryset = StockHistory.objects.filter(**FILTERS)
        data = DjangoDataFeed(queryset)
    else:
        df = get_dataframe(**FILTERS)
        data = bt.feeds.PandasData(df)

    cerebro.adddata(data)
    cerebro.addstrategy(validate_strategy(strategy))
    cerebro.addsizer(bt.sizers.SizerFix, stake=1)

    print(
        f"\nStart: {date(*BTO_TODATE__)}, Span: {SPAN.months} months")
    print(f'{Colour.BOLD}{date(*BTO_FROMDATE)} Starting portfolio value: {Colour.WARNING}{cerebro.broker.getvalue():.2f}{Colour.ENDC}\n')

    result = cerebro.run()

    net_change = (cerebro.broker.getvalue() - BTO_STARTING_CASH) / 100
    value_colour = Colour.OKGREEN if net_change >= 0 else Colour.FAIL
    print(
        f'\n{Colour.BOLD}{date(*BTO_FROMDATE)} Final portfolio value: {Colour.WARNING}{cerebro.broker.getvalue():.2f} {value_colour}({net_change:.2f}%){Colour.ENDC}')

    print(f"\nBUY:  {result[0].buy_alerts}")
    print(f"SELL: {result[0].sell_alerts}")

    return result, cerebro, BTO_STARTING_CASH
