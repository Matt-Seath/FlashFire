from flask import Blueprint, flash, g, redirect, session, render_template, request, url_for

from papertrade.auth import login_required
from papertrade.models import db_query



bp = Blueprint('platform', __name__)



data = {'avgTotalVolume': [24932116, 87240847, 56054158, 37190809, 4421104, 8466375, 2420347], 'calculationPrice': ['close', 'close', 'close', 'close', 'close', 'close', 'close'], 'change': [60.56, 0.27, 2.28, 1.48, -4.51, -1.22, 11.95], 'changePercent': [0.07478, 0.00164, 0.00944, 0.00498, -0.00147, -0.00895, 0.00444], 'close': [None, None, None, None, None, None, None], 'closeSource': ['official', 'official', 'official', 'official', 'official', 'official', 'official'], 'closeTime': [None, None, None, None, None, None, None], 'companyName': ['Tesla Inc', 'Apple Inc', 'NVIDIA Corp', 'Microsoft Corporation', 'Amazon.com Inc.', 'Walmart Inc', 'Alphabet Inc - Class A'], 'currency': ['USD', 'USD', 'USD', 'USD', 'USD', 'USD', 'USD'], 'delayedPrice': [None, None, None, None, None, None, None], 'delayedPriceTime': [None, None, None, None, None, None, None], 'extendedChange': [None, None, None, None, None, None, None], 'extendedChangePercent': [None, None, None, None, None, None, None], 'extendedPrice': [None, None, None, None, None, None, None], 'extendedPriceTime': [None, None, None, None, None, None, None], 'high': [None, None, None, None, None, None, None], 'highSource': [None, None, None, None, None, '15 minute delayed price', None], 'highTime': [None, None, None, None, None, 1646082007191, None], 'iexAskPrice': [None, None, None, None, None, None, None], 'iexAskSize': [None, None, None, None, None, None, None], 'iexBidPrice': [None, None, None, None, None, None, None], 'iexBidSize': [None, None, None, None, None, None, None], 'iexClose': [871.13, 165.28, 243.62, 298.94, 3069.56, 135.16, 2699.83], 'iexCloseTime': [1646081999610, 1646081998778, 1646081999485, 1646081999941, 1646081997414, 1646081997002, 1646081999540], 'iexLastUpdated': [None, None, None, None, None, None, None], 'iexMarketPercent': [None, None, None, None, None, None, None], 'iexOpen': [815.01, 163.14, 239.57, 294.37, 3050.07, 134.98, 2663.25], 'iexOpenTime': [1646058600000, 1646058600403, 1646058601227, 1646058601010, 1646058600084, 1646058602230, 1646058600348], 'iexRealtimePrice': [None, None, None, None, None, None, None], 'iexRealtimeSize': [None, None, None, None, None, None, None], 
'iexVolume': [None, None, None, None, None, None, None], 'lastTradeTime': [1646081999610, 1646081999980, 1646081999693, 1646081999970, 1646081999649, 1646081999841, 1646081999940], 'latestPrice': [870.43, 165.12, 243.85, 298.79, 3071.26, 135.16, 2701.14], 'latestSource': ['Close', 'Close', 'Close', 'Close', 'Close', 'Close', 'Close'], 'latestTime': ['February 28, 2022', 'February 28, 2022', 'February 28, 2022', 'February 28, 2022', 'February 28, 2022', 'February 28, 2022', 'February 28, 2022'], 'latestUpdate': [1646082000910, 1646082000441, 1646082001215, 1646082000927, 1646082001287, 1646082002062, 1646082001709], 'latestVolume': [None, None, None, None, None, None, None], 'low': [None, None, None, None, None, None, None], 'lowSource': ['IEX real time price', None, None, None, 'IEX real time price', '15 minute delayed price', 'IEX real time price'], 'lowTime': [1646058602490, None, None, None, 1646075417860, 1646076626346, 1646061273189], 'marketCap': [874142255126, 2694666097920, 609625000000, 2239988720022, 1562793482657, 374917412383, 1821489848509], 'oddLotDelayedPrice': [None, None, None, None, None, None, None], 'oddLotDelayedPriceTime': [None, None, None, None, None, None, None], 'open': [None, None, None, None, None, None, None], 'openTime': [None, None, None, None, None, None, None], 'openSource': ['official', 'official', 'official', 'official', 'official', 'official', 'official'], 'peRatio': [178, 27.43, 75.26, 31.79, 47.41, 47.59, 25.69], 'previousClose': [809.87, 164.85, 241.57, 297.31, 3075.77, 136.38, 2689.19], 'previousVolume': [25355921, 91974222, 52886551, 32546721, 3119768, 8332590, 1820299], 'primaryExchange': ['NASDAQ', 'NASDAQ', 'NASDAQ', 'NASDAQ', 'NASDAQ', 'NEW YORK STOCK EXCHANGE INC.', 'NASDAQ'], 'symbol': ['TSLA', 'AAPL', 'NVDA', 'MSFT', 'AMZN', 'WMT', 'GOOGL'], 'volume': [None, None, None, None, None, None, None], 'week52High': [1243.49, 182.71, 346.43, 348.95, 3773.08, 151.96, 3030.93], 'week52Low': [539.49, 115.52, 115.56, 222.45, 2707.04, 124.3, 1994], 'ytdChange': [-0.1015575537008649, -0.06728870977946264, -0.16144844309952067, -0.10477311805402433, -0.08037017214801126, -0.07481495265740555, -0.06318074393173723], 'isUSMarketOpen': [False, False, False, False, False, False, False]}


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
    return render_template('platform/watchlist.html', 
                            data=data)
                           

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


@bp.route('/quotes', methods=('GET', 'POST'))
@login_required
def quotes():
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


@bp.route('/trading', methods=('GET', 'POST'))
@login_required
def trading():
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
