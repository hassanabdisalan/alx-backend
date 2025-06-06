#!/usr/bin/env python3
"""
Basic Flask app with a single route
"""

from flask import Flask, render_template

app: Flask = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Route handler for the index page
    Returns rendered HTML page
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
