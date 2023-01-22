from django.db import connection
from django.db.models import Max, Min
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

    def __init__(self, *args, **kwargs):

        if kwargs["symbols_list"]:
            self.df = pd.DataFrame()
            self.df_latest_entry = pd.DataFrame()
            self.df_cols = []
            self.df_cols_renamed = {}
            self.skipped = []
            self.dropped = []
            self.added = []
            self.errors = []
            self.queries = []
            self.sleeper = kwargs["sleeper"]
            self.iterations = len(
                kwargs["symbols_list"]) if kwargs["all"] else kwargs["iterations"]
            self.symbols = kwargs["symbols_list"]
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
        for i in tqdm(range(self.iterations), desc="Scraping stock data"):
            time.sleep(self.sleeper)
            self.df_latest_entry = (pd.DataFrame(
                [yf.Ticker(self.symbols[i]).info]))
            with contextlib.redirect_stdout(io.StringIO()):
                try:
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

    def __init__(self, *args, **kwargs):

        self.start = kwargs["start"]
        self.end = kwargs["end"]
        self.period = kwargs["period"]
        self.interval = kwargs["interval"]
        self.actions = kwargs["actions"]
        self.update = kwargs["update"]

        super(StockHistoryETL, self).__init__(args, **kwargs)

    def print_range(self):
        print(
            f"Starting date: {self.start}, Ending date: {self.end}, period: {self.period}")

    def get_latest_date(self, symbol):
        queryset = StockHistory.objects.filter(stock_id=symbol)
        self.start = queryset.aggregate(
            Max("date"))["date__max"] + timedelta(days=1)

    def drop_duplicates(self, symbol):
        queryset = StockHistory.objects.filter(stock_id=symbol)
        max_date = queryset.aggregate(
            Max("date"))["date__max"]
        min_date = queryset.aggregate(
            Min("date"))["date__min"]

        self.df_latest_entry = self.df_latest_entry.loc[(
            self.df_latest_entry['date'] > max_date) | (self.df_latest_entry['date'] < min_date)]

    def extract(self):
        print("Retrieving historical data")
        self.print_range()
        self.print_iter_range()

        for i in tqdm(range(self.iterations), desc="Scraping history data"):
            time.sleep(self.sleeper)
            try:
                if self.update:
                    self.get_latest_date(self.symbols[i])
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

            try:
                if (self.df_latest_entry.index.date < self.start).any():
                    self.skipped.append(str(self.df_latest_entry.to_dict()))
                    continue
            except Exception as e:
                self.skipped.append(str(self.df_latest_entry.to_dict()))
                self.errors.append(
                    f"{self.timestamp()}: {self.symbols[i]} Error, {e} \n")
                continue

            self.df_latest_entry["date"] = self.df_latest_entry.index
            self.df_latest_entry['date'] = pd.to_datetime(
                self.df_latest_entry['date']).dt.date
            self.drop_duplicates(self.symbols[i])
            self.df_latest_entry["stock_id"] = self.symbols[i]
            self.df = pd.concat([self.df, self.df_latest_entry], axis=0)

        return

    def transform(self):
        self.df = self.df.rename(columns=self.df_cols_renamed)
        self.df = self.df.replace(np.nan, None)

        columns = list(self.df.columns.values)
        for column in columns:
            if column not in self.df_cols:
                self.df.drop(column, axis=1, inplace=True, errors="ignore")
                self.dropped.append(column)

        return

    def load(self):
        generator = self.df.iterrows()
        for _ in tqdm(range(len(self.df.index)), desc="Loading history data into database"):
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


def get_dataframe(*args, **kwargs):
    data = yf.Ticker(kwargs["stock_id"]).history(
        start=kwargs["date__gte"], end=kwargs["date__lt"], period="1d")
    print(data)
