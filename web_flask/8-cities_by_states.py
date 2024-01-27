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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """cities by states"""
    all_states = storage.all(State)
    storage_type = os.getenv('HBNB_TYPE_STORAGE')
    for s in all_states.values():
        if storage_type == 'db':
            cities = s.cities
        else:
            cities = s.cities
        s.all_cities = cities
    return render_template('8-cities_by_states.html', states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
