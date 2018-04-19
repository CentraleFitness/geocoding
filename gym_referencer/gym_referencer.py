import json
import logging.config
import requests

from cluster import ESManager
from config import LOGGING_DICT
from entry import Gym

logging.config.dictConfig(LOGGING_DICT)

GYM_DATA_PATH = './gym_data.json'

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

        #geo_loc = address_to_gps_coord(', '.join(tuple(name) + address), '', closest=True)
        geo_loc = None

        gym = Gym(
            id_gym,
            data[id_gym]['id_owner'],
            *address,
            *geo_loc
            )
        gym_list.append(gym)

if __name__ == "__main__":
    main()
