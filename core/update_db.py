from loggers.temp_logger import TempLogger
from pipelines.yf_etls import YFStockETL
from stockdata import assets


GET_ALL_ASX_STOCKS = False
SLEEPER = 0.7  # Higher value slows api request frequency to avoid throttling.
ITERATIONS = 3  # How many stocks to retrieve whenever GET_ALL_ASX_STOCKS = False

PATH_TO_ASX_LIST = "assets/stockdata/asx_list.csv"
PATH_TO_COLS_RENAME_CSV = "assets/stockdata/cols_rename.csv"
PATH_TO_COLS_WHITELIST = "assets/stockdata/cols_whitelist.csv"

ASX_LIST_COLUMN = "ASX code"
ASX_LIST_EXTENSION = ".AX"

LOGS = ["errors", "added", "dropped", "skipped", "queries"]
LOGGER_BASE_DIR = "logs/asx/"


def main():
    logger = TempLogger(*LOGS)
    logger.base_dir(LOGGER_BASE_DIR)
    logger.clear_logs(all=True)

    symbols = assets.get_list_of_symbols(
        PATH_TO_ASX_LIST, ASX_LIST_COLUMN, ASX_LIST_EXTENSION)
    cols_dict = assets.get_cols_rename_dict(
        PATH_TO_COLS_RENAME_CSV)
    cols_whitelist = assets.get_cols_whitelist(PATH_TO_COLS_WHITELIST)

    etl = YFStockETL(symbols, all=GET_ALL_ASX_STOCKS,
                     iterations=ITERATIONS, sleeper=SLEEPER)

    etl.set_whitelist(cols_whitelist)
    etl.rename_cols(cols_dict)
    etl.print_iter_range()

    etl.extract()
    etl.transform()
    etl.load()

    for log in LOGS:
        log_entry = getattr(etl, log)
        logger.entry(log, log_entry)
    logger.write_to_files(all=True)

    print(f"\nETL process finished with {len(etl.errors)} error/s")
    etl.print_added_count()
    etl.print_skipped_count()
    etl.print_dropped_count()

    return 0
