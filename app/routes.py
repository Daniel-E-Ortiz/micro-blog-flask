''' 
    routes.py module contains all the different URL's that the 
    application implements. In Flask, handlers for the application
    are written as Python functions, called view functions.
'''
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"