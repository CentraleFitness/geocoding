from elasticsearch import Elasticsearch
from config import ES_CLUSTER

class ESManager(object):
    """
    ElasticSearch Cluster Manager
    """

    def __init__(self, *args, **kwargs):
        self._es = Elasticsearch(
            [{'host': ES_CLUSTER['host'], 'port': ES_CLUSTER['port']}],
            timeout=ES_CLUSTER['timeout'],
            max_retries=ES_CLUSTER['max_retries'])
        return super().__init__(*args, **kwargs)
