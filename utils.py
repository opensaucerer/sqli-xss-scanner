# importing modules
from functools import wraps
from flask import session, flash, redirect, url_for, request, jsonify, current_app
from models import User
from flask_mail import Message
from threading import Thread
from __init__ import Mail


# login in required decorator
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'current_user' in session:
            if session['is_authenticated'] and "current_user" in session:
                user = session['current_user']

        else:
            flash('You must be signed in to access that page', 'danger')
            return redirect(url_for('main.login'))

        return f(user, *args, **kwargs)

    return decorated


# login in required decorator
def no_login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'is_authenticated' in session:
            if session["is_authenticated"] == True:
                return redirect(url_for('main.dashboard'))

        return f(*args, **kwargs)

    return decorated
