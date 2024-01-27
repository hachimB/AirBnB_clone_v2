#!/usr/bin/python3
"""module documentation"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
import os
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """remove session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """cities by states"""
    all_states = storage.all(State)
    return render_template('9-states.html', states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """state id"""
    all_states = storage.all(State)
    for state in all_states.values():
        if state.id is id:
            return render_template('9-states.html', ste=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
