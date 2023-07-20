#!/usr/bin/python3
"""
This module initializes the Flask app.
"""
from .hello_route import *
from .c_route import *

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

# Import the routes defined in the 0-hello_route.py file
from web_flask.0-hello_route import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
