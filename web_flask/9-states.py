#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_session(exception):
    """Removes the current SQLAlchemy Session."""
    storage.close()


@app.route('/states', methods=['GET'])
def states_list():
    """Displays a list of all State objects."""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<string:state_id>', methods=['GET'])
def state_cities(state_id):
    """Displays a list of City objects linked to a specific State."""
    states = storage.all(State).values()
    state = next((state for state in states if state.id == state_id), None)
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

