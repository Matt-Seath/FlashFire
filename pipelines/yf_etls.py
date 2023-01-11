from django.db import connection
from datetime import datetime
from tqdm import tqdm
import yfinance as yf
import contextlib
import pandas as pd
import numpy as np
import time
import io


class YFStockETL():

    iterations = None
    symbols = None
    sleeper = 0
    df_cols = None
    df_cols_renamed = None

    def __init__(self, symbols_list, sleeper=0, all=True, iterations=1):
        if self.symbols == None and self.df_cols == None and self.df_cols_renamed == None and symbols_list:
            self.iterations = len(symbols_list) if all else iterations
            self.df_cols = []
            self.df_cols_renamed = {}
            self.symbols = symbols_list
            self.sleeper = sleeper

    def print(self):
        print(f"Total symbols to process: {self.iterations}")

    def timestamp(self):
        return datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

    def set_whitelist(self, whitelist):
        self.df_cols = whitelist

    def rename_cols(self, col_dict):
        self.df_cols = col_dict

    def build_df(self, symbols):
        df = pd.DataFrame()
        df_entry = pd.DataFrame()
        skipped_symbols = []
        dropped_columns = []
        errors = 0
        if not self.iterations:
            loops = len(symbols)

        for t in tqdm(range(loops), desc="Retrieving stock data from yfinance"):
            time.sleep(self.sleeper)
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    df_entry = (pd.DataFrame([yf.Ticker(symbols[t]).info]))
            except Exception as e:
                errors += 0
                with open("logs/errors.log", "a") as f:
                    f.write(
                        f"{self.timestamp()}: {symbols[t]} Not Found, {e} \n")
            if len(df_entry.columns) < 130:
                # print(f"Skipping {symbols[t]}")
                skipped_symbols.append(symbols[t])
                continue

            df = pd.concat([df, df_entry], axis=0)

        df = df.reset_index(drop=True).replace(np.nan, None)
        df = df.rename(colums=self.df_cols_renamed)

        with open("assets/columns.txt") as f:
            column_list = f.read()
            columns = list(df.columns.values)
            for column in columns:
                if column not in column_list:
                    df.drop(column, axis=1, inplace=True, errors="ignore")
                    dropped_columns.append(column + ", ")

        return df, errors, skipped_symbols, dropped_columns

    def write_df_to_db(self, df, errors, skipped_symbols):
        added_symbols = []
        cols = "`,`".join([str(i) for i in df.columns.tolist()])

        with connection.cursor() as cursor:
            for i, row in tqdm(df.iterrows(), desc="Inserting stockinfo into database"):
                sql_operation = "REPLACE INTO `core_stockinfo` (`" + \
                    cols + "`)"
                sql_values = "VALUES (" + "%s,"*(len(row)-1) + "%s)"
                sql = sql_operation + sql_values
                query = f"{sql_operation} VALUES {tuple(row)}; \n"
                try:
                    cursor.execute(sql, tuple(row))
                    added_symbols.append(row["symbol"] + ", ")
                except Exception as e:
                    skipped_symbols.append(row["symbol"])
                    with open("logs/query.log", "a") as f:
                        f.write(query)
                    with open("logs/errors.log", "a") as f:
                        f.write(
                            f"{self.timestamp()}: Could not insert {row['symbol']}, {e} \n")
                    errors += 1

        return df, errors, added_symbols, skipped_symbols
