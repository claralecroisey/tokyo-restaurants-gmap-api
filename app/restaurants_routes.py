from flask import Blueprint, current_app, jsonify

restaurants_blueprint = Blueprint("restaurants", __name__, url_prefix="/restaurants")


@restaurants_blueprint.route("", methods=["GET"])
def get_restaurants_locations():
    from app import gplaces

    try:
        # WIP: hardcoding search coordinates to Tokyo location
        _hardcoded_lat = 35.709026
        _hardcoded_lng = 139.731992
        _hardcoded_radius = 500.0

        response = gplaces.search_places_nearby_coordinates(
            lat=_hardcoded_lat,
            lng=_hardcoded_lng,
            radius=_hardcoded_radius,
            type="restaurant",
        )

        if response:
            restaurants = response["places"]
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
