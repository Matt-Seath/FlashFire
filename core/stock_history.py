from pipelines.yf_etls import StockHistoryETL
from loggers.temp_logger import TempLogger
from stockdata import assets


GET_ALL_ASX_STOCKS = False  # Fully update the ASX stock table
SLEEPER = 0.7  # Higher value slows api request frequency to avoid throttling.
ITERATIONS = 6  # How many stocks to retrieve whenever GET_ALL_ASX_STOCKS = False

# Paths to static assets
# List that contains all tickers on the ASX exchange
PATH_TO_ASX_LIST = "assets/stockdata/asx_list.csv"

# Variables to format csv to list for yfinance API
ASX_LIST_COLUMN = "ASX code"  # Only append values from this column to list
ASX_LIST_EXTENSION = ".AX"  # Add this extension to end of each value for asx stocks

# Logger Configuration
LOGS = ["errors", "added", "dropped",
        "skipped", "queries"]  # Logs to be created
LOGGER_BASE_DIR = "logs/asx/"  # Logs to be written into this directory


def main():
    symbols = assets.get_list_of_symbols(   # Extract symbols from csv file to list
        PATH_TO_ASX_LIST, ASX_LIST_COLUMN, ASX_LIST_EXTENSION)

    etl = StockHistoryETL(symbols, all=GET_ALL_ASX_STOCKS,  # Initialize ETL
                          iterations=ITERATIONS, sleeper=SLEEPER)
    etl.extract()

    etl.transform()

    etl.load()

    print(etl.df)

    # Finally print error count and stats to the terminal before finishing process.
    print(f"\nETL process finished with {len(etl.errors)} error/s")
    etl.print_added_count()  # Print number of successful insertions to db
    etl.print_skipped_count()  # Print number of skipped stocks
    etl.print_dropped_count()  # Print number of columns dropped from df

    return 0
