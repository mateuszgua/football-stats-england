import os

from dotenv import load_dotenv
from os import path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    USERNAME = os.getenv('MYSQL_USERNAME')
    PASSWORD = os.getenv('MYSQL_PASSWORD')
    HOST = os.getenv('MYSQL_HOST')
    PORT = os.getenv('MYSQL_PORT')
    DB_NAME = os.getenv('MYSQL_DB_NAME')

    SECRET_KEY = os.getenv("SECRET_KEY", default=None)
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    FLASK_HOST = '0.0.0.0'
    FLAK_PORT = 9000
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True
