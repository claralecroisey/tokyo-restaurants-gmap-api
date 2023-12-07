import requests


class GooglePlaces:
    def __init__(self, api_key):
        self.base_url = "https://places.googleapis.com/v1/places"
        self.headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": api_key,
            "X-Goog-FieldMask": "*",
        }

    def search_places_nearby_coordinates(
        self, lat: int, lng: int, type: str, radius=500.0
    ):
        data = {
            "includedTypes": [type],
            "locationRestriction": {
                "circle": {
                    "center": {"latitude": lat, "longitude": lng},
                    "radius": radius,
                }
            },
        }

        response = requests.post(
            url=f"{self.base_url}:searchNearby",
            json=data,
            headers=self.headers,
        )

        response.raise_for_status()
        return response.json()
