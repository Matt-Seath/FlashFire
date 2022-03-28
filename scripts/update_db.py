from dotenv import load_dotenv
import alpaca_trade_api as ata
import datetime
import sqlite3
import os

"""THIS SCRIPT SHOULD BE RUN AFTER INITIALISING A NEW DATABASE, 
   AND THEN SCHEDULED TO AUTOMATICALLY RUN AT LEAST ONCE PER DAY."""


# Connect to flashfire database and create cursor object
conn = sqlite3.connect('instance/flashfire.sqlite')
conn.row_factory = sqlite3.Row
db = conn.cursor()

# Configure the minimum latest days of data to retrieve (backdate)
days = 20
today = datetime.date.today()
backdate = today - datetime.timedelta(days = days)

# Limit requests to handle X number of stocks at a time
chunk_size = 1000

# Get a list of total symbols from database
db.execute('SELECT id, symbol, company FROM stocks')
rows = db.fetchall()
symbols = [row['symbol'] for row in rows]

# Create dictionary with stock symols as keys and stock_id as values
stock_dict = {}
for row in rows:
    symbol = row['symbol']
    stock_dict[symbol] = row['id']

# Validate Alpaca API using secret api keys
load_dotenv()
api = ata.REST(os.environ.get('ALPACA_KEY'), os.environ.get('ALPACA_SECRET'), 
    base_url=os.environ.get('LIVE_URL'))


def main():

    update_stocks() # Retrieve and insert all current US stocks into stocks table
    update_prices() # Retrieve and Insert historical data for stocks in database
    set_snapshots() # Retrieve and insert latest snapshot data for stocks
    print('DATABASE HAS BEEN SUCCESSFULLY POPULATED')
    return 0


def update_stocks():
    """RETRIEVES AN UPDATED LIST OF AVAILABLE STOCKS ON THE MARKET AND INSERTS NEW STOCKS INTO
        THE DATABASE. INSERTIONS ARE LOGGED AT: logs/stocks.log"""

    print('RETRIEVING STOCKS')

    # Get list of assets from Alpaca database
    data = api.list_assets()
    for ticker in data: #     Iterate over each ticker and add to database if its active,
        try:            #     tradable, and not currently in the database, else throw exception.
            if ticker.status == 'active' and ticker.tradable and ticker.exchange != 'OTC' and ticker.symbol not in symbols:
                if ticker.exchange == 'ARCA':
                    ticker.exchange = 'AMEX'
                print(f'{today} {ticker.exchange} stock added ({ticker.symbol}):  {ticker.name}')
                db.execute('INSERT INTO stocks (symbol, company, exchange) VALUES (?, ?, ?)',
                            (ticker.symbol, ticker.name, ticker.exchange))
        except Exception:
            print(ticker.name)
            print(Exception)
    conn.commit()
    print('STOCKS ADDED SUCCESSFULLY')
    return 0


def update_prices():
    """RETRIEVE THE LAST 100 TRADING DAYS OF HISTORICAL DATA FOR EACH STOCK IN THE DATABASE.
       DATA IS THEN STORED IN THE 'stockHistory' TABLE"""

    print('RETRIEVING HISTORICAL DATA')

    # Configure the 'start date' for the request
    try:
        # If data already exists in db, start search one day after the date of last entry
        db.execute('SELECT date FROM stockHistory ORDER BY date DESC LIMIT 1')
        latest_entry = db.fetchone()[0]
        converted_date = datetime.datetime.strptime(latest_entry, "%Y-%m-%d").date()
        start_date = converted_date + datetime.timedelta(days = 1)
    except:
        # If no data exists in table, get last X days of data, where X = backdate
        start_date = backdate

    if start_date >= today:
        print('STOCKHISTORY HAS ALREADY BEEN UPDATED TODAY')
        return 1

    print (f' START DATE IS SET FOR: {start_date}')

    # Iterate over stocks in chunks of size chunk_size, to avoid an error from Alpaca api
    for i in range(0, len(symbols), chunk_size):
        symbol_chunk = symbols[i:i + chunk_size]

        # Retrieve historical data for current stock from Alpaca database
        bar_sets = api.get_bars(symbol_chunk, "1Day", start = start_date)
        for bar in bar_sets:
            print(f'{today} processing data ({bar.S}) : {bar.t.date()}')
            stock_id = stock_dict[bar.S]

            # Insert data into local database
            db.execute('INSERT INTO stockHistory (stock_id, date, open, high, low, close, volume, no_trades) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                        (stock_id, bar.t.date(), bar.o, bar.h, bar.l, bar.c, bar.v, bar.n))
    conn.commit()
    print ('HISTORICAL DATA ADDED SUCCESSFULLY')
    return 0


def set_snapshots():
    """Retrieve the latest quote and trade for each stock and insert the data
       into their respective tables"""

    print('RETRIEVING SNAPSHOTS')
    # Get 2 lists of stock_ids currently stored in lastestTrade and latestQuote tables
    db.execute('SELECT stock_id FROM latestTrade')
    rows = db.fetchall()
    latest_trade_db = [row['stock_id'] for row in rows]
    db.execute('SELECT stock_id FROM latestQuote')
    rows = db.fetchall()
    latest_quote_db = [row['stock_id'] for row in rows]
    
    # Iterate over stocks in chunks of size chunk_size, to avoid an error from Alpaca api
    for i in range(0, len(symbols), chunk_size):
        symbol_chunk = symbols[i:i + chunk_size]
        snaps = api.get_snapshots(symbol_chunk)

        for symbol in snaps:
            # Insert trade and quote data for each stock into local database if no entries for that stock exist.
            if stock_dict[symbol] not in latest_trade_db:
                try:     
                    db.execute('INSERT INTO latestTrade (stock_id, time, price, size) VALUES (?, ?, ?, ?)',
                                (stock_dict[symbol], snaps[symbol].latest_trade.t.ctime(), snaps[symbol].latest_trade.p, snaps[symbol].latest_trade.s))
                    print(f'{today} initialising trade data ({symbol})') 
                except:     # If not data found, insert values of 0
                    print(f'--Failed to retrieve latest trade {symbol}----------------------------!')
                    db.execute('INSERT INTO latestTrade (stock_id, time, price, size) VALUES (?, ?, ?, ?)',
                                (stock_dict[symbol], today, 0, 0))
            if stock_dict[symbol] not in latest_quote_db:
                try:       
                    ask_size = getattr(snaps[symbol].latest_quote, "as")
                    db.execute('INSERT INTO latestQuote (stock_id, time, askPrice, askSize, bidPrice, bidSize) VALUES (?, ?, ?, ?, ?, ?)',
                            (stock_dict[symbol], snaps[symbol].latest_quote.t.ctime(), snaps[symbol].latest_quote.ap, ask_size, snaps[symbol].latest_quote.bp, snaps[symbol].latest_quote.bs))
                    print(f'{today} initialising trade data ({symbol})') 
                except:    # If no data found, insert values of 0
                    print(f'---------------------------Failed to retrieve latest quote {symbol} --!')
                    db.execute('INSERT INTO latestQuote (stock_id, time, askPrice, askSize, bidPrice, bidSize) VALUES (?, ?, ?, ?, ?, ?)',
                            (stock_dict[symbol], today, 0, 0, 0, 0))
    conn.commit() # Commit insertions when finished
    print ('SNAPSHOTS ADDED SUCCESSFULLY.')
    return 0

if __name__ == "__main__":
    main()