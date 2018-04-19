import json
import logging.config
import requests

from cluster import ESManager
from config import LOGGING_DICT
from entry import Gym

logging.config.dictConfig(LOGGING_DICT)

GYM_DATA_PATH = './gym_data.json'

def request_geoloc(address: dict) -> tuple:
    try:
        resp = requests.get(
            "http://127.0.0.1:4455/geocoding",
            params=address)
        resp.raise_for_status()
        jresp = resp.json()
    except requests.RequestException as ex:
        print(ex)
        return []
    except ValueError as ex:
        print(ex)
        return []
    return (jresp[0], jresp[1])

def main() -> None:
    es_cluster = ESManager()
    print(es_cluster._es.info())
    if not es_cluster.index_exist('gym'):
        es_cluster.create_auto_index('gym')

    with open(GYM_DATA_PATH, 'r') as fh:
        data = json.load(fh)

    gym_list = list()
    for id_gym in data:
        address_dict = data[id_gym]['address']
        address_dict.update({'name': data[id_gym]['name']})
        geo_loc = request_geoloc(address_dict)
        gym = Gym(
            id_gym,
            data[id_gym]['id_owner'],
            address_dict['name'],
            address_dict['street'],
            address_dict['zip'],
            address_dict['city'],
            address_dict['country'],
            *geo_loc
            )
        gym_list.append(gym)
    for gym in gym_list:
        ret = es_cluster.reference_gym(gym)
        print(ret)
        pass

if __name__ == "__main__":
    main()
