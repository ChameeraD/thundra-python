import requests
from flask import Blueprint

post_api = Blueprint('post_api', __name__)

@post_api.route('/posts')
def get_posts():
    r =requests.get('https://jsonplaceholder.typicode.com/posts')
    return r.text