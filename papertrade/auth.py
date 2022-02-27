import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from papertrade.db import get_db
from papertrade.forms import registerForm, loginForm
from papertrade.models import db_query

bp = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO users (username, hash) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    form = loginForm()
    if request.method == 'POST':

        # Validate Form
        username = form.username.data
        password = form.password.data
        error = None

        user = db_query.get_user(username)
        if user is None:
            error = 'Incorrect username or password.'
        elif not check_password_hash(user['hash'], password):
            error = 'Incorrect username or password.'
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        flash(error)
        return render_template('auth/login.html',
                                username = username, 
                                password = password,
                                form = form)
    else:
        username = None
        password = None
        return render_template('auth/login.html',
                                username = username, 
                                password = password,
                                form = form)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))