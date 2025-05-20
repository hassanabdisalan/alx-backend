#!/usr/bin/env python3
"""
Flask app with Babel for i18n setup
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class for Flask app i18n settings
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app: Flask = Flask(__name__)
app.config.from_object(Config)

babel: Babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Route handler for the index page
    Returns rendered HTML page
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
