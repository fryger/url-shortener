from flask import Flask
from flask_cors import CORS

from users.routes import authentication_routes

from extensions import db, mail, migrate, api


def create_app(config_object="settings"):

    app = Flask(__name__)
    CORS(app)

    app.debug = True
    app.run(host="0.0.0.0")
    app.config.from_object(config_object)

    register_extensions(app)
    register_api_routes(api)

    with app.app_context():

        db.create_all()

        return app


def register_extensions(app):
    """Register Flask extensions."""

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    api.init_app(app)

    return None


def register_api_routes(api):
    """Register Flask API routes."""
    authentication_routes(api)
    return None
