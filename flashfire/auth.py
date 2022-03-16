import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash
from papertrade import db
from papertrade.forms import registerForm, loginForm, changePasswordForm
from papertrade.queries import db_query



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
        g.user = db_query.get_user_data(user_id)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    username = None
    password = None
    email = None
    form = registerForm()
    if request.method == 'POST':

        if form.validate_on_submit():           
            username = form.username.data
            password = form.password.data
            email = form.email.data
            if not db_query.register_user(username, password, email):
                flash(f"User {username} is already registered.")
            else:
                return redirect(url_for("auth.login"))
        else:
            for error in form.errors:
                flash(form.errors[error][0]) 
    return render_template('auth/register.html',
                            username = username,
                            password = password,
                            email = email,
                            form = form)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    username = None
    password = None
    form = loginForm()
    if request.method == 'POST':

        # Validate Form
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = db_query.get_user(username)
            error = None
            if user is None:
                error = 'Incorrect username or password'
            elif not check_password_hash(user['hash'], password):
                error = 'Incorrect username or password'
            if error is None:
                session.clear()
                session['user_id'] = user['id']
                return redirect(url_for('index'))
            flash(error)
        else:
            for err in form.errors:
                flash(form.errors[err][0]) 
    return render_template('auth/login.html',
                            username = username, 
                            password = password,
                            form = form)


@bp.route('/change_password', methods=('GET', 'POST'))
def change_password():
    old_password = None
    new_password = None
    form = changePasswordForm()
    if request.method == 'POST':

        if form.validate_on_submit():           
            old_password = form.oldPassword.data
            new_password = form.newPassword.data
            user_id = session.get('user_id')
            user = db_query.get_user_data(user_id)
            error = None
            if not check_password_hash(user['hash'], old_password):
                error = 'Old password is incorrect'
            else:
                if db_query.change_password(user_id, new_password):
                    flash('Password has been changed successfully!')
                    return redirect(url_for('index'))
                error = 'Password could not be changed'
            flash(error)
        else:
            for error in form.errors:
                flash(form.errors[error][0]) 
    return render_template('auth/change_password.html',
                            oldPassword = old_password,
                            newPassword = new_password,
                            form = form)


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('platform.index'))