import os
import requests
import urllib.parse
from papertrade.db import get_db, query_db
from werkzeug.security import check_password_hash, generate_password_hash



class db_query():

    def get_user(username):
        user = query_db('SELECT * FROM users WHERE username = ?',
                        [username], one=True)
        return user

    def get_cash(user_id):
        cash = query_db('SELECT cash FROM users WHERE id = ?',
                        [user_id], one=True)
        return cash

    def get_portfolio(user_id):
        portfolio = query_db('SELECT stock, symbol, SUM(shares) as total_shares, price FROM portfolio WHERE user_id = ? GROUP BY symbol',
                        [user_id])
        return portfolio

    def register_user(username, password, email):
        db = get_db()
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)",
                        (username, generate_password_hash(password)),
        db.commit())



class iex_cloud():

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

