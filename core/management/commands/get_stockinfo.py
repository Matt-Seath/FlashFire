from django.core.management.base import BaseCommand
from django.db import connection
from .progress_bar import bar
import yfinance as yf
import pandas as pd
import csv
import os




def get_symbols(file_path):
    symbols_list = []
    print("Generating list of Symbols..   ", end="")
    with open(file_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)

        for row in data:
            symbol = row["ASX code"] + ".AX"
            symbols_list.append(symbol)

    print("Done.")
    return symbols_list


def get_symbols_df(symbols):
    total_symbols = len(symbols)
    df = []
    for t in range(total_symbols):
        try:
            df = pd.DataFrame([yf.Ticker(symbols[t]).info])
            df = df.rename(columns={"yield_": "total_yield"})
        except:
            print(f"Failed to obtain information for {symbols[t]}..")
            return 1
        with connection.cursor() as cursor:

            # creating column list for insertion
            cols = "`,`".join([str(i) for i in df.columns.tolist()])
            for i,row in df.iterrows():
                sql = "INSERT INTO `core_stockinfo` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
                cursor.execute(sql, tuple(row))
                # print(sql, tuple(row))


        bar("Populating StockInfo Table", t, total_symbols, symbols[t])
        
    return df


class Command(BaseCommand):
    help = 'Populates the database with collections and products'


    def handle(self, *args, **options):
        current_dir = os.path.dirname(__file__)
        csv_path = os.path.join(current_dir, 'assets//asx.csv')

        symbols = get_symbols(csv_path)
        symbols_df = get_symbols_df(symbols)
        
        print(symbols_df)
            #     # creating column list for insertion
            #     cols = "`,`".join([str(i) for i in data.columns.tolist()])

            #     with connection.cursor() as cursor:
            #         print('Populating Stocks...')

            #         # Insert DataFrame recrds one by one.
            #         for i,row in data.iterrows():
            #             sql = "INSERT INTO `book_details` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            #             cursor.execute(sql, tuple(row))

            #             # the connection is not autocommitted by default, so we must commit to save our changes
            #             connection.commit()




            # print("done.")
