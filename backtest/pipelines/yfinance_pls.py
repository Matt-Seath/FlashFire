from django.db import connection
from django.db.models import Max
from datetime import datetime, timedelta
from tqdm import tqdm
import yfinance as yf
import contextlib
import pandas as pd
import numpy as np
import time
import io

from core.models import StockHistory, StockInfo


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
        for i in tqdm(range(self.iterations), desc="Scraping stock data from Yahoo Finance"):
            time.sleep(self.sleeper)
            self.df_latest_entry = (pd.DataFrame(
                [yf.Ticker(self.symbols[i]).info]))
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

    def load(self):
        generator = self.df.iterrows()
        for _ in tqdm(range(len(self.df.index)), desc="Loading stock info into database"):
            _, row = next(generator)
            row_dict = row.to_dict()
            entry = StockInfo(**row_dict)
            try:
                entry.save()
                self.added.append(str(row_dict))
            except Exception as e:
                self.skipped.append(str(row_dict))
                self.errors.append(
                    f"{self.timestamp()}: Could not insert {row['symbol']}, {e} Value: {str(row_dict)}")

        return


class StockHistoryETL(ETL):

    def __init__(self, symbols_list, period=None, interval=None, start=None,
                 end=None, sleeper=0, actions=True, all=True, iterations=1, update=True):
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
            self.update = update
        else:
            raise Exception("YFStockETL could not be initialized")

    def print_range(self):
        print(
            f"Starting date: {self.start}, Ending date: {self.end}, period: {self.period}")

    def get_latest_date(self, symbol):
        queryset = StockHistory.objects.filter(stock_id=symbol)
        date_max = queryset.aggregate(Max("datetime"))["datetime__max"]
        self.start = date_max + timedelta(days=1)
        self.end = datetime.today()

    def extract(self):
        print("Retrieving historical data")
        self.print_range()
        self.print_iter_range()

        for i in range(self.iterations):
            time.sleep(self.sleeper)
            try:
                if self.update:
                    self.get_latest_date(self.symbols[i])
                    print(self.start)
                    print(self.end)
                with contextlib.redirect_stdout(io.StringIO()):
                    self.df_latest_entry = yf.Ticker(self.symbols[i]).history(
                        start=self.start, end=self.end, period=self.period, actions=self.actions)
                print(len(self.df_latest_entry.index))
                print(self.df_latest_entry)
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
        self.df["datetime"] = self.df.index
        self.df = self.df.replace(np.nan, None)

        columns = list(self.df.columns.values)
        for column in columns:
            if column not in self.df_cols:
                self.df.drop(column, axis=1, inplace=True, errors="ignore")
                self.dropped.append(column)

        return

    def load(self):
        generator = self.df.iterrows()
        for _ in tqdm(range(len(self.df.index)), desc="Loading stock history into database"):
            _, row = next(generator)
            row_dict = row.to_dict()
            entry = StockHistory(**row_dict)
            try:
                entry.save()
                self.added.append(str(row_dict))
            except Exception as e:
                self.skipped.append(str(row_dict))
                self.errors.append(
                    f"{self.timestamp()}: Could not insert {row['stock_id']}, {e} Value: {str(row_dict)}")

        return
