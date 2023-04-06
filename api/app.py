"""
Launch from the project directory with
> python -m flask --app api/app.py run
"""

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    This hello world function is a simple example of endpoint.
    """
    return dict(message="Hello World!")