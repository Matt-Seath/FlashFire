from django.core.management.base import BaseCommand
from .progress_bar import bar
from datetime import datetime
from django.db import connection
import yfinance as yf
import pandas as pd
import numpy as np
import time
import csv


NOW = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")


def get_symbols():
    file_path = 'assets//asx.csv'
    symbols_list = []
    print("Generating list of Symbols..   ", end="")
    with open(file_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)

        for row in data:
            symbol = row["ASX code"].strip() + ".AX"
            symbols_list.append(symbol)

    print("Done.")
    return symbols_list


def clear_logs():
    with open("logs/dropped.log", "w") as f:
        f.truncate(0)
    with open("logs/query.log", "w") as f:
        f.truncate(0)
    with open("logs/added.log", "w") as f:
        f.truncate(0)
    with open("logs/errors.log", "w") as f:
        f.truncate(0)
    with open ("logs/skipped.log", "w") as f:
        f.truncate(0)


def write_to_logs(added=None, skipped=None, dropped=None):
    if added:
        for entry in added:
            with open ("logs/added.log", "a") as f:
                f.write(entry)
    if skipped:
        for entry in skipped:
            with open ("logs/skipped.log", "a") as f:
                f.write(entry)
    if dropped:
        for entry in dropped:
            with open ("logs/dropped.log", "a") as f:
                f.write(entry)


def get_symbols_df(symbols):
    df = pd.DataFrame()
    df_entry = pd.DataFrame()
    added_symbols = []
    skipped_symbols = []
    dropped_columns = []
    errors = 0
    # loops = 6
    loops = len(symbols)

    for t in range(loops):
        bar("Retrieving Stock Info", t + 1, loops, symbols[t])
        time.sleep(0.9)
        try:
            df_entry = (pd.DataFrame([yf.Ticker(symbols[t]).info]))
        except Exception as e:
            errors += 0
            with open("logs/errors.log", "a") as f: 
                f.write(f"{NOW}: {symbols[t]} Not Found \n")
        if len(df_entry.columns) < 130:
            # print(f"Skipping {symbols[t]}")
            skipped_symbols.append(symbols[t])
            continue

        df = pd.concat([df, df_entry], axis=0)


    df = df.replace(np.nan, None)
    df = df.reset_index(drop=True)
    df = df.rename(columns={"open": "openPrice", \
        "52WeekChange": "fiftyTwoWeekChange", "logo_url": "logoUrl"})

    with open("assets/columns.txt") as f:
        column_list = f.read()
        columns = list(df.columns.values)
        for column in columns:
            if column not in column_list:
                df.drop(column, axis=1, inplace=True, errors="ignore")
                dropped_columns.append(column + ", ")

    with connection.cursor() as cursor:
        # creating column list for insertion
        cols = "`,`".join([str(i) for i in df.columns.tolist()])
        
        for i,row in df.iterrows():
            sql = "REPLACE INTO `core_stockinfo` (`"+ cols +"`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            query = f"{sql}{tuple(row)}"
            try:
                cursor.execute(sql, tuple(row))
                added_symbols.append(row["symbol"] + ", ")
            except Exception as e:
                with open("logs/query.log", "a") as f:
                    f.write(query + '\n')
                with open("logs/errors.log", "a") as f:
                    f.write(f"{NOW}: Could not insert {row['symbol']}, {e} \n")
                errors += 1
            bar("Inserting into Database", i + 1, loops, row["symbol"])
    print("")
    print(f"Skipped Symbols: {str(skipped_symbols)}")
    print(f"Dropped Columns: {len(dropped_columns)}")
    write_to_logs(added_symbols, skipped_symbols, dropped_columns)
    return df, errors


class Command(BaseCommand):
    help = 'Populates the database with collections and products'

    def handle(self, *args, **options):
        clear_logs()

        symbols = get_symbols()
        df, errors = get_symbols_df(symbols)  

        df.to_csv("logs/raw_data.csv", index=False)
        print("")
        print(f"Task completed with {errors} error/s.")
        return 0
