#!/usr/bin/python3
"""Flask framework
    """
from flask import Flask

app = Flask(__name__)


# Define a route for the root URL with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == '__main__':
    # Run the Flask app with the specified host and port
    app.run(host='0.0.0.0', port=5000)
