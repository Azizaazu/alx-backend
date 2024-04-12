#!/usr/bin/env python3
"""
2-app.py
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


@babel.localeselector
def get_locale():
    """
    Get locale based on request.accept_languages
    """
    return request.accept_languages.best_match(app.onfig['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders index.html template
    """
    return render_template('2-index.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
