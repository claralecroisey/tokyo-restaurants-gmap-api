from os import environ

from flask import Flask
from flask_cors import CORS

from app.restaurants_routes import restaurants_blueprint
from app.services.google_places import GooglePlaces
from config import DevConfig, ProdConfig


def create_app():
    app = Flask(__name__)

    env = environ.get("FLASK_ENV")

    if env == "production":
        app.config.from_object(ProdConfig)
    elif env == "development":
        app.config.from_object(DevConfig)

    app.register_blueprint(restaurants_blueprint)

    # Enable CORS
    CORS(app, origins=[app.config["CLIENT_URL"]], supports_credentials=True)

    return app


app = create_app()

gplaces = GooglePlaces(api_key=app.config["GOOGLE_PLACES_API_KEY"])
