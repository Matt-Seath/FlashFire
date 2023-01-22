from tqdm import tqdm
import contextlib
import io

from backtest import backtest_one
from backtest.pipelines import mysql_pls
from loggers.coloured_text import Colour, int_colour
from core.models import StockInfo


TEST_ALL_STOCKS = True
CUSTOM_ITERATIONS = 600

FILTERS = {
    "current_price__gt": 5,
    "sector": "Consumer Cyclical"
}


def main(strategy):
    stocks = mysql_pls.get_col_list_from_db("symbol", FILTERS)
    iterations = len(stocks) if TEST_ALL_STOCKS else CUSTOM_ITERATIONS
    results = {}
    change_sum = 0
    tested = 0
    skipped = 0

    for i in tqdm(range(iterations), desc=f"Testing {strategy.upper()} Strategy: "):
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                data, cerebro, cash = backtest_one.main(strategy, stocks[i])
                tested += 1
        except Exception as e:
            skipped += 1
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
