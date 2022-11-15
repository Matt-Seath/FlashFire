import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext


# accept command to inialial database locally
# USAGE: CLI command:  $ flask init-db
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# Configure database for each app individually
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

# Initialize the database if it doesn't yet exist in the instance/ directory.
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# Connects to local database, configures a cursor and returns the cursor object.
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

# A simple higher-order function that makes querying the database less tedious
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# Close the database for g.user
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
