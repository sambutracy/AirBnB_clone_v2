#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!" when the root URL is accessed.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" when the /hbnb URL is accessed.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display "C " followed by the value of the text variable,
    replacing underscores with spaces.
    """
    return "C {}".format(unquote(text).replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def python_text(text):
    """
    Display "Python " followed by the value of the text variable,
    replacing underscores with spaces. Default value of text is "is cool".
    """
    return "Python {}".format(unquote(text).replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Display "n is a number" only if n is an integer.
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
