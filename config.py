import os


class Config(object):
    DEBUG = False
    TESTING = False
    CORS_HEADERS = "Content-Type"
    CLIENT_URL = ""
    GOOGLE_PLACES_API_KEY = ""


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    CLIENT_URL = "http://localhost:5173"
    GOOGLE_PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")
