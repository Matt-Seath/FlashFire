import os
from datetime import datetime
import alpaca_trade_api as ata
import sqlite3
from dotenv import load_dotenv

"""THIS SCRIPT SHOULD BE SCHEDULED TO AUTOMATICALLY RUN AT LEAST ONCE PER DAY."""


# Connect to flashfire database and create cursor object
conn = sqlite3.connect('instance/flashfire.sqlite')
conn.row_factory = sqlite3.Row
db = conn.cursor()
dt = datetime.now()

# Get dictionary of total symbols from database
db.execute('SELECT id, symbol, company FROM stocks')
rows = db.fetchall()
symbols = [row['symbol'] for row in rows]

# Validate Alpaca API using secret api keys
load_dotenv()
api = ata.REST(os.environ.get('ALPACA_KEY'), os.environ.get('ALPACA_SECRET'), 
      base_url=os.environ.get('LIVE_URL'))



def update_stocks():
    """RETRIEVES AN UPDATED LIST OF AVAILABLE STOCKS ON THE MARKET AND INSERTS NEW STOCKS INTO
        THE DATABASE. INSERTIONS ARE LOGGED AT: logs/stocks.log"""

    # Get list of assets from Alpaca database
    print('RETRIEVING STOCKS')
    data = api.list_assets()
    for ticker in data: #     Iterate over each ticker and add to database if its active,
        try:            #     tradable, and not currently in the database, else throw exception.
            if ticker.status == 'active' and ticker.tradable and ticker.exchange != 'OTC' and ticker.symbol not in symbols:
                if ticker.exchange == 'ARCA':
                    ticker.exchange = 'AMEX'
                print(f'{dt}  {ticker.exchange} stock added ({ticker.symbol}):  {ticker.name}')
                db.execute('INSERT INTO stocks (symbol, company, exchange) VALUES (?, ?, ?)',
                            (ticker.symbol, ticker.name, ticker.exchange))
        except Exception:
            print(ticker.name)
            print(Exception)
    conn.commit() # Commit insertions when finished
    print('STOCKS POPULATED')
    return 0


def update_prices():
    """RETRIEVE THE LAST 100 TRADING DAYS OF HISTORICAL DATA FOR EACH STOCK IN THE DATABASE. DATA IS THEN 
        STORED IN THE 'stockHistory' TABLE"""

    print('RETRIEVING HISTORICAL DATA')
    
    # Create dictionary with stock symols as keys and stock_id as values
    stock_dict = {}
    for row in rows:
        symbol = row['symbol']
        stock_dict[symbol] = row['id']

    # Iterate over stocks in chunks of size chunk_size, to avoid an error from Alpaca api
    chunk_size = 200
    for i in range(0, len(symbols), chunk_size):
        symbol_chunk = symbols[i:i + chunk_size]

        # Retrieve historical data for current stock from Alpaca database
        bar_sets = api.get_bars(symbol_chunk, "1Day", limit = 200)
        for symbol in bar_sets:
            print(f'{dt} processing symbol ({symbol})')
            for bar in bar_sets[symbol]:
                stock_id = stock_dict[symbol]

                # Insert data into local database
                db.execute('INSERT INTO stockHistory (stock_id, date, open, high, low, close, volume) VALUES (?, ?, ?, ?, ?, ?, ?)',
                            (stock_id, bar.t.date(), bar.o, bar.h, bar.l, bar.c, bar.v))
    conn.commit() # Commit insertions when finished
    print ('STOCK HISTORY UP TO DATE')
    return 0


if __name__ == "__main__":
    update_stocks()
    update_prices()