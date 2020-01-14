from flask import Flask

''' 
    This creates an app obj as an instance
    of class Flask imported from flask package.
'''
app = Flask(__name__)       

''' 
    routes is imported at the bottom as a workaround to circular imports,
    a common problem with Flask apps.
'''
from app import routes      