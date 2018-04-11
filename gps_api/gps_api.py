"""
Utility functions
"""

import json
import requests

CONFIGFILE_PATH = "./settings.json"

def address_to_gps_coord(address, api_key) -> list:
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
                'key': api_key
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
    return matches

def main_test():
    """ Main Test """
    with open(CONFIGFILE_PATH, 'r') as config_fh:
        data = json.load(config_fh)
        assert 'key' in data
    address = "Amiens"
    results = address_to_gps_coord(address, data['key'])
    for result in results:
        print(result)

if __name__ == "__main__":
    main_test()
