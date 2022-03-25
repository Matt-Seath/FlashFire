from re import I
import alpaca_trade_api as ata
from dotenv import load_dotenv
import datetime
import sqlite3
import os

#   THIS SCRIPT SHOULD BE SCHUDULED TO RUN AT ONE MINUTE INTERVALS
#   retrieves the latest quote and trade data of all stocks in
#   the database and REPLACES EXISTING data in their respective tables.


def main():

    # Connect to FlashFire database and create cursor object
    conn = sqlite3.connect('instance/flashfire.sqlite')
    conn.row_factory = sqlite3.Row
    db = conn.cursor()

    # Timestamp variable
    now = datetime.datetime.now()

    # Get list of existing tickers from database
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

    # Get list of stock_ids that have stored data in lastestTrade and latestQuote
    db.execute('SELECT stock_id FROM latestTrade')
    rows = db.fetchall()
    latest_trade_db = [row['stock_id'] for row in rows]
    db.execute('SELECT stock_id FROM latestQuote')
    rows = db.fetchall()
    latest_quote_db = [row['stock_id'] for row in rows]

    print('RETRIEVING SNAPSHOTS')
    # Iterate over stocks in chunks of size chunk_size, to avoid an error from Alpaca api
    chunk_size = 1000
    for i in range(0, len(symbols), chunk_size):
        symbol_chunk = symbols[i:i + chunk_size]
        snaps = api.get_snapshots(symbol_chunk)

        for symbol in snaps:
            # Update existing data into local database
            if stock_dict[symbol] in latest_trade_db: 
                try: 
                    db.execute('UPDATE latestTrade SET time = ?, price = ?, size = ? WHERE stock_id = ?',
                                (snaps[symbol].latest_trade.t.ctime() , snaps[symbol].latest_trade.p, snaps[symbol].latest_trade.s, stock_dict[symbol]))
                    print(f'{now} updating trade data ({symbol})')
                except:
                    print(f'{now} Failed to update {symbol}')
            if stock_dict[symbol] in latest_quote_db:
                try: 
                    ask_size = getattr(snaps[symbol].latest_quote, "as")
                    db.execute('UPDATE latestQuote SET time = ?, askPrice = ?, askSize = ?, bidPrice = ?, bidSize = ? WHERE stock_id = ?',
                            (snaps[symbol].latest_quote.t.ctime() , snaps[symbol].latest_quote.ap, ask_size, snaps[symbol].latest_quote.bp, snaps[symbol].latest_quote.bs, stock_dict[symbol]))
                    print(f'{now} updating quote data ({symbol})')
                except:
                    print(f'{now} Failed to update {symbol}')
    conn.commit() # Commit insertions when finished
    print('SNAPSHOTS ADDED SUCCESSFULLY')
    return 0


if __name__ == '__main__':
    main()