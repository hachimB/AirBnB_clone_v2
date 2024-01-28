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


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """filters"""
    state = storage.all(State)
    amenitie = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=state, amenities=amenitie)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
