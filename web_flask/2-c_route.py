#!/usr/bin/python3
"""Flask framework
    """
from flask import Flask

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
    return "C {}".format(escape(text))


if __name__ == '__main__':
    # Run the Flask app with the specified host and port
    app.run(host='0.0.0.0', port=5000)
