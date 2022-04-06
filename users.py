import requests
from flask import Blueprint

user_api = Blueprint('user_api', __name__)

@user_api.route('/users')
def get_users():
    url = 'https://jsonplaceholder.typicode.com/users'
    r =requests.get(uri)
    return r.text