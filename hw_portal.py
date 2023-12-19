from flask import Flask, request
from uuid import uuid4
app = Flask(__name__)

users = {
    '1':{
        'username': 'PReidy',
        'email' : 'Preidy@aol.com'
    }
}

games = {
    '1': {
        'title' : 'Halo MCC',
        'system' : 'Xbox One',
        'release date' : '2019',
        'user_id': '1'
    }
}

@app.get('/user')
def user():
    return { 'users': list(users.values())}, 200

@app.post('/user')
def create_user():
    json_body = request.get_json()
    users[uuid4()] = json_body
    return {'message' : f'{json_body["username"]} created'}, 201

@app.put('/user')
def update_user():
    return

@app.delete('/user')
def delete_user():
    pass

@app.get('/post')
def get_post():
    return

@app.post('/post')
def create_post():
    return

@app.post('/post')
def update_post():
    return

@app.delete('/post')
def delete_post():
    return