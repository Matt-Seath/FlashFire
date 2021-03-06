import os
import requests
import urllib.parse
from werkzeug.security import generate_password_hash

from flashfire.db import get_db, query_db


class db_query():

    def get_latest_trade(stock_id):
        result = query_db('SELECT * FROM latestTrade WHERE stock_id = ?', [stock_id])
        return result

    def get_latest_quote(stock_id):
        result = query_db('SELECT * FROM latestQuote WHERE stock_id = ?', [stock_id], one = True)
        return result

    def get_stocks():
        result = query_db('SELECT id, symbol, company FROM stocks')
        return result

    def get_stocklist():
        result = query_db('SELECT symbol FROM stocks')
        symbols = [row['symbol'] for row in result]
        return symbols

    def get_watchlist(user_id):
        result = query_db("""select watchlist.id, symbol, company from stocks
                             JOIN watchlist on watchlist.stock_id = stocks.id
                             WHERE user_id = ? ORDER BY symbol""", [user_id])
        return result

    def get_user(username):
        user = query_db('SELECT * FROM users WHERE username = ?',
                        [username], one = True)
        return user

    def get_user_data(user_id):
        user_data = query_db('SELECT * FROM users WHERE id = ?',
                        [user_id], one=True)
        return user_data

    def get_cash(user_id):
        cash = query_db('SELECT cash FROM users WHERE id = ?',
                        [user_id], one=True)
        return cash

    def get_portfolio(user_id):
        portfolio = query_db("""SELECT symbol, SUM(shares) as total_shares, price FROM portfolio
                                WHERE user_id = ? GROUP BY symbol""", [user_id])
        return portfolio

    def get_quote(symbol):
        quote = query_db("""SELECT date, symbol, company, exchange, open, close, high, low, volume FROM stocks 
                            JOIN stockHistory on stockHistory.stock_id = stocks.id 
                            WHERE symbol = ? ORDER BY date DESC""", [symbol])
        return quote

    def register_user(username, password, email):
        db = get_db()
        try:
            db.execute('INSERT INTO users (username, email, hash) VALUES (?, ?, ?)',
                        [username, email, generate_password_hash(password)]),
            db.commit()
            return True
        except db.IntegrityError:
            return False

    def change_password(user_id, password):
        db = get_db()
        try:
            db.execute('UPDATE users SET hash = ? WHERE id = ?', [generate_password_hash(password), user_id])
            db.commit()
            return True
        except:
            return False


class polygon():

    data = {""}

    def get_history(data):
        api_key = os.environ.get("POLYGON_KEY")
        stocks = db_query.get_stocklist()
        return data        


class iex_cloud():

    def get_data(stocks):
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

    def lookup(symbol):
        """Look up quote for symbol."""
        # Contact API
        try:
            api_key = os.environ.get("API_KEY") 
            url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/quote?token={api_key}"
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException:
            return None
        # Parse response
        try:
            quote = response.json()
            return {
                "name": quote["companyName"],
                "price": float(quote["latestPrice"]),
                "symbol": quote["symbol"]
            }
        except (KeyError, TypeError, ValueError):
            return None

    data_keys = [
        'companyName',
        'symbol',
        'avgTotalVolume',
        'calculationPrice',
        'change',
        'changePercent',
        'close',
        'closeTime',
        'delayedPrice',
        'extendedChange',
        'extendedChangePercent',
        'extendedPrice',
        'high',
        'highTime',
        'iexAskPrice',
        'iexAskSize',
        'iexBidPrice',
        'iexBidSize',
        'iexClose',
        'iexCloseTime',
        'iexLastUpdated',
        'iexMarketPercent',
        'iexOpen',
        'iexOpenTime',
        'iexRealtimePrice',
        'iexRealtimeSize',
        'iexVolume',
        'lastTradeTime',
        'latestPrice',
        'latestSource',
        'latestTime',
        'latestUpdate',
        'latestVolume',
        'low',
        'lowTime',
        'marketCap',
        'oddLotDelayedPrice',
        'oddLotDelayedPriceTime',
        'open',
        'peRatio',
        'previousClose',
        'previousVolume',
        'volume',
        'week52High',
        'week52Low',
        'ytdChange',
        'isUSMarketOpen',
    ]



