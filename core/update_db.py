from loggers.temp_logger import TempLogger
from pipelines.yf_etls import YFStockETL
from stockdata import assets


GET_ALL_ASX_STOCKS = True
SLEEPER = 0.7  # Higher value slows api request frequency to avoid throttling.
ITERATIONS = 3  # How many stocks to retrieve whenever GET_ALL_ASX_STOCKS = False


def main(*args, **options):
    logger = TempLogger("errors", "added",
                        "dropped", "skipped")
    logger.base_dir("logs/asx/")

    symbols = assets.get_list_of_symbols(
        "core/assets/stockdata/asx_list.csv", "ASX code", ".AX")
    cols_dict = assets.get_cols_rename_dict(
        "core/assets/stockdata/cols_rename.csv")

    report = YFStockETL(symbols)
    print(cols_dict)

    logger.write_to_files(all=True)
    # df, errors, skipped_symbols, dropped_columns = get_dataframe(symbols)
    # df, errors, added_symbols, skipped_symbols = write_df_to_database(
    #     df, errors, skipped_symbols)
    # write_to_logs(added_symbols, skipped_symbols, dropped_columns)
    # print_stats(errors, skipped_symbols, dropped_columns)

    return 0
