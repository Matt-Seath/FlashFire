from django.core.management.base import BaseCommand
from loggers.temp_logger import TempLogger
from stockdata.assets import get_symbols
from datetime import datetime
from django.db import connection
from tqdm import tqdm
import yfinance as yf
import contextlib
import pandas as pd
import numpy as np
import time
import io


GET_ALL_ASX_STOCKS = True
SLEEPER = 0.7 # Higher value slows api request frequency to avoid throttling.
ITERATIONS = 3 # How many stocks to retrieve if GET_ALL_ASX_STOCKS is false
NOW = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")






class Command(BaseCommand):
    help = 'Populates the database with collections and products'

    def handle(self, *args, **options):
        clear_logs()

        symbols = get_symbols()
        df, errors, skipped_symbols, dropped_columns = get_dataframe(symbols)
        df, errors, added_symbols, skipped_symbols = write_df_to_database(df, errors, skipped_symbols)
        write_to_logs(added_symbols, skipped_symbols, dropped_columns)
        print_stats(errors, skipped_symbols, dropped_columns)

        return 0
