from . import bp as app
from flask import render_template
from app.blueprints.main.models import User, Post

# Routes that return/display HTML
@app.route('/')
def home():
    posts = Post.query.all()

    logged_in_user = User.query.get(1)

    return render_template('home.html', user=logged_in_user, posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')