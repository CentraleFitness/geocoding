import json
import logging.config

from cluster import ESManager
from config import LOGGING_DICT

logging.config.dictConfig(LOGGING_DICT)

def main() -> None:
    es_cluster = ESManager()
    print(es_cluster._es.info())
    es_cluster.create_auto_index('gym')

if __name__ == "__main__":
    main()
