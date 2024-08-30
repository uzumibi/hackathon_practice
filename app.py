"""Flaskアプリケーションを起動するためのエントリーポイントがある"""

"""
from app import create_app

app = create_app()
"""

from flask import Flask

from testapp.routes import init_routes


def create_app():
    app = Flask(
        __name__, template_folder="testapp/templates", static_folder="testapp/static"
    )
    init_routes(app)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
