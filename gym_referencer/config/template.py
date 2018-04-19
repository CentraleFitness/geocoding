"""
Config file
"""

## ElasticSearch Cluster

ES_CLUSTER = {
    'host': '',
    'port': '',
    'timeout': 999,
    'max_retries': 999
}

LOG_SERVER = {
    'ip': '',
    'port': 0
}

LOGGING_DICT = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
            },
        'graypy': {
            'level': 'DEBUG',
            'class': 'graypy.GELFHandler',
            'host': LOG_SERVER['ip'],
            'port': LOG_SERVER['port'],
            },
        },
    'loggers': {
        '__main__': {
            'handlers': ['graypy', 'console'],
            'level': 'DEBUG',
            'propagate': True
            },
        'cluster': {
            'handlers': ['graypy', 'console'],
            'level': 'DEBUG',
            'propagate': True
            }
        }
    }
