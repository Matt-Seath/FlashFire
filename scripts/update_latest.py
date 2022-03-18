import os
import requests
from dotenv import load_dotenv
import sqlite3

#   THIS IS A SCRIPT THAT SHOULD BE RUN AFTER THE DATABASE IS FIRST INITIALIZED AND update_stocks.py
#   HAS BEEN EXECUTED. THE SCRIPT RETRIEVES THE LAST 100 TRADING DAYS OF HISTORICAL DATA FOR EACH STOCK
#   IN THE DATABASE. DATA IS THEN STORED IN THE 'stockHistory' TABLE. INSERTIONS ARE LOGGED AT: logs/history.log

# # Connect to FlashFire database and create cursor object
# conn = sqlite3.connect('instance/flashfire.sqlite')
# conn.row_factory = sqlite3.Row
# db = conn.cursor()

# # Get dictionary of existing tickers from database
# db.execute('SELECT symbol FROM stocks')
# rows = db.fetchall()
# stocks = [row['symbol'] for row in rows]

stocks = ['AES', 'ARTW', 'COWN']

# Iterate over all stocks and retrieve
load_dotenv()
api_key = os.environ.get("IEX_KEY")
data = {}
for stock in stocks:
    url = f"https://cloud.iexapis.com/stable/stock/{stock}/quote?token={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    stock_data = response.json()

    for item in stock_data:
        data.setdefault(item, [])
        data[item].append(stock_data.get(item))
return data