from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/log_in', methods=["GET", "POST"])
def log_in():
    data = request.form
    print(data)
    return render_template('log_in.html', bool=True)

@auth.route('/log_out')
def log_out():
    return render_template('home.html') 

@auth.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    return render_template('sign_up.html')    