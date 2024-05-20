#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, render_template
from urllib.parse import unquote

app = Flask(__name__)
app.config['DEBUG'] = True  # Enable debug mode


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
@app.route('/python/<text>', strict_slashes=False)
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Display an HTML page only if n is an integer.
    H1 tag: “Number: n” inside the tag BODY.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Display an HTML page only if n is an integer.
    H1 tag: “Number: n is even|odd” inside the tag BODY.
    """
    parity = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
