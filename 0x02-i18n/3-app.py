#!/usr/bin/env python3
"""
3-app.py
Basic Flask app with a single route '/'
"""
from flask import (
        Flask,
        render_template,
        request
)
from flask_babel import Babel


class Config:
    """
    Config class for Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale() -> str:
    """
    Get locale based on request.accept_languages
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', strict_slashes=False)
def get_index() -> str:
    """
    Renders index.html template
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
