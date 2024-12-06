# User location, country and zip/postal code
from flask import Blueprint, request, jsonify
# from __main__ import app
user_location = Blueprint('user_location', __name__, template_folder='templates')
@user_location.route('/user_location', methods=['POST'])
def show(page):
    global user_location
    data = request.get_json()
    latitude = data.get('userLatitude')
    longitude = data.get('userLongitude')
    if latitude and longitude:
        user_location = {"latitude": latitude, "longitude": longitude}
        print("Received user location:", latitude, longitude)
        return jsonify({"status": "Location received"}), 200
    else:
        return jsonify({"error": "Invalid location data"}), 400
