from django.db import connection
from datetime import datetime
from tqdm import tqdm
import yfinance as yf
import contextlib
import pandas as pd
import numpy as np
import time
import io


class StockDataFrame():

    iterations = None
    symbols = None
    sleeper = 0

    def __init__(self, *symbols_list):
        if self.symbols == None and symbols_list:
            self.symbols == symbols_list
            print(symbols_list)

    def timestamp(self):
        return datetime.now().strftime("%Y/%m/%d, %H:%M:%S")

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
        df = df.rename(columns={
            "open": "open_price",
            "address1": "address",
            "52WeekChange": "fifty_two_week_change",
            "longBusinessSummary": "long_business_summary",
            "maxAge": "max_age",
            "ebitdaMargins": "ebitda_margins",
            "profitMargins": "profit_margins",
            "grossMargins": "gross_margins",
            "operatingCashflow": "operating_cashflow",
            "revenueGrowth": "revenue_growth",
            "operatingMargins": "operating_margins",
            "recommendationKey": "recommendation_key",
            "grossProfits": "gross_profits",
            "freeCashflow": "free_cashflow",
            "currentPrice": "current_price",
            "currentRatio": "current_ratio",
            "returnOnAssets": "return_on_assets",
            "debtToEquity": "debt_to_equity",
            "returnOnEquity": "return_on_equity",
            "totalCash": "total_cash",
            "totalDebt": "total_debt",
            "totalRevenue": "total_revenue",
            "totalCashPerShare": "total_cash_per_share",
            "financialCurrency": "financial_currency",
            "revenuePerShare": "revenue_per_share",
            "quickRatio": "quick_ratio",
            "shortName": "short_name",
            "longName": "long_name",
            "exchangeTimezoneName": "exchange_timezone_name",
            "exchangeTimezoneShortName": "exchange_timezone_short_name",
            "isEsgPopulated": "is_esg_populated",
            "gmtOffSetMilliseconds": "gmt_offset_milliseconds",
            "quoteType": "quote_type",
            "messageBoardId": "message_board_id",
            "enterpriseToRevenue": "enterprise_to_revenue",
            "enterpriseToEbitda": "enterprise_to_ebitda",
            "fiftyTwoWeekChange": "fifty_two_week_change",
            "sharesOutstanding": "shares_outstanding",
            "bookValue": "book_value",
            "lastFiscalYearEnd": "last_fiscal_year_end",
            "heldPercentInstitutions": "held_percent_institutions",
            "netIncomeToCommon": "net_income_to_common",
            "trailingEps": "trailing_eps",
            "SandP52WeekChange": "s_and_p_52_week_change",
            "priceToBook": "price_to_book",
            "heldPercentInsiders": "held_percent_insiders",
            "nextFiscalYearEnd": "next_fiscal_year_end",
            "mostRecentQuarter": "most_recent_quarter",
            "floatShares": "float_shares",
            "enterpriseValue": "enterprise_value",
            "priceHint": "price_hint",
            "priceToSalesTrailing12Months": "price_to_sales_trailing_12_months",
            "forwardPE": "forward_p_e",
            "previousClose": "previous_close",
            "regularMarketOpen": "regular_market_open",
            "twoHundredDayAverage": "two_hundred_day_average",
            "trailingAnnualDividendYield": "trailing_annual_dividend_yield",
            "payoutRatio": "payout_ratio",
            "regularMarketDayHigh": "regular_market_day_high",
            "averageDailyVolume10Day": "average_daily_volume_10_day",
            "regularMarketPreviousClose": "regular_market_previous_close",
            "fiftyDayAverage": "fifty_day_average",
            "trailingAnnualDividendRate": "trailing_annual_dividend_rate",
            "averageVolume10days": "average_volume_10_days",
            "regularMarketDayLow": "regular_market_day_low",
            "regularMarketVolume": "regular_market_volume",
            "marketCap": "market_cap",
            "averageVolume": "average_volume",
            "dayLow": "day_low",
            "askSize": "ask_size",
            "fiftyTwoWeekHigh": "fifty_two_week_high",
            "fiftyTwoWeekLow": "fifty_two_week_low",
            "bidSize": "bid_size",
            "dayHigh": "day_high",
            "yield": "deleted",
            "regularMarketPrice": "regular_market_price",
        })

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
