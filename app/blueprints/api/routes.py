from app import app 
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


# Create a route to get all user information
@app.route('/api/users/')
def users(): 
    return user_data

# Create a route to get user information based on their username
@app.route('/api/user/username/<username>')
def user(username):
    if username not in user_data:
        return 'User not found'

    return user_data[username]

# Create a route to get user information based on their id
@app.route('/api/user/id/<id>')
def user_by_id(id):
    for key, user in user_data.items():
        if user['user_id'] == int(id):
            return user

        return 'User not found'