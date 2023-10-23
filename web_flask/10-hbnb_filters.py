#!/usr/bin/python3
"""hello_route"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from os import getenv

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception=None):
    """Closes the storage session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """fetches all states and presents them on html page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
