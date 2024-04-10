#!/usr/bin/env python3
""" Main Application """

from flask import Flask, render_template, request
from flask_babel import Babel
from pytz import timezone

# Create a Flask application instance
app = Flask(__name__)

# Create a Config class with LANGUAGES attribute
class Config:
    LANGUAGES = ["en", "fr", "kg"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Instantiate the Babel object and store it in a module-level variable named babel
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_name):
    """ Get user from users """
    return users.get(user_name)

def get_user_locale(user_locale):
    """ Get user locale """
    if user_locale in Config.LANGUAGES:
        return user_locale
    return None

def get_user_timezone(user_timezone):
    """ Get user timezone """
    if user_timezone in timezone.all_timezones:
        return user_timezone
    return None

@app.before_request
def before_request():
    """ Before request """
    user_name = request.args.get('login_as')
    if user_name:
        g.user = get_user(str(user_name))
    else:
        g.user = None

@app.route('/')
def index():
    """ Index """
    return render_template('5-index.html',home_title='Welcome to Holberton', home_header='Hello world!',logged_in_as=g.user,not_logged_in='Please log in')

if __name__ == '__main__':
    app.run(debug=True)