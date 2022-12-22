from . import bp as app
from flask import render_template

#Routes that return JSON
user_data = {
    'lucasl' : {
        'user_id' : 0,
        'name': 'Lucas',
        'favoriteColor' : 'blue'
    },
    'christophert' : {
        'user_id' : 1,
        'name': 'Christopher',
        'favoriteColor' : 'orange'
    },
    'joelt' : {
        'user_id' : 2,
        'name': 'Joel',
        'favoriteColor' : 'red'
    },
}

# Routes that return/display HTML
logged_in_user = user_data['christophert']



@app.route('/')
def home():
    return render_template('home.html', user=logged_in_user)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


