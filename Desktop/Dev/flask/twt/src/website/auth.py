from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/log_in')
def log_in():
    return render_template('log_in.html', bool=True)

@auth.route('/log_out')
def log_out():
    return render_template('home.html') 

@auth.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')    