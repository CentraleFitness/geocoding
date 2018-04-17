import json

from cluster import ESManager

def main() -> None:
    es_cluster = ESManager()
    print(es_cluster._es.info())

if __name__ == "__main__":
    main()
