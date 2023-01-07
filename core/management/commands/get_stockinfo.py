from django.core.management.base import BaseCommand
from .progress_bar import bar
from datetime import datetime
from django.db import connection
import yfinance as yf
import pandas as pd
import numpy as np
import csv
import os



NOW = datetime.now().strftime("%Y/%m/%d, %H:%M:%S")


def get_symbols(file_path):
    symbols_list = []
    print("Generating list of Symbols..   ", end="")
    with open(file_path, newline='') as csvfile:
        data = csv.DictReader(csvfile)

        for row in data:
            symbol = row["ASX code"].strip() + ".AX"
            symbols_list.append(symbol + ", ")

    print("Done.")
    return symbols_list


def clear_logs():
    with open("logs/query.log", "w") as f:
        f.truncate(0)
    with open("logs/added.log", "w") as f:
        f.truncate(0)
    with open("logs/errors.log", "w") as f:
        f.truncate(0)
    with open ("logs/skipped.log", "w") as f:
        f.truncate(0)


def write_to_logs(added=None, skipped=None):
    if added:
        for entry in added:
            with open ("logs/added.log", "a") as f:
                f.write(entry)
    if skipped:
        for entry in skipped:
            with open ("logs/skipped.log", "a") as f:
                f.write(entry)


def get_symbols_df(symbols):
    df = pd.DataFrame()
    df_entry = pd.DataFrame()
    added_symbols = []
    skipped_symbols = []
    errors = 0
    loops = 12
    # loops = len(symbols)

    for t in range(loops):
        try:
            df_entry = (pd.DataFrame([yf.Ticker(symbols[t]).info]))
        except Exception as e:
            errors += 0
            with open("logs/errors.log", "a") as f: 
                f.write(f"{NOW}: {symbols[t]} Not Found \n")

        print(len(df_entry.columns))
        if len(df_entry.columns) < 130:
            # print(f"Skipping {symbols[t]}")
            skipped_symbols.append(symbols[t])
            continue

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


    with connection.cursor() as cursor:
        # creating column list for insertion
        cols = "`,`".join([str(i) for i in df.columns.tolist()])
        # update_cols = "=%s, ".join([str(i) for i in df.columns.tolist()])
        
        for i,row in df.iterrows():
            # symbol_exists = cursor.execute("SELECT symbol from core_stockinfo WHERE symbol = %s", (row["symbol"], ))
            sql = "REPLACE INTO `core_stockinfo` (`"+ cols +"`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
            # update_sql = "UPDATE 'core_stockinfo' SET "+ update_cols +"`=%s WHERE symbol = " + row["symbol"]
            # method = update_sql if symbol_exists else insert_sql
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
            # print(sql, tuple(row))
            # bar("Inserting into Database", i + 1, loops, symbols[i])
    print("")
    print(f"Skipped Symbols: {str(skipped_symbols)}")
    write_to_logs(added_symbols, skipped_symbols)
    return df, errors


class Command(BaseCommand):
    help = 'Populates the database with collections and products'


    def handle(self, *args, **options):
        clear_logs()
        current_dir = os.path.dirname(__file__)
        csv_path = os.path.join(current_dir, 'assets//asx.csv')
        symbols = get_symbols(csv_path)
        df, errors = get_symbols_df(symbols)
        
        df.to_csv("logs/raw_data.csv", index=False)
        print("")

        print(f"Task completed with {errors} error/s.")
