import os
import dj_database_url
from .common import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = ['*']

# DATABASES
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600),
}