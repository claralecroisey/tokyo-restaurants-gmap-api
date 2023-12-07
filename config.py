import os


class Config(object):
    DEBUG = False
    TESTING = False
    CORS_HEADERS = "Content-Type"
    GOOGLE_PLACES_API_KEY = ""


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    GOOGLE_PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")
