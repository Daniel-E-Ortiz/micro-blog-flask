from flask import Flask

app = Flask(__name__)       ''' creates an app obj as an instance
                                of class Flask imported from flask package.'''

from app import routes      ''' imported at the bottom as a workaround to circular imports,
                                a common problem with Flask apps.'''