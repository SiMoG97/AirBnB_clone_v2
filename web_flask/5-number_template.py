#!/usr/bin/python3
"""hello_route"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/",  strict_slashes=False)
def hello_hbnb():
    """This route returns a "Hello HBNB!" string"""
    return "Hello HBNB!"


@app.route("/hbnb",  strict_slashes=False)
def hbnb_route():
    """This route returns a "HBNB" string"""
    return "HBNB"


@app.route("/c/<text>",  strict_slashes=False)
def c_route(text: str):
    """returns a string"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>",  strict_slashes=False)
def python_route(text: str):
    """returns a string"""
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>",  strict_slashes=False)
def is_a_number(n: str):
    """prints n if n is a number"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>",  strict_slashes=False)
def number_template(n: str):
    """returns a html template if n is a number"""
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
