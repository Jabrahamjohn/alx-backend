from flask import Flask, render_template, request
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

# Function to determine the locale
@babel.localeselector
def get_locale():
    # Get the locale from the request argument, if present
    locale = request.args.get('locale')
    # Check if the locale is supported
    if locale in app.config['LANGUAGES']:
        return locale
    # If the locale is not supported or not provided, use default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Route to render the index.html file
@app.route('/')
def index():
    return render_template('4-index.html', home_title='Welcome to Holberton', home_header='Hello world!')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
