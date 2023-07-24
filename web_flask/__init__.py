#!/usr/bin/python3
"""
This module initializes the Flask app.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from .hello_route import *
from .c_route import *

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

# Import the routes defined in the files
from web_flask.1_hbnb_route import *
from web_flask.2_c_route import *
from web_flask.3_python_route import *
from web_flask.4_number_route import *
from web_flask.5_number_template import *
from web_flask.6_number_odd_or_even import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
