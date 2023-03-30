import os

from dotenv import load_dotenv
from os import path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    USERNAME = os.getenv('MYSQL_USERNAME', 'root')
    PASSWORD = os.getenv('MYSQL_PASSWORD', 'root')
    HOST = os.getenv('MYSQL_HOST', 'mysql')
    PORT = os.getenv('MYSQL_PORT', '3306')
    DB_NAME = os.getenv('MYSQL_DB_NAME', 'football_eng')

    SECRET_KEY = os.getenv("SECRET_KEY", 'GDtfDCFYjDABCKSJDIF')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    FLASK_HOST = '0.0.0.0'
    FLAK_PORT = 9000
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True
