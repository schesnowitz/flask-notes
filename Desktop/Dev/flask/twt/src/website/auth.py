from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/log_in')
def log_in():
    return '<p>Log_in</p>'

@auth.route('/log_out')
def log_out():
    return '<p>Log out</p>'  

@auth.route('/sign_up')
def sign_up():
    return '<p>sign up</p>'      