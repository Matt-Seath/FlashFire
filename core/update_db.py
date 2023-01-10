from django.core.management.base import BaseCommand

from loggers.temp_logger import TempLogger
from pipelines.dataframe import StockDataFrame
from stockdata.assets import get_symbols


GET_ALL_ASX_STOCKS = True
SLEEPER = 0.7  # Higher value slows api request frequency to avoid throttling.
ITERATIONS = 3  # How many stocks to retrieve if GET_ALL_ASX_STOCKS is false


def main(*args, **options):
    logger = TempLogger("errors", "added",
                        "dropped", "skipped")
    logger.base_dir("logs/asx/")

    logger.write_to_files(all=True)
    # symbols = get_symbols()
    # df, errors, skipped_symbols, dropped_columns = get_dataframe(symbols)
    # df, errors, added_symbols, skipped_symbols = write_df_to_database(
    #     df, errors, skipped_symbols)
    # write_to_logs(added_symbols, skipped_symbols, dropped_columns)
    # print_stats(errors, skipped_symbols, dropped_columns)

    return 0
