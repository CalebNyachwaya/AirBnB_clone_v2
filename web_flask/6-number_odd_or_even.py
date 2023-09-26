#!/usr/bin/python3
"""Flask framework
    """
from flask import Flask, render_template

app = Flask(__name__)


# Define a route for the root URL with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# Define a route for the root URL with strict_slashes=False
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    # Replace underscores (_) with spaces in the text variable
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    # display Python followed by the value of text
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def num_display(n):
    # display “n is a number” only
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_html(n):
    """display HTML is "n" is a number only"""
    return render_template('5-number.html', name=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_html_even_odd(n):
    # Display H1 tag: Number: n is even|odd
    return render_template('6-number_odd_or_even.html', name=n)


if __name__ == '__main__':
    # Run the Flask app with the specified host and port
    app.run(host='0.0.0.0', port=5000)
