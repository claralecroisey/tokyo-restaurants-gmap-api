import requests
from flask import Blueprint, current_app, jsonify

restaurants_blueprint = Blueprint("restaurants", __name__, url_prefix="/restaurants")


@restaurants_blueprint.route("", methods=["GET"])
def get_restaurants_locations():
    try:
        # Tokyo location
        data = {
            "includedTypes": ["restaurant"],
            "locationRestriction": {
                "circle": {
                    "center": {"latitude": 35.709026, "longitude": 139.731992},
                    "radius": 500.0,
                }
            },
        }

        response = requests.post(
            url="https://places.googleapis.com/v1/places:searchNearby",
            json=data,
            headers={
                "Content-Type": "application/json",
                "X-Goog-Api-Key": current_app.config["GOOGLE_PLACES_API_KEY"],
                "X-Goog-FieldMask": "places.displayName",
            },
        )

        data = response.json()

        if data:
            restaurants = data["places"]
        else:
            # When there are no results, the response is an empty object
            restaurants = []

        return restaurants, 200
    except Exception as e:
        current_app.logger.error(e)
        return (
            jsonify(error="An unexpected error happened, please try again later"),
            400,
        )
