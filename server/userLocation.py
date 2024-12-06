# User location, country and zip/postal code
import sys
import globals
from flask import Blueprint, request, jsonify

# from __main__ import app
user_location = Blueprint('user_location', __name__, template_folder='templates')
@user_location.route('/user_location', methods=['POST'])
def show():
    data = request.get_json()
    latitude = data.get('userLatitude')
    longitude = data.get('userLongitude')
    if latitude and longitude:
        globals.userLocation["latitude"] = latitude
        globals.userLocation["longitude"] = longitude
        print("Received user location:", latitude, longitude, file=sys.stderr)
        return jsonify({"status": "Location received"}), 200
    else:
        return jsonify({"error": "Invalid location data"}), 400
