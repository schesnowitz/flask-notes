from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


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
        password_1 = request.form.get('password1')
        password_2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email is not valid", category="error")
        elif len(first_name) < 2:
            flash("Name is not valid", category="error")
        elif password_1 != password_2:
            flash("password does not match", category="error")
        elif len(password_1) < 7:
            flash("password must be greater than 7", category="error")
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
            password_1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
          