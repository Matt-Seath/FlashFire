from flask import Blueprint, flash, g, redirect, session, render_template, request, url_for
from papertrade.auth import login_required
from papertrade.models import db_query


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

