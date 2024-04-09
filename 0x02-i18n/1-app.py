#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup, Get locale from request,"""

from flask import Flask
from flask_babel import Babel

# Create a Flask application instance
app = Flask(__name__)

# Create a Config class with LANGUAGES attribute
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Instantiate the Babel object and store it in a module-level variable named babel
babel = Babel(app)

# Use the Config class as configuration for your Flask app
app.config.from_object(Config)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
