import os
from datetime import datetime
import alpaca_trade_api as ata
import sqlite3
from dotenv import load_dotenv

#   THIS IS A SCRIPT THAT SHOULD BE SCHEDULED TO AUTOMATICALLY RUN AT LEAST ONCE PER DAY.
#   THE SCRIPT RETRIEVES AN UPDATED LIST OF AVAILABLE STOCKS ON THE MARKET AND INSERTS NEW
#   STOCKS INTO THE DATABASE. INSERTIONS ARE LOGGED AT: logs/stocks.log

# Connect to papertrade database and create cursor object
conn = sqlite3.connect('instance/papertrade.sqlite')
conn.row_factory = sqlite3.Row
db = conn.cursor()
dt = datetime.now()

# Get dictionary of total symbols from database
db.execute('SELECT symbol FROM stocks')
rows = db.fetchall()
symbols = [row['symbol'] for row in rows]

# Validate Alpaca API using secret api keys
load_dotenv()
api = ata.REST(os.environ.get('ALPACA_KEY'), os.environ.get('ALPACA_SECRET'), 
      base_url="https://paper-api.alpaca.markets")

# Get list of assets from Alpaca database
data = api.list_assets()
for ticker in data: #     Iterate over each ticker and add to database if its active,
    try:            #     tradable, and not currently in the database, else throw exception.
        if ticker.status == 'active' and ticker.tradable and ticker.symbol not in symbols:
            print(f'{dt} Stock added ({ticker.symbol}):  {ticker.name}')
            db.execute('INSERT INTO stocks (symbol, company) VALUES (?, ?)',
                        (ticker.symbol, ticker.name))
    except Exception:
        print(ticker.name)
        print(Exception)
conn.commit()   # Commit insertions to the database