"""
Flask service to get the geolocation of a given address
"""

import json
import requests

from flask import Flask, request, jsonify

app = Flask(__name__)

CONFIGFILE_PATH = "./settings.json"

def parse_json_file():
    """
    Parse the json config file to retreive the Google Map API key
    """
    with open(CONFIGFILE_PATH, 'r') as config_fh:
        data = json.load(config_fh)
        return data['key'], data['host'], data['port']

def address_to_gps_coord(address, **kwargs) -> list:
    """
    Uses the Google Maps Geocoding API to convert an address
    to the corresponding GPS coordinates.
    Return the results matching the address on a list of
    tuples (latitude, longitude)
    """
    try:
        resp = requests.get(
            "https://maps.googleapis.com/maps/api/geocode/json",
            params=
            {
                'address': address,
                'key': API_KEY
            })
        resp.raise_for_status()
        jresp = resp.json()
    except requests.RequestException as ex:
        print(ex)
        return []
    except ValueError as ex:
        print(ex)
        return []
    matches = list()
    for result in jresp.get('results', []):
        location = result['geometry']['location']
        gps_coord = (location['lat'], location['lng'])
        matches.append(gps_coord)
    if matches and kwargs.get('closest', False):
        return matches[0]
    return matches

@app.route('/geocoding', methods=['GET'])
def geocoding_main():
    """
    Route
    """
    if request.method == 'GET':
        print(request)
        params = tuple(comp for comp in (
            request.args.get('name', ''),
            request.args.get('street', ''),
            request.args.get('zip', ''),
            request.args.get('city', ''),
            request.args.get('country', ''),
            ) if comp != '')
        location = address_to_gps_coord(', '.join(params), closest=True)
    return jsonify(location)

if __name__ == "__main__":
    API_KEY, HOST, PORT = parse_json_file()
    app.run(host=HOST, port=PORT)
