from tqdm import tqdm
import contextlib
import time
import io

from backtest import backtest_one
from backtest.pipelines import mysql_pls
from loggers.coloured_text import Colour
from core.models import StockInfo


TEST_ALL_STOCKS = False
CUSTOM_ITERATIONS = 600


def main():
    stocks = mysql_pls.get_col_list_from_db("symbol")
    iterations = len(stocks) if TEST_ALL_STOCKS else CUSTOM_ITERATIONS
    result = {}
    change_sum = 0
    tested = 0
    skipped = 0

    for i in tqdm(range(iterations), desc=f"Testing Strategy: "):
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                data, cerebro, cash = backtest_one.main(stocks[i])
                tested += 1
        except Exception as e:
            skipped += 1
            continue

        net_change = (cerebro.broker.getvalue() - cash) / 100
        change_sum += net_change
        stock_info = StockInfo.objects.filter(symbol=stocks[i])[0]

        result[stocks[i]] = {
            "symbol": stocks[i].replace(".AX", ""),
            "change": net_change,
            "name": stock_info.long_name,
            "buy_alerts": data[0].buy_alerts,
            "sell_alerts": data[0].sell_alerts,
            "total_buys": data[0].total_buys,
            "total_sells": data[0].total_sells,
            "price": stock_info.current_price,
            "avg_volume": stock_info.average_volume,
            "avg_price": stock_info.fifty_day_average
        }
        # value_colour = Colour.OKGREEN if net_change >= 0 else Colour.FAIL
        # print(
        #     f"\n{'Stock:':<10}{stock_info.long_name} {Colour.WARNING}{stocks[i]}{Colour.ENDC}")
        # print(f"{'Change:':<10}{value_colour}{net_change:.2f}%{Colour.ENDC}")

    average_change = change_sum / tested
    print(f"\nAverage Change: {average_change:.2f}%\n")
    print(f"Stocks Tested: {tested}")
    print(f"Stocks Skipped: {skipped}")
