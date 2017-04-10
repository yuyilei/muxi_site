# coding: utf-8

from flask import Blueprint

api = Blueprint(
    'api',
    __name__,
    subdomain='api',
    template_folder = 'templates',
    static_folder = 'static'
)

<<<<<<< HEAD

from . import authentication, users, comments, shares, users, find, likes, signup, login, profile
=======
from . import authentication, users, comments, shares, users, find, likes, signup, login, profile, blog
>>>>>>> 9c34cfb9f2e50768f75784d533b21897a2d1859b
