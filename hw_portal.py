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
        'release year' : '2019',
        'user_id': '1'
    },
    '1': {
        'title' : 'Skyrim',
        'system' : 'PC',
        'release year' : '2011',
        'user_id': '1'
    },
    '1': {
        'title' : '7 Days to Die',
        'system' : 'PC',
        'release year' : '2013',
        'user_id': '1'
    }
}

@app.get('/user')
def user():
  return { 'users': list(users.values()) }, 200

@app.get('/user/<user_id>')
def get_user(user_id):
  try:
    return { 'user': users[user_id] } 
  except:
    return {'message': 'invalid user'}, 400
    
@app.route('/user', methods=["POST"])
def create_user():
  user_data = request.get_json()
  users[uuid4()] = user_data
  return { 'message' : f'{user_data["username"]} created' }, 201

@app.put('/user/<user_id>')
def update_user(user_id):
  try:
    user = users[user_id]
    user_data = request.get_json()
    user |= user_data
    return { 'message': f'{user["username"]} updated'}, 202
  except KeyError:
    return {'message': "Invalid User"}, 400
      
@app.delete('/user/<user_id>')
def delete_user(user_id):
  try:
    del users[user_id]
    return { 'message': f'User Deleted' }, 202
  except:
    return {'message': "Invalid username"}, 400


@app.post('/games')
def create_post():
    post_data = request.get_json()   
    user_id = post_data['user_id']
    if user_id in users:
        games[uuid4()]= post_data
        return { 'message': "Post Created" }, 201
    return { 'message': "Invalid User"}, 401

@app.put('/post/<post_id>')
def update_post(post_id):
    try:
        post = games[post_id]
        post_data = request.get_json()
        if post_data['user_id']== post['user_id']:
            post['body'] = post_data['body']
            return {'message': 'Post Updated'}, 202
        return {'message': "Unauthorized"}, 401
    except:
        return{'message': "Invalid Post"}, 400

@app.delete('/post/<post_id>')
def delete_post(post_id):
    try:
        del games[post_id]
        return {"message": "Post Deleted"}, 202
    except:
        return {'message': "Invalid Post"}, 400