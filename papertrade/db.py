import sqlite3
import click
import requests
from flask import current_app, g
from flask.cli import with_appcontext



@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def populate_db():
    url = f"https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/2020-10-14?adjusted=true&apiKey={POLYGON_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    stock_data = response.json()
    db = get_db()
    try:
        for row in stock_data["results"]:
            db.execute('INSERT INTO stocks (symbol) VALUES (?)', row['T'])
        db.commit()
        return "Tickers successfully populated"
    except db.IntegrityError:
        return "Unable to populate database"


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
