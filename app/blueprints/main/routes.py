from . import bp as app
from flask import render_template


# Routes that return/display HTML
logged_in_user = 1

@app.route('/')
def home():
    return render_template('home.html', user=logged_in_user)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')