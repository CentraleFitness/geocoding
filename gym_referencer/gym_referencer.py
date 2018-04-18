import json
import logging.config
import requests

from cluster import ESManager
from config import LOGGING_DICT
from entry import Gym

logging.config.dictConfig(LOGGING_DICT)

GYM_DATA_PATH = './gym_data.json'


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


def main() -> None:
    es_cluster = ESManager()
    print(es_cluster._es.info())
    if not es_cluster.index_exist('gym'):
        es_cluster.create_auto_index('gym')

    with open(GYM_DATA_PATH, 'r') as fh:
        data = json.load(fh)

    gym_list = list()
    for id_gym in data:
        name = data[id_gym]['name']
        address = (
            data[id_gym]['address']['street'],
            data[id_gym]['address']['zip'],
            data[id_gym]['address']['city'],
            data[id_gym]['address']['country']
            )

        geo_loc = address_to_gps_coord(', '.join(tuple(name) + address), '')[0]

        gym = Gym(
            id_gym,
            data[id_gym]['id_owner'],
            *address,
            *geo_loc
            )
        gym_list.append(gym)

if __name__ == "__main__":
    main()
