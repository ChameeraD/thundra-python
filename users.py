import requests
from flask import Blueprint

user_api = Blueprint('user_api', __name__)

@user_api.route('/users')
def get_users():
    r =requests.get('https://jsonplaceholder.typicode.com/uses')
    print(r)
    return r.text