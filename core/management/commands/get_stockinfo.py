from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from django.db import connection
from .progress_bar import bar
import yfinance as yf
import pandas as pd
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

    for t in range(5):
        try:
            df_entry = (pd.DataFrame([yf.Ticker(symbols[t]).info]))
            # print(df.head(1))
        except Exception as e:
            f = open("logs/errors.txt", "a")
            f.write(f"Failed to obtain information for {symbols[t]}: {e}\n ")
            print(f"{symbols[t]} Not Found")
            f.close()
        df = pd.concat([df, df_entry], axis=0)
        
            
        bar("Retrieving Stock Info", t, total_symbols, symbols[t])

    df = df.rename(columns={"yield": "totalYield", "open": "openPrice", \
        "zip": "zipCode", "52WeekChange": "fiftyTwoWeekChange", "logo_url": "logoUrl"})
    df.drop(['companyOfficers'], axis=1, inplace=True)
    df.to_csv('logs/raw_data.csv', index=False)

    with connection.cursor() as cursor:
        # creating column list for insertion
        cols = "`,`".join([str(i) for i in df.columns.tolist()])
        for i,row in df.iterrows():
            sql = "INSERT INTO `core_stockinfo` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            try:
                cursor.execute("DELETE FROM core_stockinfo;")
                cursor.execute(sql, tuple(row))
                # print(df)
            except IntegrityError as e:
                print(f"{t} already exists in this database!")
            # print(sql, tuple(row))

    
    return df


class Command(BaseCommand):
    help = 'Populates the database with collections and products'


    def handle(self, *args, **options):
        current_dir = os.path.dirname(__file__)
        csv_path = os.path.join(current_dir, 'assets//asx.csv')

        symbols = get_symbols(csv_path)
        symbols_df = get_symbols_df(symbols)
        
        # print(symbols_df)
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
