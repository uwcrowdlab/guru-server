import os
import sys
import logging


class Config(object):
    MONGODB_HOST = os.environ['MONGODB_URL']
    LOGSTREAM = sys.stdout
    CELERY_BROKER_URL = os.environ['REDIS_URL']
    CELERY_BACKEND = os.environ['REDIS_URL']

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    LOGLEVEL = logging.DEBUG

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    LOGLEVEL = logging.INFO

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    LOGLEVEL = logging.ERROR
