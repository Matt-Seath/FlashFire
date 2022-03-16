from flask import Blueprint, session, render_template

from flashfire.auth import login_required
from flashfire.queries import db_query


bp = Blueprint('platform', __name__)


@bp.route('/')
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session.get('user_id')
    cash = db_query.get_cash(user_id)[0]
    portfolio = db_query.get_portfolio(user_id)
    equity = cash
    for i in portfolio:
        equity += i['price'] * i['total_shares']
    return render_template('platform/index.html', 
                            equity=equity,
                            portfolio=portfolio,
                            cash=cash)


@bp.route('/watchlist', methods=('GET', 'POST'))
@login_required
def watchlist():
    """Show portfolio of stocks"""
    user_id = session.get('user_id')
    stocks = db_query.get_watchlist(user_id)
    return render_template('platform/watchlist.html', 
                            stocks=stocks)
                           

@bp.route('/portfolio', methods=('GET', 'POST'))
@login_required
def portfolio():
    """Show portfolio of stocks"""
    user_id = session.get('user_id')
    cash = db_query.get_cash(user_id)[0]
    portfolio = db_query.get_portfolio(user_id)
    equity = cash
    for i in portfolio:
        equity += i['price'] * i['total_shares']
    return render_template('platform/index.html', 
                            equity=equity,
                            portfolio=portfolio,
                            cash=cash)


@bp.route('/quote', methods=('GET', 'POST'))
@login_required
def quote():
    """Provide interface for user to retrieve quotes for stocks"""
    return render_template('platform/quote.html')



@bp.route('/quote/<symbol>', methods=('GET', 'POST'))
@login_required
def quote_symbol(symbol):
    """Quote a particular Stock"""
    rows = db_query.get_quote(symbol)
    return render_template('platform/quote.html', 
                            rows = rows)


@bp.route('/trading', methods=('GET', 'POST'))
@login_required
def trading():
    """Show portfolio of stocks""" 
    return render_template('platform/trading.html')


@bp.route('/settings', methods=('GET', 'POST'))
@login_required
def settings():
    """Show portfolio of stocks"""
    user_id = session.get('user_id')
    cash = db_query.get_cash(user_id)[0]
    portfolio = db_query.get_portfolio(user_id)
    equity = cash
    for i in portfolio:
        equity += i['price'] * i['total_shares']
    return render_template('platform/index.html', 
                            equity=equity,
                            portfolio=portfolio,
                            cash=cash)
