import os
import alpaca_trade_api as ata
import sqlite3

# Connect to papertrade database
conn = sqlite3.connect('instance/papertrade.sqlite')
conn.row_factory = sqlite3.Row

# Create cursor object
db = conn.cursor()

# Get dictionary of symbols from database
db.execute('SELECT symbol FROM stocks')
rows = db.fetchall()

# Validate API
api = ata.REST('PKZVHL1ZUZ05I50F2JIR', '5a1kTrPo34eZo4RvysM6f92sVEFotjUeWMH1R5HM', 
      base_url="https://paper-api.alpaca.markets")

data = api.list_assets()

for ticker in data:
    try:
        if ticker.status == 'active' and ticker.tradable:
            print(f'Added new stock to database: {ticker.symbol}{ticker.name}')
            db.execute('INSERT INTO stocks (symbol, company) VALUES (?, ?)',
                        (ticker.symbol, ticker.name))
    except Exception:
        print(ticker.name)
        print(Exception)
db.commit()
