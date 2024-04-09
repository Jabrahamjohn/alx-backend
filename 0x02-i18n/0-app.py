#!/usr/bin/env python3
""" Basic Flask app"""

from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)


#defining route
@app.route('/')
def index():
    """ Route for handling root URL """
    return render_template('0-index.html')

# Run the app
if __name__ == "__main__":
    app.run(debug = True,)