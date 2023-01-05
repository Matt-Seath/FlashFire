from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from django.db import connection
from .progress_bar import bar
import yfinance as yf
import pandas as pd
import numpy as np
import csv
import os




def get_symbols(file_path):
    symbols_list = []
    # print("Generating list of Symbols..   ", end="")
    with open(file_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)

        for row in data:
            symbol = row["ASX code"] + ".AX"
            symbols_list.append(symbol)

    # print("Done.")
    return symbols_list


def get_symbols_df(symbols):
    total_symbols = len(symbols)
    pd.set_option("display.max_columns", None)
    df = pd.DataFrame()
    loops = 30

    for t in range(loops):
        try:
            df_entry = (pd.DataFrame([yf.Ticker(symbols[t]).info]))
            # print(df.head(1))
        except Exception as e:
            print(f"{symbols[t]} Not Found")
        df = pd.concat([df, df_entry], axis=0)
        
        bar("Retrieving Stock Info", t + 1, loops, symbols[t])

    df = df.rename(columns={"yield": "totalYield", "open": "openPrice", \
        "zip": "zipCode", "52WeekChange": "fiftyTwoWeekChange", "logo_url": "logoUrl"})
    df.drop(["companyOfficers", "fundInceptionDate", "lastSplitDate", \
        "lastDividendDate", "dateShortInterest"], axis=1, inplace=True)
    df = df.where(pd.notnull(df), None)
    df = df.replace(np.nan, None)
    df.to_csv('logs/raw_data.csv', index=False)

    with connection.cursor() as cursor:
        # creating column list for insertion
        cols = "`,`".join([str(i) for i in df.columns.tolist()])
        for i,row in df.iterrows():
            sql = "INSERT INTO `core_stockinfo` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            query = (sql, tuple(row))
            # print(df)
            try:
                cursor.execute("DELETE FROM core_stockinfo;")
                cursor.execute(query)
            except Exception as e:
                f = open("logs/query.txt", "w")
                f.write(query)
                f.close()
                print(e)
            # print(sql, tuple(row))

    return df


class Command(BaseCommand):
    help = 'Populates the database with collections and products'


    def handle(self, *args, **options):
        current_dir = os.path.dirname(__file__)
        csv_path = os.path.join(current_dir, 'assets//asx.csv')

        symbols = get_symbols(csv_path)
        get_symbols_df(symbols)
        
        print("Done.")
