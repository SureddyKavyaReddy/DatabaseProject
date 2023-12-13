# app.py
import bottle
from dataset import connect
import configparser
from bottle import route, run, template, request, redirect


app = bottle.default_app()

# Load database configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

database_url = config['database']['url']
db = connect(database_url)

# Define tables
users = db['users']
posts = db['posts']

@bottle.route('/')
def index():
    all_users = users.find()
    return bottle.template('views/index', users=all_users)

@bottle.route('/user/<user_id>')
def user_detail(user_id):
    user = users.find_one(id=user_id)
    user_posts = posts.find(user_id=user_id)
    return bottle.template('views/user_detail', user=user, posts=user_posts)

@bottle.route('/user/<user_id>/edit')
def edit_user_form(user_id):
    user = users.find_one(id=user_id)
    return bottle.template('views/edit_user', user=user)


@bottle.route('/user/<user_id>/update', method='POST')
def edit_user(user_id):
    new_username = bottle.request.forms.get('new_username')
    users.update(dict(id=user_id, username=new_username), ['id'])
    bottle.redirect('/user/{}'.format(user_id))


@bottle.route('/user/<user_id>/delete')
def delete_user_form(user_id):
    user = users.find_one(id=user_id)
    return bottle.template('views/delete_user', user=user)

@bottle.route('/user/<user_id>/delete', method='POST')
def delete_user(user_id):
    users.delete(id=user_id)
    bottle.redirect('/')

@bottle.route('/create_user', method='POST')
def create_user():
    username = bottle.request.forms.get('username')
    users.insert(dict(username=username))
    bottle.redirect('/')

@bottle.route('/create_post', method='POST')
def create_post():
    user_id = bottle.request.forms.get('user_id')
    title = bottle.request.forms.get('title')
    content = bottle.request.forms.get('content')
    posts.insert(dict(user_id=user_id, title=title, content=content))
    bottle.redirect('/user/{}'.format(user_id))

@bottle.route('/post/<post_id>/edit')
def edit_post_form(post_id):
    post = posts.find_one(id=post_id)
    return bottle.template('views/edit_post', post=post)

@bottle.route('/post/<post_id>/update', method='POST')
def edit_post(post_id):
    new_title = bottle.request.forms.get('new_title')
    new_content = bottle.request.forms.get('new_content')
    posts.update(dict(id=post_id, title=new_title, content=new_content), ['id'])
    user_id = bottle.request.forms.get('user_id')
    bottle.redirect('/user/{}'.format(user_id))

@bottle.route('/post/<post_id>/delete')
def delete_post_form(post_id):
    post = posts.find_one(id=post_id)
    return bottle.template('views/delete_post', post=post)

@bottle.route('/post/<post_id>/delete', method='POST')
def delete_post(post_id):
    user_id = bottle.request.forms.get('user_id')
    posts.delete(id=post_id)
    bottle.redirect('/user/{}'.format(user_id))

if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True)
