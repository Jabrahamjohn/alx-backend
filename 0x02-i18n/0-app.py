#!/usr/bin/env python3
""" Basic Flask app"""

from flask import Flask

# Create a Flask app instance
app = Flask(__name__)


#defining route
@app.route('/')
def hello_world():
    """ Route for handling root URL """
    return 'Hello world!'

# Run the app
if __name__ == "__main__":
    app.run(debug = True,)