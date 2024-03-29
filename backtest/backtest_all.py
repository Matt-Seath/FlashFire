from tqdm import tqdm
import contextlib
import io
from flashfire.settings import (
    BTA_APPLY_FILTERS,
    BTA_FILTERS,
    BTA_ITERATION_LIMIT,
    BTA_TEST_ALL_STOCKS
)
from core.models import StockInfo
from backtest import reports
from backtest import backtest_one
from backtest.pipelines import mysql_pls
from loggers.coloured_text import Colour, int_colour
from backtest.strategies.all import validate_strategy


def main(strategy):

    validate_strategy(strategy)
    filters = BTA_FILTERS if BTA_APPLY_FILTERS else None
    stocks = mysql_pls.get_col_list_from_db("symbol", filters)
    iterations = len(stocks) if BTA_TEST_ALL_STOCKS else BTA_ITERATION_LIMIT
    results = {}
    change_sum = 0
    tested = 0
    skipped = 0

    for i in tqdm(range(iterations), desc=f"Testing {strategy.upper()} Strategy: "):
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                data, cerebro, cash = backtest_one.main(strategy, stocks[i])
                tested += 1
                print(tested)
        except Exception as e:
            skipped += 1
            print(e)
            continue

        net_change = (cerebro.broker.getvalue() - cash) / 100
        change_sum += net_change
        stock_info = StockInfo.objects.filter(symbol=stocks[i])[0]

        results[stocks[i]] = {
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

    for result in results.items():
        print(f"{'Stock:':<8}{result[1]['name']} ({result[1]['symbol']})")
        print(f"{'Price:':<8}{result[1]['avg_price']}")
        print(
            f"{'Profit:':<8}{int_colour(result[1]['change'])}{result[1]['change']:.2f}%{Colour.ENDC}\n")

    avg_change_value = change_sum / tested
    print(
        f"\nAverage Profit: {int_colour(avg_change_value)}{avg_change_value:.2f}%\n{Colour.ENDC}")
    print(f"Stocks Tested: {tested}")
    print(f"Stocks Skipped: {skipped}")

    return results
