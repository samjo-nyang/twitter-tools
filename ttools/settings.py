from os import path


CONSUMER_KEY = ''

CONSUMER_SECRET = ''

ACCESS_TOKEN_KEY = ''

ACCESS_TOKEN_SECRET = ''

EMAIL_ADDRESS = ''

EMAIL_SENDER = ''

BASE_PATH = path.abspath(path.dirname(__file__))

STORAGE_PATH = path.join(BASE_PATH, 'storage/')


try:
    from .local_settings import *  # noqa: F401,F403
except:
    pass
