from . import bp as app
from flask import render_template, request, redirect, url_for 
from app.blueprints.main.models import User, Post
from app import db

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

@app.route('/post', methods=['POST'])
def create_post():
    post_title = request.form['title']
    post_body = request.form['body']

    new_post = Post(title=post_title, body=post_body, user_id=1)

    db.session.add(new_post)
    db.session.commit()

    return redirect(url_for('main.home'))