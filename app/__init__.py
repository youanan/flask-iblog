from flask import Flask
from views import bp
from models import db
from app.admin import create_admin


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    register_blueprints(app)
    register_database(app)

    create_admin(app)

    return app


def register_blueprints(app):
    app.register_blueprint(bp)


def register_database(app):
    db.init_app(app)





