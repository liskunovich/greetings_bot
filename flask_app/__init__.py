import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_config import config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    config_name = os.environ.get('FLASK_CONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    with app.app_context():
        import flask_app.models
        db.create_all()
    from .views.base import base_page
    app.register_blueprint(base_page)
    return app
