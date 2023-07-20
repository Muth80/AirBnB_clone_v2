#!/usr/bin/python3
"""
This module defines the routes for the Flask app.
"""

from flask import request
from web_flask import app

@app.route('/')
def hello_hbnb():
    """
    Route that displays "Hello HBNB!"
    """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """
    Route that displays "HBNB"
    """
    return "HBNB"

@app.route('/c/<text>')
def c_route(text):
    """
    Route that displays "C ", followed by the value of the text variable
    (replace underscore _ symbols with a space)
    """
    return "C " + text.replace("_", " ")

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    """
    Route that displays "Python ", followed by the value of the text variable
    (replace underscore _ symbols with a space).
    If no text is provided, the default value is "is cool".
    """
    return "Python " + text.replace("_", " ")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


