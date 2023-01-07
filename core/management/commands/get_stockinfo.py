from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from django.db import connection
from .progress_bar import bar
from datetime import datetime
from sqlalchemy import create_engine
import yfinance as yf
import pandas as pd
import numpy as np
import csv
import os



NOW = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")


def mysql_replace_into(table, conn, keys, data_iter):
    from sqlalchemy.dialects.mysql import insert
    from sqlalchemy.ext.compiler import compiles
    from sqlalchemy.sql.expression import Insert

    @compiles(Insert)
    def replace_string(insert, compiler, **kw):
        s = compiler.visit_insert(insert, **kw)
        s = s.replace("INSERT INTO", "REPLACE INTO")
        return s

    data = [dict(zip(keys, row)) for row in data_iter]

    conn.execute(table.table.insert(replace_string=""), data)


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
    with open("logs/query.txt", "w") as f:
        f.truncate(0)
    with open("logs/errors.txt", "w") as f:
        f.truncate(0)

    # pd.set_option("display.max_columns", None)
    df = pd.DataFrame()
    ignore_list = ["2BE.AX", "3MF.AX"]
    errors = 0
    loops = 70
    # loops = len(symbols)

    for t in range(loops):
        if symbols[t] in ignore_list:
            continue
        try:
            df_entry = (pd.DataFrame([yf.Ticker(symbols[t]).info]))
            # print(df.head(1))
        except Exception as e:
            errors += 0
            with open("logs/errors.txt", "a") as f: 
                f.write(f"{NOW}: {symbols[t]} Not Found \n")

        df = pd.concat([df, df_entry], axis=0)
        bar("Retrieving Stock Info", t + 1, loops, symbols[t])

    df = df.replace(np.nan, None)
    df = df.reset_index(drop=True)
    df = df.rename(columns={"open": "openPrice", \
        "52WeekChange": "fiftyTwoWeekChange", "logo_url": "logoUrl"})
    df.drop(["zip", "companyOfficers", "fundInceptionDate", "lastSplitDate", \
        "lastDividendDate", "dateShortInterest", "fullTimeEmployees", "fax", "targetLowPrice", \
        "targetMedianPrice", "earningsGrowth", "numberOfAnalystOpinions", "targetMeanPrice", \
        "targetHighPrice", "recommendationMean", "annualHoldingsTurnover", "beta3Year", \
        "morningStarRiskRating", "forwardEps", "revenueQuarterlyGrowth", \
        "annualReportExpenseRatio", "totalAssets", "sharesShort", "sharesPercentSharesOut", \
        "fundFamily", "yield", "shortRatio", "sharesShortPreviousMonthDate", \
        "threeYearAverageReturn", "lastSplitFactor", "legalType", "morningStarOverallRating", \
        "earningsQuarterlyGrowth", "pegRatio", "ytdReturn", "lastCapGain", "shortPercentOfFloat", \
        "sharesShortPriorMonth", "impliedSharesOutstanding", "category", "fiveYearAverageReturn", \
        "volume24Hr", "navPrice", "toCurrency", "expireDate", "algorithm", "dividendRate", \
        "exDividendDate", "circulatingSupply", "startDate", "lastMarket", "maxSupply", \
        "openInterest", "volumeAllCurrencies", "strikePrice", "fromCurrency", \
        "fiveYearAvgDividendYield", "dividendYield", "coinMarketCapLink", "preMarketPrice", \
        "trailingPegRatio", "address2", "lastDividendValue", "trailingPE", "0", "", " "], \
        axis=1, inplace=True, errors="ignore")
    # df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)


    engine = create_engine("mysql://root:root@db:3306/flashfire")


    df.to_sql("core_stockinfo", con=engine, if_exists="append", index_label="id", method=mysql_replace_into)            


    # with connection.cursor() as cursor:
    #     cursor.execute("DELETE FROM core_stockinfo;")
    #     # creating column list for insertion
    #     cols = "`,`".join([str(i) for i in df.columns.tolist()])

    #     for i,row in df.iterrows():
    #         sql = "INSERT INTO `core_stockinfo` (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    #         query = f"{sql}{tuple(row)}"
    #         try:
    #             # print(sql, tuple(row))
    #             cursor.execute(sql, tuple(row))
    #         except Exception as e:
    #             with open("logs/query.txt", "a") as f:
    #                 f.write(query + '\n')
    #             with open("logs/errors.txt", "a") as f:
    #                 f.write(f"{NOW}: Could not insert {symbols[i]}, {e} \n")
    #             errors += 1
    #         # print(sql, tuple(row))
    #         bar("Inserting into Database", i + 1, loops, symbols[i])

    return df, errors


class Command(BaseCommand):
    help = 'Populates the database with collections and products'


    def handle(self, *args, **options):
        current_dir = os.path.dirname(__file__)
        csv_path = os.path.join(current_dir, 'assets//asx.csv')

        symbols = get_symbols(csv_path)
        df, errors = get_symbols_df(symbols)
        
        print("")
        df.to_csv("logs/raw_data.csv", index=False)
        print("")
        print(f"Task completed with {errors} error/s.")
