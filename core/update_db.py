from loggers.temp_logger import TempLogger
from pipelines.yf_etls import YFStockETL
from stockdata import assets


GET_ALL_ASX_STOCKS = True
SLEEPER = 0.7  # Higher value slows api request frequency to avoid throttling.
ITERATIONS = 3  # How many stocks to retrieve whenever GET_ALL_ASX_STOCKS = False

PATH_TO_ASX_LIST = "core/assets/stockdata/asx_list.csv"
PATH_TO_COLS_RENAME_CSV = "core/assets/stockdata/cols_rename.csv"
PATH_TO_COLS_WHITELIST = "core/assets/stockdata/cols_whitelist.csv"

ASX_LIST_COLUMN = "ASX code"
ASX_LIST_EXTENSION = ".AX"

LOGS = ["errors", "added", "dropped", "skipped"]
LOGGER_BASE_DIR = "logs/asx/"


def main(*args, **options):
    logger = TempLogger(*LOGS)
    logger.base_dir(LOGGER_BASE_DIR)

    symbols = assets.get_list_of_symbols(
        PATH_TO_ASX_LIST, ASX_LIST_COLUMN, ASX_LIST_EXTENSION)
    cols_dict = assets.get_cols_rename_dict(
        PATH_TO_COLS_RENAME_CSV)
    etl = YFStockETL(symbols)

    logs = etl.extract()
    logger.entry(logs)

    logs = etl.transform()
    logger.entry(logs)

    logs = etl.load()
    logger.entry(logs)

    print(logger)
    logger.write_to_files(all=True)
    # df, errors, skipped_symbols, dropped_columns = get_dataframe(symbols)
    # df, errors, added_symbols, skipped_symbols = write_df_to_database(
    #     df, errors, skipped_symbols)
    # write_to_logs(added_symbols, skipped_symbols, dropped_columns)
    # print_stats(errors, skipped_symbols, dropped_columns)

    return 0
