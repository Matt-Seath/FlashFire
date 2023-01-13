from django.db import connection
from datetime import datetime
from tqdm import tqdm
import yfinance as yf
import contextlib
import pandas as pd
import numpy as np
import time
import io

from core.models import StockHistory


class ETL():

    symbols = None
    df = None
    df_latest_entry = None
    df_cols = None
    df_cols_renamed = None
    skipped = None
    added = None
    dropped = None
    errors = None
    queries = None

    def __init__(self, symbols_list, sleeper=0, all=True, iterations=1):
        if self.symbols == None and self.df == None and self.df_cols == None and \
                self.df_latest_entry == None and self.df_cols_renamed == None and \
            self.skipped == None and self.added == None and self.queries == None and \
                self.dropped == None and self.errors == None and symbols_list:

            self.iterations = len(symbols_list) if all else iterations
            self.symbols = symbols_list
            self.df = pd.DataFrame()
            self.df_latest_entry = pd.DataFrame()
            self.df_cols = []
            self.df_cols_renamed = {}
            self.sleeper = sleeper
            self.skipped = []
            self.dropped = []
            self.added = []
            self.errors = []
            self.queries = []
        else:
            raise Exception("YFStockETL could not be initialized")

    def print_iter_range(self):
        print(f"Total symbols to process: {self.iterations}")

    def print_error_count(self):
        print(f"Total errors: {len(self.errors)}")

    def print_skipped_count(self):
        print(f"Symbols skipped: {len(self.skipped)}")

    def print_added_count(self):
        print(f"Stocks added: {len(self.added)}")

    def print_dropped_count(self):
        print(f"Columns dropped: {len(self.dropped)}")

    def timestamp(self):
        return datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

    def set_whitelist(self, whitelist):
        self.df_cols = whitelist

    def rename_cols(self, col_dict):
        self.df_cols_renamed = col_dict

    def extract(self):
        print("User Defined Function")
        return

    def transform(self):
        self.df = self.df.rename(columns=self.df_cols_renamed)
        self.df = self.df.reset_index(drop=True).replace(np.nan, None)

        columns = list(self.df.columns.values)
        for column in columns:
            if column not in self.df_cols:
                self.df.drop(column, axis=1, inplace=True, errors="ignore")
                self.dropped.append(column)

        return

    def load(self):
        added_symbols = []
        cols = "`,`".join([str(i) for i in self.df.columns.tolist()])

        with connection.cursor() as cursor:
            for i, row in tqdm(self.df.iterrows(), desc="Inserting stockinfo into database"):
                sql_operation = "REPLACE INTO `core_stockinfo` (`" + \
                    cols + "`)"
                sql_values = "VALUES (" + "%s,"*(len(row)-1) + "%s)"
                sql = sql_operation + sql_values
                query = f"{sql_operation} VALUES {tuple(row)}; \n"
                try:
                    cursor.execute(sql, tuple(row))
                    added_symbols.append(row["symbol"] + ", ")
                    self.added.append(row["symbol"])
                except Exception as e:
                    self.queries.append(query)
                    self.skipped.append(row["symbol"])
                    self.errors.append(
                        f"{self.timestamp()}: Could not insert {row['symbol']}, {e}")

        return


class StockInfoETL(ETL):

    def extract(self):
        self.print_iter_range()

        for i in tqdm(range(self.iterations), desc="Retrieving stock info from yfinance"):
            time.sleep(self.sleeper)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    self.df_latest_entry = (pd.DataFrame(
                        [yf.Ticker(self.symbols[i]).info]))
            except Exception as e:
                self.skipped.append(self.symbols[i])
                self.errors.append(
                    f"{self.timestamp()}: {self.symbols[i]} Error, {e} \n")
                continue
            if len(self.df_latest_entry.columns) < 130:
                self.skipped.append(self.symbols[i])
                continue

            self.df = pd.concat([self.df, self.df_latest_entry], axis=0)

        return


class StockHistoryETL(ETL):

    def __init__(self, symbols_list, period=None, interval=None, start=None,
                 end=None, sleeper=0, actions=True, all=True, iterations=1):
        if self.symbols == None and self.df == None and self.df_cols == None and \
                self.df_latest_entry == None and self.df_cols_renamed == None and \
            self.skipped == None and self.added == None and self.queries == None and \
                self.dropped == None and self.errors == None and symbols_list:

            self.iterations = len(symbols_list) if all else iterations
            self.symbols = symbols_list
            self.df = pd.DataFrame()
            self.df_latest_entry = pd.DataFrame()
            self.df_cols = []
            self.df_cols_renamed = {}
            self.sleeper = sleeper
            self.skipped = []
            self.dropped = []
            self.added = []
            self.errors = []
            self.queries = []
            self.start = start
            self.end = end
            self.period = period
            self.interval = interval
            self.actions = actions
        else:
            raise Exception("YFStockETL could not be initialized")

    def print_range(self):
        print(
            f"Starting date: {self.start}, Ending date: {self.end}, period: {self.period}")

    def extract(self):
        print("Retrieving historical data")
        self.print_range()
        self.print_iter_range()

        for i in tqdm(range(self.iterations), desc="Retrieving stock history from yfinance"):
            time.sleep(self.sleeper)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    self.df_latest_entry = yf.Ticker(self.symbols[i]).history(
                        start=self.start, end=self.end, period=self.period, actions=self.actions)
            except Exception as e:
                self.skipped.append(self.symbols[i])
                self.errors.append(
                    f"{self.timestamp()}: {self.symbols[i]} Error, {e} \n")
                continue
            if len(self.df_latest_entry.columns) < 4:
                self.skipped.append(self.symbols[i])
                continue

            self.df_latest_entry["stock_id"] = self.symbols[i]
            self.df = pd.concat([self.df, self.df_latest_entry], axis=0)
        return

    def transform(self):
        self.df = self.df.rename(columns=self.df_cols_renamed)
        self.df["date"] = self.df.index
        self.df = self.df.replace(np.nan, None)

        columns = list(self.df.columns.values)
        for column in columns:
            if column not in self.df_cols:
                self.df.drop(column, axis=1, inplace=True, errors="ignore")
                self.dropped.append(column)

        return

    def load(self):

        for i, row in tqdm(self.df.iterrows(), desc="Writing stock history to the database"):
            entry = StockHistory(
                stock_id=row["stock_id"], open=row["open"], close=row["close"],
                high=row["high"], low=row["low"], volume=row["volume"], date=row["date"])
            try:
                entry.save()
                self.added.append(row["stock_id"])
            except Exception as e:
                self.skipped.append(row["stock_id"])
                self.errors.append(
                    f"{self.timestamp()}: Could not insert {row['stock_id']}, {e}")

        return
