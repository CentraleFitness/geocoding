
import requests
import json

CONFIGFILE_PATH = "./settings.json"

def address_to_gps_coord(address, api_key):
    resp = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json",
        params=
        {
            'address': address,
            'key': api_key
        })
    try:
        resp.raise_for_status()
        jresp = resp.json()
    except Exception:
        print(resp.status)
        return []
    matches = list()
    for result in jresp.get('results', []):
        location = result['geometry']['location']
        gps_coord = (location['lat'], location['lng'])
        matches.append(gps_coord)
    return matches

def main_test():
    with open(CONFIGFILE_PATH, 'r') as fh:
        data = json.load(fh)
        assert 'key' in data
    address = "Lieu dit Poggie, 20230, St Lucia di moriani"
    results = address_to_gps_coord(address, data['key'])
    for result in results:
        print(result)

if __name__ == "__main__":
    main_test()
