from application.auth import auth
from flask import render_template


@auth.route('/')
def hello_world():
    return render_template('auth.html')
