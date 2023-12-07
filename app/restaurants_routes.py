from flask import Blueprint, jsonify

restaurants_blueprint = Blueprint("restaurants", __name__, url_prefix="/restaurants")


@restaurants_blueprint.route("", methods=["GET"])
def get_restaurants_locations():
    try:
        return jsonify(restaurants=[])
    except Exception as e:
        return jsonify(error=str(e)), 400
