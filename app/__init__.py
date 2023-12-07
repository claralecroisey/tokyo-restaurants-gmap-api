from flask import Flask
from os import environ
from config import ProdConfig, DevConfig
from app.restaurants_routes import restaurants_blueprint


def create_app():
    app = Flask(__name__)

    env = environ.get("FLASK_ENV")

    if env == "production":
        app.config.from_object(ProdConfig)
    elif env == "development":
        app.config.from_object(DevConfig)

    app.register_blueprint(restaurants_blueprint)
    return app


app = create_app()
