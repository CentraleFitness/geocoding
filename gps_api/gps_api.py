
import requests
import json

CONFIGFILE_PATH = "./settings.json"

def main_test(address, api_key):
    resp = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json",
        params=
        {
            'address': address,
            'key': api_key
        })
    jresp = resp.json()
    for result in jresp.get('results', []):
        location = result['geometry']['location']
        gps_coord = (location['lat'], location['lng'])
        print(gps_coord)

if __name__ == "__main__":
    with open(CONFIGFILE_PATH, 'r') as fh:
        data = json.load(fh)
        assert 'key' in data
    address = "Lieu dit Poggie, 20230, St Lucia di moriani"
    main_test(address, data['key'])
