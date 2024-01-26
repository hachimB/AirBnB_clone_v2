#!/usr/bin/python3
"""Module documentation"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return "C " + text


@app.route("/python/", defaults={'text': 'is cool'},  strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    text = text.replace('_', ' ')
    return "Python " + text


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_temp(n):
    if isinstance(n, int):
        return render_template('5-number.html',number = n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
