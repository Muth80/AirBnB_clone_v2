#!/usr/bin/python3
"""
This module defines the routes for the Flask app.
"""

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
