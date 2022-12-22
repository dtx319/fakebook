from . import bp as app
from app.blueprints.main.models import User
from app import db
from flask import render_template, request, redirect, url_for
from flask_login import login_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    # Otherwise, attempt to login the user
    email = request.form['inputEmail']
    password = request.form['inputPassword']

    user = User.query.filter_by(email=email).first()

    # There was not a user with the input email

    # There was a user, but the password was incorrect

    # There was a user, and the password was correct

    if user is None:
        print('There was not a user with that email.')
    elif user.password != password:
        print('The password was incorrect.')
    else:
        print('Logged in successfully')
        login
        return redirect(url_for('main.home'))

    return render_template('login.html')



@app.route('/register')
def register():
    return render_template('register.html')