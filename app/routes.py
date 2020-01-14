''' 
    routes.py module contains all the different URL's that the 
    application implements. In Flask, handlers for the application
    are written as Python functions, called view functions.
'''
from app import app

'''
    @app.route() is a decorator that creates an association between the URL
    given as an argument and the function. 
    When the web browser requests either of these URL's then Flask is going
    to invoke this function and pass the return value of it back to the browser.
'''
@app.route('/')
@app.route('/index') 
def index():
    return "Hello, World!"