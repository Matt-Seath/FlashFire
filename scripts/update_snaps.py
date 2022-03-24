import alpaca_trade_api as ata
from dotenv import load_dotenv
import datetime
import sqlite3
import os

#   THIS IS A SCRIPT THAT SHOULD BE RUN AFTER THE DATABASE IS FIRST INITIALIZED AND update_stocks.py
#   HAS BEEN EXECUTED. THE SCRIPT RETRIEVES THE LAST 100 TRADING DAYS OF HISTORICAL DATA FOR EACH STOCK
#   IN THE DATABASE. DATA IS THEN STORED IN THE 'stockHistory' TABLE. INSERTIONS ARE LOGGED AT: logs/history.log

# Connect to FlashFire database and create cursor object
conn = sqlite3.connect('instance/flashfire.sqlite')
conn.row_factory = sqlite3.Row
db = conn.cursor()

# Timestamp variable
now = datetime.datetime.now()

# Get dictionary of existing tickers from database
db.execute('SELECT id, symbol, company FROM stocks')
rows = db.fetchall()
symbols = [row['symbol'] for row in rows]

# Create dictionary with stock symols as keys and stock_id as values
stock_dict = {}
for row in rows:
    symbol = row['symbol']
    stock_dict[symbol] = row['id']

# Load environment variables
load_dotenv()

# Configure Alpaca API using sercet API keys
api = ata.REST(os.environ.get('ALPACA_KEY'), os.environ.get('ALPACA_SECRET'), 
      base_url=os.environ.get('PAPER_URL'))

# Iterate over stocks in chunks of size chunk_size, to avoid an error from Alpaca api
chunk_size = 1000
for i in range(0, len(symbols), chunk_size):
    symbol_chunk = symbols[i:i + chunk_size]

    # Retrieve historical data for current stock from Alpaca database
    snaps = api.get_snapshots(symbol_chunk)
    for symbol in snaps:
        print(f'{now} updating snapshots ({symbol})')
        # Insert data into local database
        try: 
            db.execute('INSERT INTO latestTrade (stock_id, time, price, size) VALUES (?, ?, ?, ?)',
                         (stock_dict[symbol], 12, snaps[symbol].latest_trade.p, snaps[symbol].latest_trade.s))
            db.execute('INSERT INTO latestQuote (stock_id, time, askPrice, bidPrice, bidSize) VALUES (?, ?, ?, ?, ?)',
                    (stock_dict[symbol], 12, snaps[symbol].latest_quote.ap, snaps[symbol].latest_quote.bp, snaps[symbol].latest_quote.bs))
        except:
            print(f'Failed to get {symbol}')
conn.commit() # Commit insertions when finished
print ('stockHistory has been successfully populated.')