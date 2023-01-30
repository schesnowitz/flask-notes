from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/log_in', methods=["GET", "POST"])
def log_in():

    return render_template('log_in.html', bool=True)

@auth.route('/log_out')
def log_out():
    return render_template('home.html') 

@auth.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('firstname')
        first_name = request.form.get('firstname')
        password_1 = request.form.get('password1')
        password_2 = request.form.get('password2')

        if len(email) < 4:
            pass
        elif len(first_name) < 2:
            pass
        elif password_1 != password_2:
            pass
        elif password_1 < 7:
            pass
        else:
            #  add user to database
            pass
    return render_template('sign_up.html')    