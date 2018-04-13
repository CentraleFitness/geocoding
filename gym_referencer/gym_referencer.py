import json

from elasticsearch import Elasticsearch

def main() -> None:
    es_cluster = Elasticsearch([{'host': '127.0.0.1', 'port': 9200}])
    print(es_cluster.info())

if __name__ == "__main__":
    main()
