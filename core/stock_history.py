from loggers.temp_logger import TempLogger
from backtest.pipelines import assets_pls, yfinance_pls, mysql_pls

from datetime import date

"""

This script behaves as an ETL pipeline that retrieves stock history for 
Australian Securities Exchange (ASX) listed companies from the yfinance API.
The script first makes a request to the API to retrieve the current stock 
history for each ASX listed company. The returned data is then cleaned 
by the script, including handling any missing or invalid values, and 
formatting the data into a suitable structure for insertion into a MySQL 
database.

"""

GET_ALL_ASX_STOCKS = True  # Fully update the ASX stock table
UPDATE_DB = False
SLEEPER = 1.5  # Higher value slows api request frequency to avoid throttling.
ITERATIONS = 8  # How many stocks to retrieve whenever GET_ALL_ASX_STOCKS = False

START_DATE = date(2021, 1, 1)
PERIOD = "1d"
INTERVAL = None
ACTIONS = False


# Paths to static assets
# List of columns to be loaded into db
PATH_TO_COLS_WHITELIST = "assets/stockhistory/cols_whitelist.csv"
# Key-Value pairs of column names, camel-case for yfinance, then to snake-case when loaded to db
PATH_TO_COLS_RENAME_CSV = "assets/stockhistory/cols_rename.csv"

DB_COLUMN = "symbol"

# Logger Configuration
LOGS = ["errors", "added", "skipped", "dropped"]  # Logs to be created
# Logs to be written into this directory
LOGGER_BASE_DIR = "logs/stockhistory/"


# Microservice architecture was adapted for future projects.
# Refer to each app for details on each component

def main():
    logger = TempLogger(*LOGS)  # Initialize Logger
    logger.base_dir(LOGGER_BASE_DIR)  # Set base directory
    logger.clear_logs(all=True)  # Clear logs if they already exist

    symbols = mysql_pls.get_col_list_from_db(
        DB_COLUMN, None, all=GET_ALL_ASX_STOCKS, limit=ITERATIONS)
    cols_dict = assets_pls.get_cols_rename_dict(  # Get columns from csv file to dict
        PATH_TO_COLS_RENAME_CSV)
    cols_whitelist = assets_pls.get_cols_whitelist(
        PATH_TO_COLS_WHITELIST)  # Get column names for db

    params = {
        "symbols_list": symbols,
        "all": GET_ALL_ASX_STOCKS,
        "start": START_DATE,
        "end": None,
        "actions": ACTIONS,
        "period": PERIOD,
        "iterations": ITERATIONS,
        "sleeper": SLEEPER,
        "interval": INTERVAL,
        "update": UPDATE_DB
    }

    # ETL Pipeline
    etl = yfinance_pls.StockHistoryETL(**params)

    etl.set_whitelist(cols_whitelist)  # ETL will only load these columns
    # ETL will change column names before loading into db
    etl.rename_cols(cols_dict)

    # ETL iterates over stock symbols, sending a http request to yfinance endpoint for each symbol.
    # If the stock doesn't exist of if the data is corrupt, that stock is skipped and is logged.
    # Validated response data for each iteration is then appended into a single pandas dataframe
    etl.extract()

    # ulting dataframe is then stripped of Nan values, converting them to None values;
    # Column names are changed from camel-case to snake-case to conform with sql schema;
    # Finally, each column is checked against the columns in the whitelist, any column name that
    # doesn't exist in the whitelist is dropped from the dataframe.
    etl.transform()

    # Each row of the cleaned dataframe (each row contains the information of a single stock)
    # is iterated over and inserted into the database. If that stock already exists in the
    # database, it is replaced instead. Any errors are logged and the query data is stored.
    etl.load()

    # Create the logs
    for log in LOGS:  # Iterate over each log and write to the file
        log_entry = getattr(etl, log)  # Get the logged data from ETL
        # Add the data to the respective log object
        logger.entry(log, log_entry)
    # Write log data to .log files in base log directory.
    logger.write_to_files(all=True)

    # Finally print error count and stats to the terminal before finishing process.
    print(f"\nETL process finished with {len(etl.errors)} error/s")
    etl.print_added_count()  # Print number of successful insertions to db
    etl.print_skipped_count()  # Print number of skipped stocks
    etl.print_dropped_count()  # Print number of columns dropped from df

    return 0
