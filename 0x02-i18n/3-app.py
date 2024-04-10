#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup, Get locale from request,"""

from flask import Flask, render_template, request
from flask_babel import Babel, _, gettext

# Create a Flask application instance
app = Flask(__name__)

class Config:
    """ Configuration class for Babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

babel = Babel(app)
app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """ Get locale from request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """ Main route """
    return render_template('3-index.html',home_title=gettext('Hello world!'),home_header=gettext('Welcome to Holberton'))

if __name__ == '__main__':
    app.run(debug=True)
