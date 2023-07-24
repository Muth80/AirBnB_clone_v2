#!/usr/bin/python3
"""
This module defines the routes for the Flask app.
"""

from flask import render_template
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

@app.route('/number/<int:n>')
def number_route(n):
    """
    Route that displays "n is a number" only if n is an integer
    """
    return f"{n} is a number"

@app.route('/number_template/<int:n>')
def number_template(n):
    """
    Route that displays a HTML page only if n is an integer.
    It renders the template number_template.html and passes the variable 'n' to it.
    """
    return render_template('number_template.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    Route that displays a HTML page only if n is an integer.
    It renders the template number_odd_or_even.html and passes the variable 'n' and 'odd_or_even' to it.
    """
    odd_or_even = "odd" if n % 2 != 0 else "even"
    return render_template('number_odd_or_even.html', n=n, odd_or_even=odd_or_even)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

