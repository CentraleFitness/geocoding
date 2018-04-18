from logging import getLogger

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
        self.logger = getLogger(__name__)
        return super().__init__(*args, **kwargs)

    def _create_index(self, name: int, body: dict) -> bool:
        """
        Create an index in the cluster
        """
        try:
            ret = self._es.indices.create(index=str(name), body=body)
        except Exception as ex:
            self.logger.error(
                "Exception occured in _create_index: {}".format(ex))
            return False
        self.logger.info("Created index {}".format(name))
        return ret['acknowledged']

    def create_auto_index(self, name: str) -> bool:
        """
        Create the _default_ template in the cluster
        """
        res = self._create_index(name, body={
            'settings': {
                'index': {
                    'number_of_shards': 5,
                    'number_of_replicas': 1
                    }
                },
            'mappings': {
                '_default_': {
                    'dynamic_templates': [
                        {
                            'geo_location': {
                                'mapping': {
                                    'type': 'geo_point',
                                    'fielddata': {
                                        'format': 'compressed',
                                        'precision': '3m'
                                        }
                                    },
                                'match': 'location'
                                }
                        }
                        ]
                    }
                }
            })