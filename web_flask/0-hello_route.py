"""hello_route"""
from flask import Flask

app = Flask(__name__)


@app.route("/",  strict_slashes=False)
def hello_hbnb():
    """This route returns a "Hello HBNB!" string"""
    return "Hello HBNB!"
