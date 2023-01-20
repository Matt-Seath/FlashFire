from backtest import backtest_one
from backtest.pipelines import mysql_pls
import time
import contextlib
import io

from loggers.coloured_text import Colour
from core.models import StockInfo


def main():
    stocks = mysql_pls.get_col_list_from_db("symbol")

    for stock in stocks:
        with contextlib.redirect_stdout(io.StringIO()):
            result, cerebro, cash = backtest_one.main(stock)
            net_change = (cerebro.broker.getvalue() - cash) / 100
            stock_info = StockInfo.objects.filter(symbol=stock)[0]
        print(f"\nStock: {stock_info.long_name} ({stock})")
        print(f"Net Change: {net_change:.2f}")
        