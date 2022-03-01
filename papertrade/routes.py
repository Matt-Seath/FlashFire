from flask import redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash

from papertrade import app
from papertrade.models import apology, login_required, lookup, usd
from papertrade import c
  


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session.get('user_id')
    c.execute("SELECT cash FROM users WHERE id = ?", (user_id, ))
    cash = c.fetchall()[0]['cash']
    c.execute('SELECT stock, symbol, SUM(shares) as total_shares, price FROM portfolio WHERE user_id = ? GROUP BY symbol', (user_id, ))
    portfolio = c.fetchall()
    equity = cash
    for i in portfolio:
        equity += i['price'] * i['total_shares']
    return render_template('index.html', equity=equity, usd=usd, portfolio=portfolio, cash=cash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        stock = lookup(symbol)
        try:
            shares = int(request.form.get('shares'))
        except:
            return apology('Shares must be an integer')

        if shares <= 0:
            return apology('Shares must be a positive integer')

        if not symbol:
            return apology('Symbol missing')

        elif not stock:
            return apology('Invalid symbol')

        user_id = session.get('user_id')
        c.execute('SELECT cash FROM users WHERE id = ?', (user_id, ))
        cash = c.fetchall()[0]['cash']
        stock_name = stock['name']
        stock_price = stock['price']
        total = stock_price * shares
        if cash < total:
            return apology('Insufficient funds')

        else:
            new_cash_total = cash - total
            c.execute('BEGIN;')
            c.execute('UPDATE users SET cash = ? WHERE id = ?', (new_cash_total, user_id))
            c.execute('INSERT INTO portfolio (user_id, stock, symbol, shares, price, trade) VALUES (?, ?, ?, ?, ?, ?)',
                       (user_id, stock_name, symbol, shares, stock_price, 'BUY'))
            c.execute('COMMIT;')
        return redirect('/')

    else:
        return render_template('buy.html')


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session.get('user_id')
    c.execute('SELECT symbol, shares, price, trade, time FROM portfolio WHERE user_id = ?', (user_id, ))
    trade_history = c.fetchall()
    return render_template('history.html', trades=trade_history, usd=usd)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        c.execute("SELECT * FROM users WHERE username = ?", (request.form.get("username"), ))
        rows = c.fetchall()
     
        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]['hash'], request.form.get("password")):
            return apology("invalid username and/or password", 403)
    
        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
  
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if (request.method == "POST"):
        symbol = request.form.get('symbol')
        if not symbol:
            return apology('Missing symbol')

        stock = lookup(symbol)
        if not stock:
            return apology('Invalid symbol')

        return render_template('quoted.html', usd=usd, stock=stock)

    else:
        return render_template("quote.html")


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Change User Password."""
    if (request.method == "POST"):
        user_id = session.get('user_id')
        old_password = request.form.get('old')
        new_password = request.form.get('new')
        confirm_password = request.form.get('confirm')
        c.execute("SELECT * FROM users WHERE id = ?", (user_id, ))
        password = c.fetchall()[0]["hash"]
        if not old_password:
            return apology('Missing old password')

        elif not new_password:
            return apology('Missing new password')

        elif not confirm_password:
            return apology('Missing confirm password')

        elif not check_password_hash(password, old_password):
            return apology('Password is incorrect')

        elif new_password != confirm_password:
            return apology('Passwords do not match')

        hash = generate_password_hash(new_password)
        c.execute('BEGIN;')
        c.execute('UPDATE users SET hash = ? WHERE id = ?', (hash, user_id))
        c.execute('COMMIT;')
        return redirect('/')

    else:
        return render_template("password.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if (request.method == "POST"):
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirmation')
        if not username:
            return apology('Missing username')

        elif not password:
            return apology('Missing password')

        elif not confirm:
            return apology('Please confirm password')

        elif password != confirm:
            return apology('Passwords do not match')

        hash = generate_password_hash(password)
        try:
            c.execute('BEGIN;')
            c.execute('INSERT INTO users (username, hash) VALUES (?, ?)', (username, hash))
            c.execute('COMMIT;')
            return redirect('/')

        except:
            return apology('Username is already taken')

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session.get('user_id')
    if (request.method == 'POST'):
        symbol = request.form.get('symbol')
        shares = int(request.form.get('shares'))
        c.execute('SELECT shares FROM portfolio WHERE user_id = ? AND symbol = ? GROUP BY symbol', (user_id, symbol))
        total_shares = c.fetchall()[0]['shares']
        if not symbol:
            return apology('No stock selected')

        elif shares <= 0:
            return apology('Shares must be a positive integer')

        elif shares > total_shares:
            return apology('Insufficient shares')

        c.execute('SELECT cash FROM users WHERE id = ?', (user_id, ))
        cash = c.fetchall()[0]['cash']
        stock = lookup(symbol)
        stock_name = stock['name']
        stock_price = stock['price']
        total_share_price = stock_price * shares
        total_cash = total_share_price + cash
        c.execute('BEGIN;')
        c.execute('UPDATE users SET cash = ? WHERE id = ?', (total_cash, user_id))
        c.execute('INSERT INTO portfolio (user_id, stock, symbol, shares, price, trade) VALUES (?, ?, ?, ?, ?, ?)',
                   (user_id, stock_name, symbol, -shares, stock_price, 'SELL'))
        c.execute('COMMIT;')
        return redirect('/')

    else:
        c.execute('SELECT symbol FROM portfolio WHERE user_id = ? GROUP BY symbol', (user_id, ))
        stocks = c.fetchall()
        return render_template('sell.html', stocks=stocks)
